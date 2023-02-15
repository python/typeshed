import _tkinter
import tkinter
from _typeshed import ReadableBuffer, StrOrBytesPath, SupportsRead
from typing import Any

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
        # These are forwarded to tkinter.PhotoImage.__init__():
        name: str | None = None,
        cnf: dict[str, Any] = ...,
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
    def __init__(
        self,
        image: Image | None = None,
        *,
        file: StrOrBytesPath | SupportsRead[bytes] = ...,
        data: ReadableBuffer = ...,
        # These are forwarded to tkinter.Bitmap.__init__():
        name: str | None = None,
        cnf: dict[str, Any] = ...,
        master: tkinter.Misc | _tkinter.TkappType | None = None,
        background: tkinter._Color = ...,
        foreground: tkinter._Color = ...,
        maskdata: str = ...,
        maskfile: StrOrBytesPath = ...,
    ) -> None: ...
    def __del__(self) -> None: ...
    def width(self) -> int: ...
    def height(self) -> int: ...

def getimage(photo: tkinter.PhotoImage) -> Image: ...
