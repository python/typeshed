from _typeshed import Incomplete
from collections.abc import Callable
from ctypes.wintypes import PFLOAT
from typing_extensions import Literal, TypeAlias

from PIL import Image

_Frame: TypeAlias = Image.Image | Incomplete
# FIXME: When #5768 is resolved:
# _Frame: TypeAlias = Image.Image | npt.NDArray[np.int32] | npt.NDArray[np.float32] | _Tensor

class Display:
    name: str
    adapter_name: str
    resolution: tuple[int, int]
    position: dict[Literal["left", "top", "right", "bottom"], int]
    rotation: int
    scale_factor: float
    is_primary: bool
    hmonitor: int
    dxgi_output: Incomplete | None
    dxgi_adapter: Incomplete | None
    d3d_device: Incomplete
    d3d_device_context: Incomplete
    dxgi_output_duplication: Incomplete

    def __init__(
        self,
        name: str | None = ...,
        adapter_name: str | None = ...,
        resolution: tuple[int, int] | None = ...,
        position: dict[Literal["left", "top", "right", "bottom"], int] | None = ...,
        rotation: int | None = ...,
        scale_factor: float | None = ...,
        is_primary: bool = ...,
        hmonitor: int | None = ...,
        dxgi_output: Incomplete | None = ...,
        dxgi_adapter: Incomplete | None = ...,
    ) -> None: ...
    def capture(
        self,
        process_func: Callable[[PFLOAT, int, int, int, tuple[int, int, int, int], int], _Frame | None] | None,
        region: tuple[int, int, int, int] | None = ...,
    ) -> _Frame: ...
    @classmethod
    def discover_displays(cls) -> list[Display]: ...
