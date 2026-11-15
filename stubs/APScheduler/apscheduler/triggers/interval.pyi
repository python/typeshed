from datetime import date, datetime, timedelta, tzinfo

from apscheduler.triggers.base import BaseTrigger

class IntervalTrigger(BaseTrigger):
    interval: timedelta
    interval_length: float
    timezone: tzinfo
    # __init__ gives start_date now plus the interval when it is given none.
    start_date: datetime
    end_date: datetime | None
    jitter: float | None
    def __init__(
        self,
        weeks: float = 0,
        days: float = 0,
        hours: float = 0,
        minutes: float = 0,
        seconds: float = 0,
        start_date: datetime | date | str | None = None,
        end_date: datetime | date | str | None = None,
        timezone: tzinfo | str | None = None,
        jitter: float | None = None,
    ) -> None: ...
    def get_next_fire_time(self, previous_fire_time: datetime | None, now: datetime) -> datetime | None: ...
