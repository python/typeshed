from _typeshed import FloatInt
from typing import Any, TypeAlias

_Image: TypeAlias = Any  # actually PIL.Image, but not worth adding a dependency

def shift_hue(image: _Image, hue: FloatInt) -> _Image: ...
def make_transparent(image: _Image) -> _Image: ...
