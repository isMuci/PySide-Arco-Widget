import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel

from pyside_arco_widget.common.font import setFont
from pyside_arco_widget.common.icon.svg import ArcoIcon
from pyside_arco_widget.component.widget.button import Button


class BaseView(QWidget):

    def __init__(self):
        super().__init__()
        # setTheme(Theme.DARK)
        self.setStyleSheet("BaseView{background: rgb(255,255,255)}")
        self.setContentsMargins(50, 50, 50, 50)


class BasicUsage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.button = Button('Primary')
        self.button1 = Button('Secondary', 'secondary')
        self.button2 = Button('Dashed', 'dashed')
        self.button3 = Button('Outline', 'outline')
        self.button4 = Button('Text', 'text')
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)


class IconButton(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)
        self.button = Button(icon=ArcoIcon.Plus.svg)
        self.button1 = Button('Delete', icon=ArcoIcon.Delete.svg)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button1)


class ButtonShape(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)
        self.button = Button(icon=ArcoIcon.Plus.svg)
        self.button1 = Button(icon=ArcoIcon.Plus.svg, shape='circle')
        self.button2 = Button('Primary', shape='round')
        self.button3 = Button('Primary')
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)


class ButtonSize(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)
        self.button = Button('Mini', size='mini')
        self.button1 = Button('Small', size='small')
        self.button2 = Button('Default')
        self.button3 = Button('Large', size='large')
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)


class ButtonDemo(BaseView):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.label = QLabel('基本用法')
        setFont(self.label, 20)
        self.layout.addWidget(self.label)
        self.layout.addWidget(BasicUsage())

        self.label1 = QLabel('图标按钮')
        setFont(self.label1, 20)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(IconButton())

        self.label2 = QLabel('按钮形状')
        setFont(self.label2, 20)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(ButtonShape())

        self.label3 = QLabel('按钮尺寸')
        setFont(self.label3, 20)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(ButtonSize())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w1 = ButtonDemo()
    w1.show()
    app.exec()
