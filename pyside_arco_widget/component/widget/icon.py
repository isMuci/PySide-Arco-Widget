from PySide6.QtGui import QIcon, QPixmap, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import QSize, Qt, QTimer, QRectF
from PySide6.QtWidgets import QPushButton, QApplication


class Icon:
    def __init__(self,parent, svg_path: str, size: QSize = QSize(14, 14), step: int = 12):
        self.svg_path = svg_path
        self.size = size
        self.step = step
        self.frames = {}  # 缓存所有角度的帧
        self.parent = parent
        self.current_angle = 0  # 当前角度
        self.timer = None  # 定时器
        self.svg_renderer = QSvgRenderer(svg_path)  # 加载 SVG 渲染器
        self._pre_render_frames()

    def _pre_render_frames(self):
        for angle in range(0, 360, self.step):
            # 创建 Pixmap 用于绘制每一帧
            pixmap = QPixmap(self.size)
            pixmap.fill(Qt.transparent)

            painter = QPainter(pixmap)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)

            # 设置旋转变换
            painter.translate(self.size.width() / 2, self.size.height() / 2)
            painter.rotate(angle)
            painter.translate(-self.size.width() / 2, -self.size.height() / 2)

            # 渲染 SVG 到 Pixmap 中心
            target_rect = QRectF(0, 0, self.size.width(), self.size.height())
            self.svg_renderer.render(painter, target_rect)

            painter.end()

            # 缓存帧
            self.frames[angle] = pixmap

    def get_rotated_icon(self, angle: int) -> QIcon:
        normalized_angle = angle % 360
        closest_angle = (normalized_angle // self.step) * self.step
        return QIcon(self.frames[closest_angle])

    def start_rotation(self, interval: int = 33):
        if not self.parent:
            raise ValueError("Parent component is not set.")

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_parent_icon)
        self.timer.start(interval)

    def update_parent_icon(self):
        """
        更新父组件的图标。
        """
        self.current_angle = (self.current_angle + self.step) % 360
        icon = self.get_rotated_icon(self.current_angle)

        if isinstance(self.parent, QPushButton):
            self.parent.setIcon(icon)

    def stop_rotation(self):
        """
        停止定时器。
        """
        if self.timer:
            self.timer.stop()
            self.timer = None
