from ctypes import _CVoidConstPLike
from typing import TypeVar

from d3dshot.capture_output import CaptureOutput
from PIL import Image

_T = TypeVar("_T")

class PILCaptureOutput(CaptureOutput):
    def __init__(self) -> None: ...
    def process(
        self,
        pointer: _CVoidConstPLike,
        pitch: int,
        size: int,
        width: int,
        height: int,
        region: tuple[int, int, int, int],
        rotation: int,
    ) -> Image.Image: ...
    def to_pil(self, frame: _T) -> _T: ...
    def stack(self, frames: list[Image.Image], stack_dimension: int) -> list[Image.Image]: ...
