import dataclasses
from enum import Enum
from dataclasses import dataclass

from PySide6.QtGui import QIcon


@dataclass
class Svg:
    path: str

    @property
    def svg(self):
        return QIcon(self.path)


class SvgEnum(Enum):
    def __new__(cls, path):
        self = object.__new__(cls)
        self.path=f':/pysidearcowidget/image/icon/{path}.svg'
        self._value_ = Svg(self.path)
        return self

    @property
    def svg(self):
        return self.value.svg


class ArcoIcon(SvgEnum):
    Plus = 'Plus'
    Delete = 'Delete'
    Loading = 'Loading'


