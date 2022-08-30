from _typeshed import Incomplete
from typing_extensions import TypeAlias

import torch
from d3dshot.capture_output import CaptureOutput as CaptureOutput
from PIL.Image import Image

Pointer: TypeAlias = Incomplete

class PytorchFloatGPUCaptureOutput(CaptureOutput):
    device: Incomplete
    def __init__(self) -> None: ...
    def process(
        self, pointer: Pointer, size: int, width: int, height: int, region: tuple[int, int, int, int], rotation: int
    ) -> torch.Tensor: ...
    def to_pil(self, frame: torch.Tensor) -> Image: ...
    def stack(self, frames: list[torch.Tensor], stack_dimension: int) -> torch.Tensor: ...
