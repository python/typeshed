import sys
from decimal import Decimal
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

CODESET: int
D_T_FMT: int
D_FMT: int
T_FMT: int
T_FMT_AMPM: int

DAY_1: int
DAY_2: int
DAY_3: int
DAY_4: int
DAY_5: int
DAY_6: int
DAY_7: int
ABDAY_1: int
ABDAY_2: int
ABDAY_3: int
ABDAY_4: int
ABDAY_5: int
ABDAY_6: int
ABDAY_7: int

MON_1: int
MON_2: int
MON_3: int
MON_4: int
MON_5: int
MON_6: int
MON_7: int
MON_8: int
MON_9: int
MON_10: int
MON_11: int
MON_12: int
ABMON_1: int
ABMON_2: int
ABMON_3: int
ABMON_4: int
ABMON_5: int
ABMON_6: int
ABMON_7: int
ABMON_8: int
ABMON_9: int
ABMON_10: int
ABMON_11: int
ABMON_12: int

RADIXCHAR: int
THOUSEP: int
YESEXPR: int
NOEXPR: int
CRNCYSTR: int

ERA: int
ERA_D_T_FMT: int
ERA_D_FMT: int
ERA_T_FMT: int

ALT_DIGITS: int

LC_CTYPE: int
LC_COLLATE: int
LC_TIME: int
LC_MONETARY: int
LC_MESSAGES: int
LC_NUMERIC: int
LC_ALL: int

CHAR_MAX: int

class Error(Exception): ...

def setlocale(category: int, locale: Union[str, Iterable[str], None] = ...) -> str: ...
def localeconv() -> Mapping[str, Union[int, str, List[int]]]: ...
def nl_langinfo(__key: int) -> str: ...
def getdefaultlocale(envvars: Tuple[str, ...] = ...) -> Tuple[Optional[str], Optional[str]]: ...
def getlocale(category: int = ...) -> Sequence[str]: ...
def getpreferredencoding(do_setlocale: bool = ...) -> str: ...
def normalize(localename: str) -> str: ...
def resetlocale(category: int = ...) -> None: ...
def strcoll(string1: str, string2: str) -> int: ...
def strxfrm(string: str) -> str: ...
def format(percent: str, value: Union[float, Decimal], grouping: bool = ..., monetary: bool = ..., *additional: Any) -> str: ...

if sys.version_info >= (3, 7):
    def format_string(f: str, val: Any, grouping: bool = ..., monetary: bool = ...) -> str: ...

else:
    def format_string(f: str, val: Any, grouping: bool = ...) -> str: ...

def currency(val: Union[int, float, Decimal], symbol: bool = ..., grouping: bool = ..., international: bool = ...) -> str: ...
def delocalize(string: str) -> str: ...
def atof(string: str, func: Callable[[str], float] = ...) -> float: ...
def atoi(string: str) -> int: ...
def str(val: float) -> str: ...

locale_alias: Dict[str, str]  # undocumented
locale_encoding_alias: Dict[str, str]  # undocumented
windows_locale: Dict[int, str]  # undocumented
