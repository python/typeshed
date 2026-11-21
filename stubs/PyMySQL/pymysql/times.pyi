from _typeshed import FloatInt
from datetime import date, datetime, time, timedelta

Date: type[date]
Time: type[time]
TimeDelta: type[timedelta]
Timestamp: type[datetime]

def DateFromTicks(ticks: FloatInt | None) -> date: ...
def TimeFromTicks(ticks: FloatInt | None) -> time: ...
def TimestampFromTicks(ticks: FloatInt | None) -> datetime: ...
