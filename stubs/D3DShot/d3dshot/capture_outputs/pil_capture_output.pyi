from _typeshed import Incomplete
from typing_extensions import TypeAlias

from d3dshot.capture_output import CaptureOutput as CaptureOutput
from PIL.Image import Image

_Pointer: TypeAlias = Incomplete

class PILCaptureOutput(CaptureOutput):
    def __init__(self) -> None: ...
    def process(
        self, pointer: _Pointer, size: int, width: int, height: int, region: tuple[int, int, int, int], rotation: int
    ) -> Image: ...
    def to_pil(self, frame: Image) -> Image: ...
    def stack(self, frames: list[Image], stack_dimension: int) -> list[Image]: ...
