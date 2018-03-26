from . import _Pointer, _SimpleCData, Array, Structure, c_byte, c_char, c_char_p, c_double, c_float, c_int, c_long, c_longlong, c_short, c_uint, c_ulong, c_ulonglong, c_ushort, c_void_p, c_wchar, c_wchar_p

BYTE = c_byte
WORD = c_ushort
DWORD = c_ulong 
CHAR = c_char
WCHAR = c_wchar
UINT = c_uint
INT = c_int
DOUBLE = c_double
FLOAT = c_float 
BOOLEAN = BYTE
BOOL = c_long 
class VARIANT_BOOL(_SimpleCData[bool]): ... 
ULONG = c_ulong
LONG = c_long 
USHORT = c_ushort
SHORT = c_short 
_LARGE_INTEGER = LARGE_INTEGER = c_longlong
_ULARGE_INTEGER = ULARGE_INTEGER = c_ulonglong

LPCOLESTR = LPOLESTR = OLESTR = c_wchar_p
LPCWSTR = LPWSTR = c_wchar_p
LPCSTR = LPSTR = c_char_p
LPCVOID = LPVOID = c_void_p

# These two types are pointer-sized unsigned and signed ints, respectively.
# At runtime, they are either c_[u]long or c_[u]longlong, depending on the host's pointer size (they are not really separate classes).
class WPARAM(_SimpleCData[int]): ...
class LPARAM(_SimpleCData[int]): ...

ATOM = WORD
LANGID = WORD 
COLORREF = DWORD
LGRPID = DWORD
LCTYPE = DWORD 
LCID = DWORD

HANDLE = c_void_p 
HACCEL = HANDLE
HBITMAP = HANDLE
HBRUSH = HANDLE
HCOLORSPACE = HANDLE
HDC = HANDLE
HDESK = HANDLE
HDWP = HANDLE
HENHMETAFILE = HANDLE
HFONT = HANDLE
HGDIOBJ = HANDLE
HGLOBAL = HANDLE
HHOOK = HANDLE
HICON = HANDLE
HINSTANCE = HANDLE
HKEY = HANDLE
HKL = HANDLE
HLOCAL = HANDLE
HMENU = HANDLE
HMETAFILE = HANDLE
HMODULE = HANDLE
HMONITOR = HANDLE
HPALETTE = HANDLE
HPEN = HANDLE
HRGN = HANDLE
HRSRC = HANDLE
HSTR = HANDLE
HTASK = HANDLE
HWINSTA = HANDLE
HWND = HANDLE
SC_HANDLE = HANDLE
SERVICE_STATUS_HANDLE = HANDLE

class RECT(Structure):
    left: LONG
    top: LONG
    right: LONG
    bottom: LONG
tagRECT = _RECTL = RECTL = RECT

class _SMALL_RECT(Structure):
    Left: SHORT
    Top: SHORT
    Right: SHORT
    Bottom: SHORT
SMALL_RECT = _SMALL_RECT

class _COORD(Structure):
    X: SHORT
    Y: SHORT

class POINT(Structure):
    x: LONG
    y: LONG
tagPOINT = _POINTL = POINTL = POINT

class SIZE(Structure):
    cx: LONG
    cy: LONG
tagSIZE = SIZEL = SIZE

def RGB(red: int, green: int, blue: int) -> int: ...

class FILETIME(Structure):
    dwLowDateTime: DWORD
    dwHighDateTime: DWORD
_FILETIME = FILETIME

class MSG(Structure):
    hWnd: HWND
    message: UINT
    wParam: WPARAM
    lParam: LPARAM
    time: DWORD
    pt: POINT
tagMSG = MSG
MAX_PATH: int

class WIN32_FIND_DATAA(Structure):
    dwFileAttributes: DWORD
    ftCreationTime: FILETIME
    ftLastAccessTime: FILETIME
    ftLastWriteTime: FILETIME
    nFileSizeHigh: DWORD
    nFileSizeLow: DWORD
    dwReserved0: DWORD
    dwReserved1: DWORD
    cFileName: Array[CHAR]
    cAlternateFileName: Array[CHAR]

class WIN32_FIND_DATAW(Structure):
    dwFileAttributes: DWORD
    ftCreationTime: FILETIME
    ftLastAccessTime: FILETIME
    ftLastWriteTime: FILETIME
    nFileSizeHigh: DWORD
    nFileSizeLow: DWORD
    dwReserved0: DWORD
    dwReserved1: DWORD
    cFileName: Array[WCHAR]
    cAlternateFileName: Array[WCHAR]

# These pointer type definitions use _Pointer instead of POINTER, to allow them to be used in type annotations.
LPBOOL = PBOOL = _Pointer[BOOL]
PBOOLEAN = _Pointer[BOOLEAN]
LPBYTE = PBYTE = _Pointer[BYTE]
PCHAR = _Pointer[CHAR]
LPCOLORREF = _Pointer[COLORREF]
LPDWORD = PDWORD = _Pointer[DWORD]
LPFILETIME = PFILETIME = _Pointer[FILETIME]
PFLOAT = _Pointer[FLOAT]
LPHANDLE = PHANDLE = _Pointer[HANDLE]
PHKEY = _Pointer[HKEY]
LPHKL = _Pointer[HKL]
LPINT = PINT = _Pointer[INT]
PLARGE_INTEGER = _Pointer[LARGE_INTEGER]
PLCID = _Pointer[LCID]
LPLONG = PLONG = _Pointer[LONG]
LPMSG = PMSG = _Pointer[MSG]
LPPOINT = PPOINT = _Pointer[POINT]
PPOINTL = _Pointer[POINTL]
LPRECT = PRECT = _Pointer[RECT]
LPRECTL = PRECTL = _Pointer[RECTL]
LPSC_HANDLE = _Pointer[SC_HANDLE]
PSHORT = _Pointer[SHORT]
LPSIZE = PSIZE = _Pointer[SIZE]
LPSIZEL = PSIZEL = _Pointer[SIZEL]
PSMALL_RECT = _Pointer[SMALL_RECT]
LPUINT = PUINT = _Pointer[UINT]
PULARGE_INTEGER = _Pointer[ULARGE_INTEGER]
PULONG = _Pointer[ULONG]
PUSHORT = _Pointer[USHORT]
PWCHAR = _Pointer[WCHAR]
LPWIN32_FIND_DATAA = PWIN32_FIND_DATAA = _Pointer[WIN32_FIND_DATAA]
LPWIN32_FIND_DATAW = PWIN32_FIND_DATAW = _Pointer[WIN32_FIND_DATAW]
LPWORD = PWORD = _Pointer[WORD]
