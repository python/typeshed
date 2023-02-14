import _tkinter
import tkinter
from _typeshed import Incomplete, ReadableBuffer, StrOrBytesPath, SupportsRead
from typing import overload

from PIL.Image import Image, _Box, _Mode, _Size

class PhotoImage:
    tk: _tkinter.TkappType
    def __init__(
        self,
        image: Image | _Mode | None = None,
        size: _Size | None = None,
        *,
        file: StrOrBytesPath | SupportsRead[bytes] = ...,
        data: ReadableBuffer = ...,
        # These are the same as tkinter.PhotoImage:
        format: str = ...,
        gamma: float = ...,
        height: int = ...,
        palette: int | str = ...,
        width: int = ...,
    ) -> None: ...
    def __del__(self) -> None: ...
    def width(self) -> int: ...
    def height(self) -> int: ...
    # box is deprecated and unused
    def paste(self, im: Image, box: _Box | None = ...) -> None: ...

class BitmapImage:
    tk: _tkinter.TkappType  # Not actually present, but required for tkinter._Image protocol
    def __init__(self, image: Image | None = None, **kw: Incomplete) -> None: ...
    def __del__(self) -> None: ...
    def width(self) -> int: ...
    def height(self) -> int: ...

def getimage(photo: tkinter.PhotoImage) -> Image: ...
