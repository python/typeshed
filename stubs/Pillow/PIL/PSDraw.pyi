from typing import Any

from .Image import Image

class PSDraw:
    fp: Any
    def __init__(self, fp: Any | None = ...) -> None: ...
    isofont: Any
    def begin_document(self, id: Any | None = ...) -> None: ...
    def end_document(self) -> None: ...
    def setfont(self, font: str, size: int) -> None: ...
    def line(self, xy0: tuple[int, int], xy1: tuple[int, int]) -> None: ...
    def rectangle(self, box: tuple[int, int, int, int]) -> None: ...
    def text(self, xy: tuple[int, int], text: str) -> None: ...
    def image(self, box: tuple[int, int, int, int], im: Image, dpi: float | None = ...) -> None: ...

EDROFF_PS: str
VDI_PS: str
ERROR_PS: str
