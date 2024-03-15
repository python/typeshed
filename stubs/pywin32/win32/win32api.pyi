from _typeshed import Incomplete, ReadableBuffer
from collections.abc import Callable, Iterable
from typing import TypedDict
from typing_extensions import deprecated

import _win32typing
from win32.lib.pywintypes import TimeType, error as error

class _MonitorInfo(TypedDict):
    Monitor: tuple[int, int, int, int]
    Work: tuple[int, int, int, int]
    Flags: int
    Device: str

class _FileVersionInfo(TypedDict):
    Signature: int
    StrucVersion: int
    FileVersionMS: int
    FileVersionLS: int
    ProductVersionMS: int
    ProductVersionLS: int
    FileFlagsMask: int
    FileFlags: int
    FileOS: int
    FileType: int
    FileSubtype: int
    FileDate: None | Incomplete

def AbortSystemShutdown(computerName: str, /) -> None: ...
def InitiateSystemShutdown(computerName: str, message: str, timeOut, bForceClose, bRebootAfterShutdown, /) -> None: ...
def Apply(exceptionHandler, func, args, /): ...
def Beep(freq, dur, /) -> None: ...
def BeginUpdateResource(filename: str, delete, /) -> int: ...
def ChangeDisplaySettings(DevMode: _win32typing.PyDEVMODE, Flags, /): ...
def ChangeDisplaySettingsEx(DeviceName: str | None = ..., DevMode: _win32typing.PyDEVMODE | None = ..., Flags=...) -> int: ...
def ClipCursor(arg: tuple[Incomplete, Incomplete, Incomplete, Incomplete], /) -> None: ...
def CloseHandle(handle: int, /) -> None: ...
def CopyFile(src, dest: str, bFailOnExist: int = ..., /) -> None: ...
def DebugBreak() -> None: ...
def DeleteFile(fileName: str, /) -> None: ...
def DragQueryFile(hDrop, fileNum: int = ..., /) -> str: ...
def DragFinish(hDrop, /) -> None: ...
def DuplicateHandle(
    hSourceProcess: int, hSource: int, hTargetProcessHandle: int, desiredAccess: int, bInheritHandle: int, options: int, /
) -> int: ...
def EndUpdateResource(handle: int, discard, /) -> None: ...
def EnumDisplayDevices(Device: str | None = ..., DevNum: int = ..., Flags: int = ...) -> _win32typing.PyDISPLAY_DEVICE: ...
def EnumDisplayMonitors(
    hdc: int | None = ..., rcClip: _win32typing.PyRECT | None = ...
) -> list[tuple[_win32typing.PyHANDLE, _win32typing.PyHANDLE, tuple[int, int, int, int]]]: ...
def EnumDisplaySettings(DeviceName: str | None = ..., ModeNum: int = ...) -> _win32typing.PyDEVMODEW: ...
def EnumDisplaySettingsEx(DeviceName: str | None = ..., ModeNum=..., Flags=...) -> _win32typing.PyDEVMODEW: ...
def EnumResourceLanguages(
    hmodule: int, lpType: _win32typing.PyResourceId, lpName: _win32typing.PyResourceId, /
) -> list[Incomplete]: ...
def EnumResourceNames(hmodule: int, resType: _win32typing.PyResourceId, /) -> list[str]: ...
def EnumResourceTypes(hmodule: int, /) -> list[Incomplete]: ...
def ExpandEnvironmentStrings(_in: str, /) -> str: ...
def ExitWindows(reserved1: int = ..., reserved2: int = ..., /) -> None: ...
def ExitWindowsEx(flags, reserved: int = ..., /) -> None: ...
def FindFiles(fileSpec: str, /): ...
def FindFirstChangeNotification(pathName: str, bSubDirs, _filter, /): ...
def FindNextChangeNotification(handle: int, /) -> None: ...
def FindCloseChangeNotification(handle, /) -> None: ...
def FindExecutable(filename: str, _dir: str, /) -> tuple[Incomplete, str]: ...
def FormatMessage(
    flags: int, source: str | None = ..., messageId: int = ..., languageID: int = ..., inserts: Iterable[str] | None = ..., /
) -> str: ...
def FormatMessageW(
    flags: int, source: int | None = ..., messageId: int = ..., languageID: int = ..., inserts: Iterable[str] | None = ..., /
) -> str: ...
def FreeLibrary(hModule: int, /) -> None: ...
def GenerateConsoleCtrlEvent(controlEvent: int, processGroupId: int, /) -> None: ...
def GetAsyncKeyState(key, /): ...
def GetCommandLine() -> str: ...
def GetComputerName() -> str: ...
def GetComputerNameEx(NameType, /) -> str: ...
def GetComputerObjectName(NameFormat, /) -> str: ...
def GetMonitorInfo(hMonitor: int) -> _MonitorInfo: ...
def GetUserName() -> str: ...
def GetUserNameEx(NameFormat: int, /) -> str: ...
def GetCursorPos() -> tuple[Incomplete, Incomplete]: ...
def GetCurrentThread(): ...
def GetCurrentThreadId(): ...
def GetCurrentProcessId(): ...
def GetCurrentProcess() -> int: ...
def GetConsoleTitle() -> str: ...
def GetDateFormat(locale, flags, time: TimeType, _format: str, /) -> str: ...
def GetDiskFreeSpace(rootPath: str, /): ...
def GetDiskFreeSpaceEx(rootPath: str, /) -> tuple[int, int, int]: ...
def GetDllDirectory() -> str: ...
def GetDomainName() -> str: ...
def GetEnvironmentVariable(variable, /): ...
def GetEnvironmentVariableW(Name, /) -> str: ...
def GetFileAttributes(pathName: str, /): ...
def GetFileVersionInfo(Filename: str, SubBlock: str, /) -> _FileVersionInfo: ...
def GetFocus(): ...
def GetFullPathName(fileName: str, /) -> str: ...
def GetHandleInformation(Object: int, /): ...
def GetKeyboardLayout(threadId: int = ..., /): ...
def GetKeyboardLayoutName(): ...
def GetKeyboardState() -> str: ...
def GetKeyState(key, /): ...
def GetLastError(): ...
def GetLastInputInfo(): ...
def GetLocalTime(): ...
def GetLongPathName(fileName: str, /) -> str: ...
def GetLongPathNameW(fileName: str, /) -> str: ...
def GetLogicalDrives(): ...
def GetLogicalDriveStrings() -> str: ...
def GetModuleFileName(hModule: int, /) -> str: ...
def GetModuleFileNameW(hModule: int, /) -> str: ...
def GetModuleHandle(fileName: str | None = ..., /) -> int: ...
def GetPwrCapabilities(): ...
@deprecated("This function is obsolete, applications should use the registry instead.")
def GetProfileSection(section: str, iniName: str | None = ..., /): ...
def GetProcAddress(hModule: int, functionName: _win32typing.PyResourceId, /): ...
@deprecated("This function is obsolete, applications should use the registry instead.")
def GetProfileVal(section: str, entry: str, defValue: str, iniName: str | None = ..., /) -> str: ...
def GetShortPathName(path: str, /) -> str: ...
def GetStdHandle(handle: int, /) -> _win32typing.PyHANDLE: ...
def GetSysColor(index, /): ...
def GetSystemDefaultLangID(): ...
def GetSystemDefaultLCID(): ...
def GetSystemDirectory() -> str: ...
def GetSystemFileCacheSize(): ...
def SetSystemFileCacheSize(MinimumFileCacheSize, MaximumFileCacheSize, Flags=...) -> None: ...
def GetSystemInfo(): ...
def GetNativeSystemInfo(): ...
def GetSystemMetrics(index: int, /) -> int: ...
def GetSystemPowerStatus() -> dict[str, int]: ...
def GetSystemTime(): ...
def GetTempFileName(path: str, prefix: str, nUnique, /): ...
def GetTempPath() -> str: ...
def GetThreadLocale(): ...
def GetTickCount() -> int: ...
def GetTimeFormat(locale, flags, time: TimeType, _format: str, /) -> str: ...
def GetTimeZoneInformation(times_as_tuples: bool = ..., /): ...
def GetVersion(): ...
def GetVersionEx(_format: int = ..., /): ...
def GetVolumeInformation(path: str, /): ...
def GetWindowsDirectory() -> str: ...
def GetWindowLong(hwnd: int | None, offset: int, /) -> int: ...
def GetUserDefaultLangID(): ...
def GetUserDefaultLCID(): ...
def GlobalMemoryStatus(): ...
def GlobalMemoryStatusEx() -> dict[str, int]: ...
def keybd_event(bVk, bScan, dwFlags: int = ..., dwExtraInfo: int = ..., /) -> None: ...
def mouse_event(dx, dy, dwData, dwFlags: int = ..., dwExtraInfo=..., /) -> None: ...
def LoadCursor(hInstance: int, cursorid: _win32typing.PyResourceId, /) -> int: ...
def LoadKeyboardLayout(KLID: str, Flags: int = ..., /): ...
def LoadLibrary(fileName: str, /): ...
def LoadLibraryEx(fileName: str, handle: int, handle1, /) -> int: ...
def LoadResource(handle: int, _type: _win32typing.PyResourceId, name: _win32typing.PyResourceId, language, /) -> str: ...
def LoadString(handle: int, stringId, numChars: int = ..., /) -> str: ...
def MessageBeep(arg, /): ...
def MessageBox(hwnd: int | None, message: str, title: str | None = ..., style=..., language=..., /) -> int: ...
def MonitorFromPoint(pt: tuple[Incomplete, Incomplete], Flags: int = ...) -> int: ...
def MonitorFromRect(rc: _win32typing.PyRECT | tuple[int, int, int, int], Flags: int = ...) -> int: ...
def MonitorFromWindow(hwnd: int, Flags: int = ...) -> int: ...
def MoveFile(srcName: str, destName: str, /) -> None: ...
def MoveFileEx(srcName: str, destName: str, flag, /) -> None: ...
def OpenProcess(reqdAccess: int, bInherit: int | bool, pid: int, /) -> int: ...
def OutputDebugString(msg: str, /) -> None: ...
def PostMessage(hwnd: int, idMessage, wParam: Incomplete | None = ..., lParam: Incomplete | None = ..., /) -> None: ...
def PostQuitMessage(exitCode: int = ..., /) -> None: ...
def PostThreadMessage(tid, idMessage, wParam: Incomplete | None = ..., lParam: Incomplete | None = ..., /) -> None: ...
def RegCloseKey(key: _win32typing.PyHKEY, /) -> None: ...
def RegConnectRegistry(computerName: str, key, /): ...
def RegCopyTree(KeySrc: _win32typing.PyHKEY, SubKey: str, KeyDest: _win32typing.PyHKEY) -> None: ...
def RegCreateKey(key: _win32typing.PyHKEY | int, subKey: str, /) -> _win32typing.PyHKEY: ...
def RegCreateKeyEx(
    Key: _win32typing.PyHKEY,
    SubKey: str,
    samDesired,
    Class: str | None = ...,
    Options=...,
    SecurityAttributes: _win32typing.PySECURITY_ATTRIBUTES | None = ...,
    Transaction: int | None = ...,
) -> tuple[_win32typing.PyHKEY, Incomplete]: ...
def RegDeleteKey(key: _win32typing.PyHKEY, subKey: str, /) -> None: ...
def RegDeleteKeyEx(Key: _win32typing.PyHKEY, SubKey: str, samDesired: int = ..., Transaction: int | None = ...) -> None: ...
def RegDeleteTree(Key: _win32typing.PyHKEY, SubKey: str) -> None: ...
def RegDeleteValue(key: _win32typing.PyHKEY, value: str, /) -> None: ...
def RegEnumKey(key: _win32typing.PyHKEY, index, /) -> str: ...
def RegEnumKeyEx(Key: _win32typing.PyHKEY, /): ...
def RegEnumKeyExW(Key: _win32typing.PyHKEY, /): ...
def RegEnumValue(key: _win32typing.PyHKEY, index, /) -> tuple[str, Incomplete, Incomplete]: ...
def RegFlushKey(key: _win32typing.PyHKEY, /) -> None: ...
def RegGetKeySecurity(key: _win32typing.PyHKEY, security_info, /) -> _win32typing.PySECURITY_DESCRIPTOR: ...
def RegLoadKey(key: _win32typing.PyHKEY, subKey: str, filename: str, /) -> None: ...
def RegOpenCurrentUser(samDesired=..., /) -> _win32typing.PyHKEY: ...
def RegOpenKey(
    key: _win32typing.PyHKEY | int, subkey: str | None, reserved: bool = ..., sam: int = ..., /
) -> _win32typing.PyHKEY: ...
def RegOpenKeyEx(key: _win32typing.PyHKEY, subKey: str, sam: int, reserved: bool = ..., /) -> _win32typing.PyHKEY: ...
def RegOpenKeyTransacted(
    Key: _win32typing.PyHKEY, SubKey: str, samDesired, Transaction: int, Options: int = ...
) -> _win32typing.PyHKEY: ...
def RegOverridePredefKey(Key: _win32typing.PyHKEY, NewKey: _win32typing.PyHKEY) -> None: ...
def RegQueryValue(key: _win32typing.PyHKEY | int, subKey: str | None, /) -> str: ...
def RegQueryValueEx(key: _win32typing.PyHKEY | int, valueName: str, /) -> tuple[str, int]: ...
def RegQueryInfoKey(key: _win32typing.PyHKEY, /) -> tuple[Incomplete, Incomplete, Incomplete]: ...
def RegQueryInfoKeyW(Key: _win32typing.PyHKEY, /): ...
def RegRestoreKey(Key: _win32typing.PyHKEY, File: str, Flags: int = ...) -> None: ...
def RegSaveKey(key: _win32typing.PyHKEY, filename: str, sa: _win32typing.PySECURITY_ATTRIBUTES | None = ..., /) -> None: ...
def RegSaveKeyEx(
    Key: _win32typing.PyHKEY, File: str, SecurityAttributes: _win32typing.PySECURITY_ATTRIBUTES | None = ..., Flags=...
) -> None: ...
def RegSetKeySecurity(key: _win32typing.PyHKEY, security_info, sd: _win32typing.PySECURITY_DESCRIPTOR, /) -> None: ...
def RegSetValue(key: _win32typing.PyHKEY, subKey: str | None, _type, value: str, /) -> None: ...
def RegSetValueEx(key: _win32typing.PyHKEY, valueName: str, reserved, _type, value, /) -> None: ...
def RegUnLoadKey(key: _win32typing.PyHKEY, subKey: str, /) -> None: ...
def RegisterWindowMessage(msgString: str, /) -> None: ...
def RegNotifyChangeKeyValue(key: _win32typing.PyHKEY, bWatchSubTree, dwNotifyFilter, hKey: int, fAsynchronous, /) -> None: ...
def SearchPath(path: str, fileName: str, fileExt: str | None = ..., /): ...
def SendMessage(hwnd: int, idMessage, wParam: str | None = ..., lParam: str | None = ..., /) -> None: ...
def SetConsoleCtrlHandler(ctrlHandler: Callable[[int], bool], bAdd: bool, /) -> None: ...
def SetConsoleTitle(title: str, /) -> None: ...
def SetCursorPos(arg: tuple[Incomplete, Incomplete], /) -> None: ...
def SetDllDirectory(PathName: str, /) -> None: ...
def SetErrorMode(errorMode, /): ...
def SetFileAttributes(pathName: str, attrs, /): ...
def SetLastError(): ...
def SetSysColors(Elements, RgbValues, /) -> None: ...
def SetLocalTime(SystemTime: TimeType, /) -> None: ...
def SetSystemTime(year, month, dayOfWeek, day, hour, minute, second, millseconds, /): ...
def SetClassLong(hwnd: int, offset, val, /): ...
@deprecated("This function is obsolete, use `win32api.SetClassLong` instead")
def SetClassWord(hwnd: int, offset, val, /): ...
def SetCursor(hCursor: int, /) -> int: ...
def SetEnvironmentVariable(Name, Value, /) -> None: ...
def SetEnvironmentVariableW(Name, Value, /) -> None: ...
def SetHandleInformation(Object: int, Mask, Flags, /) -> None: ...
def SetStdHandle(handle, handle1: int, /) -> None: ...
def SetSystemPowerState(Suspend, Force, /) -> None: ...
def SetThreadLocale(lcid, /) -> None: ...
def SetTimeZoneInformation(tzi, /): ...
def SetWindowLong(hwnd: int | None, offset: int, value: float, /) -> int: ...

