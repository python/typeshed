from typing import Any, ClassVar
from typing_extensions import Literal, TypeAlias

from .ImageFile import ImageFile

_OleFileIO: TypeAlias = Any  # olefile.OleFileIO
_OleStream: TypeAlias = Any  # olefile.OleStream

MODES: dict[tuple[int, ...], tuple[str, str]]

class FpxImageFile(ImageFile):
    ole: _OleFileIO
    format: ClassVar[Literal["FPX"]]
    format_description: ClassVar[str]
    fp: _OleStream | None
    def load(self): ...
