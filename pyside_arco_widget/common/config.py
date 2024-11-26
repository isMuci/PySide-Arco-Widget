from enum import Enum


class Theme(Enum):
    LIGHT = "Light"
    DARK = "Dark"
    AUTO = "Auto"


class Config:
    theme = Theme.LIGHT
