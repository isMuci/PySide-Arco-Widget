from enum import Enum
from string import Template
from typing import List, Union
import weakref
from PySide6.QtCore import QObject, QEvent, QFile, QResource, QTextStream
from PySide6.QtWidgets import QWidget



class StyleSheetManager(QObject):
    """ Arco 样式表管理器 """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StyleSheetManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            super().__init__()
            self.widgets = weakref.WeakKeyDictionary()
            self.initialized = True

    def register(self, source, widget: QWidget, reset=True):
        """ 注册组件样式

        Parameters
        ----------
        source: str | StyleSheetBase
            样式源，可以是：
            * `str`: qss 文件路径
            * `StyleSheetBase`: 样式表实例

        widget: QWidget
            需要设置样式的组件

        reset: bool
            是否重置样式源
        """
        if isinstance(source, str):
            source = StyleSheetFile(source)

        if widget not in self.widgets:
            widget.destroyed.connect(self.deregister)
            widget.installEventFilter(StyleSheetWatcher(widget))
            widget.installEventFilter(DirtyStyleSheetWatcher(widget))
            self.widgets[widget] = StyleSheetCompose([source, StyleSheet(widget)])

        if not reset:
            self.source(widget).add(source)
        else:
            self.widgets[widget] = StyleSheetCompose([source, StyleSheet(widget)])

    def deregister(self, widget: QWidget):
        """ 注销组件样式 """
        if widget in self.widgets:
            self.widgets.pop(widget)

    def source(self, widget: QWidget):
        """ 获取组件的样式源 """
        return self.widgets.get(widget, StyleSheetCompose([]))


# 全局样式管理器实例
styleSheetManager = StyleSheetManager()


class QssTemplate(Template):
    """ 样式表模板 """
    delimiter = '--'



class StyleSheetBase:
    """ 样式表基类 """

    def path(self):
        """ 获取样式表路径 """
        raise NotImplementedError

    def content(self):
        """ 获取样式表内容 """
        return getStyleSheetFromFile(self.path())

    def apply(self, widget: QWidget):
        """ 应用样式表到组件 """
        setStyleSheet(widget, self)

class StyleSheetFile(StyleSheetBase):
    """ 样式表文件类 """

    def __init__(self, path: str):
        super().__init__()
        self.filePath = path

    def path(self):
        """ 获取样式表路径 """
        return self.filePath

class ArcoStyleSheet(StyleSheetBase, Enum):
    """ Arco 样式表 """

    # 基础组件
    Button = "button"
    ButtonGroup = "button-group"

    def path(self):
        return f":/pysidearcowidget/qss/{self.value}.qss"


class StyleSheetCompose(StyleSheetBase):
    """ 样式表组合 """

    def __init__(self, sources: List[StyleSheetBase]):
        super().__init__()
        self.sources = sources

    def content(self):
        return '\n'.join([i.content() for i in self.sources])

    def add(self, source: StyleSheetBase):
        """ 添加样式源 """
        if source is self or source in self.sources:
            return
        self.sources.append(source)

    def remove(self, source: StyleSheetBase):
        """ 移除样式源 """
        if source in self.sources:
            self.sources.remove(source)


class StyleSheet(StyleSheetBase):
    STYLE_SHEET_KEY = 'StyleSheet'

    def __init__(self, widget: QWidget):
        super().__init__()
        self.widget = widget

    def path(self):
        return ''

    def setStyleSheet(self, qss: str):
        self.widget.setProperty(self.STYLE_SHEET_KEY, qss)
        return self

    def content(self):
        return self.widget.property(self.STYLE_SHEET_KEY) or ''
    
class StyleSheetWatcher(QObject):
    """ 自定义样式表监听器 """

    def eventFilter(self, obj: QWidget, e: QEvent):
        if e.type() != QEvent.DynamicPropertyChange:
            return super().eventFilter(obj, e)

        name = e.propertyName().data().decode()
        if name in [StyleSheet.STYLE_SHEET_KEY]:
            addStyleSheet(obj, StyleSheet(obj))

        return super().eventFilter(obj, e)


class DirtyStyleSheetWatcher(QObject):
    """ 脏样式表监听器 """

    def eventFilter(self, obj: QWidget, e: QEvent):
        if e.type() != QEvent.Type.Paint or not obj.property('dirty-qss'):
            return super().eventFilter(obj, e)

        obj.setProperty('dirty-qss', False)
        if obj in styleSheetManager.widgets:
            obj.setStyleSheet(getStyleSheet(styleSheetManager.source(obj)))

        return super().eventFilter(obj, e)


def getStyleSheetFromFile(file: Union[str, QFile]):
    """ 从文件中获取样式表内容 """
    file = QFile(file)
    file.open(QFile.ReadOnly)
    stream = QTextStream(file)
    stylesheet = stream.readAll()
    file.close()
    return stylesheet


def getStyleSheet(source: Union[str, StyleSheetBase]):
    """ 获取样式表内容 """
    if isinstance(source, str):
        source = StyleSheetFile(source)
    return source.content()


def setStyleSheet(widget: QWidget, source: Union[str, StyleSheetBase]):
    """ 设置组件样式表 """
    if isinstance(source, str):
        source = StyleSheetFile(source)

    styleSheetManager.register(source, widget)
    qss = getStyleSheet(source)
    widget.setStyleSheet(qss)


def addStyleSheet(widget: QWidget, source: Union[str, StyleSheetBase]):
    """ 添加组件样式表 """
    if isinstance(source, str):
        source = StyleSheetFile(source)

    styleSheetManager.register(source, widget, False)
    qss = getStyleSheet(styleSheetManager.source(widget))
    # print(qss)
    widget.setStyleSheet(qss)
