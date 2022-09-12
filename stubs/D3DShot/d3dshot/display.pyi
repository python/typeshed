from ctypes import _Pointer
from typing_extensions import TypedDict

from d3dshot.dll import _ProcessFunc, _ProcessFuncRegionArg, _ProcessFuncReturn
from d3dshot.dll.d3d import ID3D11Device, ID3D11DeviceContext
from d3dshot.dll.dxgi import IDXGIAdapter, IDXGIOutput1, IDXGIOutputDuplication

class _PositionDict(TypedDict):
    left: int
    top: int
    right: int
    bottom: int

class Display:
    name: str
    adapter_name: str
    resolution: tuple[int, int]
    position: _PositionDict
    rotation: int
    scale_factor: float
    is_primary: bool
    hmonitor: int
    dxgi_output: IDXGIOutput1 | None
    dxgi_adapter: _Pointer[IDXGIAdapter] | None
    d3d_device: ID3D11Device
    d3d_device_context: ID3D11DeviceContext
    dxgi_output_duplication: _Pointer[IDXGIOutputDuplication]

    def __init__(
        self,
        name: str | None = ...,
        adapter_name: str | None = ...,
        resolution: tuple[int, int] | None = ...,
        position: _PositionDict | None = ...,
        rotation: int | None = ...,
        scale_factor: float | None = ...,
        is_primary: bool = ...,
        hmonitor: int | None = ...,
        dxgi_output: IDXGIOutput1 | None = ...,
        dxgi_adapter: _Pointer[IDXGIAdapter] | None = ...,
    ) -> None: ...
    def capture(
        self, process_func: _ProcessFunc[_ProcessFuncRegionArg, _ProcessFuncReturn] | None, region: _ProcessFuncRegionArg = ...
    ) -> _ProcessFuncReturn: ...
    @classmethod
    def discover_displays(cls) -> list[Display]: ...
