from typing import Any, ClassVar
from typing_extensions import Literal

from ._imaging import PixelAccess
from .ImageFile import ImageFile
from .PyAccess import PyAccess

class GbrImageFile(ImageFile):
    format: ClassVar[Literal["GBR"]]
    format_description: ClassVar[str]
    im: Any
    def load(self) -> PixelAccess | PyAccess: ...
