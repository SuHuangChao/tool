# tool — 常用小工具 / Commonly Used Utilities

A lightweight Python library and CLI providing common day-to-day utility functions grouped by category.

## 功能 / Features

| 模块 / Module | 功能 / Functionality |
|---|---|
| `tools/encode.py` | Base64 编解码, URL 编解码 / Base64 & URL encoding/decoding |
| `tools/hash.py` | MD5, SHA1, SHA256, SHA512 哈希 / Hash generation |
| `tools/time_utils.py` | 时间戳转换, 时长格式化 / Timestamp conversion, duration formatting |
| `tools/json_utils.py` | JSON 格式化, 压缩, 验证 / JSON formatting, minification, validation |
| `tools/text.py` | 字数统计, 大小写转换, 文件大小格式化等 / Word count, case conversion, file-size formatting, etc. |

## 安装 / Installation

```bash
# No external dependencies — uses Python standard library only
python --version  # Python 3.8+
```

## 命令行用法 / CLI Usage

```bash
# 编码解码 / Encoding & Decoding
python main.py encode b64enc "hello world"
python main.py encode b64dec "aGVsbG8gd29ybGQ="
python main.py encode urlenc "hello world"
python main.py encode urldec "hello%20world"

# 哈希 / Hashing
python main.py hash md5    "hello"
python main.py hash sha1   "hello"
python main.py hash sha256 "hello"
python main.py hash sha512 "hello"

# 时间 / Time
python main.py time now
python main.py time ts2dt 1700000000
python main.py time dt2ts "2023-11-14 22:13:20"
python main.py time duration 3661

# JSON
python main.py json format   '{"b":2,"a":1}'
python main.py json minify   '{ "a" : 1 }'
python main.py json validate '{"ok": true}'

# 文本 / Text
python main.py text stats        "hello world"
python main.py text camel2snake  "helloWorld"
python main.py text snake2camel  "hello_world"
python main.py text truncate     "a very long string" --length 10
python main.py text size         1073741824
```

## 作为库使用 / Library Usage

```python
from tools.encode import base64_encode, url_encode
from tools.hash import sha256
from tools.time_utils import timestamp_to_datetime, format_duration
from tools.json_utils import format_json, is_valid_json
from tools.text import camel_to_snake, format_size

print(base64_encode("hello"))          # aGVsbG8=
print(sha256("hello"))                 # 2cf24dba...
print(timestamp_to_datetime(0, local=False))  # 1970-01-01 00:00:00
print(format_duration(3661))           # 1h 1m 1s
print(format_json('{"b":2,"a":1}'))   # pretty-printed JSON
print(camel_to_snake("helloWorld"))    # hello_world
print(format_size(1024 * 1024))        # 1.00 MB
```

## 测试 / Tests

```bash
pip install pytest
python -m pytest tests/ -v
```