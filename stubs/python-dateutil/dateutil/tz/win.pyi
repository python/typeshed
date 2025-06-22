import sys
import winreg
from ctypes import _Pointer, c_wchar
from datetime import datetime, timedelta
from typing import Any, ClassVar, Final
from typing_extensions import Self

from ._common import tzrangebase

if sys.platform == "win32":
    __all__ = ["tzwin", "tzwinlocal", "tzres"]

    ONEWEEK: timedelta
    TZKEYNAMENT: Final[str]
    TZKEYNAME9X: Final[str]
    TZLOCALKEYNAME: Final[str]
    TZKEYNAME: Final[str]

    class tzres:
        p_wchar: ClassVar[type[_Pointer[c_wchar]]]
        def __init__(self, tzres_loc="tzres.dll"): ...
        def load_name(self, offset): ...
        def name_from_string(self, tzname_str: str): ...

    class tzwinbase(tzrangebase):
        hasdst: bool
        def __eq__(self, other: tzwinbase) -> bool: ...  # type: ignore[override]
        @staticmethod
        def list() -> list[str]: ...
        def display(self) -> str | None: ...
        def transitions(self, year: int) -> tuple[datetime, datetime] | None: ...

    class tzwin(tzwinbase):
        hasdst: bool
        def __init__(self, name: str) -> None: ...
        def __reduce__(self) -> tuple[type[Self], tuple[str, ...]]: ...

    class tzwinlocal(tzwinbase):
        hasdst: bool
        def __init__(self) -> None: ...
        def __reduce__(self) -> tuple[type[Self], tuple[str, ...]]: ...

    def picknthweekday(year: int, month: int, dayofweek: int, hour: int, minute: int, whichweek: int) -> datetime: ...
    def valuestodict(
        key: winreg._KeyType,
    ) -> dict[str, Any]: ...  # keys and values in dict are results of winreg.EnumValue() function
