from enum import Enum

import dark_color as Dark
import light_color as Light
from pyside_arco_widget.common.color.color_base import ColorEnum

class SchemeEnum(Enum):
    def __new__(cls, value: ColorEnum):
        self = object.__new__(cls)
        self._value_ = value
        return self

    @property
    def default(self):
        return self.value.default.color


class DARKTheme(SchemeEnum):
    Red = Dark.Red
    OrangeRed = Dark.OrangeRed
    Orange = Dark.Orange
    Gold = Dark.Gold
    Yellow = Dark.Yellow
    Lime = Dark.Lime
    Green = Dark.Green
    Cyan = Dark.Cyan
    Blue = Dark.Blue
    ArcoBlue = Dark.ArcoBlue
    Purple = Dark.Purple
    PinkPurple = Dark.PinkPurple
    Magenta = Dark.Magenta
    Grey = Dark.Grey


class LIGHTTheme(SchemeEnum):
    Red = Light.Red
    OrangeRed = Light.OrangeRed
    Orange = Light.Orange
    Gold = Light.Gold
    Yellow = Light.Yellow
    Lime = Light.Lime
    Green = Light.Green
    Cyan = Light.Cyan
    Blue = Light.Blue
    ArcoBlue = Light.ArcoBlue
    Purple = Light.Purple
    PinkPurple = Light.PinkPurple
    Magenta = Light.Magenta
    Grey = Light.Grey
