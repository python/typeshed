__all__ = ["TZProvider"]

import datetime
from abc import ABC, abstractmethod

from dateutil.rrule import rrule

from ..prop import vRecur

class TZProvider(ABC):
    """Interface for timezone implementations."""

    @property
    @abstractmethod
    def name(self) -> str: ...
    @abstractmethod
    def localize_utc(self, dt: datetime.datetime) -> datetime.datetime: ...
    @abstractmethod
    def localize(self, dt: datetime.datetime, tz: datetime.tzinfo) -> datetime.datetime: ...
    @abstractmethod
    def knows_timezone_id(self, id: str) -> bool: ...
    @abstractmethod
    def fix_rrule_until(self, rrule: rrule, ical_rrule: vRecur) -> None: ...
    @abstractmethod
    def create_timezone(self, name: str, transition_times, transition_info) -> datetime.tzinfo: ...
    @abstractmethod
    def timezone(self, name: str) -> datetime.tzinfo | None: ...
    @abstractmethod
    def uses_pytz(self) -> bool: ...
    @abstractmethod
    def uses_zoneinfo(self) -> bool: ...
