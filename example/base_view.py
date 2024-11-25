from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QLabel

from pyside_arco_widget.common.font import setFont


class BaseView(QWidget):
    def __init__(self, title: str = None):
        super().__init__()
        self.setWindowTitle(title)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.scroll_area = QScrollArea()
        self.scroll_area.setStyleSheet("""
            QScrollArea { 
                border: none; 
            }
        """)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.content_widget = QWidget()

        self.content_widget.setStyleSheet("background-color: rgb(255,255,255)")
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setAlignment(Qt.AlignTop)
        self.content_layout.setContentsMargins(50, 50, 50, 50)

        self.scroll_area.setWidget(self.content_widget)
        self.main_layout.addWidget(self.scroll_area)

    def addSection(self, title, widget):
        label = QLabel(title)
        setFont(label, 20)
        self.content_layout.addWidget(label)
        self.content_layout.addWidget(widget)
