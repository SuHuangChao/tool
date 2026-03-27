"""Tests for tools/encode.py"""

import pytest

from tools.encode import base64_decode, base64_encode, url_decode, url_encode


class TestBase64:
    def test_encode_ascii(self):
        assert base64_encode("hello") == "aGVsbG8="

    def test_encode_chinese(self):
        encoded = base64_encode("你好")
        assert base64_decode(encoded) == "你好"

    def test_decode_ascii(self):
        assert base64_decode("aGVsbG8=") == "hello"

    def test_roundtrip(self):
        for text in ("", "abc", "hello world", "Hello, 世界! 123"):
            assert base64_decode(base64_encode(text)) == text


class TestUrl:
    def test_encode_spaces(self):
        assert url_encode("hello world") == "hello%20world"

    def test_encode_special(self):
        result = url_encode("a=1&b=2")
        assert "=" not in result
        assert "&" not in result

    def test_decode(self):
        assert url_decode("hello%20world") == "hello world"

    def test_roundtrip(self):
        for text in ("", "hello", "hello world", "a=1&b=2", "中文"):
            assert url_decode(url_encode(text)) == text
