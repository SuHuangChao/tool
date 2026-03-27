"""
时间工具 - Time/date utilities
支持时间戳转换、格式化
"""

import time
from datetime import datetime, timezone


def timestamp_to_datetime(ts: float, local: bool = True) -> str:
    """将时间戳转换为可读日期时间字符串
    Convert a Unix timestamp to a human-readable datetime string.

    Args:
        ts: Unix 时间戳（秒）/ Unix timestamp in seconds
        local: True 表示本地时间，False 表示 UTC / True for local time, False for UTC

    Returns:
        格式化的日期时间字符串 / Formatted datetime string
    """
    if local:
        dt = datetime.fromtimestamp(ts)
    else:
        dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def datetime_to_timestamp(dt_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> float:
    """将日期时间字符串转换为时间戳
    Convert a datetime string to a Unix timestamp.

    Args:
        dt_str: 日期时间字符串 / Datetime string
        fmt: 日期时间格式 / Datetime format

    Returns:
        Unix 时间戳（秒）/ Unix timestamp in seconds
    """
    dt = datetime.strptime(dt_str, fmt)
    return dt.timestamp()


def now_timestamp() -> float:
    """获取当前时间戳 / Get current Unix timestamp"""
    return time.time()


def now_datetime(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """获取当前格式化时间 / Get current formatted datetime string"""
    return datetime.now().strftime(fmt)


def format_duration(seconds: float) -> str:
    """将秒数格式化为人类可读的时长
    Format a duration in seconds to a human-readable string.

    Example:
        format_duration(3661) -> "1h 1m 1s"
    """
    seconds = int(seconds)
    parts = []
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    parts.append(f"{seconds}s")
    return " ".join(parts)
