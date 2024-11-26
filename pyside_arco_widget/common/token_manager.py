import json
import os
from typing import Dict, Any, Union
from PySide6.QtCore import QFile, QResource, QTextStream

from pyside_arco_widget.common.config import Theme, Config
from pyside_arco_widget._rc import resource_rc
from pyside_arco_widget.common.util import file


class TokenManager:
    """样式令牌管理器"""

    _instance = None
    _tokens = []
    _mapping = {}

    def __init__(self, paths: Union[str, list[str]] = None):
        self.loadTokens(paths)

    @property
    def mapping(self):
        return self._mapping

    def loadTokens(self, paths: Union[str, list[str]]):
        self._tokens = []
        paths = paths if isinstance(paths, list) else [paths]
        for path in paths:
            self.loadToken(path)
        self._create_token_mapping()

    def loadToken(self, path: str):
        self._tokens.append(file.read_json(path))

    def token(self, token_path: str) -> str:
        return self._mapping[token_path]

    def _create_token_mapping(self):
        """创建样式令牌映射"""
        self._mapping = {}

        def add_mapping(prefix: str, data: Dict):
            for key, value in data.items():
                if isinstance(value, dict):
                    add_mapping(f"{prefix}{key}-", value)
                else:
                    self._mapping[f"{prefix}{key}"] = value

        for token in self._tokens:
            add_mapping("", token)


# 全局令牌管理器实例
theme_token_manager = TokenManager(':/pysidearcowidget/styletoken/base.json')
var_token_manager = TokenManager(':/pysidearcowidget/styletoken/var.json')