import dataclasses
from enum import Enum
from dataclasses import dataclass

from PySide6.QtCore import QFile, QIODevice, QXmlStreamWriter, QXmlStreamReader, QUrl, QResource, QByteArray
from PySide6.QtGui import QIcon
from PySide6.QtSvg import QSvgRenderer
from pyside_arco_widget._rc import resource_rc


@dataclass
class Svg:
    path: str

    @property
    def svg(self):
        return QIcon(self.path)


class SvgEnum(Enum):
    def __new__(cls, path):
        self = object.__new__(cls)
        self.path = f':/pysidearcowidget/image/icon/{path}.svg'
        self._value_ = Svg(self.path)
        return self

    @property
    def svg(self):
        return self.value.svg


class ArcoIcon(SvgEnum):
    Plus = 'Plus'
    Delete = 'Delete'
    Loading = 'Loading'


import xml.etree.ElementTree as ET
class SVGXml:
    # : / pysidearcowidget / image / icon / Loading.svg
    def __init__(self, filename: str, parent=None):
        super().__init__()
        self.filename = filename
        self.xml = None
        self.animatedXml = None

        self.load(filename)
        print(self.xml)
        print(self.animatedXml)

    def load(self, filename: str,sec=1):
        """
        从指定路径加载 SVG 文件，并初始化渲染器。
        """
        resource_data = QResource(filename)
        # 读取数据并解析 SVG（XML）
        # 读取数据并解析 SVG（XML）
        if resource_data.isValid():
            svg_data = resource_data.data()  # 获取资源文件的数据（返回的是 memoryview 类型）
            svg_xml = bytes(svg_data)  # 将 memoryview 转换为字节流

            # 使用 xml.etree.ElementTree 解析 XML 数据
            root = ET.ElementTree(ET.fromstring(svg_xml))

            # 获取根元素
            svg_root = root.getroot()
            xml = ET.tostring(svg_root, encoding='unicode')
            self.xml = QByteArray(xml.encode('utf-8'))

            # 获取 SVG 的 viewBox 属性（如果存在）
            viewBox = svg_root.attrib.get('viewBox', None)

            if viewBox:
                # 解析 viewBox 的四个值：min-x, min-y, width, height
                min_x, min_y, width, height = map(float, viewBox.split())

                # 计算旋转中心（基于 viewBox 的宽度和高度）
                center_x = min_x + width / 2
                center_y = min_y + height / 2
            else:
                # 如果没有 viewBox，使用默认值
                width = float(svg_root.attrib['width']) if 'width' in svg_root.attrib else 100
                height = float(svg_root.attrib['height']) if 'height' in svg_root.attrib else 100
                center_x = width / 2
                center_y = height / 2

            # 查找所有的 <path> 元素并添加旋转动画
            for path in svg_root.findall('.//path'):
                # 创建动画元素 <animateTransform>，设置旋转动画
                animate_transform = ET.Element('animateTransform', {
                    'attributeName': 'transform',
                    'type': 'rotate',
                    'from': f'0 {center_x} {center_y}',  # 旋转起始角度和旋转中心
                    'to': f'360 {center_x} {center_y}',  # 旋转终止角度
                    'dur': f'{sec}s',  # 动画持续时间
                    'repeatCount': 'indefinite'  # 无限循环
                })

                # 将动画元素添加到 <path> 元素中
                path.append(animate_transform)

            # 将修改后的 XML 导出为字符串（或者保存为文件）
            animatedXml = ET.tostring(svg_root, encoding='unicode')
            self.animatedXml = QByteArray(animatedXml.encode('utf-8'))



        else:
            print("Resource not found.")
