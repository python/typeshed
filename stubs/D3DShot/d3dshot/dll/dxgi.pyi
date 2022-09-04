from _typeshed import Incomplete
from collections.abc import Callable
from ctypes import HRESULT, _CArgObject, _CData, Array, Structure, c_uint, c_ulong, wintypes
from typing import TypedDict
from typing_extensions import TypeAlias
from PIL import Image
from d3dshot.dll.d3d import ID3D11Device

# TODO: Complete types once we can import non-types dependencies
# See: https://github.com/python/typeshed/issues/5768
# from torch import Tensor
# import comtypes
# import numpy.typing as npt
# _IUnknown: TypeAlias = Incomplete
_Frame: TypeAlias = Image.Image | Incomplete
# _Frame: TypeAlias = Image.Image | npt.NDArray[np.int32] | npt.NDArray[np.float32] | Tensor

class _IUnknown:  # From comtypes.IUnknown
    def QueryInterface(self, interface: type, iid: _CData | None = ...) -> HRESULT: ...
    def AddRef(self) -> c_ulong: ...
    def Release(self) -> c_ulong: ...

class _DXGIOutputPosition(TypedDict):
    left: wintypes.LONG
    top: wintypes.LONG
    right: wintypes.LONG
    bottom: wintypes.LONG

class _DXGIOutput(TypedDict):
    name: str
    position: _DXGIOutputPosition
    resolution: tuple[tuple[wintypes.LONG, wintypes.LONG], tuple[wintypes.LONG, wintypes.LONG]]
    rotation: int
    is_attached_to_desktop: bool

class LUID(Structure):
    LowPart: wintypes.DWORD
    HighPart: wintypes.LONG

class DXGI_ADAPTER_DESC1(Structure):
    Description: Array[wintypes.WCHAR]
    VendorId: wintypes.UINT
    DeviceId: wintypes.UINT
    SubSysId: wintypes.UINT
    Revision: wintypes.UINT
    DedicatedVideoMemory: wintypes.ULARGE_INTEGER
    DedicatedSystemMemory: wintypes.ULARGE_INTEGER
    SharedSystemMemory: wintypes.ULARGE_INTEGER
    AdapterLuid: LUID
    Flags: wintypes.UINT

class DXGI_OUTPUT_DESC(Structure):
    DeviceName: Array[wintypes.WCHAR]
    DesktopCoordinates: wintypes.RECT
    AttachedToDesktop: wintypes.BOOL
    Rotation: wintypes.UINT
    Monitor: wintypes.HMONITOR

class DXGI_OUTDUPL_POINTER_POSITION(Structure):
    Position: wintypes.POINT
    Visible: wintypes.BOOL

class DXGI_OUTDUPL_FRAME_INFO(Structure):
    LastPresentTime: wintypes.LARGE_INTEGER
    LastMouseUpdateTime: wintypes.LARGE_INTEGER
    AccumulatedFrames: wintypes.UINT
    RectsCoalesced: wintypes.BOOL
    ProtectedContentMaskedOut: wintypes.BOOL
    PointerPosition: DXGI_OUTDUPL_POINTER_POSITION
    TotalMetadataBufferSize: wintypes.UINT
    PointerShapeBufferSize: wintypes.UINT

class DXGI_MAPPED_RECT(Structure):
    Pitch: wintypes.INT
    pBits: wintypes.PFLOAT

class IDXGIObject(_IUnknown):
    SetPrivateData: Callable[[], HRESULT]
    SetPrivateDataInterface: Callable[[], HRESULT]
    GetPrivateData: Callable[[], HRESULT]
    GetParent: Callable[[], HRESULT]

class IDXGIDeviceSubObject(IDXGIObject):
    GetDevice: Callable[[], HRESULT]

class IDXGIResource(IDXGIDeviceSubObject):
    GetSharedHandle: Callable[[], HRESULT]
    GetUsage: Callable[[], HRESULT]
    SetEvictionPriority: Callable[[], HRESULT]
    GetEvictionPriority: Callable[[], HRESULT]

