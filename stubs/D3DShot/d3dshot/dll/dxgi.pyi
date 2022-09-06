import sys
from _typeshed import Incomplete
from collections.abc import Callable
from ctypes import Array, Structure, _CArgObject, _CData, c_uint, c_ulong
from ctypes.wintypes import BOOL, DWORD, HMONITOR, INT, LARGE_INTEGER, LONG, PFLOAT, POINT, RECT, UINT, ULARGE_INTEGER, WCHAR
from typing_extensions import TypeAlias, TypedDict

from d3dshot.dll.d3d import ID3D11Device
from PIL import Image

# TODO: Complete types once we can import non-types dependencies
# See: https://github.com/python/typeshed/issues/5768
# from torch import Tensor
# import comtypes
# import numpy.typing as npt
# _IUnknown: TypeAlias = Incomplete
_Frame: TypeAlias = Image.Image | Incomplete
# _Frame: TypeAlias = Image.Image | npt.NDArray[np.int32] | npt.NDArray[np.float32] | Tensor

# mypy does not support os.name checks, while pyright does https://github.com/python/mypy/issues/13002
# import os
# if os.name == "nt":  # noqa: Y002
if sys.platform == "win32":
    from ctypes import HRESULT

    _HRESULT: TypeAlias = HRESULT
else:
    _HRESULT: TypeAlias = Incomplete

class _IUnknown:  # From comtypes.IUnknown
    def QueryInterface(self, interface: type, iid: _CData | None = ...) -> _HRESULT: ...
    def AddRef(self) -> c_ulong: ...
    def Release(self) -> c_ulong: ...

class _DXGIOutputPosition(TypedDict):
    left: LONG
    top: LONG
    right: LONG
    bottom: LONG

class _DXGIOutput(TypedDict):
    name: str
    position: _DXGIOutputPosition
    resolution: tuple[tuple[LONG, LONG], tuple[LONG, LONG]]
    rotation: int
    is_attached_to_desktop: bool

class LUID(Structure):
    LowPart: DWORD
    HighPart: LONG

class DXGI_ADAPTER_DESC1(Structure):
    Description: Array[WCHAR]
    VendorId: UINT
    DeviceId: UINT
    SubSysId: UINT
    Revision: UINT
    DedicatedVideoMemory: ULARGE_INTEGER
    DedicatedSystemMemory: ULARGE_INTEGER
    SharedSystemMemory: ULARGE_INTEGER
    AdapterLuid: LUID
    Flags: UINT

class DXGI_OUTPUT_DESC(Structure):
    DeviceName: Array[WCHAR]
    DesktopCoordinates: RECT
    AttachedToDesktop: BOOL
    Rotation: UINT
    Monitor: HMONITOR

class DXGI_OUTDUPL_POINTER_POSITION(Structure):
    Position: POINT
    Visible: BOOL

class DXGI_OUTDUPL_FRAME_INFO(Structure):
    LastPresentTime: LARGE_INTEGER
    LastMouseUpdateTime: LARGE_INTEGER
    AccumulatedFrames: UINT
    RectsCoalesced: BOOL
    ProtectedContentMaskedOut: BOOL
    PointerPosition: DXGI_OUTDUPL_POINTER_POSITION
    TotalMetadataBufferSize: UINT
    PointerShapeBufferSize: UINT

class DXGI_MAPPED_RECT(Structure):
    Pitch: INT
    pBits: PFLOAT

class IDXGIObject(_IUnknown):
    def SetPrivateData(self) -> _HRESULT: ...
    def SetPrivateDataInterface(self) -> _HRESULT: ...
    def GetPrivateData(self) -> _HRESULT: ...
    def GetParent(self) -> _HRESULT: ...

class IDXGIDeviceSubObject(IDXGIObject):
    def GetDevice(self) -> _HRESULT: ...

class IDXGIResource(IDXGIDeviceSubObject):
    def GetSharedHandle(self) -> _HRESULT: ...
    def GetUsage(self) -> _HRESULT: ...
    def SetEvictionPriority(self) -> _HRESULT: ...
    def GetEvictionPriority(self) -> _HRESULT: ...

class IDXGISurface(IDXGIDeviceSubObject):
    def GetDesc(self) -> _HRESULT: ...
    def Map(self, pLockedRect: DXGI_MAPPED_RECT, MapFlags: UINT) -> _HRESULT: ...
    def Unmap(self) -> _HRESULT: ...

