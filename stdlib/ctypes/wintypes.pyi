from ctypes import (
    Array,
    Structure,
    _CField,
    _Pointer,
    _SimpleCData,
    c_byte,
    c_char,
    c_char_p,
    c_double,
    c_float,
    c_int,
    c_long,
    c_longlong,
    c_short,
    c_uint,
    c_ulong,
    c_ulonglong,
    c_ushort,
    c_void_p,
    c_wchar,
    c_wchar_p,
)
from typing import Final, TypeVar
from typing_extensions import TypeAlias

BYTE: Final = c_byte
WORD: Final = c_ushort
DWORD: Final = c_ulong
CHAR: Final = c_char
WCHAR: Final = c_wchar
UINT: Final = c_uint
INT: Final = c_int
DOUBLE: Final = c_double
FLOAT: Final = c_float
BOOLEAN: Final = BYTE
BOOL: Final = c_long

class VARIANT_BOOL(_SimpleCData[bool]): ...

ULONG: Final = c_ulong
LONG: Final = c_long
USHORT: Final = c_ushort
SHORT: Final = c_short
LARGE_INTEGER: Final = c_longlong
_LARGE_INTEGER: Final = c_longlong
ULARGE_INTEGER: Final = c_ulonglong
_ULARGE_INTEGER: Final = c_ulonglong

OLESTR: Final = c_wchar_p
LPOLESTR: Final = c_wchar_p
LPCOLESTR: Final = c_wchar_p
LPWSTR: Final = c_wchar_p
LPCWSTR: Final = c_wchar_p
LPSTR: Final = c_char_p
LPCSTR: Final = c_char_p
LPVOID: Final = c_void_p
LPCVOID: Final = c_void_p

# These two types are pointer-sized unsigned and signed ints, respectively.
# At runtime, they are either c_[u]long or c_[u]longlong, depending on the host's pointer size
# (they are not really separate classes).
class WPARAM(_SimpleCData[int]): ...
class LPARAM(_SimpleCData[int]): ...

ATOM: Final = WORD
LANGID: Final = WORD
COLORREF: Final = DWORD
LGRPID: Final = DWORD
LCTYPE: Final = DWORD
LCID: Final = DWORD

HANDLE: Final = c_void_p
HACCEL: Final = HANDLE
HBITMAP: Final = HANDLE
HBRUSH: Final = HANDLE
HCOLORSPACE: Final = HANDLE
HDC: Final = HANDLE
HDESK: Final = HANDLE
HDWP: Final = HANDLE
HENHMETAFILE: Final = HANDLE
HFONT: Final = HANDLE
HGDIOBJ: Final = HANDLE
HGLOBAL: Final = HANDLE
HHOOK: Final = HANDLE
HICON: Final = HANDLE
HINSTANCE: Final = HANDLE
HKEY: Final = HANDLE
HKL: Final = HANDLE
HLOCAL: Final = HANDLE
HMENU: Final = HANDLE
HMETAFILE: Final = HANDLE
HMODULE: Final = HANDLE
HMONITOR: Final = HANDLE
HPALETTE: Final = HANDLE
HPEN: Final = HANDLE
HRGN: Final = HANDLE
HRSRC: Final = HANDLE
HSTR: Final = HANDLE
HTASK: Final = HANDLE
HWINSTA: Final = HANDLE
HWND: Final = HANDLE
SC_HANDLE: Final = HANDLE
SERVICE_STATUS_HANDLE: Final = HANDLE

_CIntLikeT = TypeVar("_CIntLikeT", bound=_SimpleCData[int])
_CIntLikeField: TypeAlias = _CField[_CIntLikeT, int, _CIntLikeT | int]

class RECT(Structure):
    left: _CIntLikeField[LONG]
    top: _CIntLikeField[LONG]
    right: _CIntLikeField[LONG]
    bottom: _CIntLikeField[LONG]

RECTL: Final = RECT
_RECTL: Final = RECT
tagRECT = RECT

class _SMALL_RECT(Structure):
    Left: _CIntLikeField[SHORT]
    Top: _CIntLikeField[SHORT]
    Right: _CIntLikeField[SHORT]
    Bottom: _CIntLikeField[SHORT]

SMALL_RECT: Final = _SMALL_RECT

class _COORD(Structure):
    X: _CIntLikeField[SHORT]
    Y: _CIntLikeField[SHORT]

class POINT(Structure):
    x: _CIntLikeField[LONG]
    y: _CIntLikeField[LONG]

POINTL: Final = POINT
_POINTL: Final = POINT
tagPOINT = POINT

class SIZE(Structure):
    cx: _CIntLikeField[LONG]
    cy: _CIntLikeField[LONG]

SIZEL: Final = SIZE
tagSIZE = SIZE

def RGB(red: int, green: int, blue: int) -> int: ...

class FILETIME(Structure):
    dwLowDateTime: _CIntLikeField[DWORD]
    dwHighDateTime: _CIntLikeField[DWORD]

_FILETIME: Final = FILETIME

class MSG(Structure):
    hWnd: _CField[HWND, int | None, HWND | int | None]
    message: _CIntLikeField[UINT]
    wParam: _CIntLikeField[WPARAM]
    lParam: _CIntLikeField[LPARAM]
    time: _CIntLikeField[DWORD]
    pt: _CField[POINT, POINT, POINT]

