from _typeshed import Incomplete
from typing_extensions import TypeAlias

from d3dshot.capture_output import CaptureOutput as CaptureOutput
from PIL import Image

# TODO: Complete types once we can import non-types dependencies
# See: https://github.com/python/typeshed/issues/5768
# from torch import device, Tensor
_Tensor: TypeAlias = Incomplete
_Device: TypeAlias = Incomplete

_Pointer: TypeAlias = Incomplete

class PytorchGPUCaptureOutput(CaptureOutput):
    device: _Device
    def __init__(self) -> None: ...
    def process(
        self, pointer: _Pointer, size: int, width: int, height: int, region: tuple[int, int, int, int], rotation: int
    ) -> _Tensor: ...
    def to_pil(self, frame: _Tensor) -> Image.Image: ...
    def stack(self, frames: list[_Tensor], stack_dimension: int): ...
