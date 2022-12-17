from collections.abc import Sequence
from ctypes import _CVoidConstPLike
from typing_extensions import Literal, TypeAlias

import numpy as np
import numpy.typing as npt
from d3dshot.capture_outputs.numpy_capture_output import NumpyCaptureOutput
from PIL import Image

_NDArray: TypeAlias = npt.NDArray[np.float64]

class NumpyFloatCaptureOutput(NumpyCaptureOutput):
    def __init__(self) -> None: ...
    def process(  # type: ignore[override]
        self,
        pointer: _CVoidConstPLike,
        pitch: float,
        size: int,
        width: float,
        height: float,
        region: tuple[float, float, float, float],
        rotation: int,
    ) -> _NDArray: ...
    def to_pil(self, frame: _NDArray) -> Image.Image: ...  # type: ignore[override]
    def stack(  # type: ignore[override]
        self, frames: Sequence[_NDArray] | _NDArray, stack_dimension: Literal["first", "last"]
    ) -> _NDArray: ...
