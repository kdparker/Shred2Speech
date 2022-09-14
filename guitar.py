from collections import OrderedDict
from dataclasses import dataclass
from sound import play_sound


@dataclass
class Button:
    color: str
    held: int = 0


class Guitar:
    def __init__(self):
        self.held_buttons: OrderedDict[int, Button] = OrderedDict(
            {
                13: Button("🟢"),
                14: Button("🔴"),
                16: Button("🟡"),
                15: Button("🔵"),
                9: Button("🟠"),
            }
        )

    def _text_output_for_input(self, strummed_down: bool) -> str:
        return "".join(
            button.color if button.held else "" for button in self.held_buttons.values()
        ) + ("⬇" if strummed_down else "⬆")

    def _get_numeric_value_for_input(self, key: int) -> int:
        strum_binary_value = (
            "1" if key == 1 else "0"
        )  # strum down results in "lower" values
        buttons_binary_value = "".join(
            str(button.held) for button in self.held_buttons.values()
        )[
            ::-1
        ]  # reversing so that "green" is least significant digit
        return int(strum_binary_value + buttons_binary_value, 2)

    def button_update(self, key: int, pressed: int):
        if key not in self.held_buttons:
            return
        button: Button = self.held_buttons[key]
        button.held = pressed

    def strum(self, key: int, pressed: int):
        if not pressed or key not in (1, 2):
            return
        numeric_value = self._get_numeric_value_for_input(key)
        output = "{} - {}".format(numeric_value, self._text_output_for_input(key == 2))
        play_sound(numeric_value)
        print(output)
