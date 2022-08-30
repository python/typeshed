import enum
from _typeshed import Incomplete
from typing_extensions import TypeAlias

import numpy as np
import numpy.typing as npt
from d3dshot import pytorch_is_available
from PIL.Image import Image

if pytorch_is_available:
    import torch

    Frame: TypeAlias = Image | npt.NDArray[np.int32] | npt.NDArray[np.float32] | torch.Tensor
else:
    Frame: TypeAlias = Image | npt.NDArray[np.int32] | npt.NDArray[np.float32]
Pointer: TypeAlias = Incomplete

class CaptureOutputs(enum.Enum):
    PIL: int
    NUMPY: int
    NUMPY_FLOAT: int
    PYTORCH: int
    PYTORCH_FLOAT: int
    PYTORCH_GPU: int
    PYTORCH_FLOAT_GPU: int

class CaptureOutputError(BaseException): ...

class CaptureOutput:
    backend: CaptureOutput
    def __init__(self, backend: CaptureOutputs = ...) -> None: ...
    def process(
        self, pointer: Pointer, size: int, width: int, height: int, region: tuple[int, int, int, int], rotation: int
    ) -> Frame: ...
    def to_pil(self, frame: Frame) -> Image: ...
    def stack(self, frames: list[Frame], stack_dimension) -> Frame: ...
