# Stubs for msvcrt

# NOTE: These are incomplete!

from typing import BinaryIO, TextIO, overload

def get_osfhandle(file: int) -> int: ...
def open_osfhandle(handle: int, flags: int) -> int: ...
