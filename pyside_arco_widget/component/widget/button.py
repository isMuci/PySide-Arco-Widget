from functools import singledispatchmethod
from typing import Union

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QColor, Qt
from PySide6.QtWidgets import QPushButton, QWidget, QApplication, QGraphicsDropShadowEffect, QHBoxLayout, QSizePolicy

from pyside_arco_widget.common.font import setFont
from pyside_arco_widget.common.icon.svg import ArcoIcon
from pyside_arco_widget.component.widget.icon import Icon

style_base = """
    Button{
        padding: 0 15px;
        height: 32px;
        border-radius: 2px;
        font-size: 14px;
        outline: none;
        background-color: rgb(242,243,245);
        color: rgb(78,89,105);
        border: 1px solid transparent;
    }
    Button:hover{
        background-color: rgb(229,230,235);
    }
    Button:pressed{
        background-color: rgb(201,205,212);
    }
    Button[IconOnly=true]{
        width: 32px;
        padding: 0;
    }
    Button[Shape=circle]{
        width: 32px;
        padding: 0;
        text-align: center;
        border-radius: 16px;
    }
    Button[Shape=round]{
        border-radius: 16px;
    }
    Button[Size=mini]{
        font-size: 12px;
        height: 24px;
    }
    Button[Size=small]{
        height: 28px;
    }
    Button[Size=large]{
        padding: 0 19px;
        height: 36px;
    }
"""

style = {
    'primary': """
        Button{
            background-color: rgb(22,93,255);
            color: #ffffff;
            border: 1px solid transparent;
        }
        Button[Disabled=true]{
            background-color: rgb(148,191,255);
        }
        Button:hover{
            background-color: rgb(64,128,255);
        }
        Button:pressed{
            background-color: rgb(14,66,210);
        }
        Button[Status=warning]{
            background-color: rgb(255,150,38);
        }
        Button[Status=warning][Disabled=true]{
            background-color: rgb(255,207,139);
        }
        Button[Status=warning]:hover{
            background-color: rgb(255,154,46);
        }
        Button[Status=warning]:pressed{
            background-color: rgb(210,95,0);
        }
        Button[Status=danger]{
            background-color: rgb(245,63,63);
        }
        Button[Status=danger][Disabled=true]{
            background-color: rgb(251,172,163);
        }
        Button[Status=danger]:hover{
            background-color: rgb(247,101,96);
        }
        Button[Status=danger]:pressed{
            background-color: rgb(203,39,45);
        }
        Button[Status=success]{
            background-color: rgb(0,180,42);
        }
        Button[Status=success][Disabled=true]{
            background-color: rgb(123,225,136);
        }
        Button[Status=success]:hover{
            background-color: rgb(35,195,67);
        }
        Button[Status=success]:pressed{
            background-color: rgb(0,154,41);
        }
    """,
    'secondary': """
        Button[Disabled=true]{
            background-color: rgb(247,248,250);
            color: rgb(201,205,212);
        }
        Button:hover{
            background-color: rgb(229,230,235);
        }
        Button:pressed{
            background-color: rgb(201,205,212);
        }
        Button[Status=warning]{
            background-color: rgb(255,247,232);
            color: rgb(255,125,0);
        }
        Button[Status=warning][Disabled=true]{
            color: rgb(255,207,139);
        }
        Button[Status=warning]:hover{
            background-color: rgb(255,228,186);
        }
        Button[Status=warning]:pressed{
            background-color: rgb(255,207,139);
        }
        Button[Status=danger]{
            background-color: rgb(255,236,232);
            color: rgb(245,63,63);
        }
        Button[Status=danger][Disabled=true]{
            color: rgb(251,172,163);
        }
        Button[Status=danger]:hover{
            background-color: rgb(253,205,197);
        }
        Button[Status=danger]:pressed{
            background-color: rgb(251,172,163);
        }
        Button[Status=success]{
            background-color: rgb(232,255,234);
            color: rgb(0,180,42);
        }
        Button[Status=success][Disabled=true]{
            color: rgb(123,225,136);
        }
        Button[Status=success]:hover{
            background-color: rgb(175,240,181);
        }
        Button[Status=success]:pressed{
            background-color: rgb(123,225,136);
        }
    """,
    'dashed': """
        Button{
            border: 1px dashed rgb(229,230,235);
        }
        Button[Disabled=true]{
            color: rgb(201,205,212);
        }
        Button:hover{
            background-color: rgb(229,230,235);
            border-color: rgb(201,205,212);
        }
        Button:pressed{
            background-color: rgb(201,205,212);
            border-color: rgb(169,174,184);
        }
        Button[Status=warning]{
            background-color: rgb(255,247,232);
            color: rgb(255,125,0);
            border-color: rgb(255,228,186);
        }
        Button[Status=warning][Disabled=true]{
            color: rgb(255,207,139);
        }
        Button[Status=warning]:hover{
            background-color: rgb(255,228,186);
            border-color: rgb(255,207,139);
        }
        Button[Status=warning]:pressed{
            background-color: rgb(255,207,139);
            border-color: rgb(255,182,93);
        }
        Button[Status=danger]{
            background-color: rgb(255,236,232);
            color: rgb(245,63,63);
            border-color: rgb(253,205,197);
        }
        Button[Status=danger][Disabled=true]{
            color: rgb(251,172,163);
        }
        Button[Status=danger]:hover{
            background-color: rgb(253,205,197);
            border-color: rgb(251,172,163);
        }
        Button[Status=danger]:pressed{
            background-color: rgb(251,172,163);
            border-color: rgb(249,137,129);
        }
        Button[Status=success]{
            background-color: rgb(232,255,234);
            color: rgb(0,180,42);
            border-color: rgb(175,240,181);
        }
        Button[Status=success][Disabled=true]{
            color: rgb(123,225,136);
        }
        Button[Status=success]:hover{
            background-color: rgb(175,240,181);
            border-color: rgb(123,225,136);
        }
        Button[Status=success]:pressed{
            background-color: rgb(123,225,136);
            border-color: rgb(76,210,99);
        }
    """,
    'outline': """
        Button{
            background-color: transparent;
            color: rgb(22,93,255);
            border: 1px solid rgb(22,93,255);
        }
        Button[Disabled=true]{
            color: rgb(148,191,255);
            border: 1px solid rgb(148,191,255);
        }
        Button:hover{
            color: rgb(64,128,255);
            border-color: rgb(64,128,255);
            background-color: transparent;
        }
        Button:pressed{
            color: rgb(14,66,210);
            border-color: rgb(14,66,210);
            background-color: transparent;
        }
        Button[Status=warning]{
            color: rgb(255,125,0);
            border-color: rgb(255,125,0);
        }
        Button[Status=warning][Disabled=true]{
            color: rgb(255,207,139);
            border-color: rgb(255,207,139);
        }
        Button[Status=warning]:hover{
            color: rgb(255,154,46);
            border-color: rgb(255,154,46);
            background-color: transparent;
        }
        Button[Status=warning]:pressed{
            color: rgb(210,95,0);
            border-color: rgb(210,95,0);
        }
        Button[Status=danger]{
            color: rgb(245,63,63);
            border-color: rgb(245,63,63);
        }
        Button[Status=danger][Disabled=true]{
            color: rgb(251,172,163);
            border-color: rgb(251,172,163);
        }
        Button[Status=danger]:hover{
            color: rgb(247,101,96);
            border-color: rgb(247,101,96);
            background-color: transparent;
        }
        Button[Status=danger]:pressed{
            color: rgb(203,39,45);
            border-color: rgb(203,39,45);
        }
        Button[Status=success]{
            color: rgb(0,180,42);
            border-color: rgb(0,180,42);
        }
        Button[Status=success][Disabled=true]{
            color: rgb(123,225,136);
            border-color: rgb(123,225,136);
        }
        Button[Status=success]:hover{
            color: rgb(35,195,67);
            border-color: rgb(35,195,67);
            background-color: transparent;
        }
        Button[Status=success]:pressed{
            color: rgb(0,154,41);
            border-color: rgb(0,154,41);
        }
    """,
    'text': """
        Button{
            background-color: transparent;
            color: rgb(22,93,255);
            border: 1px solid transparent;
        }
        Button[Disabled=true]{
            color: rgb(148,191,255);
        }
        Button:hover{
            background-color: rgb(242,243,245);
        }
        Button:pressed{
            background-color: rgb(229,230,235);
        }
        Button[Status=warning]{
            color: rgb(255,125,0);
        }
        Button[Status=warning][Disabled=true]{
            color: rgb(255,207,139);
        }
        Button[Status=danger]{
            color: rgb(245,63,63);
        }
        Button[Status=danger][Disabled=true]{
            color: rgb(251,172,163);
        }
        Button[Status=success]{
            color: rgb(0,180,42);
        }
        Button[Status=success][Disabled=true]{
            color: rgb(123,225,136);
        }
    """
}

