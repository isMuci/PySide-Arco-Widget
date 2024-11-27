import sys

from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QIcon, QFont, QPalette, QColor
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QGridLayout, \
    QScrollArea

from example.base_view import BaseView
from pyside_arco_widget.common.font import setFont
from pyside_arco_widget.common.icon.icon import ArcoIcon, Icon
from pyside_arco_widget.component.general.button import Button, ButtonGroup
from pyside_arco_widget.component.general.link import Link


class Basic(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)

        self.link = Link('Link')
        self.link1 = Link('Link',True)
        self.layout.addWidget(self.link)
        self.layout.addWidget(self.link1)


class Status(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.widget = QWidget()
        self.widget_layout = QHBoxLayout(self.widget)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setAlignment(Qt.AlignLeft)
        self.link = Link('Error Link', status='error')
        self.link.setFixedWidth(100)
        self.link1 = Link('Error Link', True, 'error')
        self.link1.setFixedWidth(100)
        self.widget_layout.addWidget(self.link)
        self.widget_layout.addWidget(self.link1)
        self.layout.addWidget(self.widget)

        self.widget1 = QWidget()
        self.widget_layout1 = QHBoxLayout(self.widget1)
        self.widget_layout1.setContentsMargins(0, 0, 0, 0)
        self.widget_layout1.setAlignment(Qt.AlignLeft)
        self.link2 = Link('Success Link', status='success')
        self.link2.setFixedWidth(100)
        self.link3 = Link('Success Link', True, 'success')
        self.link3.setFixedWidth(100)
        self.widget_layout1.addWidget(self.link2)
        self.widget_layout1.addWidget(self.link3)
        self.layout.addWidget(self.widget1)

        self.widget2 = QWidget()
        self.widget_layout2 = QHBoxLayout(self.widget2)
        self.widget_layout2.setContentsMargins(0, 0, 0, 0)
        self.widget_layout2.setAlignment(Qt.AlignLeft)
        self.link4 = Link('Warning Link', status='warning')
        self.link4.setFixedWidth(100)
        self.link5 = Link('Warning Link', True, 'warning')
        self.link5.setFixedWidth(100)
        self.widget_layout2.addWidget(self.link4)
        self.widget_layout2.addWidget(self.link5)
        self.layout.addWidget(self.widget2)

class Icon(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.widget = QWidget()
        self.widget_layout = QHBoxLayout(self.widget)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setAlignment(Qt.AlignLeft)
        self.link = Link('Hyperlinks', icon=True)
        self.link.setFixedWidth(100)
        self.link1 = Link('Hyperlinks', True,  icon=True)
        self.link1.setFixedWidth(100)
        self.widget_layout.addWidget(self.link)
        self.widget_layout.addWidget(self.link1)
        self.layout.addWidget(self.widget)

        self.widget1 = QWidget()
        self.widget_layout1 = QHBoxLayout(self.widget1)
        self.widget_layout1.setContentsMargins(0, 0, 0, 0)
        self.widget_layout1.setAlignment(Qt.AlignLeft)
        self.link2 = Link('Hyperlinks',icon=ArcoIcon.Edit.renderer)
        self.link2.setFixedWidth(100)
        self.link3 = Link('Hyperlinks', True, icon=ArcoIcon.Edit.renderer)
        self.link3.setFixedWidth(100)
        self.widget_layout1.addWidget(self.link2)
        self.widget_layout1.addWidget(self.link3)
        self.layout.addWidget(self.widget1)

class Hoverable(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)

        self.link = Link('Link',hoverable=False)
        self.link1 = Link('Link',status='error',hoverable=False)
        self.layout.addWidget(self.link)
        self.layout.addWidget(self.link1)

class LinkDemo(BaseView):

    def __init__(self, title: str = None):
        super().__init__(title)

        sections = [
            ('基础用法', Basic()),
            ('其他状态', Status()),
            ('图标', Icon()),
            ('悬浮状态样式', Hoverable()),
            ('配合dropdown使用', Hoverable())
        ]

        for title, widget in sections:
            self.addSection(title, widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = LinkDemo('图标 Icon')
    demo.resize(1280, 720)
    demo.show()
    app.exec()
