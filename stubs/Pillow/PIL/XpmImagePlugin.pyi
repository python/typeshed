from typing import Any, ClassVar
from typing_extensions import Literal

from .ImageFile import ImageFile

xpm_head: Any

class XpmImageFile(ImageFile):
    format: ClassVar[Literal["XPM"]]
    def load_read(self, bytes): ...
