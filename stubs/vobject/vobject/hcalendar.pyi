from _typeshed import Incomplete
from typing import Any

from .icalendar import VCalendar2_0

class HCalendar(VCalendar2_0):
    name: str
    @classmethod
    def serialize(cls, obj, buf: Incomplete | None = ..., lineLength: Incomplete | None = ..., validate: bool = ...): ...