icon_size = {
    'mini': 12,
    'small': 14,
    'default': 14,
    'large': 14
}


class Button(QPushButton):
    def __init__(self, text: str = None, btype: str = 'secondary', icon: QIcon = None, shape: str = 'square',
                 size: str = 'default', status: str = None, disabled: bool = False, loading: bool = False,
                 long: bool = False,
                 parent=None):
        super().__init__(parent)
        self._loading = None
        self.setStyleSheet(style_base + style[btype])
        setFont(self)
        self._text = text
        self.setText(True if icon else False)
        self.setIconSize(QSize(icon_size[size], icon_size[size]))
        if icon:
            self._icon = icon
            self.setIcon(icon)
        self.setProperty('Shape', shape)
        self.setProperty('Size', size)
        if status:
            self.setProperty('Status', status)
        self.setDisabled(disabled)
        if loading:
            self.setLoading(loading)
        if not long:
            self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    def setDisabled(self, arg__1: bool) -> None:
        self.setProperty('Disabled', arg__1)
        super().setDisabled(arg__1)

    def setEnabled(self, arg__1: bool) -> None:
        self.setProperty('Disabled', not arg__1)
        super().setEnabled(arg__1)

    def setText(self, has_icon: bool = True):
        if self._text:
            super().setText(f'{' ' if has_icon else ''}{self._text}')
        else:
            self.setProperty('IconOnly', True)

    def setLoading(self, loading: bool):
        self.setProperty('Loading', loading)
        if loading:
            if not self._loading:
                self._loading = Icon(self, ArcoIcon.Loading.path, self.iconSize())
            self._loading.start_rotation()
            self.setText(loading)
        else:
            self._loading.stop_rotation()
            self.setIcon(self._icon)
            self.setText(loading)
