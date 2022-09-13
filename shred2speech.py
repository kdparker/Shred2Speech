from dataclasses import dataclass
from xinput import XInputJoystick

from collections import OrderedDict

import sys
import time


@dataclass
class Button:
    color: str
    held: int = 0


class Guitar:
    def __init__(self):
        self.held_buttons: OrderedDict[int, Button] = OrderedDict(
            {
                13: Button("green"),
                14: Button("red"),
                16: Button("yellow"),
                15: Button("blue"),
                9: Button("orange"),
            }
        )

    def button_update(self, key: int, pressed: int):
        if key not in self.held_buttons:
            return
        button: Button = self.held_buttons[key]
        button.held = pressed
        held_text = "held" if pressed else "let go"
        print("{} button {}".format(button.color, held_text))

    def strum(self, key: int, pressed: int):
        if not pressed or key not in (1, 2):
            return
        strum_binary_value = str(1 - (key - 1)) # flipping so that down strums result in "lower" values
        buttons_binary_value = "".join(
            str(button.held) for button in self.held_buttons.values()
        )[::-1] # reversing so that "green" is least significant digit
        print(int(strum_binary_value + buttons_binary_value, 2))

def run():
    joysticks: list[XInputJoystick] = XInputJoystick.enumerate_devices()
    if not joysticks:
        print("Please plug in a 360 Guitar Hero Controller and start again")
        sys.exit(1)
    guitar_controller: XInputJoystick = joysticks[0]
    guitar = Guitar()

    @guitar_controller.event
    def on_button(button, pressed):
        guitar.button_update(button, pressed)
        guitar.strum(button, pressed)

    print(guitar_controller)

    while True:
        guitar_controller.dispatch_events()
        time.sleep(0.01)


if __name__ == "__main__":
    run()
