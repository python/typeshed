import sys
from _typeshed import Self
from types import TracebackType
from typing import Any, Union
from typing_extensions import Literal, final

if sys.platform == "win32":
    _KeyType = Union[HKEYType, int]
    def CloseKey(__hkey: _KeyType) -> None: ...
    def ConnectRegistry(__computer_name: str | None, __key: _KeyType) -> HKEYType: ...
    def CreateKey(__key: _KeyType, __sub_key: str | None) -> HKEYType: ...
    def CreateKeyEx(key: _KeyType, sub_key: str | None, reserved: int = ..., access: int = ...) -> HKEYType: ...
    def DeleteKey(__key: _KeyType, __sub_key: str) -> None: ...
    def DeleteKeyEx(key: _KeyType, sub_key: str, access: int = ..., reserved: int = ...) -> None: ...
    def DeleteValue(__key: _KeyType, __value: str) -> None: ...
    def EnumKey(__key: _KeyType, __index: int) -> str: ...
    def EnumValue(__key: _KeyType, __index: int) -> tuple[str, Any, int]: ...
    def ExpandEnvironmentStrings(__str: str) -> str: ...
    def FlushKey(__key: _KeyType) -> None: ...
    def LoadKey(__key: _KeyType, __sub_key: str, __file_name: str) -> None: ...
    def OpenKey(key: _KeyType, sub_key: str, reserved: int = ..., access: int = ...) -> HKEYType: ...
    def OpenKeyEx(key: _KeyType, sub_key: str, reserved: int = ..., access: int = ...) -> HKEYType: ...
    def QueryInfoKey(__key: _KeyType) -> tuple[int, int, int]: ...
    def QueryValue(__key: _KeyType, __sub_key: str | None) -> str: ...
    def QueryValueEx(__key: _KeyType, __name: str) -> tuple[Any, int]: ...
    def SaveKey(__key: _KeyType, __file_name: str) -> None: ...
    def SetValue(__key: _KeyType, __sub_key: str, __type: int, __value: str) -> None: ...
    def SetValueEx(
        __key: _KeyType, __value_name: str | None, __reserved: Any, __type: int, __value: str | int
    ) -> None: ...  # reserved is ignored
    def DisableReflectionKey(__key: _KeyType) -> None: ...
    def EnableReflectionKey(__key: _KeyType) -> None: ...
    def QueryReflectionKey(__key: _KeyType) -> bool: ...
    HKEY_CLASSES_ROOT: int
    HKEY_CURRENT_USER: int
    HKEY_LOCAL_MACHINE: int
    HKEY_USERS: int
    HKEY_PERFORMANCE_DATA: int
    HKEY_CURRENT_CONFIG: int
    HKEY_DYN_DATA: int

    KEY_ALL_ACCESS: Literal[983103]
    KEY_WRITE: Literal[131078]
    KEY_READ: Literal[131097]
    KEY_EXECUTE: Literal[131097]
    KEY_QUERY_VALUE: Literal[1]
    KEY_SET_VALUE: Literal[2]
    KEY_CREATE_SUB_KEY: Literal[4]
    KEY_ENUMERATE_SUB_KEYS: Literal[8]
    KEY_NOTIFY: Literal[16]
    KEY_CREATE_LINK: Literal[32]

    KEY_WOW64_64KEY: Literal[256]
    KEY_WOW64_32KEY: Literal[512]

    REG_BINARY: Literal[3]
    REG_DWORD: Literal[4]
    REG_DWORD_LITTLE_ENDIAN: Literal[4]
    REG_DWORD_BIG_ENDIAN: Literal[5]
    REG_EXPAND_SZ: Literal[2]
    REG_LINK: Literal[6]
    REG_MULTI_SZ: Literal[7]
    REG_NONE: Literal[0]
    REG_QWORD: Literal[11]
    REG_QWORD_LITTLE_ENDIAN: Literal[11]
    REG_RESOURCE_LIST: Literal[8]
    REG_FULL_RESOURCE_DESCRIPTOR: Literal[9]
    REG_RESOURCE_REQUIREMENTS_LIST: Literal[10]
    REG_SZ: Literal[1]

    REG_CREATED_NEW_KEY: int  # undocumented
    REG_LEGAL_CHANGE_FILTER: int  # undocumented
    REG_LEGAL_OPTION: int  # undocumented
    REG_NOTIFY_CHANGE_ATTRIBUTES: int  # undocumented
    REG_NOTIFY_CHANGE_LAST_SET: int  # undocumented
    REG_NOTIFY_CHANGE_NAME: int  # undocumented
    REG_NOTIFY_CHANGE_SECURITY: int  # undocumented
    REG_NO_LAZY_FLUSH: int  # undocumented
    REG_OPENED_EXISTING_KEY: int  # undocumented
    REG_OPTION_BACKUP_RESTORE: int  # undocumented
    REG_OPTION_CREATE_LINK: int  # undocumented
    REG_OPTION_NON_VOLATILE: int  # undocumented
    REG_OPTION_OPEN_LINK: int  # undocumented
    REG_OPTION_RESERVED: int  # undocumented
    REG_OPTION_VOLATILE: int  # undocumented
    REG_REFRESH_HIVE: int  # undocumented
    REG_WHOLE_HIVE_VOLATILE: int  # undocumented

    error = OSError

    # Though this class has a __name__ of PyHKEY, it's exposed as HKEYType for some reason
    @final
    class HKEYType:
        def __bool__(self) -> bool: ...
        def __int__(self) -> int: ...
        def __enter__(self: Self) -> Self: ...
        def __exit__(
            self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
        ) -> bool | None: ...
        def Close(self) -> None: ...
        def Detach(self) -> int: ...
