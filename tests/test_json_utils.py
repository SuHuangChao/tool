"""Tests for tools/json_utils.py"""

import json

import pytest

from tools.json_utils import dump_json, format_json, is_valid_json, load_json, minify_json


class TestFormatJson:
    def test_format_simple(self):
        result = format_json('{"b":2,"a":1}', indent=2)
        parsed = json.loads(result)
        assert parsed == {"a": 1, "b": 2}
        assert "\n" in result

    def test_format_preserves_unicode(self):
        result = format_json('{"name":"张三"}', ensure_ascii=False)
        assert "张三" in result

    def test_invalid_raises(self):
        with pytest.raises(Exception):
            format_json("not json")


class TestMinifyJson:
    def test_minify(self):
        pretty = '{\n    "a": 1,\n    "b": 2\n}'
        minified = minify_json(pretty)
        assert "\n" not in minified
        assert " " not in minified
        assert json.loads(minified) == {"a": 1, "b": 2}


class TestIsValidJson:
    def test_valid(self):
        assert is_valid_json('{"key": "value"}') is True
        assert is_valid_json("[1, 2, 3]") is True
        assert is_valid_json('"hello"') is True

    def test_invalid(self):
        assert is_valid_json("{bad json}") is False
        assert is_valid_json("") is False


class TestLoadDump:
    def test_load_dump_roundtrip(self):
        obj = {"name": "Alice", "scores": [1, 2, 3]}
        assert load_json(dump_json(obj)) == obj
