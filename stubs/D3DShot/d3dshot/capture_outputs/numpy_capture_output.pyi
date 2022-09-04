from _typeshed import Incomplete
from typing_extensions import TypeAlias

from d3dshot.capture_output import CaptureOutput
from PIL import Image

# TODO: Complete types once we can import non-types dependencies
# See: https://github.com/python/typeshed/issues/5768
# import numpy as np
# import numpy.typing as npt
# NDArray: TypeAlias = npt.NDArray[np.int32]
_NDArray: TypeAlias = Incomplete
_Pointer: TypeAlias = Incomplete

class NumpyCaptureOutput(CaptureOutput):
    def __init__(self) -> None: ...
    def process(
        self, pointer: _Pointer, pitch: int, size: int, width: int, height: int, region: tuple[int, int, int, int], rotation: int
    ) -> _NDArray: ...
    def to_pil(self, frame: _NDArray) -> Image.Image: ...
    def stack(self, frames: list[_NDArray] | _NDArray, stack_dimension: int) -> _NDArray: ...
