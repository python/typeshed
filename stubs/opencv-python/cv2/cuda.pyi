from typing import TypeVar, overload

from cv2 import Mat
from cv2.cv2 import _Boolean, _NumericScalar, _UMat, cuda_Event, cuda_GpuMat, cuda_GpuMat_Allocator, cuda_Stream

_TGpuMat = TypeVar("_TGpuMat", bound=cuda_GpuMat | _UMat)

DEVICE_INFO_COMPUTE_MODE_DEFAULT: int
DEVICE_INFO_COMPUTE_MODE_EXCLUSIVE: int
DEVICE_INFO_COMPUTE_MODE_EXCLUSIVE_PROCESS: int
DEVICE_INFO_COMPUTE_MODE_PROHIBITED: int
DYNAMIC_PARALLELISM: int
DeviceInfo_ComputeModeDefault: int
DeviceInfo_ComputeModeExclusive: int
DeviceInfo_ComputeModeExclusiveProcess: int
DeviceInfo_ComputeModeProhibited: int
EVENT_BLOCKING_SYNC: int
EVENT_DEFAULT: int
EVENT_DISABLE_TIMING: int
EVENT_INTERPROCESS: int
Event_BLOCKING_SYNC: int
Event_DEFAULT: int
Event_DISABLE_TIMING: int
Event_INTERPROCESS: int
FEATURE_SET_COMPUTE_10: int
FEATURE_SET_COMPUTE_11: int
FEATURE_SET_COMPUTE_12: int
FEATURE_SET_COMPUTE_13: int
FEATURE_SET_COMPUTE_20: int
FEATURE_SET_COMPUTE_21: int
FEATURE_SET_COMPUTE_30: int
FEATURE_SET_COMPUTE_32: int
FEATURE_SET_COMPUTE_35: int
FEATURE_SET_COMPUTE_50: int
GLOBAL_ATOMICS: int
HOST_MEM_PAGE_LOCKED: int
HOST_MEM_SHARED: int
HOST_MEM_WRITE_COMBINED: int
HostMem_PAGE_LOCKED: int
HostMem_SHARED: int
HostMem_WRITE_COMBINED: int
NATIVE_DOUBLE: int
SHARED_ATOMICS: int
WARP_SHUFFLE_FUNCTIONS: int

def Event_elapsedTime(start: cuda_Event, end: cuda_Event) -> float: ...
def GpuMat_defaultAllocator() -> cuda_GpuMat_Allocator: ...
def GpuMat_setDefaultAllocator(allocator: cuda_GpuMat_Allocator) -> None: ...
def Stream_Null() -> cuda_Stream: ...
def TargetArchs_has(major: int | None, minor: int | None) -> bool: ...
def TargetArchs_hasBin(major: int | None, minor: int | None) -> bool: ...
def TargetArchs_hasEqualOrGreater(major: int | None, minor: int | None) -> bool: ...
def TargetArchs_hasEqualOrGreaterBin(major: int | None, minor: int | None) -> bool: ...
def TargetArchs_hasEqualOrGreaterPtx(major: int | None, minor: int | None) -> bool: ...
def TargetArchs_hasEqualOrLessPtx(major: int | None, minor: int | None) -> bool: ...
def TargetArchs_hasPtx(major: int | None, minor: int | None) -> bool: ...
@overload
def createContinuous(rows: int, cols: int, type: int, arr: _NumericScalar) -> Mat: ...  # type: ignore[misc]  # https://github.com/python/mypy/issues/8881
@overload
def createContinuous(rows: int, cols: int, type: int, arr: _TGpuMat) -> _TGpuMat: ...  # type: ignore[misc]  # https://github.com/python/mypy/issues/8881
@overload
def createContinuous(rows: int | None, cols: int | None, type: int | None, arr: cuda_GpuMat | _UMat = ...) -> None: ...
@overload
def ensureSizeIsEnough(rows: int, cols: int, type: int, arr: _NumericScalar) -> Mat: ...  # type: ignore[misc]  # https://github.com/python/mypy/issues/8881
@overload
def ensureSizeIsEnough(rows: int, cols: int, type: int, arr: _TGpuMat) -> _TGpuMat: ...  # type: ignore[misc]  # https://github.com/python/mypy/issues/8881
@overload
def ensureSizeIsEnough(rows: int | None, cols: int | None, type: int | None, arr: cuda_GpuMat | _UMat = ...) -> None: ...
def getCudaEnabledDeviceCount() -> int: ...
def getDevice() -> int: ...
def printCudaDeviceInfo(device: int | None) -> None: ...
def printShortCudaDeviceInfo(device: int | None) -> None: ...
def registerPageLocked(m: Mat | _NumericScalar) -> None: ...
def resetDevice() -> None: ...
def setBufferPoolConfig(deviceId: int | None, stackSize: int | None, stackCount: int | None) -> None: ...
def setBufferPoolUsage(on: _Boolean) -> None: ...
def setDevice(device: int | None) -> None: ...
def unregisterPageLocked(m: Mat | _NumericScalar) -> None: ...
