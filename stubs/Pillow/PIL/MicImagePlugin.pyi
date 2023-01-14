from typing import Any, ClassVar
from typing_extensions import Literal, TypeAlias

from .TiffImagePlugin import TiffImageFile

_OleFileIO: TypeAlias = Any  # olefile.OleFileIO
_OleStream: TypeAlias = Any  # olefile.OleStream

class MicImageFile(TiffImageFile):
    ole: _OleFileIO
    format: ClassVar[Literal["MIC"]]
    fp: _OleStream
    frame: int
    def seek(self, frame: int) -> None: ...
    def tell(self) -> int: ...
