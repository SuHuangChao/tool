"""
哈希工具 - Hash utilities
支持 MD5、SHA1、SHA256、SHA512
"""

import hashlib


def md5(text: str, encoding: str = "utf-8") -> str:
    """计算字符串的 MD5 哈希值 / Compute MD5 hash of a string"""
    return hashlib.md5(text.encode(encoding)).hexdigest()


def sha1(text: str, encoding: str = "utf-8") -> str:
    """计算字符串的 SHA1 哈希值 / Compute SHA1 hash of a string"""
    return hashlib.sha1(text.encode(encoding)).hexdigest()


def sha256(text: str, encoding: str = "utf-8") -> str:
    """计算字符串的 SHA256 哈希值 / Compute SHA256 hash of a string"""
    return hashlib.sha256(text.encode(encoding)).hexdigest()


def sha512(text: str, encoding: str = "utf-8") -> str:
    """计算字符串的 SHA512 哈希值 / Compute SHA512 hash of a string"""
    return hashlib.sha512(text.encode(encoding)).hexdigest()


def md5_file(file_path: str) -> str:
    """计算文件的 MD5 哈希值 / Compute MD5 hash of a file"""
    h = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_file(file_path: str) -> str:
    """计算文件的 SHA256 哈希值 / Compute SHA256 hash of a file"""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()
