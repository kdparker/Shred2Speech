from xinput import XInputJoystick

from guitar import Guitar

import sys


def run():
    joysticks: list[XInputJoystick] = XInputJoystick.enumerate_devices()
    if not joysticks:
        print("Please plug in a 360 Guitar Hero Controller and start again")
        sys.exit(1)
    guitar_controller: XInputJoystick = joysticks[0]
    guitar = Guitar()

    @guitar_controller.event
    def on_button(button, pressed):
        if button in (13,14,15,16,9):
            guitar.button_update(button, pressed)
        if not pressed:
            return
        if button in (1,2):
            guitar.strum(button, pressed)
        elif button == 5:
            guitar.clear_store()
        elif button == 6:
            guitar.play_store()

    print("Ready to Rock!")

    while True:
        guitar_controller.dispatch_events()


if __name__ == "__main__":
    run()