class IDXGIOutputDuplication(IDXGIObject):
    def GetDesc(self) -> None: ...
    def AcquireNextFrame(
        self, TimeoutInMilliseconds: UINT, pFrameInfo: DXGI_OUTDUPL_FRAME_INFO, ppDesktopResource: _CArgObject
    ) -> _HRESULT: ...
    def GetFrameDirtyRects(self) -> _HRESULT: ...
    def GetFrameMoveRects(self) -> _HRESULT: ...
    def GetFramePointerShape(self) -> _HRESULT: ...
    def MapDesktopSurface(self) -> _HRESULT: ...
    def UnMapDesktopSurface(self) -> _HRESULT: ...
    def ReleaseFrame(self) -> _HRESULT: ...

class IDXGIOutput(IDXGIObject):
    def GetDesc(self, pDesc: DXGI_OUTPUT_DESC) -> _HRESULT: ...
    def GetDisplayModeList(self) -> _HRESULT: ...
    def FindClosestMatchingMode(self) -> _HRESULT: ...
    def WaitForVBlank(self) -> _HRESULT: ...
    def TakeOwnership(self) -> _HRESULT: ...
    def ReleaseOwnership(self) -> None: ...
    def GetGammaControlCapabilities(self) -> _HRESULT: ...
    def SetGammaControl(self) -> _HRESULT: ...
    def GetGammaControl(self) -> _HRESULT: ...
    def SetDisplaySurface(self) -> _HRESULT: ...
    def GetDisplaySurfaceData(self) -> _HRESULT: ...
    def GetFrameStatistics(self) -> _HRESULT: ...

class IDXGIOutput1(IDXGIOutput):
    def GetDisplayModeList1(self) -> _HRESULT: ...
    def FindClosestMatchingMode1(self) -> _HRESULT: ...
    def GetDisplaySurfaceData1(self) -> _HRESULT: ...
    def DuplicateOutput(self, pDevice: ID3D11Device, ppOutputDuplication: _CArgObject) -> _HRESULT: ...

class IDXGIAdapter(IDXGIObject):
    def EnumOutputs(self, Output: UINT, ppOutput: _CArgObject) -> _HRESULT: ...
    def GetDesc(self) -> _HRESULT: ...
    def CheckInterfaceSupport(self) -> _HRESULT: ...

class IDXGIAdapter1(IDXGIAdapter):
    def GetDesc1(self, pDesc: DXGI_ADAPTER_DESC1) -> _HRESULT: ...

class IDXGIFactory(IDXGIObject):
    def EnumAdapters(self) -> _HRESULT: ...
    def MakeWindowAssociation(self) -> _HRESULT: ...
    def GetWindowAssociation(self) -> _HRESULT: ...
    def CreateSwapChain(self) -> _HRESULT: ...
    def CreateSoftwareAdapter(self) -> _HRESULT: ...

class IDXGIFactory1(IDXGIFactory):
    def EnumAdapters1(self, Adapter: c_uint, ppAdapter: _CArgObject) -> _HRESULT: ...
    def IsCurrent(self) -> BOOL: ...

def initialize_dxgi_factory() -> IDXGIFactory1: ...
def discover_dxgi_adapters(dxgi_factory: IDXGIFactory1) -> list[IDXGIAdapter1]: ...
def describe_dxgi_adapter(dxgi_adapter: IDXGIAdapter1) -> Array[WCHAR]: ...
def discover_dxgi_outputs(dxgi_adapter: IDXGIAdapter) -> list[IDXGIOutput1]: ...
def describe_dxgi_output(dxgi_output: IDXGIOutput) -> _DXGIOutput: ...
def initialize_dxgi_output_duplication(dxgi_output: IDXGIOutput1, d3d_device: ID3D11Device) -> IDXGIOutputDuplication: ...
def get_dxgi_output_duplication_frame(
    dxgi_output_duplication: IDXGIOutputDuplication,
    d3d_device: ID3D11Device,
    process_func: Callable[[PFLOAT, int, int, int, tuple[int, int, int, int], int], _Frame | None] | None = ...,
    width: int = ...,
    height: int = ...,
    region: tuple[int, int, int, int] | None = ...,
    rotation: int = ...,
) -> _Frame: ...
