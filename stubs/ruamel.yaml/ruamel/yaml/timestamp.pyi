from _typeshed import Unused
from datetime import datetime, tzinfo as _TzInfo
from typing import Literal, SupportsIndex
from typing_extensions import Self

class TimeStamp(datetime):
    def __deepcopy__(self, memo: Unused) -> TimeStamp: ...
    def replace(
        self,
        year: SupportsIndex | None = None,
        month: SupportsIndex | None = None,
        day: SupportsIndex | None = None,
        hour: SupportsIndex | None = None,
        minute: SupportsIndex | None = None,
        second: SupportsIndex | None = None,
        microsecond: SupportsIndex | None = None,
        tzinfo: _TzInfo | Literal[True] | None = True,
        fold: int | None = None,
    ) -> Self: ...
