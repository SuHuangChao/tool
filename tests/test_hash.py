"""Tests for tools/hash.py"""

import pytest

from tools.hash import md5, sha1, sha256, sha512


class TestHash:
    # Known hash values sourced from standard references
    def test_md5_empty(self):
        assert md5("") == "d41d8cd98f00b204e9800998ecf8427e"

    def test_md5_hello(self):
        assert md5("hello") == "5d41402abc4b2a76b9719d911017c592"

    def test_sha1_empty(self):
        assert sha1("") == "da39a3ee5e6b4b0d3255bfef95601890afd80709"

    def test_sha256_empty(self):
        assert sha256("") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

    def test_sha512_hello(self):
        result = sha512("hello")
        assert len(result) == 128  # SHA-512 produces 128 hex chars

    def test_different_inputs_differ(self):
        assert md5("a") != md5("b")
        assert sha256("a") != sha256("b")
