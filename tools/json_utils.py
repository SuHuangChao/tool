"""
JSON 工具 - JSON utilities
支持 JSON 格式化、验证、压缩
"""

import json
from typing import Any


def format_json(text: str, indent: int = 4, ensure_ascii: bool = False) -> str:
    """格式化 JSON 字符串 / Pretty-print a JSON string

    Args:
        text: JSON 字符串 / JSON string
        indent: 缩进空格数 / Number of spaces for indentation
        ensure_ascii: 是否转义非 ASCII 字符 / Whether to escape non-ASCII characters

    Returns:
        格式化后的 JSON 字符串 / Formatted JSON string
    """
    obj = json.loads(text)
    return json.dumps(obj, indent=indent, ensure_ascii=ensure_ascii)


def minify_json(text: str, ensure_ascii: bool = False) -> str:
    """压缩 JSON 字符串（去除多余空白）/ Minify a JSON string

    Args:
        text: JSON 字符串 / JSON string
        ensure_ascii: 是否转义非 ASCII 字符 / Whether to escape non-ASCII characters

    Returns:
        压缩后的 JSON 字符串 / Minified JSON string
    """
    obj = json.loads(text)
    return json.dumps(obj, separators=(",", ":"), ensure_ascii=ensure_ascii)


def is_valid_json(text: str) -> bool:
    """验证字符串是否是合法的 JSON / Check whether a string is valid JSON

    Note: An empty string is considered invalid JSON per RFC 8259.
    """
    try:
        json.loads(text)
        return True
    except (json.JSONDecodeError, ValueError):
        return False


def load_json(text: str) -> Any:
    """将 JSON 字符串解析为 Python 对象 / Parse a JSON string into a Python object"""
    return json.loads(text)


def dump_json(obj: Any, indent: int = 4, ensure_ascii: bool = False) -> str:
    """将 Python 对象序列化为 JSON 字符串 / Serialize a Python object to a JSON string"""
    return json.dumps(obj, indent=indent, ensure_ascii=ensure_ascii)