tagMSG = MSG
MAX_PATH: Final[int]

class WIN32_FIND_DATAA(Structure):
    dwFileAttributes: _CIntLikeField[DWORD]
    ftCreationTime: _CField[FILETIME, FILETIME, FILETIME]
    ftLastAccessTime: _CField[FILETIME, FILETIME, FILETIME]
    ftLastWriteTime: _CField[FILETIME, FILETIME, FILETIME]
    nFileSizeHigh: _CIntLikeField[DWORD]
    nFileSizeLow: _CIntLikeField[DWORD]
    dwReserved0: _CIntLikeField[DWORD]
    dwReserved1: _CIntLikeField[DWORD]
    cFileName: _CField[Array[CHAR], bytes, bytes]
    cAlternateFileName: _CField[Array[CHAR], bytes, bytes]

class WIN32_FIND_DATAW(Structure):
    dwFileAttributes: _CIntLikeField[DWORD]
    ftCreationTime: _CField[FILETIME, FILETIME, FILETIME]
    ftLastAccessTime: _CField[FILETIME, FILETIME, FILETIME]
    ftLastWriteTime: _CField[FILETIME, FILETIME, FILETIME]
    nFileSizeHigh: _CIntLikeField[DWORD]
    nFileSizeLow: _CIntLikeField[DWORD]
    dwReserved0: _CIntLikeField[DWORD]
    dwReserved1: _CIntLikeField[DWORD]
    cFileName: _CField[Array[WCHAR], str, str]
    cAlternateFileName: _CField[Array[WCHAR], str, str]

# These are all defined with the POINTER() function, which keeps a cache and will
# return a previously created class if it can. The self-reported __name__
# of these classes is f"LP_{typ.__name__}", where typ is the original class
# passed in to the POINTER() function.

# LP_c_short
class PSHORT(_Pointer[SHORT]): ...

# LP_c_ushort
class PUSHORT(_Pointer[USHORT]): ...

PWORD: Final = PUSHORT
LPWORD: Final = PUSHORT

# LP_c_long
class PLONG(_Pointer[LONG]): ...

LPLONG: Final = PLONG
PBOOL: Final = PLONG
LPBOOL: Final = PLONG

# LP_c_ulong
class PULONG(_Pointer[ULONG]): ...

PDWORD: Final = PULONG
LPDWORD: Final = PDWORD
LPCOLORREF: Final = PDWORD
PLCID: Final = PDWORD

# LP_c_int (or LP_c_long if int and long have the same size)
class PINT(_Pointer[INT]): ...

LPINT: Final = PINT

# LP_c_uint (or LP_c_ulong if int and long have the same size)
class PUINT(_Pointer[UINT]): ...

LPUINT: Final = PUINT

# LP_c_float
class PFLOAT(_Pointer[FLOAT]): ...

# LP_c_longlong (or LP_c_long if long and long long have the same size)
class PLARGE_INTEGER(_Pointer[LARGE_INTEGER]): ...

# LP_c_ulonglong (or LP_c_ulong if long and long long have the same size)
class PULARGE_INTEGER(_Pointer[ULARGE_INTEGER]): ...

# LP_c_byte types
class PBYTE(_Pointer[BYTE]): ...

LPBYTE: Final = PBYTE
PBOOLEAN: Final = PBYTE

# LP_c_char
class PCHAR(_Pointer[CHAR]): ...

# LP_c_wchar
class PWCHAR(_Pointer[WCHAR]): ...

# LP_c_void_p
class PHANDLE(_Pointer[HANDLE]): ...

LPHANDLE: Final = PHANDLE
PHKEY: Final = PHANDLE
LPHKL: Final = PHANDLE
LPSC_HANDLE: Final = PHANDLE

# LP_FILETIME
class PFILETIME(_Pointer[FILETIME]): ...

LPFILETIME: Final = PFILETIME

# LP_MSG
class PMSG(_Pointer[MSG]): ...

LPMSG: Final = PMSG

# LP_POINT
class PPOINT(_Pointer[POINT]): ...

LPPOINT: Final = PPOINT
PPOINTL: Final = PPOINT

# LP_RECT
class PRECT(_Pointer[RECT]): ...

LPRECT: Final = PRECT
PRECTL: Final = PRECT
LPRECTL: Final = PRECT

# LP_SIZE
class PSIZE(_Pointer[SIZE]): ...

LPSIZE: Final = PSIZE
PSIZEL: Final = PSIZE
LPSIZEL: Final = PSIZE

# LP__SMALL_RECT
class PSMALL_RECT(_Pointer[SMALL_RECT]): ...

# LP_WIN32_FIND_DATAA
class PWIN32_FIND_DATAA(_Pointer[WIN32_FIND_DATAA]): ...

LPWIN32_FIND_DATAA: Final = PWIN32_FIND_DATAA

# LP_WIN32_FIND_DATAW
class PWIN32_FIND_DATAW(_Pointer[WIN32_FIND_DATAW]): ...

LPWIN32_FIND_DATAW: Final = PWIN32_FIND_DATAW
