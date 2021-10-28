import datetime
from typing import Any, NamedTuple, Pattern

class SizeUnit(NamedTuple):
    divider: int
    symbol: str
    name: str

class CombinedUnit(NamedTuple):
    decimal: SizeUnit
    binary: SizeUnit

disk_size_units: Any
length_size_units: Any
time_units: Any

def coerce_boolean(value: Any) -> bool: ...
def coerce_pattern(value: str | Pattern[str], flags: int = ...) -> Pattern[str]: ...
def coerce_seconds(value: float | datetime.timedelta) -> float: ...
def format_size(num_bytes: float, keep_width: bool = ..., binary: bool = ...) -> str: ...
def parse_size(size: str, binary: bool = ...) -> int: ...
def format_length(num_metres: float, keep_width: bool = ...) -> str: ...
def parse_length(length: str) -> float: ...
def format_number(number: float, num_decimals: int = ...) -> str: ...
def round_number(count: float, keep_width: bool = ...) -> str: ...
def format_timespan(num_seconds: float | datetime.timedelta, detailed: bool = ..., max_units: int = ...) -> str: ...
def parse_timespan(timespan: str) -> float: ...
def parse_date(datestring: str) -> tuple[int, int, int, int, int, int]: ...
def format_path(pathname: str) -> str: ...
def parse_path(pathname: str) -> str: ...

class Timer:
    monotonic: bool
    resumable: bool
    start_time: float
    total_time: float
    def __init__(self, start_time: Any | None = ..., resumable: bool = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any | None = ..., exc_value: Any | None = ..., traceback: Any | None = ...) -> None: ...
    def sleep(self, seconds: float) -> None: ...
    @property
    def elapsed_time(self): ...
    @property
    def rounded(self): ...

class InvalidDate(Exception): ...
class InvalidSize(Exception): ...
class InvalidLength(Exception): ...
class InvalidTimespan(Exception): ...
