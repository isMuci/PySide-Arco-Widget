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
from pyside_arco_widget.common.token_manager import token_manager


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
        self._disabled = None
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
        self.shape = shape
        self.bsize = size
        self.status = status
        self.setDisabled(disabled)
        self.setIcon(self._icon)
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
            self._loading.spin = False
            self._loading = None
            self.setIcon(self._icon)

            self._setText(not self._icon.isNull())

    def setIcon(self, icon: [QIcon | Icon | QPixmap]):
        if isinstance(icon, Icon):
            key = f"""color-button-{self._button_type}{f'-{self._status}' if self._status else ''}{f'-disabled' if self._disabled else ''}"""
            stroke = token_manager.mapping[key]
            # print(f'{key} : {stroke}')
            icon.renderer.setStroke(stroke)
            super().setIcon(icon.icon)
        else:
            super().setIcon(icon)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._overlay.setGeometry(self.rect())

    def setDisabled(self, disabled: bool):
        self._disabled = disabled
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
