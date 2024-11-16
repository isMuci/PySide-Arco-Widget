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


class Basic(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)
        self.button = Button('Primary', 'primary')
        self.button1 = Button('Secondary', 'secondary')
        self.button2 = Button('Dashed', 'dashed')
        self.button3 = Button('Outline', 'outline')
        self.button4 = Button('Text', 'text')
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)


class Icon(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)
        self.button = Button(btype='primary', icon=ArcoIcon.Plus.svg)
        self.button1 = Button('Delete', 'primary', icon=ArcoIcon.Delete.svg)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button1)


class Shape(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)
        self.button = Button(btype='primary', icon=ArcoIcon.Plus.svg)
        self.button1 = Button(btype='primary', icon=ArcoIcon.Plus.svg, shape='circle')
        self.button2 = Button('Primary', 'primary', shape='round')
        self.button3 = Button('Primary', 'primary')
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)


class Size(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)
        self.button = Button('Mini', 'primary', size='mini')
        self.button1 = Button('Small', 'primary', size='small')
        self.button2 = Button('Default', 'primary')
        self.button3 = Button('Large', 'primary', size='large')
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)


class Status(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.widget = QWidget()
        self.widget_layout = QHBoxLayout(self.widget)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setAlignment(Qt.AlignLeft)
        self.button = Button('Warning', btype='primary', status='warning')
        self.button.setFixedWidth(100)
        self.button1 = Button('Warning', status='warning')
        self.button1.setFixedWidth(100)
        self.button2 = Button('Warning', btype='dashed', status='warning')
        self.button2.setFixedWidth(100)
        self.button3 = Button('Warning', btype='outline', status='warning')
        self.button3.setFixedWidth(100)
        self.button4 = Button('Warning', btype='text', status='warning')
        self.button4.setFixedWidth(100)
        self.widget_layout.addWidget(self.button)
        self.widget_layout.addWidget(self.button1)
        self.widget_layout.addWidget(self.button2)
        self.widget_layout.addWidget(self.button3)
        self.widget_layout.addWidget(self.button4)
        self.layout.addWidget(self.widget)

        self.widget1 = QWidget()
        self.widget1_layout = QHBoxLayout(self.widget1)
        self.widget1_layout.setContentsMargins(0, 0, 0, 0)
        self.widget1_layout.setAlignment(Qt.AlignLeft)
        self.button5 = Button('Danger', btype='primary', status='danger')
        self.button5.setFixedWidth(100)
        self.button6 = Button('Danger', status='danger')
        self.button6.setFixedWidth(100)
        self.button7 = Button('Danger', btype='dashed', status='danger')
        self.button7.setFixedWidth(100)
        self.button8 = Button('Danger', btype='outline', status='danger')
        self.button8.setFixedWidth(100)
        self.button9 = Button('Danger', btype='text', status='danger')
        self.button9.setFixedWidth(100)
        self.widget1_layout.addWidget(self.button5)
        self.widget1_layout.addWidget(self.button6)
        self.widget1_layout.addWidget(self.button7)
        self.widget1_layout.addWidget(self.button8)
        self.widget1_layout.addWidget(self.button9)
        self.layout.addWidget(self.widget1)

        self.widget2 = QWidget()
        self.widget2_layout = QHBoxLayout(self.widget2)
        self.widget2_layout.setContentsMargins(0, 0, 0, 0)
        self.widget2_layout.setAlignment(Qt.AlignLeft)
        self.button10 = Button('Success', btype='primary', status='success')
        self.button10.setFixedWidth(100)
        self.button11 = Button('Success', status='success')
        self.button11.setFixedWidth(100)
        self.button12 = Button('Success', btype='dashed', status='success')
        self.button12.setFixedWidth(100)
        self.button13 = Button('Success', btype='outline', status='success')
        self.button13.setFixedWidth(100)
        self.button14 = Button('Success', btype='text', status='success')
        self.button14.setFixedWidth(100)
        self.widget2_layout.addWidget(self.button10)
        self.widget2_layout.addWidget(self.button11)
        self.widget2_layout.addWidget(self.button12)
        self.widget2_layout.addWidget(self.button13)
        self.widget2_layout.addWidget(self.button14)
        self.layout.addWidget(self.widget2)


class Disabled(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.widget = QWidget()
        self.widget_layout = QHBoxLayout(self.widget)
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setAlignment(Qt.AlignLeft)
        self.button = Button('Primary', btype='primary', disabled=True)
        self.button1 = Button('Secondary', disabled=True)
        self.button2 = Button('Dashed', btype='dashed', disabled=True)
        self.button3 = Button('Outline', btype='outline', disabled=True)
        self.button4 = Button('Text', btype='text', disabled=True)
        self.widget_layout.addWidget(self.button)
        self.widget_layout.addWidget(self.button1)
        self.widget_layout.addWidget(self.button2)
        self.widget_layout.addWidget(self.button3)
        self.widget_layout.addWidget(self.button4)
        self.layout.addWidget(self.widget)

        self.widget1 = QWidget()
        self.widget1_layout = QHBoxLayout(self.widget1)
        self.widget1_layout.setContentsMargins(0, 0, 0, 0)
        self.widget1_layout.setAlignment(Qt.AlignLeft)
        self.button5 = Button('Primary', btype='primary', status='danger', disabled=True)
        self.button6 = Button('Secondary', status='danger', disabled=True)
        self.button7 = Button('Dashed', btype='dashed', status='danger', disabled=True)
        self.button8 = Button('Outline', btype='outline', status='danger', disabled=True)
        self.button9 = Button('Text', btype='text', status='danger', disabled=True)
        self.widget1_layout.addWidget(self.button5)
        self.widget1_layout.addWidget(self.button6)
        self.widget1_layout.addWidget(self.button7)
        self.widget1_layout.addWidget(self.button8)
        self.widget1_layout.addWidget(self.button9)
        self.layout.addWidget(self.widget1)

        self.widget2 = QWidget()
        self.widget2_layout = QHBoxLayout(self.widget2)
        self.widget2_layout.setContentsMargins(0, 0, 0, 0)
        self.widget2_layout.setAlignment(Qt.AlignLeft)
        self.button10 = Button('Primary', btype='primary', status='warning', disabled=True)
        self.button11 = Button('Secondary', status='warning', disabled=True)
        self.button12 = Button('Dashed', btype='dashed', status='warning', disabled=True)
        self.button13 = Button('Outline', btype='outline', status='warning', disabled=True)
        self.button14 = Button('Text', btype='text', status='warning', disabled=True)
        self.widget2_layout.addWidget(self.button10)
        self.widget2_layout.addWidget(self.button11)
        self.widget2_layout.addWidget(self.button12)
        self.widget2_layout.addWidget(self.button13)
        self.widget2_layout.addWidget(self.button14)
        self.layout.addWidget(self.widget2)

        self.widget3 = QWidget()
        self.widget3_layout = QHBoxLayout(self.widget3)
        self.widget3_layout.setContentsMargins(0, 0, 0, 0)
        self.widget3_layout.setAlignment(Qt.AlignLeft)
        self.button15 = Button('Primary', btype='primary', status='success', disabled=True)
        self.button16 = Button('Secondary', status='success', disabled=True)
        self.button17 = Button('Dashed', btype='dashed', status='success', disabled=True)
        self.button18 = Button('Outline', btype='outline', status='success', disabled=True)
        self.button19 = Button('Text', btype='text', status='success', disabled=True)
        self.widget3_layout.addWidget(self.button15)
        self.widget3_layout.addWidget(self.button16)
        self.widget3_layout.addWidget(self.button17)
        self.widget3_layout.addWidget(self.button18)
        self.widget3_layout.addWidget(self.button19)
        self.layout.addWidget(self.widget3)


class ButtonDemo(BaseView):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.label = QLabel('基本用法')
        setFont(self.label, 20)
        self.layout.addWidget(self.label)
        self.layout.addWidget(Basic())

        self.label1 = QLabel('图标按钮')
        setFont(self.label1, 20)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(Icon())

        self.label2 = QLabel('按钮形状')
        setFont(self.label2, 20)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(Shape())

        self.label3 = QLabel('按钮尺寸')
        setFont(self.label3, 20)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(Size())

        self.label3 = QLabel('按钮状态')
        setFont(self.label3, 20)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(Status())

        self.label4 = QLabel('禁用按钮')
        setFont(self.label4, 20)
        self.layout.addWidget(self.label4)
        self.layout.addWidget(Disabled())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w1 = ButtonDemo()
    w1.show()
    app.exec()
