from types import ModuleType
from typing_extensions import Literal

from PIL import Image as ImageModule

PILImage: ModuleType | Literal[False]

class Image:
    anchor: str
    ref: ImageModule.Image | str
    format: str
    def __init__(self, img) -> None: ...
    @property
    def path(self): ...
