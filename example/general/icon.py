import sys

from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QIcon, QFont, QPalette, QColor
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QGridLayout, \
    QScrollArea

from pyside_arco_widget.common.font import setFont
from pyside_arco_widget.common.icon.icon import ArcoIcon, Icon
from pyside_arco_widget.component.general.button import Button, ButtonGroup


class BaseView(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("BaseView{background-color: rgb(255,255,255)}")
        self.setContentsMargins(50, 50, 50, 50)


class Basic(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)

        self.icon = Icon(ArcoIcon.Star.renderer)
        self.label = QLabel()
        self.label.setPixmap(self.icon.pixmap)
        self.layout.addWidget(self.label)

        self.icon1 = Icon(ArcoIcon.Star.renderer)
        self.icon1.renderer.setStroke('#ffcd00')
        self.label1 = QLabel()
        self.label1.setPixmap(self.icon1.pixmap)
        self.layout.addWidget(self.label1)


class Spin(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)

        self.label = QLabel()
        self.icon = Icon(ArcoIcon.Sync.renderer, True, self.label.setPixmap, QSize(40, 40))
        self.label.setPixmap(self.icon.pixmap)
        self.layout.addWidget(self.label)

class ButtonDemo(BaseView):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)

        self.label = QLabel('基础用法')
        setFont(self.label, 20)
        self.layout.addWidget(self.label)
        self.layout.addWidget(Basic())

        self.label1 = QLabel('加载中')
        setFont(self.label1, 20)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(Spin())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setWidget(ButtonDemo())
    scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    scroll.resize(1280, 720)
    scroll.show()
    app.exec()
