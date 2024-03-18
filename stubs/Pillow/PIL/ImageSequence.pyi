from typing import Callable
from typing_extensions import Self

from .Image import Image

class Iterator:
    im: Image
    position: int
    def __init__(self, im: Image) -> None: ...
    def __getitem__(self, ix: int) -> Image: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> Image: ...

def all_frames(im: Image | list[Image], func: Callable[[Image], Image] | None = None) -> list[Image]: ...
