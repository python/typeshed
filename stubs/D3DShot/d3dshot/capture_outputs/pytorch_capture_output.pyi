from collections.abc import Sequence
from ctypes import _CVoidConstPLike
from typing_extensions import Literal

from d3dshot.capture_output import CaptureOutput
from PIL import Image
from torch import Tensor

class PytorchCaptureOutput(CaptureOutput):
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
    ) -> Tensor: ...
    def to_pil(self, frame: Tensor) -> Image.Image: ...  # type: ignore[override]
    def stack(self, frames: Sequence[Tensor], stack_dimension: Literal["first", "last"]) -> Tensor: ...  # type: ignore[override]
