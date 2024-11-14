from dataclasses import dataclass
from enum import Enum

from PySide6.QtGui import QColor

from pyside_arco_widget.common.util.color import hex_to_rgba


@dataclass
class Color:
    rgba: tuple[int, int, int, float]

    @property
    def color(self):
        return QColor(*self.rgba)


class ColorEnum(Enum):
    def __new__(cls, r, g, b, a=255):
        self = object.__new__(cls)
        self._value_ = Color((r, g, b, a))
        return self

    @property
    def hex(self):
        return self.value.HEX

    @property
    def color(self):
        return self.value.color
