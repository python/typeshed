import datetime
from _typeshed import Incomplete

class TimeStamp(datetime.datetime):
    def __init__(self, *args, **kw) -> None: ...
    def __new__(cls, *args, **kw): ...
    def __deepcopy__(self, memo): ...
    def replace(
        self,
        year: Incomplete | None = None,
        month: Incomplete | None = None,
        day: Incomplete | None = None,
        hour: Incomplete | None = None,
        minute: Incomplete | None = None,
        second: Incomplete | None = None,
        microsecond: Incomplete | None = None,
        tzinfo: bool = True,
        fold: Incomplete | None = None,
    ): ...
