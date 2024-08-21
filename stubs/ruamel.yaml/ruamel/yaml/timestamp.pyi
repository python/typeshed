import datetime
from typing import Any

class TimeStamp(datetime.datetime):
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    def __new__(cls, *args: Any, **kw: Any) -> Any: ...
    def __deepcopy__(self, memo: Any) -> Any: ...
    def replace(
        self,
        year: Any = None,
        month: Any = None,
        day: Any = None,
        hour: Any = None,
        minute: Any = None,
        second: Any = None,
        microsecond: Any = None,
        tzinfo: Any = True,
        fold: Any = None,
    ) -> Any: ...
