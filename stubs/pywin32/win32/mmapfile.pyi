import _win32typing
from win32.lib.pywintypes import error as error

def mmapfile(
    File, Name, MaximumSize: int = ..., FileOffset: int = ..., NumberOfBytesToMap: int = ..., /
) -> _win32typing.Pymmapfile: ...
