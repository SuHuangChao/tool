"""Tests for tools/text.py"""

import pytest

from tools.text import (
    camel_to_snake,
    char_count,
    extract_numbers,
    format_size,
    line_count,
    remove_extra_spaces,
    snake_to_camel,
    truncate,
    word_count,
)


class TestCounts:
    def test_word_count(self):
        assert word_count("hello world foo") == 3
        assert word_count("") == 0

    def test_char_count_with_spaces(self):
        assert char_count("hello world") == 11

    def test_char_count_without_spaces(self):
        assert char_count("hello world", include_spaces=False) == 10

    def test_line_count(self):
        assert line_count("a\nb\nc") == 3
        assert line_count("") == 0
        assert line_count("single") == 1


class TestTruncate:
    def test_no_truncation_needed(self):
        assert truncate("hello", 10) == "hello"

    def test_truncation(self):
        result = truncate("hello world", 8)
        assert len(result) == 8
        assert result.endswith("...")

    def test_exact_length(self):
        assert truncate("hello", 5) == "hello"


class TestCaseConversion:
    def test_camel_to_snake(self):
        assert camel_to_snake("helloWorld") == "hello_world"
        assert camel_to_snake("myHTTPServer") == "my_http_server"
        assert camel_to_snake("alreadylower") == "alreadylower"

    def test_snake_to_camel(self):
        assert snake_to_camel("hello_world") == "helloWorld"
        assert snake_to_camel("my_http_server") == "myHttpServer"
        assert snake_to_camel("single") == "single"


class TestExtractNumbers:
    def test_extract(self):
        assert extract_numbers("abc 3.14 and -7 foo 42") == [3.14, -7.0, 42.0]

    def test_empty(self):
        assert extract_numbers("no numbers here") == []


class TestFormatSize:
    def test_bytes(self):
        assert format_size(500) == "500.00 B"

    def test_kilobytes(self):
        assert format_size(1024) == "1.00 KB"

    def test_megabytes(self):
        assert format_size(1024 * 1024) == "1.00 MB"


class TestRemoveExtraSpaces:
    def test_removes_extra(self):
        assert remove_extra_spaces("hello   world") == "hello world"

    def test_strips(self):
        assert remove_extra_spaces("  hello  ") == "hello"
