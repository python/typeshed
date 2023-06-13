from datetime import datetime
from re import Pattern
from typing_extensions import Final

MAC_EPOCH: Final[datetime]
WINDOWS_EPOCH: Final[datetime]
# The following two constants are defined twice in the implementation.
CALENDAR_WINDOWS_1900 = WINDOWS_EPOCH
CALENDAR_MAC_1904 = MAC_EPOCH
SECS_PER_DAY: Final = 86400
ISO_FORMAT: Final = "%Y-%m-%dT%H:%M:%SZ"
ISO_REGEX: Final[Pattern[str]]
ISO_DURATION: Final[Pattern[str]]

def to_ISO8601(dt): ...
def from_ISO8601(formatted_string): ...
def to_excel(dt, epoch=...): ...
def from_excel(value, epoch=..., timedelta: bool = False): ...
def time_to_days(value): ...
def timedelta_to_days(value): ...
def days_to_time(value): ...
