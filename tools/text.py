"""
文本工具 - Text utilities
支持字数统计、大小写转换、字符串处理
"""

import re
from typing import List


def word_count(text: str) -> int:
    """统计英文单词数 / Count the number of English words"""
    return len(re.findall(r"\b\w+\b", text))


def char_count(text: str, include_spaces: bool = True) -> int:
    """统计字符数 / Count characters

    Args:
        text: 输入文本 / Input text
        include_spaces: 是否包含空格（仅普通空格 ' '）/
                        Whether to include regular space characters (' ')

    Returns:
        字符数 / Character count
    """
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def line_count(text: str) -> int:
    """统计行数 / Count lines"""
    if not text:
        return 0
    return len(text.splitlines())


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """截断文本到指定长度 / Truncate text to a maximum length

    Args:
        text: 输入文本 / Input text
        max_length: 最大长度 / Maximum length
        suffix: 截断后缀 / Suffix to append when truncated

    Returns:
        截断后的文本 / Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def remove_extra_spaces(text: str) -> str:
    """移除多余空白（连续空格替换为单个）/ Remove extra whitespace"""
    return re.sub(r" +", " ", text).strip()


def camel_to_snake(name: str) -> str:
    """驼峰命名转下划线命名 / Convert camelCase to snake_case

    Example:
        camel_to_snake("helloWorld") -> "hello_world"
    """
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def snake_to_camel(name: str) -> str:
    """下划线命名转驼峰命名 / Convert snake_case to camelCase

    Example:
        snake_to_camel("hello_world") -> "helloWorld"
    """
    parts = name.split("_")
    return parts[0] + "".join(p.title() for p in parts[1:])


def extract_numbers(text: str) -> List[float]:
    """从文本中提取所有数字 / Extract all numbers from text"""
    return [float(n) for n in re.findall(r"-?\d+(?:\.\d+)?", text)]


def format_size(size_bytes: int) -> str:
    """将字节数格式化为人类可读的文件大小
    Format byte count to a human-readable file size string.

    Example:
        format_size(1536) -> "1.50 KB"
    """
    for unit in ("B", "KB", "MB", "GB", "TB", "PB"):
        if abs(size_bytes) < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} EB"
