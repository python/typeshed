from _typeshed import Incomplete
from socket import socket
from typing import overload

import _win32typing
from win32.lib.pywintypes import error as error

def AreFileApisANSI(): ...
def CancelIo(handle: int, /) -> None: ...
def CopyFile(_from: str, to: str, bFailIfExists, /) -> None: ...
def CopyFileW(_from: str, to: str, bFailIfExists, /) -> None: ...
def CreateDirectory(__name: str, __sa: _win32typing.PySECURITY_ATTRIBUTES, /) -> None: ...
def CreateDirectoryW(name: str, sa: _win32typing.PySECURITY_ATTRIBUTES, /) -> None: ...
def CreateDirectoryEx(templateName: str, newDirectory: str, sa: _win32typing.PySECURITY_ATTRIBUTES, /) -> None: ...
def CreateFile(
    __fileName: str,
    __desiredAccess: int,
    __shareMode: int,
    __attributes: _win32typing.PySECURITY_ATTRIBUTES | None,
    __CreationDisposition: int,
    __flagsAndAttributes: int,
    __hTemplateFile: int | None,
    /,
) -> _win32typing.PyHANDLE: ...
def CreateIoCompletionPort(handle: int, existing: int, completionKey, numThreads, /) -> int: ...
def CreateMailslot(Name, MaxMessageSize, ReadTimeout, SecurityAttributes: _win32typing.PySECURITY_ATTRIBUTES, /) -> int: ...
def GetMailslotInfo(Mailslot: int, /) -> tuple[Incomplete, Incomplete, Incomplete, Incomplete]: ...
def SetMailslotInfo(Mailslot: int, ReadTimeout, /) -> None: ...
def DefineDosDevice(flags, deviceName: str, targetPath: str, /) -> None: ...
def DefineDosDeviceW(flags, deviceName: str, targetPath: str, /) -> None: ...
def DeleteFile(fileName: str, /) -> None: ...
def DeviceIoControl(Device: int, IoControlCode, InBuffer, OutBuffer, Overlapped: _win32typing.PyOVERLAPPED | None = ..., /): ...
def FindClose(hFindFile, /) -> None: ...
def FindCloseChangeNotification(hChangeHandle, /) -> None: ...
def FindFirstChangeNotification(pathName: str, bWatchSubtree, notifyFilter, /): ...
def FindNextChangeNotification(hChangeHandle, /): ...
def FlushFileBuffers(hFile: int, /) -> None: ...
def GetBinaryType(appName: str, /): ...
def GetDiskFreeSpace(rootPathName: str, /) -> tuple[Incomplete, Incomplete, Incomplete, Incomplete]: ...
def GetDiskFreeSpaceEx(__rootPathName: str, /) -> tuple[int, int, int]: ...
def GetDriveType(rootPathName: str, /): ...
def GetDriveTypeW(rootPathName: str, /): ...
def GetFileAttributes(fileName: str, /): ...
def GetFileAttributesW(fileName: str, /): ...
def GetFileTime(
    handle: int, creationTime: _win32typing.PyTime, accessTime: _win32typing.PyTime, writeTime: _win32typing.PyTime, /
) -> tuple[_win32typing.PyTime, _win32typing.PyTime, _win32typing.PyTime]: ...
def SetFileTime(
    File: int,
    CreationTime: _win32typing.PyTime | None = ...,
    LastAccessTime: _win32typing.PyTime | None = ...,
    LastWriteTime: _win32typing.PyTime | None = ...,
    UTCTimes: bool = ...,
    /,
) -> None: ...
def GetFileInformationByHandle(handle: int, /): ...
def GetCompressedFileSize(): ...
def GetFileSize(): ...
def AllocateReadBuffer(__bufSize: int, /) -> _win32typing.PyOVERLAPPEDReadBuffer: ...
@overload
def ReadFile(__hFile: int, __bufSize: int, /) -> tuple[int, str]: ...
@overload
def ReadFile(
    __hFile: int, __buffer: _win32typing.PyOVERLAPPEDReadBuffer, __overlapped: _win32typing.PyOVERLAPPED | None, /
) -> tuple[int, str]: ...
def WriteFile(
    __hFile: int, __data: str | bytes | _win32typing.PyOVERLAPPEDReadBuffer, __ol: _win32typing.PyOVERLAPPED | None = ..., /
) -> tuple[int, int]: ...
def CloseHandle(__handle: int, /) -> None: ...
def LockFileEx(hFile: int, _int, _int1, _int2, ol: _win32typing.PyOVERLAPPED | None = ..., /) -> None: ...
def UnlockFileEx(hFile: int, _int, _int1, ol: _win32typing.PyOVERLAPPED | None = ..., /) -> None: ...
def GetQueuedCompletionStatus(hPort: int, timeOut, /) -> tuple[Incomplete, Incomplete, Incomplete, _win32typing.PyOVERLAPPED]: ...
def PostQueuedCompletionStatus(
    handle: int, numberOfbytes: int = ..., completionKey: int = ..., overlapped: _win32typing.PyOVERLAPPED | None = ..., /
): ...
def GetFileType(hFile: int, /): ...
def GetLogicalDrives(): ...
def GetOverlappedResult(__hFile: int, __overlapped: _win32typing.PyOVERLAPPED, __bWait: int | bool, /) -> int: ...
def LockFile(hFile: int, offsetLow, offsetHigh, nNumberOfBytesToLockLow, nNumberOfBytesToLockHigh, /) -> None: ...
def MoveFile(existingFileName: str, newFileName: str, /) -> None: ...
def MoveFileW(existingFileName: str, newFileName: str, /) -> None: ...
def MoveFileEx(existingFileName: str, newFileName: str, flags, /) -> None: ...
def MoveFileExW(existingFileName: str, newFileName: str, flags, /) -> None: ...
def QueryDosDevice(DeviceName: str, /) -> str: ...
def ReadDirectoryChangesW(
    handle: int, size, bWatchSubtree, dwNotifyFilter, overlapped: _win32typing.PyOVERLAPPED | None = ..., /
) -> None: ...
def FILE_NOTIFY_INFORMATION(buffer: str, size, /) -> tuple[tuple[Incomplete, Incomplete], ...]: ...
def SetCurrentDirectory(lpPathName: str, /) -> None: ...
def SetEndOfFile(hFile: int, /) -> None: ...
def SetFileApisToANSI() -> None: ...
def SetFileApisToOEM() -> None: ...
def SetFileAttributes(__filename: str, __newAttributes: int, /) -> None: ...
def SetFilePointer(handle: int, offset, moveMethod, /) -> None: ...
def SetVolumeLabel(rootPathName: str, volumeName: str, /) -> None: ...
def UnlockFile(hFile: int, offsetLow, offsetHigh, nNumberOfBytesToUnlockLow, nNumberOfBytesToUnlockHigh, /) -> None: ...
def TransmitFile(
    Socket,
    File: int,
    NumberOfBytesToWrite,
    NumberOfBytesPerSend,
    Overlapped: _win32typing.PyOVERLAPPED,
    Flags,
    Head: Incomplete | None = ...,
    Tail: Incomplete | None = ...,
    /,
) -> None: ...
def ConnectEx(
    s, name, Overlapped: _win32typing.PyOVERLAPPED, SendBuffer: Incomplete | None = ..., /
) -> tuple[Incomplete, Incomplete]: ...
def AcceptEx(slistening, sAccepting, buffer, ol: _win32typing.PyOVERLAPPED, /) -> None: ...
def CalculateSocketEndPointSize(socket, /): ...
def GetAcceptExSockaddrs(
    sAccepting, buffer: _win32typing.PyOVERLAPPEDReadBuffer, /
) -> tuple[Incomplete, Incomplete, Incomplete]: ...
def WSAEventSelect(__socket: socket, __hEvent: int, __networkEvents: int, /) -> None: ...
def WSAEnumNetworkEvents(__s: socket, __hEvent: int, /) -> dict[int, int]: ...
def WSAAsyncSelect(socket, hwnd: int, _int, networkEvents, /) -> None: ...
def WSASend(s, buffer: str, ol: _win32typing.PyOVERLAPPED, dwFlags, /) -> tuple[Incomplete, Incomplete]: ...
def WSARecv(s, buffer, ol: _win32typing.PyOVERLAPPED, dwFlags, /) -> tuple[Incomplete, Incomplete]: ...
def BuildCommDCB(_def: str, dcb: _win32typing.PyDCB, /) -> _win32typing.PyDCB: ...
def ClearCommError(__handle: int, /) -> tuple[Incomplete, _win32typing.PyCOMSTAT]: ...
def EscapeCommFunction(handle: int, /) -> None: ...
def GetCommState(handle: int, /) -> _win32typing.PyDCB: ...
def SetCommState(handle: int, dcb: _win32typing.PyDCB, /) -> None: ...
def ClearCommBreak(handle: int, /) -> None: ...
def GetCommMask(handle: int, /): ...
def SetCommMask(handle: int, val, /): ...
def GetCommModemStatus(handle: int, /): ...
def GetCommTimeouts(handle: int, /): ...
def SetCommTimeouts(handle: int, val, /): ...
def PurgeComm(handle: int, action, /) -> None: ...
def SetCommBreak(handle: int, /) -> None: ...
def SetupComm(handle: int, dwInQueue, dwOutQueue, /) -> None: ...
def TransmitCommChar(handle: int, cChar, /) -> None: ...
def WaitCommEvent(handle: int, overlapped: _win32typing.PyOVERLAPPED, /) -> None: ...
def SetVolumeMountPoint(VolumeMountPoint: str, VolumeName: str, /) -> str: ...
def DeleteVolumeMountPoint(VolumeMountPoint: str, /) -> None: ...
def GetVolumeNameForVolumeMountPoint(VolumeMountPoint: str, /) -> str: ...
def GetVolumePathName(FileName: str, BufferLength: int = ..., /) -> str: ...
def GetVolumePathNamesForVolumeName(VolumeName: str, /) -> list[Incomplete]: ...
def CreateHardLink(
    FileName: str,
    ExistingFileName: str,
    SecurityAttributes: _win32typing.PySECURITY_ATTRIBUTES | None = ...,
    Transaction: int | None = ...,
    /,
) -> None: ...
def CreateSymbolicLink(SymlinkFileName: str, TargetFileName: str, Flags: int = ..., Transaction: int | None = ..., /) -> None: ...
def EncryptFile(filename: str, /) -> None: ...
def DecryptFile(filename: str, /) -> None: ...
def EncryptionDisable(DirName: str, Disable, /) -> None: ...
def FileEncryptionStatus(FileName: str, /): ...
def QueryUsersOnEncryptedFile(FileName: str, /) -> tuple[_win32typing.PySID, str, Incomplete]: ...
def QueryRecoveryAgentsOnEncryptedFile(FileName: str, /) -> tuple[_win32typing.PySID, str, Incomplete]: ...
def RemoveUsersFromEncryptedFile(FileName: str, pHashes: tuple[tuple[_win32typing.PySID, str, Incomplete], ...], /) -> None: ...
def AddUsersToEncryptedFile(FileName: str, pUsers: tuple[tuple[_win32typing.PySID, str, Incomplete], ...], /) -> None: ...
def DuplicateEncryptionInfoFile(
    SrcFileName: str,
    DstFileName: str,
    CreationDisposition,
    Attributes,
    SecurityAttributes: _win32typing.PySECURITY_ATTRIBUTES | None = ...,
    /,
) -> None: ...
def BackupRead(
    hFile: int, NumberOfBytesToRead, Buffer, bAbort, bProcessSecurity, lpContext, /
) -> tuple[Incomplete, Incomplete, Incomplete]: ...
def BackupSeek(hFile: int, NumberOfBytesToSeek, lpContext, /): ...
def BackupWrite(
    hFile: int, NumberOfBytesToWrite, Buffer: str, bAbort, bProcessSecurity, lpContext, /
) -> tuple[Incomplete, Incomplete]: ...
def SetFileShortName(hFile: int, ShortName, /) -> None: ...
def CopyFileEx(
    ExistingFileName,
    NewFileName,
    ProgressRoutine: _win32typing.CopyProgressRoutine | None = ...,
    Data: Incomplete | None = ...,
    Cancel: bool = ...,
    CopyFlags: int = ...,
    Transaction: int | None = ...,
    /,
) -> None: ...
def MoveFileWithProgress(
    ExistingFileName,
    NewFileName,
    ProgressRoutine: _win32typing.CopyProgressRoutine | None = ...,
    Data: Incomplete | None = ...,
    Flags: int = ...,
    Transaction: int | None = ...,
    /,
) -> None: ...
def ReplaceFile(
    ReplacedFileName,
    ReplacementFileName,
    BackupFileName: Incomplete | None = ...,
    ReplaceFlags: int = ...,
    Exclude: Incomplete | None = ...,
    Reserved: Incomplete | None = ...,
    /,
) -> None: ...
def OpenEncryptedFileRaw(FileName, Flags, /): ...
def ReadEncryptedFileRaw(ExportCallback, CallbackContext, Context, /) -> None: ...
def WriteEncryptedFileRaw(ImportCallback, CallbackContext, Context, /) -> None: ...
def CloseEncryptedFileRaw(Context, /) -> None: ...
def CreateFileW(
    FileName: str,
    DesiredAccess,
    ShareMode,
    SecurityAttributes: _win32typing.PySECURITY_ATTRIBUTES,
    CreationDisposition,
    FlagsAndAttributes,
    TemplateFile: int | None = ...,
    Transaction: int | None = ...,
    MiniVersion: Incomplete | None = ...,
    ExtendedParameter: Incomplete | None = ...,
    /,
) -> int: ...
def DeleteFileW(FileName: str, Transaction: int | None = ..., /) -> None: ...
def GetFileAttributesEx(FileName: str, InfoLevelId, Transaction: int | None = ..., /): ...
def SetFileAttributesW(FileName, FileAttributes, Transaction: int | None = ..., /) -> None: ...
def CreateDirectoryExW(
    TemplateDirectory: str,
    NewDirectory: str,
    SecurityAttributes: _win32typing.PySECURITY_ATTRIBUTES | None = ...,
    Transaction: int | None = ...,
    /,
) -> None: ...
def RemoveDirectory(PathName: str, Transaction: int | None = ..., /) -> None: ...
def FindFilesW(FileName: str, Transaction: int | None = ..., /): ...
def FindFilesIterator(FileName: str, Transaction: int | None = ..., /): ...
def FindStreams(FileName: str, Transaction: int | None = ..., /) -> list[tuple[Incomplete, str]]: ...
def FindFileNames(FileName: str, Transaction: int | None = ..., /) -> list[Incomplete]: ...
def GetFinalPathNameByHandle(File: int, Flags, /) -> str: ...
def SfcGetNextProtectedFile() -> list[Incomplete]: ...
def SfcIsFileProtected(ProtFileName: str, /): ...
def GetLongPathName(__ShortPath: str, __Transaction: int | None = ..., /) -> str: ...
def GetFullPathName(FileName, Transaction: int | None = ..., /): ...
def Wow64DisableWow64FsRedirection(): ...
def Wow64RevertWow64FsRedirection(OldValue, /) -> None: ...
def GetFileInformationByHandleEx(File: int, FileInformationClass, /): ...
def SetFileInformationByHandle(File: int, FileInformationClass, Information, /) -> None: ...
def ReOpenFile(OriginalFile: int, DesiredAccess, ShareMode, Flags, /) -> int: ...
def OpenFileById(
    File: int,
    FileId: _win32typing.PyIID,
    DesiredAccess,
    ShareMode,
    Flags,
    SecurityAttributes: _win32typing.PySECURITY_ATTRIBUTES | None = ...,
    /,
) -> int: ...
def DCB(*args): ...  # incomplete
def GetFileAttributesExW(*args): ...  # incomplete
def OVERLAPPED() -> _win32typing.PyOVERLAPPED: ...

