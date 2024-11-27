import sys

from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QIcon, QFont, QPalette, QColor
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QGridLayout, \
    QScrollArea

from example.base_view import BaseView
from pyside_arco_widget.common.font import setFont
from pyside_arco_widget.common.icon.icon import ArcoIcon, Icon
from pyside_arco_widget.component.general.button import Button, ButtonGroup


class Basic(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)

        self.icon = Icon(ArcoIcon.Star.renderer)
        self.label = QLabel()
        self.label.setPixmap(self.icon.icon)
        self.layout.addWidget(self.label)

        self.icon1 = Icon(ArcoIcon.Star.renderer)
        self.icon1.renderer.setStroke('#ffcd00')
        self.label1 = QLabel()
        self.label1.setPixmap(self.icon1.icon)
        self.layout.addWidget(self.label1)


class Spin(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)

        self.label = QLabel()
        self.icon = Icon(ArcoIcon.Sync.renderer, True, self.label.setPixmap, QSize(40, 40))
        self.label.setPixmap(self.icon.icon)
        self.layout.addWidget(self.label)


class IconDemo(BaseView):

    def __init__(self, title: str = None):
        super().__init__(title)

        sections = [
            ('基本用法', Basic()),
            ('加载中', Spin())
        ]

        for title, widget in sections:
            self.addSection(title, widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = IconDemo('图标 Icon')
    demo.resize(1280, 720)
    demo.show()
    app.exec()
