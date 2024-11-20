import dataclasses
from enum import Enum
from dataclasses import dataclass
from PySide6.QtCore import QFile, QIODevice, QXmlStreamWriter, QXmlStreamReader, QUrl, QResource, QByteArray
from PySide6.QtGui import QIcon
from PySide6.QtSvg import QSvgRenderer
import xml.etree.ElementTree as ET


class SvgEnum(Enum):
    def __new__(cls, path):
        self = object.__new__(cls)
        self._value_ = f':/pysidearcowidget/image/icon/{path}.svg'
        return self

    @property
    def path(self):
        return self.value

    @property
    def svg(self):
        return QIcon(self.value)

    @property
    def renderer(self):
        return SVGRenderer(self.value)


class ArcoIcon(SvgEnum):
    Plus = 'Plus'
    Delete = 'Delete'
    Loading = 'Loading'


class SVGRenderer(QSvgRenderer):
    # :/pysidearcowidget/image/icon/Loading.svg
    def __init__(self, filename: str, parent=None):
        super().__init__()
        self.filename = filename
        self._xml = None
        self._rotate_animate_xml = None
        self.rotated = False

        self._load_xml(filename)

    def _load_xml(self, filename: str, sec=1):
        resource_data = QResource(filename)
        if resource_data.isValid():
            svg_data = resource_data.data()  # 获取资源文件的数据（返回的是 memoryview 类型）
            svg_xml = bytes(svg_data)  # 将 memoryview 转换为字节流
            root = ET.ElementTree(ET.fromstring(svg_xml))
            svg_root = root.getroot()

            self._xml = ET.tostring(svg_root, encoding='unicode')

            viewBox = svg_root.attrib.get('viewBox', None)
            if viewBox:
                # 解析 viewBox 的四个值：min-x, min-y, width, height
                min_x, min_y, width, height = map(float, viewBox.split())

                # 计算旋转中心（基于 viewBox 的宽度和高度）
                center_x = min_x + width / 2
                center_y = min_y + height / 2
            else:
                # 如果没有 viewBox，使用默认值
                width = float(svg_root.attrib['width']) if 'width' in svg_root.attrib else 24
                height = float(svg_root.attrib['height']) if 'height' in svg_root.attrib else 24
                center_x = width / 2
                center_y = height / 2

            # 包裹现有的内容到一个 <g> 元素中
            g_element = ET.Element('g')
            for child in list(svg_root):
                g_element.append(child)
                svg_root.remove(child)
            svg_root.append(g_element)
            animate_transform = ET.Element('animateTransform', {
                'attributeName': 'transform',
                'type': 'rotate',
                'from': f'0 {center_x} {center_y}',  # 旋转起始角度和旋转中心
                'to': f'360 {center_x} {center_y}',  # 旋转终止角度
                'dur': f'{sec}s',  # 动画持续时间
                'repeatCount': 'indefinite'  # 无限循环
            })
            g_element.append(animate_transform)

            self._rotate_animate_xml = ET.tostring(svg_root, encoding='unicode')
        else:
            print("Resource not found.")

    def setRotated(self, rotate: bool):
        self.rotated = rotate
        if rotate:
            self.load(QByteArray(self._rotate_animate_xml.encode('utf-8')))
        else:
            self.load(QByteArray(self._xml.encode('utf-8')))

    @staticmethod
    def _set_xml_attribute(node: ET.Element, attribute_name, value):
        node.set(attribute_name, value)

    def _set_svg_xml(self, xml, node_name, attribute_name, value):
        root = ET.ElementTree(ET.fromstring(xml))
        svg_root = root.getroot()
        for node in svg_root.findall(f'.//{node_name}'):
            self._set_xml_attribute(node, attribute_name, value)
        return ET.tostring(svg_root, encoding='unicode')

    def setSvgAttribute(self, node_name, attribute_name, value):
        self._xml = self._set_svg_xml(self._xml, node_name, attribute_name, value)
        self._rotate_animate_xml = self._set_svg_xml(self._rotate_animate_xml, node_name, attribute_name, value)
        self.setRotated(self.rotated)

    def setSvgFill(self, value):
        self.setSvgAttribute('path', 'fill', value)

    def setSvgStroke(self, value):
        self.setSvgAttribute('path', 'stroke', value)

    def setSvgStrokeWidth(self, value):
        self.setSvgAttribute('path', 'stroke-width', value)
