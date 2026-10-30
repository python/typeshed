import _win32typing
from win32.lib.pywintypes import error as error

def mmapfile(
    File: str | None, Name: str | None, MaximumSize: int = 0, FileOffset: int = 0, NumberOfBytesToMap: int | None = None
) -> _win32typing.Pymmapfile: ...
