# Can't generate with stubgen because:
# "KeyError: 'pywintypes'"
from _typeshed import Incomplete
from datetime import datetime
from typing_extensions import Literal

import _win32typing

class error(Exception):
    winerror: int
    funcname: str
    strerror: str
    def __init__(self, winerror: int, funcname: str, strerror: str): ...

class com_error(Exception): ...
class UnicodeType(str): ...

class TimeType(datetime):
    Format = datetime.strftime

def DosDateTimeToTime() -> _win32typing.PyTime: ...
def Unicode() -> str: ...
def UnicodeFromRaw(_str: str) -> str: ...
def IsTextUnicode(_str: str, flags) -> tuple[Incomplete, Incomplete]: ...
def OVERLAPPED() -> _win32typing.PyOVERLAPPED: ...
def IID(iidString: str, is_bytes: bool = ...) -> _win32typing.PyIID: ...
def Time(timeRepr) -> _win32typing.PyTime: ...
def CreateGuid() -> _win32typing.PyIID: ...
def ACL(bufSize: int = ...) -> _win32typing.PyACL: ...
def SID(buffer, idAuthority, subAuthorities, bufSize=...) -> _win32typing.PySID: ...
def SECURITY_ATTRIBUTES() -> _win32typing.PySECURITY_ATTRIBUTES: ...
def SECURITY_DESCRIPTOR() -> _win32typing.PySECURITY_DESCRIPTOR: ...
def HANDLE() -> int: ...
def HKEY() -> _win32typing.PyHKEY: ...
def WAVEFORMATEX() -> _win32typing.PyWAVEFORMATEX: ...
def TimeStamp(*args, **kwargs): ...  # incomplete

FALSE: Literal[False]
TRUE: Literal[True]
WAVE_FORMAT_PCM: int
