from _typeshed import Incomplete
from typing_extensions import TypeAlias

import numpy as np
import numpy.typing as npt
from d3dshot.capture_output import CaptureOutput as CaptureOutput
from PIL.Image import Image

Pointer: TypeAlias = Incomplete
NDArray: TypeAlias = npt.NDArray[np.float32]

class NumpyFloatCaptureOutput(CaptureOutput):
    def __init__(self) -> None: ...
    def process(
        self, pointer: Pointer, size: int, width: int, height: int, region: tuple[int, int, int, int], rotation: int
    ) -> NDArray: ...
    def to_pil(self, frame: NDArray) -> Image: ...
    def stack(self, frames: list[NDArray] | NDArray, stack_dimension: int) -> NDArray: ...
