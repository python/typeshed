import sys
from typing import Any, NoReturn, Sequence, overload
from typing_extensions import Literal, final

if sys.platform == "win32":
    CREATE_NEW_CONSOLE: Literal[16]
    CREATE_NEW_PROCESS_GROUP: Literal[512]
    DUPLICATE_CLOSE_SOURCE: Literal[1]
    DUPLICATE_SAME_ACCESS: Literal[2]
    ERROR_ALREADY_EXISTS: Literal[183]
    ERROR_BROKEN_PIPE: Literal[109]
    ERROR_IO_PENDING: Literal[997]
    ERROR_MORE_DATA: Literal[234]
    ERROR_NETNAME_DELETED: Literal[64]
    ERROR_NO_DATA: Literal[232]
    ERROR_NO_SYSTEM_RESOURCES: Literal[1450]
    ERROR_OPERATION_ABORTED: Literal[995]
    ERROR_PIPE_BUSY: Literal[231]
    ERROR_PIPE_CONNECTED: Literal[535]
    ERROR_SEM_TIMEOUT: Literal[121]
    FILE_FLAG_FIRST_PIPE_INSTANCE: Literal[524288]
    FILE_FLAG_OVERLAPPED: Literal[1073741824]
    FILE_GENERIC_READ: Literal[1179785]
    FILE_GENERIC_WRITE: Literal[1179926]
    GENERIC_READ: Literal[2147483648]
    GENERIC_WRITE: Literal[1073741824]
    INFINITE: Literal[4294967295]
    NMPWAIT_WAIT_FOREVER: Literal[4294967295]
    NULL: Literal[0]
    OPEN_EXISTING: Literal[3]
    PIPE_ACCESS_DUPLEX: Literal[3]
    PIPE_ACCESS_INBOUND: Literal[1]
    PIPE_READMODE_MESSAGE: Literal[2]
    PIPE_TYPE_MESSAGE: Literal[4]
    PIPE_UNLIMITED_INSTANCES: Literal[255]
    PIPE_WAIT: Literal[0]
    PROCESS_ALL_ACCESS: Literal[2097151]
    PROCESS_DUP_HANDLE: Literal[64]
    STARTF_USESHOWWINDOW: Literal[1]
    STARTF_USESTDHANDLES: Literal[256]
    STD_ERROR_HANDLE: Literal[4294967284]
    STD_INPUT_HANDLE: Literal[4294967286]
    STD_OUTPUT_HANDLE: Literal[4294967285]
    STILL_ACTIVE: Literal[259]
    SW_HIDE: Literal[0]
    WAIT_ABANDONED_0: Literal[128]
    WAIT_OBJECT_0: Literal[0]
    WAIT_TIMEOUT: Literal[258]
    def CloseHandle(__handle: int) -> None: ...
    @overload
    def ConnectNamedPipe(handle: int, overlapped: Literal[True]) -> Overlapped: ...
    @overload
    def ConnectNamedPipe(handle: int, overlapped: Literal[False] = ...) -> None: ...
    @overload
    def ConnectNamedPipe(handle: int, overlapped: bool) -> Overlapped | None: ...
    def CreateFile(
        __file_name: str,
        __desired_access: int,
        __share_mode: int,
        __security_attributes: int,
        __creation_disposition: int,
        __flags_and_attributes: int,
        __template_file: int,
    ) -> int: ...
    def CreateJunction(__src_path: str, __dst_path: str) -> None: ...
    def CreateNamedPipe(
        __name: str,
        __open_mode: int,
        __pipe_mode: int,
        __max_instances: int,
        __out_buffer_size: int,
        __in_buffer_size: int,
        __default_timeout: int,
        __security_attributes: int,
    ) -> int: ...
    def CreatePipe(__pipe_attrs: Any, __size: int) -> tuple[int, int]: ...
    def CreateProcess(
        __application_name: str | None,
        __command_line: str | None,
        __proc_attrs: Any,
        __thread_attrs: Any,
        __inherit_handles: bool,
        __creation_flags: int,
        __env_mapping: dict[str, str],
        __current_directory: str | None,
        __startup_info: Any,
    ) -> tuple[int, int, int, int]: ...
    def DuplicateHandle(
        __source_process_handle: int,
        __source_handle: int,
        __target_process_handle: int,
        __desired_access: int,
        __inherit_handle: bool,
        __options: int = ...,
    ) -> int: ...
    def ExitProcess(__ExitCode: int) -> NoReturn: ...
    if sys.version_info >= (3, 7):
        def GetACP() -> int: ...
        def GetFileType(handle: int) -> int: ...
    def GetCurrentProcess() -> int: ...
    def GetExitCodeProcess(__process: int) -> int: ...
    def GetLastError() -> int: ...
    def GetModuleFileName(__module_handle: int) -> str: ...
    def GetStdHandle(__std_handle: int) -> int: ...
    def GetVersion() -> int: ...
    def OpenProcess(__desired_access: int, __inherit_handle: bool, __process_id: int) -> int: ...
    def PeekNamedPipe(__handle: int, __size: int = ...) -> tuple[int, int] | tuple[bytes, int, int]: ...
    @overload
    def ReadFile(handle: int, size: int, overlapped: Literal[True]) -> tuple[Overlapped, int]: ...
    @overload
    def ReadFile(handle: int, size: int, overlapped: Literal[False] = ...) -> tuple[bytes, int]: ...
    @overload
    def ReadFile(handle: int, size: int, overlapped: int | bool) -> tuple[Any, int]: ...
    def SetNamedPipeHandleState(
        __named_pipe: int, __mode: int | None, __max_collection_count: int | None, __collect_data_timeout: int | None
    ) -> None: ...
    def TerminateProcess(__handle: int, __exit_code: int) -> None: ...
    def WaitForMultipleObjects(__handle_seq: Sequence[int], __wait_flag: bool, __milliseconds: int = ...) -> int: ...
    def WaitForSingleObject(__handle: int, __milliseconds: int) -> int: ...
    def WaitNamedPipe(__name: str, __timeout: int) -> None: ...
    @overload
    def WriteFile(handle: int, buffer: bytes, overlapped: Literal[True]) -> tuple[Overlapped, int]: ...
    @overload
    def WriteFile(handle: int, buffer: bytes, overlapped: Literal[False] = ...) -> tuple[int, int]: ...
    @overload
    def WriteFile(handle: int, buffer: bytes, overlapped: int | bool) -> tuple[Any, int]: ...
    @final
    class Overlapped:
        event: int
        def GetOverlappedResult(self, __wait: bool) -> tuple[int, int]: ...
        def cancel(self) -> None: ...
        def getbuffer(self) -> bytes | None: ...
