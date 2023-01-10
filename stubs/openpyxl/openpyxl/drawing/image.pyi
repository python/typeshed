from typing_extensions import Literal

from PIL import Image as ImageModule

# Using "object" because modules can't by used as type
PILImage: object | Literal[False]

class Image:
    anchor: str
    ref: ImageModule.Image | str
    format: str
    def __init__(self, img) -> None: ...
    @property
    def path(self): ...
