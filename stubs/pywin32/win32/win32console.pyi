from typing import Final, Literal, overload
from typing_extensions import Never

import _win32typing
from win32.lib.pywintypes import error as error

def GetConsoleProcessList() -> tuple[int, ...]: ...
def CreateConsoleScreenBuffer(
    DesiredAccess: int = ...,
    ShareMode: int = ...,
    SecurityAttributes: _win32typing.PySECURITY_ATTRIBUTES | None = None,
    Flags: int = ...,
) -> _win32typing.PyConsoleScreenBuffer: ...
def GetConsoleDisplayMode() -> int: ...
def AttachConsole(ProcessId: int) -> None: ...
def AllocConsole() -> None: ...
def FreeConsole() -> None: ...
def GetConsoleCP() -> int: ...
def GetConsoleOutputCP() -> int: ...
def SetConsoleCP(CodePageID: int) -> None: ...
def SetConsoleOutputCP(CodePageID: int) -> None: ...
def GetConsoleSelectionInfo() -> _win32typing.ConsoleSelectionInfo: ...
def AddConsoleAlias(Source: str, Target: str | None, ExeName: str) -> None: ...
def GetConsoleAliases(ExeName: str) -> str: ...
def GetConsoleAliasExes() -> str: ...
def GetConsoleWindow() -> int: ...
def GetNumberOfConsoleFonts() -> int: ...
def SetConsoleTitle(ConsoleTitle: str) -> None: ...
def GetConsoleTitle() -> str: ...

@overload
def GenerateConsoleCtrlEvent(CtrlEvent: Literal[1], ProcessGroupId: Literal[0] = 0) -> Never: ...
@overload
def GenerateConsoleCtrlEvent(CtrlEvent: Literal[0, 1], ProcessGroupId: int) -> None: ...

def GetStdHandle(StdHandle: int) -> _win32typing.PyConsoleScreenBuffer | None: ...

PyConsoleScreenBufferType = _win32typing.PyConsoleScreenBuffer
PySMALL_RECTType = _win32typing.PySMALL_RECT
PyCOORDType = _win32typing.PyCOORD
PyINPUT_RECORDType = _win32typing.PyINPUT_RECORD

CONSOLE_TEXTMODE_BUFFER: Final[int]
CONSOLE_FULLSCREEN: Final[int]
CONSOLE_FULLSCREEN_HARDWARE: Final[int]
ATTACH_PARENT_PROCESS: Final[int]
ENABLE_LINE_INPUT: Final = 0x0002
ENABLE_ECHO_INPUT: Final = 0x0004
ENABLE_PROCESSED_INPUT: Final = 0x0001
ENABLE_WINDOW_INPUT: Final = 0x0008
ENABLE_MOUSE_INPUT: Final = 0x0010
ENABLE_PROCESSED_OUTPUT: Final = 0x0001
ENABLE_WRAP_AT_EOL_OUTPUT: Final = 0x0002
FOREGROUND_BLUE: Final = 0x0001
FOREGROUND_GREEN: Final = 0x0002
FOREGROUND_RED: Final = 0x0004
FOREGROUND_INTENSITY: Final = 0x0008
BACKGROUND_BLUE: Final = 0x0010
BACKGROUND_GREEN: Final = 0x0020
BACKGROUND_RED: Final = 0x0040
BACKGROUND_INTENSITY: Final = 0x0080
COMMON_LVB_LEADING_BYTE: Final = 0x0100
COMMON_LVB_TRAILING_BYTE: Final = 0x0200
COMMON_LVB_GRID_HORIZONTAL: Final = 0x0400
COMMON_LVB_GRID_LVERTICAL: Final = 0x0800
COMMON_LVB_GRID_RVERTICAL: Final = 0x1000
COMMON_LVB_REVERSE_VIDEO: Final = 0x4000
COMMON_LVB_UNDERSCORE: Final = 0x8000
CONSOLE_NO_SELECTION: Final = 0x0000
CONSOLE_SELECTION_IN_PROGRESS: Final = 0x0001
CONSOLE_SELECTION_NOT_EMPTY: Final = 0x0002
CONSOLE_MOUSE_SELECTION: Final = 0x0004
CONSOLE_MOUSE_DOWN: Final = 0x0008
LOCALE_USER_DEFAULT: Final = 0x0400
KEY_EVENT: Final = 0x0001
MOUSE_EVENT: Final = 0x0002
WINDOW_BUFFER_SIZE_EVENT: Final = 0x0004
MENU_EVENT: Final = 0x0008
FOCUS_EVENT: Final = 0x0010
CTRL_C_EVENT: Final = 0
CTRL_BREAK_EVENT: Final = 1
STD_INPUT_HANDLE: Final[int]
STD_OUTPUT_HANDLE: Final[int]
STD_ERROR_HANDLE: Final[int]
CONSOLE_FULLSCREEN_MODE: Final = 1
CONSOLE_WINDOWED_MODE: Final = 2
