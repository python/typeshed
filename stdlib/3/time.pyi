# Stubs for time
# Ron Murawski <ron@horizonchess.com>

# based on: http://docs.python.org/3.2/library/time.html#module-time
# see: http://nullege.com/codes/search?cq=time

import sys
from typing import Tuple, Union

# ----- variables and constants -----
accept2dyear = False
altzone = 0
daylight = 0
timezone = 0
tzname = ... # type: Tuple[str, str]


# ----- classes/methods -----
class struct_time:
    # this is supposed to be a namedtuple object
    # namedtuple is not yet implemented (see file: mypy/stubs/collections.py)
    # see: http://docs.python.org/3.2/library/time.html#time.struct_time
    # see: http://nullege.com/codes/search/time.struct_time
    # TODO: namedtuple() object problem
    #namedtuple __init__(self, int, int, int, int, int, int, int, int, int):
    #    ...
    tm_year = 0
    tm_mon = 0
    tm_mday = 0
    tm_hour = 0
    tm_min = 0
    tm_sec = 0
    tm_wday = 0
    tm_yday = 0
    tm_isdst = 0
    if sys.version_info >= (3, 3):
        tm_gmtoff = 0
        tm_zone = 'GMT'

# ----- functions -----
def asctime(t: Union[Tuple[int, int, int, int, int, int, int, int, int],
                     struct_time,
                     None] = ...) -> str: ...  # return current time

def clock() -> float: ...

def ctime(secs: Union[float, None] = ...) -> str: ...  # return current time

def gmtime(secs: Union[float, None] = ...) -> struct_time: ...  # return current time

def localtime(secs: Union[float, None] = ...) -> struct_time: ...  # return current time

def mktime(t: Union[Tuple[int, int, int, int, int,
                          int, int, int, int],
                    struct_time]) -> float: ...

def sleep(secs: Union[int, float]) -> None: ...

def strftime(format: str, t: Union[Tuple[int, int, int, int, int,
                                         int, int, int, int],
                                   struct_time,
                                   None] = ...) -> str: ...  # return current time

def strptime(string: str,
             format: str = ...) -> struct_time: ...
def time() -> float: ...
def tzset() -> None: ...  # Unix only