CALLBACK_CHUNK_FINISHED: int
CALLBACK_STREAM_SWITCH: int
CBR_110: int
CBR_115200: int
CBR_1200: int
CBR_128000: int
CBR_14400: int
CBR_19200: int
CBR_2400: int
CBR_256000: int
CBR_300: int
CBR_38400: int
CBR_4800: int
CBR_56000: int
CBR_57600: int
CBR_600: int
CBR_9600: int
CLRBREAK: int
CLRDTR: int
CLRRTS: int
COPY_FILE_ALLOW_DECRYPTED_DESTINATION: int
COPY_FILE_FAIL_IF_EXISTS: int
COPY_FILE_OPEN_SOURCE_FOR_WRITE: int
COPY_FILE_RESTARTABLE: int
CREATE_ALWAYS: int
CREATE_FOR_DIR: int
CREATE_FOR_IMPORT: int
CREATE_NEW: int
DRIVE_CDROM: int
DRIVE_FIXED: int
DRIVE_NO_ROOT_DIR: int
DRIVE_RAMDISK: int
DRIVE_REMOTE: int
DRIVE_REMOVABLE: int
DRIVE_UNKNOWN: int
DTR_CONTROL_DISABLE: int
DTR_CONTROL_ENABLE: int
DTR_CONTROL_HANDSHAKE: int
EV_BREAK: int
EV_CTS: int
EV_DSR: int
EV_ERR: int
EV_RING: int
EV_RLSD: int
EV_RXCHAR: int
EV_RXFLAG: int
EV_TXEMPTY: int
EVENPARITY: int
FD_ACCEPT: int
FD_CLOSE: int
FD_CONNECT: int
FD_GROUP_QOS: int
FD_OOB: int
FD_QOS: int
FD_READ: int
FD_ROUTING_INTERFACE_CHANGE: int
FD_WRITE: int
FILE_ALL_ACCESS: int
FILE_ATTRIBUTE_ARCHIVE: int
FILE_ATTRIBUTE_COMPRESSED: int
FILE_ATTRIBUTE_DIRECTORY: int
FILE_ATTRIBUTE_HIDDEN: int
FILE_ATTRIBUTE_NORMAL: int
FILE_ATTRIBUTE_OFFLINE: int
FILE_ATTRIBUTE_READONLY: int
FILE_ATTRIBUTE_SYSTEM: int
FILE_ATTRIBUTE_TEMPORARY: int
FILE_BEGIN: int
FILE_CURRENT: int
FILE_ENCRYPTABLE: int
FILE_END: int
FILE_FLAG_BACKUP_SEMANTICS: int
FILE_FLAG_DELETE_ON_CLOSE: int
FILE_FLAG_NO_BUFFERING: int
FILE_FLAG_OPEN_REPARSE_POINT: int
FILE_FLAG_OVERLAPPED: int
FILE_FLAG_POSIX_SEMANTICS: int
FILE_FLAG_RANDOM_ACCESS: int
FILE_FLAG_SEQUENTIAL_SCAN: int
FILE_FLAG_WRITE_THROUGH: int
FILE_GENERIC_READ: int
FILE_GENERIC_WRITE: int
FILE_IS_ENCRYPTED: int
FILE_READ_ONLY: int
FILE_ROOT_DIR: int
FILE_SHARE_DELETE: int
FILE_SHARE_READ: int
FILE_SHARE_WRITE: int
FILE_SYSTEM_ATTR: int
FILE_SYSTEM_DIR: int
FILE_SYSTEM_NOT_SUPPORT: int
FILE_TYPE_CHAR: int
FILE_TYPE_DISK: int
FILE_TYPE_PIPE: int
FILE_TYPE_UNKNOWN: int
FILE_UNKNOWN: int
FILE_USER_DISALLOWED: int
FileAllocationInfo: int
FileAttributeTagInfo: int
FileBasicInfo: int
FileCompressionInfo: int
FileDispositionInfo: int
FileEndOfFileInfo: int
FileIdBothDirectoryInfo: int
FileIdBothDirectoryRestartInfo: int
FileIdType: int
FileIoPriorityHintInfo: int
FileNameInfo: int
FileRenameInfo: int
FileStandardInfo: int
FileStreamInfo: int
GENERIC_EXECUTE: int
GENERIC_READ: int
GENERIC_WRITE: int
GetFileExInfoStandard: int
IoPriorityHintLow: int
IoPriorityHintNormal: int
IoPriorityHintVeryLow: int
MARKPARITY: int
MOVEFILE_COPY_ALLOWED: int
MOVEFILE_CREATE_HARDLINK: int
MOVEFILE_DELAY_UNTIL_REBOOT: int
MOVEFILE_FAIL_IF_NOT_TRACKABLE: int
MOVEFILE_REPLACE_EXISTING: int
MOVEFILE_WRITE_THROUGH: int
NOPARITY: int
ObjectIdType: int
ODDPARITY: int
ONE5STOPBITS: int
ONESTOPBIT: int
OPEN_ALWAYS: int
OPEN_EXISTING: int
OVERWRITE_HIDDEN: int
PROGRESS_CANCEL: int
PROGRESS_CONTINUE: int
PROGRESS_QUIET: int
PROGRESS_STOP: int
PURGE_RXABORT: int
PURGE_RXCLEAR: int
PURGE_TXABORT: int
PURGE_TXCLEAR: int
REPLACEFILE_IGNORE_MERGE_ERRORS: int
REPLACEFILE_WRITE_THROUGH: int
RTS_CONTROL_DISABLE: int
RTS_CONTROL_ENABLE: int
RTS_CONTROL_HANDSHAKE: int
RTS_CONTROL_TOGGLE: int
SCS_32BIT_BINARY: int
SCS_DOS_BINARY: int
SCS_OS216_BINARY: int
SCS_PIF_BINARY: int
SCS_POSIX_BINARY: int
SCS_WOW_BINARY: int
SECURITY_ANONYMOUS: int
SECURITY_CONTEXT_TRACKING: int
SECURITY_DELEGATION: int
SECURITY_EFFECTIVE_ONLY: int
SECURITY_IDENTIFICATION: int
SECURITY_IMPERSONATION: int
SETBREAK: int
SETDTR: int
SETRTS: int
SETXOFF: int
SETXON: int
SO_CONNECT_TIME: int
SO_UPDATE_ACCEPT_CONTEXT: int
SO_UPDATE_CONNECT_CONTEXT: int
SPACEPARITY: int
SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE: int
SYMBOLIC_LINK_FLAG_DIRECTORY: int
TF_DISCONNECT: int
TF_REUSE_SOCKET: int
TF_USE_DEFAULT_WORKER: int
TF_USE_KERNEL_APC: int
TF_USE_SYSTEM_THREAD: int
TF_WRITE_BEHIND: int
TRUNCATE_EXISTING: int
TWOSTOPBITS: int
WSA_IO_PENDING: int
WSA_OPERATION_ABORTED: int
WSAECONNABORTED: int
WSAECONNRESET: int
WSAEDISCON: int
WSAEFAULT: int
WSAEINPROGRESS: int
WSAEINTR: int
WSAEINVAL: int
WSAEMSGSIZE: int
WSAENETDOWN: int
WSAENETRESET: int
WSAENOBUFS: int
WSAENOTCONN: int
WSAENOTSOCK: int
WSAEOPNOTSUPP: int
WSAESHUTDOWN: int
WSAEWOULDBLOCK: int
FD_ADDRESS_LIST_CHANGE: int
INVALID_HANDLE_VALUE: int
UNICODE: int

# win32pipe.FDCreatePipe is the only known public method to expose this. But it opens both read and write handles.
def _open_osfhandle(osfhandle: _win32typing.PyHANDLE, flags: int, /) -> int: ...