# This method is accidentally overwritten in source, can re-introduce once fixed:
# https://github.com/mhammond/pywin32/pull/2199
# @deprecated("This function is obsolete, use `win32api.SetWindowLong` instead")
# def SetWindowWord(hwnd, offset: int, val: int) -> int: ...
def ShellExecute(hwnd: int, op: str, file: str, params: str, _dir: str, bShow, /): ...
def ShowCursor(show, /): ...
def Sleep(time, bAlterable: int = ..., /): ...
def TerminateProcess(handle: int, exitCode: int, /) -> None: ...
def ToAsciiEx(vk, scancode, keyboardstate, flags: int = ..., hlayout: Incomplete | None = ..., /): ...
def Unicode() -> str: ...
def UpdateResource(
    handle: int,
    type: _win32typing.PyResourceId | int,
    name: _win32typing.PyResourceId | int,
    data: ReadableBuffer | None,
    language: int = ...,
    /,
) -> None: ...
def VkKeyScan(char, char1, /): ...
def WinExec(cmdLine: str, arg, /) -> None: ...
def WinHelp(hwnd: int, hlpFile: str, cmd, data: str | int = ..., /) -> None: ...
@deprecated("This function is obsolete, applications should use the registry instead.")
def WriteProfileSection(section: str, data: str, iniName: str | None = ..., /): ...
@deprecated("This function is obsolete, applications should use the registry instead.")
def WriteProfileVal(section: str, entry: str, value: str, iniName: str | None = ..., /) -> None: ...
def HIBYTE(val: int, /) -> int: ...
def LOBYTE(val: int, /) -> int: ...
def HIWORD(val: int, /) -> int: ...
def LOWORD(val: int, /) -> int: ...
def RGB(red, green, blue, /): ...
def MAKELANGID(PrimaryLanguage, SubLanguage, /): ...
def MAKEWORD(low, high, /): ...
def MAKELONG(low, high, /): ...
def CommandLineToArgv(*args): ...  # incomplete
def GetKeyboardLayoutList(*args): ...  # incomplete
def MapVirtualKey(*args): ...  # incomplete
def MessageBoxEx(*args): ...  # incomplete
def OpenThread(*args): ...  # incomplete
def SleepEx(*args): ...  # incomplete
def VkKeyScanEx(*args): ...  # incomplete

