"""Tests for the CLI entry point (main.py)"""

import pytest

from main import main


class TestEncodeCLI:
    def test_b64enc(self, capsys):
        main(["encode", "b64enc", "hello"])
        captured = capsys.readouterr()
        assert captured.out.strip() == "aGVsbG8="

    def test_b64dec(self, capsys):
        main(["encode", "b64dec", "aGVsbG8="])
        captured = capsys.readouterr()
        assert captured.out.strip() == "hello"

    def test_urlenc(self, capsys):
        main(["encode", "urlenc", "hello world"])
        captured = capsys.readouterr()
        assert captured.out.strip() == "hello%20world"

    def test_urldec(self, capsys):
        main(["encode", "urldec", "hello%20world"])
        captured = capsys.readouterr()
        assert captured.out.strip() == "hello world"


class TestHashCLI:
    def test_md5(self, capsys):
        main(["hash", "md5", "hello"])
        captured = capsys.readouterr()
        assert captured.out.strip() == "5d41402abc4b2a76b9719d911017c592"

    def test_sha256(self, capsys):
        main(["hash", "sha256", ""])
        captured = capsys.readouterr()
        assert captured.out.strip() == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


class TestTimeCLI:
    def test_now(self, capsys):
        main(["time", "now"])
        captured = capsys.readouterr()
        assert "timestamp" in captured.out
        assert "datetime" in captured.out

    def test_ts2dt(self, capsys):
        main(["time", "ts2dt", "0"])
        captured = capsys.readouterr()
        # Result depends on local timezone; just check format
        assert len(captured.out.strip()) == 19

    def test_duration(self, capsys):
        main(["time", "duration", "3661"])
        captured = capsys.readouterr()
        assert captured.out.strip() == "1h 1m 1s"


class TestJsonCLI:
    def test_format(self, capsys):
        main(["json", "format", '{"b":2,"a":1}'])
        captured = capsys.readouterr()
        assert '"b": 2' in captured.out or '"a": 1' in captured.out

    def test_minify(self, capsys):
        main(["json", "minify", '{ "a" : 1 }'])
        captured = capsys.readouterr()
        assert captured.out.strip() == '{"a":1}'

    def test_validate_valid(self, capsys):
        main(["json", "validate", '{"ok": true}'])
        captured = capsys.readouterr()
        assert "Valid" in captured.out or "合法" in captured.out

    def test_validate_invalid(self, capsys):
        with pytest.raises(SystemExit) as exc:
            main(["json", "validate", "bad json"])
        assert exc.value.code == 1


class TestTextCLI:
    def test_stats(self, capsys):
        main(["text", "stats", "hello world"])
        captured = capsys.readouterr()
        assert "11" in captured.out  # char count with spaces

    def test_camel2snake(self, capsys):
        main(["text", "camel2snake", "helloWorld"])
        captured = capsys.readouterr()
        assert captured.out.strip() == "hello_world"

    def test_snake2camel(self, capsys):
        main(["text", "snake2camel", "hello_world"])
        captured = capsys.readouterr()
        assert captured.out.strip() == "helloWorld"

    def test_size(self, capsys):
        main(["text", "size", "1024"])
        captured = capsys.readouterr()
        assert "1.00 KB" in captured.out
