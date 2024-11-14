from functools import singledispatchmethod
from typing import Union

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QColor, Qt
from PySide6.QtWidgets import QPushButton, QWidget, QApplication, QGraphicsDropShadowEffect, QHBoxLayout, QSizePolicy

from pyside_arco_widget.common.font import setFont

style_base = """
    Button{
        padding: 0 15px;
        height: 32px;
        border-radius: 2px;
        font-size: 14px;
        outline: none;
    }
"""

style = {
    'primary': """
        Button{
            background-color: rgb(22,93,255);
            color: #ffffff;
            border: 1px solid transparent;
        }
        Button:hover{
            background-color: rgb(64,128,255);
        }
        Button:pressed{
            background-color: rgb(14,66,210);
        }
    """,
    'secondary': """
        Button{
            background-color: rgb(242,243,245);
            color: rgb(78,89,105);
            border: 1px solid transparent;
        }
        Button:hover{
            background-color: rgb(229,230,235);
        }
        Button:pressed{
            background-color: rgb(201,205,212);
        }
    """,
    'dashed': """
        Button{
            background-color: rgb(242,243,245);
            color: rgb(78,89,105);
            border: 1px dashed rgb(229,230,235);
        }
        Button:hover{
            background-color: rgb(229,230,235);
            border-color: rgb(201,205,212);
        }
        Button:pressed{
            background-color: rgb(201,205,212);
            border-color: rgb(169,174,184);
        }
    """,
    'outline': """
        Button{
            background-color: transparent;
            color: rgb(22,93,255);
            border: 1px solid rgb(22,93,255);
        }
        Button:hover{
            color: rgb(64,128,255);
            border-color: rgb(64,128,255);
        }
        Button:pressed{
            color: rgb(14,66,210);
            border-color: rgb(14,66,210);
        }
    """,
    'text': """
        Button{
            background-color: transparent;
            color: rgb(22,93,255);
            border: 1px solid transparent;
        }
        Button:hover{
            background-color: rgb(242,243,245);
        }
        Button:pressed{
            background-color: rgb(229,230,235);
        }
    """
}


class Button(QPushButton):
    def __init__(self, text: str = None, btype: str = 'primary', long: bool = False, parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setStyleSheet(style_base + style[btype])
        if not long:
            self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        setFont(self)
