from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget


def setFont(widget: QWidget, fontSize=14, weight=QFont.Normal):
    widget.setFont(getFont(fontSize, weight))


def getFont(fontSize=14, weight=QFont.Normal):
    font = QFont()
    font.setFamilies(['Inter','-apple-system','BlinkMacSystemFont','PingFang SC','Hiragino Sans GB','noto sans','Microsoft YaHei','Helvetica Neue','Helvetica','Arial','sans-serif'])
    font.setPixelSize(fontSize)
    font.setWeight(weight)
    return font