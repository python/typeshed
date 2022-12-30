from datetime import datetime, timedelta, tzinfo
from threading import Lock

date_helper: DateHelper | None
lock_: Lock

class DateHelper:
    timezone: tzinfo
    def __init__(self, timezone: tzinfo = ...) -> None: ...
    def parse_date(self, date_string: str) -> datetime: ...
    def to_nanoseconds(self, delta: timedelta) -> int: ...
    def to_utc(self, value: datetime) -> datetime: ...

def get_date_helper() -> DateHelper: ...
