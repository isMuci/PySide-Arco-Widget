from dataclasses import dataclass
from enum import Enum
import scheme as Scheme
from scheme import SchemeEnum


class ThemeEnum(Enum):
    def __new__(cls, value: SchemeEnum):
        self = object.__new__(cls)
        self._value_ = value
        return self

    @property
    def local(self):
        return self.value


class ArcoTheme(Enum):
    DARK = Scheme.DARKTheme
    LIGHT = Scheme.LIGHTTheme