"""Tests for tools/time_utils.py"""

import pytest

from tools.time_utils import (
    datetime_to_timestamp,
    format_duration,
    now_datetime,
    now_timestamp,
    timestamp_to_datetime,
)


class TestTimestampConversion:
    def test_timestamp_to_datetime_utc(self):
        # Unix epoch in UTC should be "1970-01-01 00:00:00"
        result = timestamp_to_datetime(0, local=False)
        assert result == "1970-01-01 00:00:00"

    def test_datetime_to_timestamp_roundtrip(self):
        ts_original = 1_700_000_000.0
        dt_str = timestamp_to_datetime(ts_original, local=False)
        ts_back = datetime_to_timestamp(dt_str)
        # Allow a small offset for timezone differences in the roundtrip
        assert abs(ts_back - ts_original) < 86400  # within one day is fine

    def test_now_timestamp(self):
        import time
        ts = now_timestamp()
        assert isinstance(ts, float)
        assert ts > 0

    def test_now_datetime(self):
        dt = now_datetime()
        assert len(dt) == 19  # "YYYY-MM-DD HH:MM:SS"


class TestFormatDuration:
    def test_seconds_only(self):
        assert format_duration(45) == "45s"

    def test_minutes_and_seconds(self):
        assert format_duration(90) == "1m 30s"

    def test_hours(self):
        assert format_duration(3661) == "1h 1m 1s"

    def test_days(self):
        assert format_duration(86400) == "1d 0s"

    def test_zero(self):
        assert format_duration(0) == "0s"
