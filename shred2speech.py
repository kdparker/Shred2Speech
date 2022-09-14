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
        guitar.button_update(button, pressed)
        guitar.strum(button, pressed)

    print("Ready to Rock!")

    while True:
        guitar_controller.dispatch_events()


if __name__ == "__main__":
    run()
