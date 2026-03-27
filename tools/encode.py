"""
编码/解码工具 - Encoding/Decoding utilities
支持 Base64、URL 编码解码
"""

import base64
import urllib.parse


def base64_encode(text: str, encoding: str = "utf-8") -> str:
    """将字符串编码为 Base64 / Encode a string to Base64"""
    return base64.b64encode(text.encode(encoding)).decode("ascii")


def base64_decode(text: str, encoding: str = "utf-8") -> str:
    """将 Base64 字符串解码 / Decode a Base64 string"""
    return base64.b64decode(text).decode(encoding)


def url_encode(text: str) -> str:
    """URL 编码 / URL-encode a string"""
    return urllib.parse.quote(text, safe="")


def url_decode(text: str) -> str:
    """URL 解码 / URL-decode a string"""
    return urllib.parse.unquote(text)


def base64_encode_file(file_path: str) -> str:
    """将文件内容编码为 Base64 / Encode file contents to Base64"""
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def base64_decode_file(b64_text: str, output_path: str) -> None:
    """将 Base64 字符串解码并写入文件 / Decode Base64 and write to file"""
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(b64_text))
