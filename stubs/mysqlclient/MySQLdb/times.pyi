from _typeshed import Unused
from datetime import date, datetime, time, timedelta

from MySQLdb._mysql import string_literal as string_literal

Date = date
Time = time
TimeDelta = timedelta
Timestamp = datetime
DateTimeDeltaType = timedelta
DateTimeType = datetime

def DateFromTicks(ticks: float | None) -> date: ...
def TimeFromTicks(ticks: float | None) -> time: ...
def TimestampFromTicks(ticks: float | None) -> datetime: ...

format_TIME = str
format_DATE = str

def format_TIMEDELTA(v: timedelta) -> str: ...
def format_TIMESTAMP(d: datetime) -> str: ...
def DateTime_or_None(s: str) -> datetime | None: ...
def TimeDelta_or_None(s: str) -> timedelta | None: ...
def Time_or_None(s: str) -> time | None: ...
def Date_or_None(s: str) -> date | None: ...
def DateTime2literal(d: datetime, c: Unused) -> str: ...
def DateTimeDelta2literal(d: datetime, c: Unused) -> str: ...
