from typing import Optional, Dict, Any

ABDAY_1 = ...  # type: int
ABDAY_2 = ...  # type: int
ABDAY_3 = ...  # type: int
ABDAY_4 = ...  # type: int
ABDAY_5 = ...  # type: int
ABDAY_6 = ...  # type: int
ABDAY_7 = ...  # type: int
ABMON_1 = ...  # type: int
ABMON_10 = ...  # type: int
ABMON_11 = ...  # type: int
ABMON_12 = ...  # type: int
ABMON_2 = ...  # type: int
ABMON_3 = ...  # type: int
ABMON_4 = ...  # type: int
ABMON_5 = ...  # type: int
ABMON_6 = ...  # type: int
ABMON_7 = ...  # type: int
ABMON_8 = ...  # type: int
ABMON_9 = ...  # type: int
ALT_DIGITS = ...  # type: int
AM_STR = ...  # type: int
CHAR_MAX = ...  # type: int
CODESET = ...  # type: int
CRNCYSTR = ...  # type: int
DAY_1 = ...  # type: int
DAY_2 = ...  # type: int
DAY_3 = ...  # type: int
DAY_4 = ...  # type: int
DAY_5 = ...  # type: int
DAY_6 = ...  # type: int
DAY_7 = ...  # type: int
D_FMT = ...  # type: int
D_T_FMT = ...  # type: int
ERA = ...  # type: int
ERA_D_FMT = ...  # type: int
ERA_D_T_FMT = ...  # type: int
ERA_T_FMT = ...  # type: int
LC_ALL = ...  # type: int
LC_COLLATE = ...  # type: int
LC_CTYPE = ...  # type: int
LC_MESSAGES = ...  # type: int
LC_MONETARY = ...  # type: int
LC_NUMERIC = ...  # type: int
LC_TIME = ...  # type: int
MON_1 = ...  # type: int
MON_10 = ...  # type: int
MON_11 = ...  # type: int
MON_12 = ...  # type: int
MON_2 = ...  # type: int
MON_3 = ...  # type: int
MON_4 = ...  # type: int
MON_5 = ...  # type: int
MON_6 = ...  # type: int
MON_7 = ...  # type: int
MON_8 = ...  # type: int
MON_9 = ...  # type: int
NOEXPR = ...  # type: int
PM_STR = ...  # type: int
RADIXCHAR = ...  # type: int
THOUSEP = ...  # type: int
T_FMT = ...  # type: int
T_FMT_AMPM = ...  # type: int
YESEXPR = ...  # type: int
_DATE_FMT = ...  # type: int

class Error(Exception):
    pass

def bind_textdomain_codeset(domain: Optional[str], codeset: Optional[str]) -> Optional[str]: pass
def bindtextdomain(domain: Optional[str], dir: Optional[str]) -> str: pass
def dcgettext(domain: Optional[str], msg: str, category: int) -> str: pass
def dgettext(domain: Optional[str], msg: str) -> str: pass
def gettext(msg: str) -> str: pass
def localeconv() -> Dict[str, Any]: pass
def nl_langinfo(key: int) -> str: pass
def setlocale(i: int, s: str) -> str: pass
def strcoll(left: str, right: str) -> int: pass
def strxfrm(s: str) -> str: pass
def textdomain(domain: Optional[str]) -> str: pass
