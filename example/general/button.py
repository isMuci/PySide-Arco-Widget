import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QFont, QPalette, QColor
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QGridLayout, \
    QScrollArea

from example.base_view import BaseView
from pyside_arco_widget.common.font import setFont
from pyside_arco_widget.common.icon.icon import ArcoIcon
from pyside_arco_widget.component.general.button import Button, ButtonGroup


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
        self.button = Button(button_type='primary', icon=ArcoIcon.Plus.renderer)
        self.button1 = Button('Delete', 'primary', icon=ArcoIcon.Delete.renderer)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button1)


class Shape(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)
        self.button = Button(button_type='primary', icon=ArcoIcon.Plus.renderer)
        self.button1 = Button(button_type='primary', icon=ArcoIcon.Plus.renderer, shape='circle')
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
        self.button = Button('Warning', button_type='primary', status='warning')
        self.button.setFixedWidth(100)
        self.button1 = Button('Warning', status='warning')
        self.button1.setFixedWidth(100)
        self.button2 = Button('Warning', button_type='dashed', status='warning')
        self.button2.setFixedWidth(100)
        self.button3 = Button('Warning', button_type='outline', status='warning')
        self.button3.setFixedWidth(100)
        self.button4 = Button('Warning', button_type='text', status='warning')
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
        self.button5 = Button('Danger', button_type='primary', status='danger')
        self.button5.setFixedWidth(100)
        self.button6 = Button('Danger', status='danger')
        self.button6.setFixedWidth(100)
        self.button7 = Button('Danger', button_type='dashed', status='danger')
        self.button7.setFixedWidth(100)
        self.button8 = Button('Danger', button_type='outline', status='danger')
        self.button8.setFixedWidth(100)
        self.button9 = Button('Danger', button_type='text', status='danger')
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
        self.button10 = Button('Success', button_type='primary', status='success')
        self.button10.setFixedWidth(100)
        self.button11 = Button('Success', status='success')
        self.button11.setFixedWidth(100)
        self.button12 = Button('Success', button_type='dashed', status='success')
        self.button12.setFixedWidth(100)
        self.button13 = Button('Success', button_type='outline', status='success')
        self.button13.setFixedWidth(100)
        self.button14 = Button('Success', button_type='text', status='success')
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
        self.button = Button('Primary', button_type='primary', disabled=True)
        self.button1 = Button('Secondary', disabled=True)
        self.button2 = Button('Dashed', button_type='dashed', disabled=True)
        self.button3 = Button('Outline', button_type='outline', disabled=True)
        self.button4 = Button('Text', button_type='text', disabled=True)
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
        self.button5 = Button('Primary', button_type='primary', status='danger', disabled=True)
        self.button6 = Button('Secondary', status='danger', disabled=True)
        self.button7 = Button('Dashed', button_type='dashed', status='danger', disabled=True)
        self.button8 = Button('Outline', button_type='outline', status='danger', disabled=True)
        self.button9 = Button('Text', button_type='text', status='danger', disabled=True)
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
        self.button10 = Button('Primary', button_type='primary', status='warning', disabled=True)
        self.button11 = Button('Secondary', status='warning', disabled=True)
        self.button12 = Button('Dashed', button_type='dashed', status='warning', disabled=True)
        self.button13 = Button('Outline', button_type='outline', status='warning', disabled=True)
        self.button14 = Button('Text', button_type='text', status='warning', disabled=True)
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
        self.button15 = Button('Primary', button_type='primary', status='success', disabled=True)
        self.button16 = Button('Secondary', status='success', disabled=True)
        self.button17 = Button('Dashed', button_type='dashed', status='success', disabled=True)
        self.button18 = Button('Outline', button_type='outline', status='success', disabled=True)
        self.button19 = Button('Text', button_type='text', status='success', disabled=True)
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

        self.button3 = Button(button_type='primary', shape='circle', loading=True)
        self.button4 = Button(shape='circle', loading=True)
        self.button5 = Button(button_type='dashed', shape='circle', loading=True)
        self.layout.addWidget(self.button3, 1, 0)
        self.layout.addWidget(self.button4, 1, 1)
        self.layout.addWidget(self.button5, 1, 2)

        self.button6 = Button('Click Me', 'primary')
        self.button6.clicked.connect(lambda: self.button_clicked(self.button6))
        self.button7 = Button('Click Me', 'primary', ArcoIcon.Plus.renderer)
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
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(Qt.AlignLeft)
        self.button = Button('Publish')
        self.button1 = Button(icon=ArcoIcon.Down.renderer)
        self.button_group = ButtonGroup([self.button, self.button1])
        self.layout.addWidget(self.button_group, 0, 0, Qt.AlignLeft)

        self.button2 = Button('Publish', 'secondary')
        self.button3 = Button(button_type='secondary', icon=ArcoIcon.More.renderer)
        self.button_group1 = ButtonGroup([self.button2, self.button3])
        self.layout.addWidget(self.button_group1, 0, 1, Qt.AlignLeft)

        self.button4 = Button('Publish', 'primary')
        self.button5 = Button(button_type='primary', icon=ArcoIcon.Down.renderer)
        self.button_group2 = ButtonGroup([self.button4, self.button5])
        self.layout.addWidget(self.button_group2, 1, 0, Qt.AlignLeft)

        self.button6 = Button('Prev', 'primary', ArcoIcon.Left.renderer, 'round')
        self.button7 = Button('Next', 'primary', ArcoIcon.Right.renderer, 'round', icon_right=True)
        self.button_group3 = ButtonGroup([self.button6, self.button7])
        self.layout.addWidget(self.button_group3, 2, 0, Qt.AlignLeft)

        self.button8 = Button(button_type='primary', icon=ArcoIcon.Star.renderer)
        self.button9 = Button(button_type='primary', icon=ArcoIcon.Message.renderer)
        self.button10 = Button(button_type='primary', icon=ArcoIcon.Settings.renderer)
        self.button_group4 = ButtonGroup([self.button8, self.button9, self.button10])
        self.layout.addWidget(self.button_group4, 2, 1, Qt.AlignLeft)

        self.button11 = Button('Favorite','outline', status='success', icon=ArcoIcon.Star.renderer)
        self.button12 = Button('Setting', 'outline', ArcoIcon.Settings.renderer)
        self.button_group5 = ButtonGroup([self.button11, self.button12])
        self.layout.addWidget(self.button_group5, 2, 2, Qt.AlignLeft)


class Long(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(360)
        self.layout = QVBoxLayout(self)
        self.button = Button('Primary', 'primary', long=True)
        self.button1 = Button('Secondary', 'secondary', long=True)
        self.button2 = Button('Dashed', 'dashed', long=True)
        self.button3 = Button('Outline', 'outline', long=True)
        self.button4 = Button('Text', 'text', long=True)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)


class ButtonDemo(BaseView):
    def __init__(self, title: str = None):
        super().__init__(title)

        sections = [
            ('基本用法', Basic()),
            ('图标按钮', Icon()),
            ('按钮形状', Shape()),
            ('按钮尺寸', Size()),
            ('按钮状态', Status()),
            ('禁用按钮', Disabled()),
            ('加载中按钮', Loading()),
            ('组合按钮', Button_Group()),
            ('长按钮', Long())
        ]

        for title, widget in sections:
            self.addSection(title, widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ButtonDemo('按钮 Button')
    demo.resize(1280, 720)
    demo.show()
    app.exec()