NameCanonical: int
NameCanonicalEx: int
NameDisplay: int
NameFullyQualifiedDN: int
NameSamCompatible: int
NameServicePrincipal: int
NameUniqueId: int
NameUnknown: int
NameUserPrincipal: int
PyDISPLAY_DEVICEType = _win32typing.PyDISPLAY_DEVICE
REG_NOTIFY_CHANGE_ATTRIBUTES: int
REG_NOTIFY_CHANGE_LAST_SET: int
REG_NOTIFY_CHANGE_NAME: int
REG_NOTIFY_CHANGE_SECURITY: int
STD_ERROR_HANDLE: int
STD_INPUT_HANDLE: int
STD_OUTPUT_HANDLE: int
VFT_APP: int
VFT_DLL: int
VFT_DRV: int
VFT_FONT: int
VFT_STATIC_LIB: int
VFT_UNKNOWN: int
VFT_VXD: int
VOS_DOS: int
VOS_DOS_WINDOWS16: int
VOS_DOS_WINDOWS32: int
VOS_NT: int
VOS_NT_WINDOWS32: int
VOS_OS216: int
VOS_OS216_PM16: int
VOS_OS232: int
VOS_OS232_PM32: int
VOS_UNKNOWN: int
VOS__PM16: int
VOS__PM32: int
VOS__WINDOWS16: int
VOS__WINDOWS32: int
VS_FF_DEBUG: int
VS_FF_INFOINFERRED: int
VS_FF_PATCHED: int
VS_FF_PRERELEASE: int
VS_FF_PRIVATEBUILD: int
VS_FF_SPECIALBUILD: int
