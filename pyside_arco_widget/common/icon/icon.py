from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, Qt, QPainter

from pyside_arco_widget.common.icon.svg import SVGRenderer


class SVGIcon:
    def __init__(self,parent, renderer: SVGRenderer, animation: bool = False,  size: QSize = QSize(14, 14)):
        self._parent = parent
        self._renderer = renderer
        self._size = size
        self._renderer.repaintNeeded.connect(self._repaint)
        self.setSVGAnimation(animation)

    def isNull(self):
        print('is null')
        return True if self._renderer else False

    def setSVGAnimation(self, animation: bool):
        self._renderer.setRotated(animation)

    @property
    def pixmap(self):
        pixmap = QPixmap(self._size)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        self._renderer.render(painter)
        painter.end()
        return pixmap.scaled(self._size)

    def _repaint(self):
        self._parent.setIcon(self.pixmap)
