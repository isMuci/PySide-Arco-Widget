from functools import singledispatchmethod
from typing import Union

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QColor, Qt, QPixmap
from PySide6.QtWidgets import QPushButton, QWidget, QApplication, QGraphicsDropShadowEffect, QHBoxLayout, QSizePolicy, \
    QButtonGroup

from pyside_arco_widget.common.font import setFont
from pyside_arco_widget.common.icon.icon import Icon, ArcoIcon
from pyside_arco_widget.common.icon.svg import SVGRenderer
from pyside_arco_widget.common.style_sheet import ArcoStyleSheet, addStyleSheet

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
    Button[Shape=circle], #LoadingOverlay[Shape=circle]{
        width: 32px;
        padding: 0;
        text-align: center;
        border-radius: 16px;
    }
    Button[Shape=round], #LoadingOverlay[Shape=round]{
        border-radius: 16px;
    }
    Button[Size=mini], #LoadingOverlay[Size=mini]{
        font-size: 12px;
        height: 24px;
    }
    Button[Size=small], #LoadingOverlay[Size=small]{
        height: 28px;
    }
    Button[Size=large], #LoadingOverlay[Size=large]{
        padding: 0 19px;
        height: 36px;
    }
    #LoadingOverlay {
        background: rgba(255, 255, 255, 0.4);
        border-radius: 2px;
        border: 1px solid transparent;
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
        Button[Loading=true]::before{
            content: "";
            position: absolute;
            top: -1px;
            right: -1px;
            bottom: -1px;
            left: -1px;
            z-index: 1;
            background: rgba(255, 255, 255, 0.4);
            border-radius: inherit;
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
    def __init__(self, text: str = None, button_type: str = 'secondary', icon: [QIcon | SVGRenderer] = None,
                 shape: str = 'square', size: str = 'default', status: str = None, disabled: bool = False,
                 loading: bool = False, long: bool = False, icon_right: bool = False, parent=None):
        super().__init__(parent)
        self._text = text
        self._button_type = None
        self._icon = QIcon()
        self._shape = None
        self._size = None
        self._status = None
        self._loading = None
        self._overlay = QWidget(self)
        self._overlay.setObjectName('LoadingOverlay')
        self._overlay.setVisible(False)
        self._long = None
        ArcoStyleSheet.Button.apply(self)
        setFont(self)
        self._setText(True if icon else False)
        self.buttonType = button_type
        if icon:
            if isinstance(icon, QIcon):
                self._icon = icon
            elif isinstance(icon, SVGRenderer):
                self._icon = Icon(icon)
            self.setIcon(self._icon)
        self.shape = shape
        self.bsize = size
        self.status = status
        self.setDisabled(disabled)
        if loading:
            self.setLoading(loading)
        self.long = long
        if icon_right:
            self.setLayoutDirection(Qt.RightToLeft)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text
        if isinstance(self._icon, Icon):
            self._setText(self._icon.renderer is not None)
        elif isinstance(self._icon, QIcon):
            self._setText(self._icon.isNull())

    def _setText(self, has_icon: bool):
        if self._text:
            self.setText(f"{' ' if has_icon else ''}{self._text}")
        else:
            self.setProperty('IconOnly', True)

    @property
    def buttonType(self):
        return self._button_type

    @buttonType.setter
    def buttonType(self, button_type: str):
        self._button_type = button_type
        self.setProperty('Type', button_type)

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, shape: str):
        self._shape = shape
        self.setProperty('Shape', shape)
        self._overlay.setProperty('Shape', shape)

    @property
    def bsize(self):
        return self._size

    @bsize.setter
    def bsize(self, size: str):
        self._size = size
        self.setProperty('Size', size)
        self._overlay.setProperty('Size', size)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: str):
        self._status = status
        self.setProperty('Status', status)

    @property
    def long(self):
        return self._long

    @long.setter
    def long(self, long: bool):
        self._long = long
        if long:
            self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        else:
            self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    def setLoading(self, loading: bool):
        self.setProperty('Loading', loading)
        self._overlay.setVisible(loading)
        super().setDisabled(loading)
        if loading:
            self._loading = Icon(ArcoIcon.Loading.renderer, True, self.setIcon, self.iconSize())
            self.setIcon(self._loading)
            self._setText(True)
        else:
            self._loading.spin=False
            self._loading = None
            self.setIcon(self._icon)

            self._setText(not self._icon.isNull())

    def setIcon(self, icon: [QIcon | Icon | QPixmap]):
        if isinstance(icon, Icon):
            super().setIcon(icon.pixmap)
        else:
            super().setIcon(icon)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._overlay.setGeometry(self.rect())

    def setDisabled(self, disabled: bool):
        self.setProperty('Disabled', disabled)
        super().setDisabled(disabled)

    def setEnabled(self, enabled: bool):
        self.setDisabled(not enabled)


class ButtonGroup(QWidget):
    def __init__(self, buttons: list[Button] = None, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(0)
        if buttons:
            self.addButtons(buttons)

    def addButtons(self, buttons: list[Button]):
        """添加一组按钮到ButtonGroup"""
        for i, button in enumerate(buttons):
            self.addButton(button)
            button.setProperty('Group', True)

            if i == 0:  # 第一个按钮
                button.setProperty('Position', 'first')
                addStyleSheet(button, ArcoStyleSheet.ButtonGroup)
            elif i == len(buttons) - 1:  # 最后一个按钮
                button.setProperty('Position', 'last')
                addStyleSheet(button, ArcoStyleSheet.ButtonGroup)
            else:  # 中间的按钮
                addStyleSheet(button, ArcoStyleSheet.ButtonGroup)

    def addButton(self, button: Button):
        """添加单个按钮到ButtonGroup"""
        # button.setInButtonGroup(True)
        self.layout.addWidget(button)
