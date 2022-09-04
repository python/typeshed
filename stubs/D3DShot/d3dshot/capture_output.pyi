import enum
from _typeshed import Incomplete
from typing_extensions import TypeAlias

from PIL import Image

_Frame: TypeAlias = Incomplete
# _Frame: TypeAlias = Image.Image | npt.NDArray[np.int32] | npt.NDArray[np.float32] | _Tensor
_Pointer: TypeAlias = Incomplete

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
        self, pointer: _Pointer, pitch: int, size: int, width: int, height: int, region: tuple[int, int, int, int], rotation: int
    ) -> _Frame: ...
    def to_pil(self, frame: _Frame) -> Image.Image: ...
    def stack(self, frames: list[_Frame], stack_dimension) -> _Frame: ...
