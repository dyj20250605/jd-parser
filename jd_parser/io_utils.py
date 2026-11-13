import json
from pathlib import Path


def load_json(path: str | Path) -> dict:
    """读取 path 指向的 JSON 文件，返回字典"""
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save_json(data: dict, path: str | Path) -> None:
    """把字典保存成 JSON 文件"""
    temp = json.dumps(data, ensure_ascii=False, indent=2)
    Path(path).write_text(temp, encoding="utf-8")

def read_text(path: str | Path) -> str:
    """读取文本文件，返回字符串"""
    return Path(path).read_text(encoding="utf-8")