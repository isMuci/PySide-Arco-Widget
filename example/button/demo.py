import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QGridLayout, \
    QScrollArea

from pyside_arco_widget.common.font import setFont
from pyside_arco_widget.common.icon.svg import ArcoIcon
from pyside_arco_widget.component.widget.button import Button, ButtonGroup


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
        self.button = Button(bType='primary', icon=ArcoIcon.Plus.svg)
        self.button1 = Button('Delete', 'primary', icon=ArcoIcon.Delete.svg)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button1)


class Shape(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)
        self.button = Button(bType='primary', icon=ArcoIcon.Plus.svg)
        self.button1 = Button(bType='primary', icon=ArcoIcon.Plus.svg, shape='circle')
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
        self.button = Button('Warning', bType='primary', status='warning')
        self.button.setFixedWidth(100)
        self.button1 = Button('Warning', status='warning')
        self.button1.setFixedWidth(100)
        self.button2 = Button('Warning', bType='dashed', status='warning')
        self.button2.setFixedWidth(100)
        self.button3 = Button('Warning', bType='outline', status='warning')
        self.button3.setFixedWidth(100)
        self.button4 = Button('Warning', bType='text', status='warning')
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
        self.button5 = Button('Danger', bType='primary', status='danger')
        self.button5.setFixedWidth(100)
        self.button6 = Button('Danger', status='danger')
        self.button6.setFixedWidth(100)
        self.button7 = Button('Danger', bType='dashed', status='danger')
        self.button7.setFixedWidth(100)
        self.button8 = Button('Danger', bType='outline', status='danger')
        self.button8.setFixedWidth(100)
        self.button9 = Button('Danger', bType='text', status='danger')
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
        self.button10 = Button('Success', bType='primary', status='success')
        self.button10.setFixedWidth(100)
        self.button11 = Button('Success', status='success')
        self.button11.setFixedWidth(100)
        self.button12 = Button('Success', bType='dashed', status='success')
        self.button12.setFixedWidth(100)
        self.button13 = Button('Success', bType='outline', status='success')
        self.button13.setFixedWidth(100)
        self.button14 = Button('Success', bType='text', status='success')
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
        self.button = Button('Primary', bType='primary', disabled=True)
        self.button1 = Button('Secondary', disabled=True)
        self.button2 = Button('Dashed', bType='dashed', disabled=True)
        self.button3 = Button('Outline', bType='outline', disabled=True)
        self.button4 = Button('Text', bType='text', disabled=True)
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
        self.button5 = Button('Primary', bType='primary', status='danger', disabled=True)
        self.button6 = Button('Secondary', status='danger', disabled=True)
        self.button7 = Button('Dashed', bType='dashed', status='danger', disabled=True)
        self.button8 = Button('Outline', bType='outline', status='danger', disabled=True)
        self.button9 = Button('Text', bType='text', status='danger', disabled=True)
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
        self.button10 = Button('Primary', bType='primary', status='warning', disabled=True)
        self.button11 = Button('Secondary', status='warning', disabled=True)
        self.button12 = Button('Dashed', bType='dashed', status='warning', disabled=True)
        self.button13 = Button('Outline', bType='outline', status='warning', disabled=True)
        self.button14 = Button('Text', bType='text', status='warning', disabled=True)
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
        self.button15 = Button('Primary', bType='primary', status='success', disabled=True)
        self.button16 = Button('Secondary', status='success', disabled=True)
        self.button17 = Button('Dashed', bType='dashed', status='success', disabled=True)
        self.button18 = Button('Outline', bType='outline', status='success', disabled=True)
        self.button19 = Button('Text', bType='text', status='success', disabled=True)
        self.widget3_layout.addWidget(self.button15)
        self.widget3_layout.addWidget(self.button16)
        self.widget3_layout.addWidget(self.button17)
        self.widget3_layout.addWidget(self.button18)
        self.widget3_layout.addWidget(self.button19)
        self.layout.addWidget(self.widget3)


class Loading(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)

        self.button = Button('Loading', 'primary', loading=True)
        self.button.setFixedWidth(100)
        self.button1 = Button('Loading', loading=True)
        self.button1.setFixedWidth(100)
        self.button2 = Button('Loading', 'dashed', loading=True)
        self.button2.setFixedWidth(100)
        self.layout.addWidget(self.button, 0, 0)
        self.layout.addWidget(self.button1, 0, 1)
        self.layout.addWidget(self.button2, 0, 2)

        self.button3 = Button(bType='primary', shape='circle', loading=True)
        self.button4 = Button(shape='circle', loading=True)
        self.button5 = Button(bType='dashed', shape='circle', loading=True)
        self.layout.addWidget(self.button3, 1, 0)
        self.layout.addWidget(self.button4, 1, 1)
        self.layout.addWidget(self.button5, 1, 2)

        self.button6 = Button('Click Me', 'primary')
        self.button6.clicked.connect(lambda: self.button_clicked(self.button6))
        self.button7 = Button('Click Me', 'primary', ArcoIcon.Plus.svg)
        self.button7.clicked.connect(lambda: self.button_clicked(self.button7))
        self.layout.addWidget(self.button6, 2, 0)
        self.layout.addWidget(self.button7, 2, 1)

    def button_clicked(self, button):
        button.setLoading(True)
        QTimer.singleShot(2000, lambda: self.button_finished(button))

    @staticmethod
    def button_finished(button):
        button.setLoading(False)

class Button_Group(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.button = Button('Prev', 'primary', ArcoIcon.Left.svg)
        self.button1 = Button('Next', 'primary', ArcoIcon.Right.svg,iconRight=True)
        self.button_group = ButtonGroup([self.button, self.button1])
        self.layout.addWidget(self.button_group)

        self.button2 = Button(bType='primary', icon=ArcoIcon.Start.svg)
        self.button3 = Button(bType='primary', icon=ArcoIcon.Message.svg)
        self.button4 = Button(bType='primary', icon=ArcoIcon.Settings.svg)
        self.button_group2 = ButtonGroup([self.button2, self.button3, self.button4])
        self.layout.addWidget(self.button_group2)


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

        self.label5 = QLabel('加载中按钮')
        setFont(self.label5, 20)
        self.layout.addWidget(self.label5)
        self.layout.addWidget(Loading())

        self.label6 = QLabel('组合按钮')
        setFont(self.label6, 20)
        self.layout.addWidget(self.label6)
        self.layout.addWidget(Button_Group())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w1 = ButtonDemo()
    w1.show()
    app.exec()
