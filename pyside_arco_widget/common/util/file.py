import json
from typing import Union, Dict, Any

from PySide6.QtCore import QFile


def read(path: Union[str, QFile]):
    file = QFile(path)
    file.open(QFile.ReadOnly)
    data = file.readAll().data().decode('utf-8')
    file.close()
    return data


def read_json(path: str) -> Dict[str, Any]:
    data = read(path)
    return json.loads(data)
