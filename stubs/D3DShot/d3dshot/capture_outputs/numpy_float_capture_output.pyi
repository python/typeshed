from _typeshed import Incomplete
from typing_extensions import TypeAlias

from d3dshot.capture_output import CaptureOutput as CaptureOutput
from PIL.Image import Image

# TODO: Complete types once we can import non-types dependencies
# See: https://github.com/python/typeshed/issues/5768
# import numpy as np
# import numpy.typing as npt
# NDArray: TypeAlias = npt.NDArray[np.float32]
NDArray: TypeAlias = Incomplete
_Pointer: TypeAlias = Incomplete

class NumpyFloatCaptureOutput(CaptureOutput):
    def __init__(self) -> None: ...
    def process(
        self, pointer: _Pointer, size: int, width: int, height: int, region: tuple[int, int, int, int], rotation: int
    ) -> NDArray: ...
    def to_pil(self, frame: NDArray) -> Image: ...
    def stack(self, frames: list[NDArray] | NDArray, stack_dimension: int) -> NDArray: ...