class IDXGISurface(IDXGIDeviceSubObject):
    GetDesc: Callable[[], HRESULT]
    Map: Callable[[DXGI_MAPPED_RECT, wintypes.UINT], HRESULT]
    Unmap: Callable[[], HRESULT]

class IDXGIOutputDuplication(IDXGIObject):
    GetDesc: Callable[[], None]
    AcquireNextFrame: Callable[[wintypes.UINT, DXGI_OUTDUPL_FRAME_INFO, _CArgObject], HRESULT]
    GetFrameDirtyRects: Callable[[], HRESULT]
    GetFrameMoveRects: Callable[[], HRESULT]
    GetFramePointerShape: Callable[[], HRESULT]
    MapDesktopSurface: Callable[[], HRESULT]
    UnMapDesktopSurface: Callable[[], HRESULT]
    ReleaseFrame: Callable[[], HRESULT]

class IDXGIOutput(IDXGIObject):
    GetDesc: Callable[[DXGI_OUTPUT_DESC], HRESULT]
    GetDisplayModeList: Callable[[], HRESULT]
    FindClosestMatchingMode: Callable[[], HRESULT]
    WaitForVBlank: Callable[[], HRESULT]
    TakeOwnership: Callable[[], HRESULT]
    ReleaseOwnership: Callable[[], None]
    GetGammaControlCapabilities: Callable[[], HRESULT]
    SetGammaControl: Callable[[], HRESULT]
    GetGammaControl: Callable[[], HRESULT]
    SetDisplaySurface: Callable[[], HRESULT]
    GetDisplaySurfaceData: Callable[[], HRESULT]
    GetFrameStatistics: Callable[[], HRESULT]

class IDXGIOutput1(IDXGIOutput):
    GetDisplayModeList1: Callable[[], HRESULT]
    FindClosestMatchingMode1: Callable[[], HRESULT]
    GetDisplaySurfaceData1: Callable[[], HRESULT]
    DuplicateOutput: Callable[[ID3D11Device, _CArgObject], HRESULT]

class IDXGIAdapter(IDXGIObject):
    EnumOutputs: Callable[[wintypes.UINT, _CArgObject], HRESULT]
    GetDesc: Callable[[], HRESULT]
    CheckInterfaceSupport: Callable[[], HRESULT]

class IDXGIAdapter1(IDXGIAdapter):
    GetDesc1: Callable[[DXGI_ADAPTER_DESC1], HRESULT]

class IDXGIFactory(IDXGIObject):
    EnumAdapters: Callable[[], HRESULT]
    MakeWindowAssociation: Callable[[], HRESULT]
    GetWindowAssociation: Callable[[], HRESULT]
    CreateSwapChain: Callable[[], HRESULT]
    CreateSoftwareAdapter: Callable[[], HRESULT]

class IDXGIFactory1(IDXGIFactory):
    EnumAdapters1: Callable[[c_uint, _CArgObject], HRESULT]
    IsCurrent: Callable[[], wintypes.BOOL]

def initialize_dxgi_factory() -> IDXGIFactory1: ...
def discover_dxgi_adapters(dxgi_factory: IDXGIFactory1) -> list[IDXGIAdapter1]: ...
def describe_dxgi_adapter(dxgi_adapter: IDXGIAdapter1) -> Array[wintypes.WCHAR]: ...
def discover_dxgi_outputs(dxgi_adapter: IDXGIAdapter) -> list[IDXGIOutput1]: ...
def describe_dxgi_output(dxgi_output: IDXGIOutput) -> _DXGIOutput: ...
def initialize_dxgi_output_duplication(dxgi_output: IDXGIOutput1, d3d_device: ID3D11Device) -> IDXGIOutputDuplication: ...
def get_dxgi_output_duplication_frame(
    dxgi_output_duplication: IDXGIOutputDuplication,
    d3d_device: ID3D11Device,
    process_func: Callable[[wintypes.PFLOAT, int, int, int, tuple[int, int, int, int], int], _Frame | None] | None = ...,
    width: int = ...,
    height: int = ...,
    region: tuple[int, int, int, int] | None = ...,
    rotation: int = ...,
) -> _Frame: ...
