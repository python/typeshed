import ctypes
from _typeshed import Incomplete
from ctypes import wintypes
from typing_extensions import TypeAlias

_Pointer: TypeAlias = Incomplete

class DISPLAY_DEVICE(ctypes.Structure):
    cb: wintypes.DWORD
    DeviceName: wintypes.WCHAR
    DeviceString: wintypes.WCHAR
    StateFlags: wintypes.DWORD
    DeviceID: wintypes.WCHAR
    DeviceKey: wintypes.WCHAR

def get_display_device_name_mapping() -> dict[str, tuple[str, bool]]: ...
def get_hmonitor_by_point(x: int, y: int) -> _Pointer: ...  # ctypes.windll.user32.MonitorFromPoint(point, 0)
