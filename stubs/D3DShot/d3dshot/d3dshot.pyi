from _typeshed import Incomplete
from collections import deque
from typing import Any
from typing_extensions import TypeAlias
from PIL import Image

from d3dshot.capture_output import CaptureOutput as CaptureOutput, CaptureOutputs as CaptureOutputs
from d3dshot.display import Display as Display

_Frame: TypeAlias = Image.Image | Incomplete
# _Frame: TypeAlias = Image.Image | npt.NDArray[np.int32] | npt.NDArray[np.float32] | _Tensor

class Singleton(type):
    def __call__(cls, *args: Any, **kwargs: Any) -> Any: ...

class D3DShot:
    displays: list[Display]
    display: Display
    capture_output: CaptureOutput
    frame_buffer_size: int
    frame_buffer: deque[_Frame]
    previous_screenshot: _Frame | None
    region: tuple[int, int, int, int] | None

    def __init__(
        self,
        capture_output: CaptureOutputs = ...,
        frame_buffer_size: int = ...,
        pil_is_available: bool = ...,
        numpy_is_available: bool = ...,
        pytorch_is_available: bool = ...,
        pytorch_gpu_is_available: bool = ...,
    ) -> None: ...
    @property
    def is_capturing(self) -> bool: ...
    def get_latest_frame(self) -> _Frame | None: ...
    def get_frame(self, frame_index: int) -> _Frame | None: ...
    def get_frames(self, frame_indices: list[int]) -> list[_Frame]: ...
    def get_frame_stack(self, frame_indices: list[int], stack_dimension: str | None = ...) -> _Frame: ...
    def screenshot(self, region: tuple[int, int, int, int] | None = ...) -> _Frame | None: ...
    def screenshot_to_disk(
        self, directory: str | None = ..., file_name: str | None = ..., region: tuple[int, int, int, int] | None = ...
    ) -> str: ...
    def frame_buffer_to_disk(self, directory: str | None = ...) -> None: ...
    def capture(self, target_fps: int = ..., region: tuple[int, int, int, int] | None = ...) -> bool: ...
    def screenshot_every(self, interval: float, region: tuple[int, int, int, int] | None = ...) -> bool: ...
    def screenshot_to_disk_every(
        self, interval: float, directory: str | None = ..., region: tuple[int, int, int, int] | None = ...
    ) -> bool: ...
    def stop(self) -> bool: ...
    def benchmark(self) -> None: ...
    def detect_displays(self) -> None: ...
