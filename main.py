#!/usr/bin/env python3
"""
tool - 常用小工具命令行界面
tool - Command-line interface for commonly used small utilities

用法 / Usage:
    python main.py <command> [options]

命令 / Commands:
    encode      Base64 / URL 编码解码
    hash        计算哈希值
    time        时间戳转换
    json        JSON 格式化/验证/压缩
    text        文本统计与处理
"""

import argparse
import sys

from tools.encode import base64_decode, base64_encode, url_decode, url_encode
from tools.hash import md5, sha1, sha256, sha512
from tools.json_utils import format_json, is_valid_json, minify_json
from tools.text import (
    camel_to_snake,
    char_count,
    format_size,
    line_count,
    snake_to_camel,
    truncate,
    word_count,
)
from tools.time_utils import (
    datetime_to_timestamp,
    format_duration,
    now_datetime,
    now_timestamp,
    timestamp_to_datetime,
)


# ---------------------------------------------------------------------------
# encode sub-command
# ---------------------------------------------------------------------------

def cmd_encode(args: argparse.Namespace) -> None:
    if args.action == "b64enc":
        print(base64_encode(args.text))
    elif args.action == "b64dec":
        print(base64_decode(args.text))
    elif args.action == "urlenc":
        print(url_encode(args.text))
    elif args.action == "urldec":
        print(url_decode(args.text))


# ---------------------------------------------------------------------------
# hash sub-command
# ---------------------------------------------------------------------------

def cmd_hash(args: argparse.Namespace) -> None:
    algorithms = {
        "md5": md5,
        "sha1": sha1,
        "sha256": sha256,
        "sha512": sha512,
    }
    func = algorithms[args.algorithm]
    print(func(args.text))


# ---------------------------------------------------------------------------
# time sub-command
# ---------------------------------------------------------------------------

def cmd_time(args: argparse.Namespace) -> None:
    if args.action == "now":
        print(f"timestamp : {now_timestamp():.0f}")
        print(f"datetime  : {now_datetime()}")
    elif args.action == "ts2dt":
        print(timestamp_to_datetime(float(args.value)))
    elif args.action == "dt2ts":
        print(datetime_to_timestamp(args.value))
    elif args.action == "duration":
        print(format_duration(float(args.value)))


# ---------------------------------------------------------------------------
# json sub-command
# ---------------------------------------------------------------------------

def cmd_json(args: argparse.Namespace) -> None:
    text = args.text
    if args.action == "format":
        try:
            print(format_json(text, indent=args.indent))
        except Exception as exc:
            print(f"错误 / Error: {exc}", file=sys.stderr)
            sys.exit(1)
    elif args.action == "minify":
        try:
            print(minify_json(text))
        except Exception as exc:
            print(f"错误 / Error: {exc}", file=sys.stderr)
            sys.exit(1)
    elif args.action == "validate":
        if is_valid_json(text):
            print("✓ 合法的 JSON / Valid JSON")
        else:
            print("✗ 非法的 JSON / Invalid JSON", file=sys.stderr)
            sys.exit(1)


# ---------------------------------------------------------------------------
# text sub-command
# ---------------------------------------------------------------------------

def cmd_text(args: argparse.Namespace) -> None:
    text = args.text
    if args.action == "stats":
        print(f"字符数 (含空格) / chars (with spaces) : {char_count(text)}")
        print(f"字符数 (不含空格) / chars (no spaces)  : {char_count(text, include_spaces=False)}")
        print(f"单词数 / words                         : {word_count(text)}")
        print(f"行数   / lines                         : {line_count(text)}")
    elif args.action == "camel2snake":
        print(camel_to_snake(text))
    elif args.action == "snake2camel":
        print(snake_to_camel(text))
    elif args.action == "truncate":
        print(truncate(text, args.length))
    elif args.action == "size":
        print(format_size(int(text)))


# ---------------------------------------------------------------------------
# argument parser
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tool",
        description="常用小工具 / Commonly used small utilities",
    )
    sub = parser.add_subparsers(dest="command", metavar="command")
    sub.required = True

    # -- encode ---
    p_enc = sub.add_parser("encode", help="Base64 / URL 编码解码")
    p_enc.add_argument(
        "action",
        choices=["b64enc", "b64dec", "urlenc", "urldec"],
        help="b64enc|b64dec|urlenc|urldec",
    )
    p_enc.add_argument("text", help="要处理的文本 / Text to process")
    p_enc.set_defaults(func=cmd_encode)

    # -- hash ---
    p_hash = sub.add_parser("hash", help="计算哈希值 / Compute hash")
    p_hash.add_argument(
        "algorithm",
        choices=["md5", "sha1", "sha256", "sha512"],
        help="哈希算法 / Hash algorithm",
    )
    p_hash.add_argument("text", help="要哈希的文本 / Text to hash")
    p_hash.set_defaults(func=cmd_hash)

    # -- time ---
    p_time = sub.add_parser("time", help="时间戳转换 / Timestamp conversion")
    p_time.add_argument(
        "action",
        choices=["now", "ts2dt", "dt2ts", "duration"],
        help="now|ts2dt|dt2ts|duration",
    )
    p_time.add_argument("value", nargs="?", default=None, help="输入值 / Input value")
    p_time.set_defaults(func=cmd_time)

    # -- json ---
    p_json = sub.add_parser("json", help="JSON 格式化/验证/压缩")
    p_json.add_argument(
        "action",
        choices=["format", "minify", "validate"],
        help="format|minify|validate",
    )
    p_json.add_argument("text", help="JSON 字符串 / JSON string")
    p_json.add_argument(
        "--indent", type=int, default=4, help="缩进空格数 / Indentation (default: 4)"
    )
    p_json.set_defaults(func=cmd_json)

    # -- text ---
    p_text = sub.add_parser("text", help="文本统计与处理 / Text statistics and processing")
    p_text.add_argument(
        "action",
        choices=["stats", "camel2snake", "snake2camel", "truncate", "size"],
        help="stats|camel2snake|snake2camel|truncate|size",
    )
    p_text.add_argument("text", help="输入文本 / Input text")
    p_text.add_argument(
        "--length", type=int, default=50, help="截断长度 / Truncate length (default: 50)"
    )
    p_text.set_defaults(func=cmd_text)

    return parser


def main(argv=None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
