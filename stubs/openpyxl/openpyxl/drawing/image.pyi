from types import ModuleType
from typing import Any
from typing_extensions import Literal, TypeAlias

# Is actually PIL.Image.Image
_PILImageImage: TypeAlias = Any

PILImage: ModuleType | Literal[False]

class Image:
    anchor: str
    ref: _PILImageImage | str
    format: str
    def __init__(self, img) -> None: ...
    @property
    def path(self): ...
