from typing import ClassVar
from typing_extensions import Literal

from . import ImageFile
from ._imaging import _PixelAccess
from .PyAccess import PyAccess

class WalImageFile(ImageFile.ImageFile):
    format: ClassVar[Literal["WAL"]]
    format_description: ClassVar[str]
    def load(self) -> _PixelAccess | PyAccess: ...

def open(filename): ...

quake2palette: bytes
