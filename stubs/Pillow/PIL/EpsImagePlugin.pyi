from typing import Any, ClassVar
from typing_extensions import Literal

from ._imaging import _PixelAccess
from .ImageFile import ImageFile
from .PyAccess import PyAccess

split: Any
field: Any
gs_windows_binary: Any

def has_ghostscript(): ...
def Ghostscript(tile, size, fp, scale: int = 1, transparency: bool = False): ...

class PSFile:
    fp: Any
    char: Any
    def __init__(self, fp) -> None: ...
    def seek(self, offset, whence=0) -> None: ...
    def readline(self): ...

class EpsImageFile(ImageFile):
    format: ClassVar[Literal["EPS"]]
    format_description: ClassVar[str]
    mode_map: Any
    im: Any
    mode: Any
    tile: Any
    def load(self, scale: int = 1, transparency: bool = False) -> _PixelAccess | PyAccess: ...
    def load_seek(self, *args, **kwargs) -> None: ...
