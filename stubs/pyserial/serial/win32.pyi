import sys
from ctypes import Structure, Union, _CField, _NamedFuncPointer, _Pointer, c_int64, c_ulong, c_void_p
from ctypes.wintypes import DWORD
from typing import Any
from typing_extensions import TypeAlias

if sys.platform == "win32":
    def is_64bit() -> bool: ...

    ULONG_PTR: type[c_int64 | c_ulong]

    class _SECURITY_ATTRIBUTES(Structure):
        nLength: _CField[Any, Any, Any]
        lpSecurityDescriptor: _CField[Any, Any, Any]
        bInheritHandle: _CField[Any, Any, Any]
    LPSECURITY_ATTRIBUTES: type[_Pointer[_SECURITY_ATTRIBUTES]]
    CreateEvent: _NamedFuncPointer
    CreateFile: _NamedFuncPointer
    # The following are included in __all__ but their existence is not guaranteed as
    # they are defined in a try/except block. Their aliases above are always defined.
    CreateEventW: _NamedFuncPointer
    CreateFileW: _NamedFuncPointer

    class _OVERLAPPED(Structure):
        Internal: _CField[Any, Any, Any]
        InternalHigh: _CField[Any, Any, Any]
        Offset: _CField[Any, Any, Any]
        OffsetHigh: _CField[Any, Any, Any]
        Pointer: _CField[Any, Any, Any]
        hEvent: _CField[Any, Any, Any]
    OVERLAPPED: TypeAlias = _OVERLAPPED

    class _COMSTAT(Structure):
        fCtsHold: _CField[Any, Any, Any]
        fDsrHold: _CField[Any, Any, Any]
        fRlsdHold: _CField[Any, Any, Any]
        fXoffHold: _CField[Any, Any, Any]
        fXoffSent: _CField[Any, Any, Any]
        fEof: _CField[Any, Any, Any]
        fTxim: _CField[Any, Any, Any]
        fReserved: _CField[Any, Any, Any]
        cbInQue: _CField[Any, Any, Any]
        cbOutQue: _CField[Any, Any, Any]
    COMSTAT: TypeAlias = _COMSTAT

    class _DCB(Structure):
        DCBlength: _CField[Any, Any, Any]
        BaudRate: _CField[Any, Any, Any]
        fBinary: _CField[Any, Any, Any]
        fParity: _CField[Any, Any, Any]
        fOutxCtsFlow: _CField[Any, Any, Any]
        fOutxDsrFlow: _CField[Any, Any, Any]
        fDtrControl: _CField[Any, Any, Any]
        fDsrSensitivity: _CField[Any, Any, Any]
        fTXContinueOnXoff: _CField[Any, Any, Any]
        fOutX: _CField[Any, Any, Any]
        fInX: _CField[Any, Any, Any]
        fErrorChar: _CField[Any, Any, Any]
        fNull: _CField[Any, Any, Any]
        fRtsControl: _CField[Any, Any, Any]
        fAbortOnError: _CField[Any, Any, Any]
        fDummy2: _CField[Any, Any, Any]
        wReserved: _CField[Any, Any, Any]
        XonLim: _CField[Any, Any, Any]
        XoffLim: _CField[Any, Any, Any]
        ByteSize: _CField[Any, Any, Any]
        Parity: _CField[Any, Any, Any]
        StopBits: _CField[Any, Any, Any]
        XonChar: _CField[Any, Any, Any]
        XoffChar: _CField[Any, Any, Any]
        ErrorChar: _CField[Any, Any, Any]
        EofChar: _CField[Any, Any, Any]
        EvtChar: _CField[Any, Any, Any]
        wReserved1: _CField[Any, Any, Any]
    DCB: TypeAlias = _DCB

    class _COMMTIMEOUTS(Structure):
        ReadIntervalTimeout: _CField[Any, Any, Any]
        ReadTotalTimeoutMultiplier: _CField[Any, Any, Any]
        ReadTotalTimeoutConstant: _CField[Any, Any, Any]
        WriteTotalTimeoutMultiplier: _CField[Any, Any, Any]
        WriteTotalTimeoutConstant: _CField[Any, Any, Any]
    COMMTIMEOUTS: TypeAlias = _COMMTIMEOUTS

    GetLastError: _NamedFuncPointer
    LPOVERLAPPED: type[_Pointer[_OVERLAPPED]]
    LPDWORD: type[_Pointer[DWORD]]
    GetOverlappedResult: _NamedFuncPointer
    ResetEvent: _NamedFuncPointer
    LPCVOID = c_void_p
    WriteFile: _NamedFuncPointer
    LPVOID = c_void_p
    ReadFile: _NamedFuncPointer
    CloseHandle: _NamedFuncPointer
    ClearCommBreak: _NamedFuncPointer
    LPCOMSTAT: type[_Pointer[_COMSTAT]]
    ClearCommError: _NamedFuncPointer
    SetupComm: _NamedFuncPointer
    EscapeCommFunction: _NamedFuncPointer
    GetCommModemStatus: _NamedFuncPointer
    LPDCB: type[_Pointer[_DCB]]
    GetCommState: _NamedFuncPointer
    LPCOMMTIMEOUTS: type[_Pointer[_COMMTIMEOUTS]]
    GetCommTimeouts: _NamedFuncPointer
    PurgeComm: _NamedFuncPointer
    SetCommBreak: _NamedFuncPointer
    SetCommMask: _NamedFuncPointer
    SetCommState: _NamedFuncPointer
    SetCommTimeouts: _NamedFuncPointer
    WaitForSingleObject: _NamedFuncPointer
    WaitCommEvent: _NamedFuncPointer
    CancelIoEx: _NamedFuncPointer

    ONESTOPBIT: int
    TWOSTOPBITS: int
    NOPARITY: int
    ODDPARITY: int
    EVENPARITY: int
    RTS_CONTROL_HANDSHAKE: int
    RTS_CONTROL_ENABLE: int
    DTR_CONTROL_HANDSHAKE: int
    DTR_CONTROL_ENABLE: int
    MS_DSR_ON: int
    EV_RING: int
    EV_PERR: int
    EV_ERR: int
    SETXOFF: int
    EV_RXCHAR: int
    GENERIC_WRITE: int
    PURGE_TXCLEAR: int
    FILE_FLAG_OVERLAPPED: int
    EV_DSR: int
    MAXDWORD: int
    EV_RLSD: int
    ERROR_IO_PENDING: int
    MS_CTS_ON: int
    EV_EVENT1: int
    EV_RX80FULL: int
    PURGE_RXABORT: int
    FILE_ATTRIBUTE_NORMAL: int
    PURGE_TXABORT: int
    SETXON: int
    OPEN_EXISTING: int
    MS_RING_ON: int
    EV_TXEMPTY: int
    EV_RXFLAG: int
    MS_RLSD_ON: int
    GENERIC_READ: int
    EV_EVENT2: int
    EV_CTS: int
    EV_BREAK: int
    PURGE_RXCLEAR: int

    class N11_OVERLAPPED4DOLLAR_48E(Union):
        Offset: _CField[Any, Any, Any]
        OffsetHigh: _CField[Any, Any, Any]
        Pointer: _CField[Any, Any, Any]

    class N11_OVERLAPPED4DOLLAR_484DOLLAR_49E(Structure):
        Offset: _CField[Any, Any, Any]
        OffsetHigh: _CField[Any, Any, Any]
    PVOID: TypeAlias = c_void_p
