# Stubs for locale

from typing import Any, Iterable, List, Mapping, Optional, Sequence, Tuple, Union
import sys

_str = str


CODESET = ...  # type: int
D_T_FMT = ...  # type: int
D_FMT = ...  # type: int
T_FMT = ...  # type: int
T_FMT_AMPM = ...  # type: int

DAY_1 = ...  # type: int
DAY_2 = ...  # type: int
DAY_3 = ...  # type: int
DAY_4 = ...  # type: int
DAY_5 = ...  # type: int
DAY_6 = ...  # type: int
DAY_7 = ...  # type: int
ABDAY_1 = ...  # type: int
ABDAY_2 = ...  # type: int
ABDAY_3 = ...  # type: int
ABDAY_4 = ...  # type: int
ABDAY_5 = ...  # type: int
ABDAY_6 = ...  # type: int
ABDAY_7 = ...  # type: int

MON_1 = ...  # type: int
MON_2 = ...  # type: int
MON_3 = ...  # type: int
MON_4 = ...  # type: int
MON_5 = ...  # type: int
MON_6 = ...  # type: int
MON_7 = ...  # type: int
MON_8 = ...  # type: int
MON_9 = ...  # type: int
MON_10 = ...  # type: int
MON_11 = ...  # type: int
MON_12 = ...  # type: int
ABMON_1 = ...  # type: int
ABMON_2 = ...  # type: int
ABMON_3 = ...  # type: int
ABMON_4 = ...  # type: int
ABMON_5 = ...  # type: int
ABMON_6 = ...  # type: int
ABMON_7 = ...  # type: int
ABMON_8 = ...  # type: int
ABMON_9 = ...  # type: int
ABMON_10 = ...  # type: int
ABMON_11 = ...  # type: int
ABMON_12 = ...  # type: int

RADIXCHAR = ...  # type: int
THOUSEP = ...  # type: int
YESEXPR = ...  # type: int
NOEXPR = ...  # type: int
CRNCYSTR = ...  # type: int

ERA = ...  # type: int
ERA_D_T_FMT = ...  # type: int
ERA_D_FMT = ...  # type: int
ERA_T_FMT = ...  # type: int

ALT_DIGITS = ...  # type: int

LC_CTYPE = ...  # type: int
LC_COLLATE = ...  # type: int
LC_TIME = ...  # type: int
LC_MONETARY = ...  # type: int
LC_MESSAGES = ...  # type: int
LC_NUMERIC = ...  # type: int
LC_ALL = ...  # type: int

CHAR_MAX = ...  # type: int

class Error(Exception): ...

def setlocale(category: int,
              locale: Union[str, Iterable[str], None] = ...) -> str: ...
def localeconv() -> Mapping[str, Union[int, str, List[int]]]: ...
def nl_langinfo(option: int) -> str: ...
def getdefaultlocale(envvars: Tuple[str] = ...) -> Tuple[Optional[str], Optional[str]]: ...
def getlocale(category: int = ...) -> Sequence[str]: ...
def getpreferredencoding(do_setlocale: bool = ...) -> str: ...
def normalize(localename: str) -> str: ...
def resetlocale(category: int = ...) -> None: ...
def strcoll(string1: str, string2: str) -> int: ...
def strxfrm(string: str) -> str: ...
def format(format: str, val: int, grouping: bool = ...,
           monetary: bool = ...) -> str: ...
def format_string(format: str, val: Sequence[Any],
                  grouping: bool = ...) -> str: ...
def currency(val: int, symbol: bool = ..., grouping: bool = ...,
             international: bool = ...) -> str: ...
def str(float: float) -> _str: ...
if sys.version_info >= (3, 5):
    def delocalize(string: str) -> None: ...
def atof(string: str) -> float: ...
def atoi(string: str) -> int: ...
