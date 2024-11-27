from PySide6.QtGui import QIcon, QPixmap, Qt
from PySide6.QtWidgets import QPushButton, QWidget

from pyside_arco_widget.common.font import setFont
from pyside_arco_widget.common.icon.icon import Icon, ArcoIcon
from pyside_arco_widget.common.icon.svg import SVGRenderer
from pyside_arco_widget.common.style_sheet import ArcoStyleSheet
from pyside_arco_widget.common.token_manager import token_manager


class Link(QPushButton):
    def __init__(self, text: str = None, disabled: bool = False, status: str = None, icon: [bool|QIcon | SVGRenderer] = None,
                 hoverable: bool = True, icon_right: bool = False, parent=None):
        super().__init__(parent)

        self._text = text
        self._disabled = None
        self._status = None
        self._icon = QIcon()
        self._hoverable = None
        ArcoStyleSheet.Link.apply(self)
        setFont(self)
        self._setText(True if icon else False)
        if icon:
            if isinstance(icon, bool):
                self._icon = Icon(ArcoIcon.Link.renderer)
            elif isinstance(icon, QIcon):
                self._icon = icon
            elif isinstance(icon, SVGRenderer):
                self._icon = Icon(icon)
        self.status = status
        self.setDisabled(disabled)
        self.setIcon(self._icon)
        self.hoverable = hoverable
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
    def status(self):
        return self._status

    @status.setter
    def status(self, status: str):
        self._status = status
        self.setProperty('Status', status)

    @property
    def hoverable(self):
        return self._hoverable

    @hoverable.setter
    def hoverable(self, hoverable: bool):
        self._hoverable = hoverable
        self.setProperty('Hoverable', hoverable)

    def setIcon(self, icon: [QIcon | Icon | QPixmap]):
        if isinstance(icon, Icon):
            key = f"""color-link{f'-{self._status}' if self._status else ''}{f'-disabled' if self._disabled else ''}"""
            stroke = token_manager.mapping[key]
            # print(f'{key} : {stroke}')
            icon.renderer.setStroke(stroke)
            # print(icon.renderer._xml)
            super().setIcon(icon.icon)
        else:
            super().setIcon(icon)

    def setDisabled(self, disabled: bool):
        self._disabled = disabled
        self.setProperty('Disabled', disabled)
        super().setDisabled(disabled)

    def setEnabled(self, enabled: bool):
        self.setDisabled(not enabled)
