from collections.abc import Sequence
from ctypes import _CVoidConstPLike
from typing_extensions import Literal, TypeAlias

import numpy as np
import numpy.typing as npt
from d3dshot.capture_output import CaptureOutput
from PIL import Image

_NDArray: TypeAlias = npt.NDArray[np.int32]

class NumpyCaptureOutput(CaptureOutput):
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
    ) -> _NDArray: ...
    def to_pil(self, frame: _NDArray) -> Image.Image: ...  # type: ignore[override]
    def stack(  # type: ignore[override]
        self, frames: Sequence[_NDArray] | _NDArray, stack_dimension: Literal["first", "last"]
    ) -> _NDArray: ...
