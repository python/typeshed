from _typeshed import Incomplete
from array import array

is64bit: bool

def UnpackWMNOTIFY(lparam) -> tuple[Incomplete, ...]: ...
def UnpackNMITEMACTIVATE(lparam) -> tuple[Incomplete, ...]: ...
def PackMENUITEMINFO(
    fType: Incomplete | None = ...,
    fState: Incomplete | None = ...,
    wID: Incomplete | None = ...,
    hSubMenu: Incomplete | None = ...,
    hbmpChecked: Incomplete | None = ...,
    hbmpUnchecked: Incomplete | None = ...,
    dwItemData: Incomplete | None = ...,
    text: Incomplete | None = ...,
    hbmpItem: Incomplete | None = ...,
    dwTypeData: Incomplete | None = ...,
) -> tuple[array[int], list[Incomplete]]: ...
def UnpackMENUITEMINFO(
    s,
) -> tuple[
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
    str | None,
    Incomplete | None,
]: ...
def EmptyMENUITEMINFO(mask: Incomplete | None = ..., text_buf_size: int = ...) -> tuple[array[int], list[Incomplete]]: ...
def PackMENUINFO(
    dwStyle: Incomplete | None = ...,
    cyMax: Incomplete | None = ...,
    hbrBack: Incomplete | None = ...,
    dwContextHelpID: Incomplete | None = ...,
    dwMenuData: Incomplete | None = ...,
    fMask: int = ...,
) -> array[int]: ...
def UnpackMENUINFO(s) -> tuple[Incomplete | None, Incomplete | None, Incomplete | None, Incomplete | None, Incomplete | None]: ...
def EmptyMENUINFO(mask: Incomplete | None = ...) -> array[int]: ...
def PackTVINSERTSTRUCT(parent, insertAfter, tvitem) -> tuple[bytes, list[Incomplete]]: ...
def PackTVITEM(hitem, state, stateMask, text, image, selimage, citems, param) -> tuple[array[int], list[Incomplete]]: ...
def EmptyTVITEM(hitem, mask: Incomplete | None = ..., text_buf_size: int = ...) -> tuple[array[int], list[Incomplete]]: ...
def UnpackTVITEM(
    buffer,
) -> tuple[
    Incomplete,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
]: ...
def UnpackTVNOTIFY(
    lparam,
) -> tuple[
    Incomplete,
    Incomplete,
    Incomplete,
    Incomplete,
    tuple[
        Incomplete,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
    ],
    tuple[
        Incomplete,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
    ],
]: ...
def UnpackTVDISPINFO(
    lparam,
) -> tuple[
    Incomplete,
    Incomplete,
    Incomplete,
    tuple[
        Incomplete,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
    ],
]: ...
def PackLVITEM(
    item: Incomplete | None = ...,
    subItem: Incomplete | None = ...,
    state: Incomplete | None = ...,
    stateMask: Incomplete | None = ...,
    text: Incomplete | None = ...,
    image: Incomplete | None = ...,
    param: Incomplete | None = ...,
    indent: Incomplete | None = ...,
) -> tuple[array[int], list[Incomplete]]: ...
def UnpackLVITEM(
    buffer,
) -> tuple[
    Incomplete,
    Incomplete,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
    Incomplete | None,
]: ...
def UnpackLVDISPINFO(
    lparam,
) -> tuple[
    Incomplete,
    Incomplete,
    Incomplete,
    tuple[
        Incomplete,
        Incomplete,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
        Incomplete | None,
    ],
]: ...
def UnpackLVNOTIFY(
    lparam,
) -> tuple[
    Incomplete,
    Incomplete,
    Incomplete,
    Incomplete,
    Incomplete,
    Incomplete,
    Incomplete,
    Incomplete,
    tuple[Incomplete, Incomplete],
    Incomplete,
]: ...
def EmptyLVITEM(
    item, subitem, mask: Incomplete | None = ..., text_buf_size: int = ...
) -> tuple[array[int], list[Incomplete]]: ...
def PackLVCOLUMN(
    fmt: Incomplete | None = ...,
    cx: Incomplete | None = ...,
    text: Incomplete | None = ...,
    subItem: Incomplete | None = ...,
    image: Incomplete | None = ...,
    order: Incomplete | None = ...,
) -> tuple[array[int], list[Incomplete]]: ...
def UnpackLVCOLUMN(
    lparam,
) -> tuple[Incomplete | None, Incomplete | None, Incomplete | None, Incomplete | None, Incomplete | None, Incomplete | None]: ...
def EmptyLVCOLUMN(mask: Incomplete | None = ..., text_buf_size: int = ...) -> tuple[array[int], list[Incomplete]]: ...
def PackLVHITTEST(pt) -> tuple[array[int], None]: ...
def UnpackLVHITTEST(buf) -> tuple[tuple[Incomplete, Incomplete], Incomplete, Incomplete, Incomplete]: ...
def PackHDITEM(
    cxy: Incomplete | None = ...,
    text: Incomplete | None = ...,
    hbm: Incomplete | None = ...,
    fmt: Incomplete | None = ...,
    param: Incomplete | None = ...,
    image: Incomplete | None = ...,
    order: Incomplete | None = ...,
) -> tuple[array[int], list[Incomplete]]: ...
def PackDEV_BROADCAST(devicetype, rest_fmt, rest_data, extra_data=...) -> bytes: ...
def PackDEV_BROADCAST_HANDLE(handle, hdevnotify: int = ..., guid=..., name_offset: int = ..., data=...) -> bytes: ...
def PackDEV_BROADCAST_VOLUME(unitmask, flags) -> bytes: ...
def PackDEV_BROADCAST_DEVICEINTERFACE(classguid, name: str = ...) -> bytes: ...

class DEV_BROADCAST_INFO:
    devicetype: Incomplete
    def __init__(self, devicetype, **kw) -> None: ...

def UnpackDEV_BROADCAST(lparam) -> DEV_BROADCAST_INFO | None: ...
