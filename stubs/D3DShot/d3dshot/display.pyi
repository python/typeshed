from _typeshed import Incomplete
from collections.abc import Callable
from typing import Literal
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

class Display:
    name: str
    adapter_name: str
    resolution: tuple[int, int]
    position: dict[Literal["left", "top", "right", "bottom"], int]
    rotation: int
    scale_factor: int
    is_primary: bool
    hmonitor: int
    dxgi_output: Incomplete | None
    dxgi_adapter: Incomplete | None
    d3d_device: Incomplete  # ctypes.POINTER(ID3D11Device)()
    d3d_device_context: Incomplete  # ctypes.POINTER(ID3D11DeviceContext)()
    dxgi_output_duplication: Incomplete  # ctypes.POINTER(IDXGIOutputDuplication)()

    def __init__(
        self,
        name: str | None = ...,
        adapter_name: str | None = ...,
        resolution: tuple[int, int] | None = ...,
        position: dict[Literal["left", "top", "right", "bottom"], int] | None = ...,
        rotation: int | None = ...,
        scale_factor: int | None = ...,
        is_primary: bool = ...,
        hmonitor: int | None = ...,
        dxgi_output: Incomplete | None = ...,
        dxgi_adapter: Incomplete | None = ...,
    ) -> None: ...
    def capture(
        self,
        # Incomplete: dxgi_mapped_rect.pBits
        process_func: Callable[[Pointer, int, int, int, tuple[int, int, int, int], int], Frame | None] | None,
        region: tuple[int, int, int, int] = ...,
    ) -> Frame: ...
    @classmethod
    def discover_displays(cls) -> list[Display]: ...
