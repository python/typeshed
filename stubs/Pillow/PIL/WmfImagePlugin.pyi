import sys
from _typeshed import Incomplete
from typing import Any, ClassVar
from typing_extensions import Literal

from ._imaging import _PixelAccess
from .ImageFile import StubImageFile
from .PyAccess import PyAccess

def register_handler(handler) -> None: ...

if sys.platform == "win32":
    class WmfHandler:
        bbox: Any
        def open(self, im) -> None: ...
        def load(self, im): ...

class WmfStubImageFile(StubImageFile):
    format: ClassVar[Literal["WMF"]]
    format_description: ClassVar[str]
    def load(self, dpi: Incomplete | None = ...) -> _PixelAccess | PyAccess: ...
