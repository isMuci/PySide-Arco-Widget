import sys

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout

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
        self.button = Button()
        self.layout.addWidget(self.button)


class ButtonDemo(BaseView):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(BasicUsage())
        self.layout.addWidget(IconButton())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w1 = ButtonDemo()
    w1.show()
    app.exec()
