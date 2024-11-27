import json
import os
import re
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

    def __new__(cls, paths: Union[str, list[str]] = None):
        if cls._instance is None:
            cls._instance = super(TokenManager,cls).__new__(cls)
        return cls._instance

    def __init__(self, paths: Union[str, list[str]] = None):
        self._load_tokens(paths)

    @property
    def mapping(self):
        return self._mapping

    def _load_tokens(self, paths: Union[str, list[str]]):
        self._tokens = []
        paths = paths if isinstance(paths, list) else [paths]
        for path in paths:
            self._load_token(path)
        self._create_token_mapping()

    def _load_token(self, path: str):
        self._tokens.append(file.read_json(path))

    def token(self, token_path: str) -> str:
        return self._mapping[token_path]

    def addToken(self, token: Dict[str, Any]) -> None:
        # 将新token添加到tokens列表
        self._tokens.append(token)

        # 更新mapping
        self._mapping.update(token)

        # 重新处理所有var()引用
        self._resolve_all_vars(token)

    def _resolve_all_vars(self, token: Dict[str, Any]) -> None:
        """解析并处理所有var()引用"""
        var_pattern = re.compile(r'(?<=var\()(.+?)(?=\))')

        for key, value in token.items():
            if not isinstance(value, str):
                continue

            # 查找并替换所有var()引用
            new_value = value
            for match in var_pattern.finditer(value):
                var_name = match.group(1)
                if var_name not in self._mapping:
                    raise KeyError(f"未找到变量定义: {var_name}")
                new_value = new_value.replace(f"var({var_name})", self._mapping[var_name])

            self._mapping[key] = new_value

    def _create_token_mapping(self):
        """创建样式令牌映射"""
        self._mapping = {}

        # 合并所有token
        for token in self._tokens:
            self._mapping.update(token)

            # 处理所有var()引用
            self._resolve_all_vars(token)



token_manager = TokenManager(':/pysidearcowidget/styletoken/token.json')
