from typing import Any

from .ImageFile import ImageFile

class Jpeg2KImageFile(ImageFile):
    format: str
    format_description: str
    @property
    def reduce(self): ...
    @reduce.setter
    def reduce(self, value) -> None: ...
    tile: Any
    def load(self): ...
