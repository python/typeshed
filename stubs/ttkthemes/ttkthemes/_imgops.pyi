from typing import Any
from typing_extensions import TypeAlias

Image: TypeAlias = Any  # actually PIL.Image, but not worth adding a dependency

def shift_hue(image: Image, hue: float) -> Image: ...
def make_transparent(image: Image) -> Image: ...
