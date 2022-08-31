import ctypes
from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any
from typing_extensions import TypeAlias

import comtypes
from d3dshot.dll.d3d import (
    ID3D11Device as ID3D11Device,
    ID3D11DeviceContext as ID3D11DeviceContext,
    ID3D11Texture2D as ID3D11Texture2D,
    prepare_d3d11_texture_2d_for_cpu as prepare_d3d11_texture_2d_for_cpu,
)

Frame: TypeAlias = Any
# Frame: TypeAlias = Image | npt.NDArray[np.int32] | npt.NDArray[np.float32] | torch.Tensor
Pointer: TypeAlias = Incomplete

class LUID(ctypes.Structure): ...
class DXGI_ADAPTER_DESC1(ctypes.Structure): ...
class DXGI_OUTPUT_DESC(ctypes.Structure): ...
class DXGI_OUTDUPL_POINTER_POSITION(ctypes.Structure): ...
class DXGI_OUTDUPL_FRAME_INFO(ctypes.Structure): ...
class DXGI_MAPPED_RECT(ctypes.Structure): ...
class IDXGIObject(comtypes.IUnknown): ...
class IDXGIDeviceSubObject(IDXGIObject): ...
class IDXGIResource(IDXGIDeviceSubObject): ...
class IDXGISurface(IDXGIDeviceSubObject): ...
class IDXGIOutputDuplication(IDXGIObject): ...
class IDXGIOutput(IDXGIObject): ...
class IDXGIOutput1(IDXGIOutput): ...
class IDXGIAdapter(IDXGIObject): ...
class IDXGIAdapter1(IDXGIAdapter): ...
class IDXGIFactory(IDXGIObject): ...
class IDXGIFactory1(IDXGIFactory): ...

def initialize_dxgi_factory() -> Pointer: ...  # ctypes.POINTER(IDXGIFactory1)(handle.value)
def discover_dxgi_adapters(dxgi_factory: Pointer) -> list[Pointer]: ...
def describe_dxgi_adapter(dxgi_adapter: Pointer) -> Pointer: ...
def discover_dxgi_outputs(dxgi_adapter: Pointer) -> list[Pointer]: ...
def describe_dxgi_output(dxgi_output: Pointer) -> Pointer: ...
def initialize_dxgi_output_duplication(dxgi_output: Pointer, d3d_device: Pointer) -> Pointer: ...
def get_dxgi_output_duplication_frame(
    dxgi_output_duplication: Pointer,
    d3d_device: Pointer,
    process_func: Callable[[Pointer, int, int, int, tuple[int, int, int, int], int], Frame | None] | None = ...,
    width: int = ...,
    height: int = ...,
    region: tuple[int, int, int, int] | None = ...,
    rotation: int = ...,
) -> Frame: ...
