from typing import Any, Dict, NoReturn, Optional, Sequence, Tuple, Union, overload

CREATE_NEW_CONSOLE: int
CREATE_NEW_PROCESS_GROUP: int
DUPLICATE_CLOSE_SOURCE: int
DUPLICATE_SAME_ACCESS: int
ERROR_ALREADY_EXISTS: int
ERROR_BROKEN_PIPE: int
ERROR_IO_PENDING: int
ERROR_MORE_DATA: int
ERROR_NETNAME_DELETED: int
ERROR_NO_DATA: int
ERROR_NO_SYSTEM_RESOURCES: int
ERROR_OPERATION_ABORTED: int
ERROR_PIPE_BUSY: int
ERROR_PIPE_CONNECTED: int
ERROR_SEM_TIMEOUT: int
FILE_FLAG_FIRST_PIPE_INSTANCE: int
FILE_FLAG_OVERLAPPED: int
FILE_GENERIC_READ: int
FILE_GENERIC_WRITE: int
GENERIC_READ: int
GENERIC_WRITE: int
INFINITE: int
NMPWAIT_WAIT_FOREVER: int
NULL: int
OPEN_EXISTING: int
PIPE_ACCESS_DUPLEX: int
PIPE_ACCESS_INBOUND: int
PIPE_READMODE_MESSAGE: int
PIPE_TYPE_MESSAGE: int
PIPE_UNLIMITED_INSTANCES: int
PIPE_WAIT: int
PROCESS_ALL_ACCESS: int
PROCESS_DUP_HANDLE: int
STARTF_USESHOWWINDOW: int
STARTF_USESTDHANDLES: int
STD_ERROR_HANDLE: int
STD_INPUT_HANDLE: int
STD_OUTPUT_HANDLE: int
STILL_ACTIVE: int
SW_HIDE: int
WAIT_ABANDONED_0: int
WAIT_OBJECT_0: int
WAIT_TIMEOUT: int

def CloseHandle(handle: int) -> None: ...

# TODO: once literal types are supported, overload with Literal[True/False]
@overload
def ConnectNamedPipe(handle: int, overlapped: Union[int, bool]) -> Any: ...
@overload
def ConnectNamedPipe(handle: int) -> None: ...
def CreateFile(
    file_name: str,
    desired_access: int,
    share_mode: int,
    security_attributes: int,
    creation_disposition: int,
    flags_and_attributes: int,
    template_file: int,
) -> int: ...
def CreateJunction(src_path: str, dest_path: str) -> None: ...
def CreateNamedPipe(
    name: str,
    open_mode: int,
    pipe_mode: int,
    max_instances: int,
    out_buffer_size: int,
    in_buffer_size: int,
    default_timeout: int,
    security_attributes: int,
) -> int: ...
def CreatePipe(pipe_attrs: Any, size: int) -> Tuple[int, int]: ...
def CreateProcess(
    application_name: Optional[str],
    command_line: Optional[str],
    proc_attrs: Any,
    thread_attrs: Any,
    inherit_handles: bool,
    creation_flags: int,
    env_mapping: Dict[str, str],
    cwd: Optional[str],
    startup_info: Any,
) -> Tuple[int, int, int, int]: ...
def DuplicateHandle(
    source_process_handle: int,
    source_handle: int,
    target_process_handle: int,
    desired_access: int,
    inherit_handle: bool,
    options: int = ...,
) -> int: ...
def ExitProcess(ExitCode: int) -> NoReturn: ...
def GetACP() -> int: ...
def GetFileType(handle: int) -> int: ...
def GetCurrentProcess() -> int: ...
def GetExitCodeProcess(process: int) -> int: ...
def GetLastError() -> int: ...
def GetModuleFileName(module_handle: int) -> str: ...
def GetStdHandle(std_handle: int) -> int: ...
def GetVersion() -> int: ...
def OpenProcess(desired_access: int, inherit_handle: bool, process_id: int) -> int: ...
def PeekNamedPipe(handle: int, size: int = ...) -> Union[Tuple[int, int], Tuple[bytes, int, int]]: ...

# TODO: once literal types are supported, overload with Literal[True/False]
@overload
def ReadFile(handle: int, size: int, overlapped: Union[int, bool]) -> Any: ...
@overload
def ReadFile(handle: int, size: int) -> Tuple[int, int]: ...
def SetNamedPipeHandleState(
    named_pipe: int, mode: Optional[int], max_collection_count: Optional[int], collect_data_timeout: Optional[int]
) -> None: ...
def TerminateProcess(handle: int, exit_code: int) -> None: ...
def WaitForMultipleObjects(handle_seq: Sequence[int], wait_flag: bool, milliseconds: int = ...) -> int: ...
def WaitForSingleObject(handle: int, milliseconds: int) -> int: ...
def WaitNamedPipe(name: str, timeout: int) -> None: ...

# TODO: once literal types are supported, overload with Literal[True/False]
@overload
def WriteFile(handle: int, buffer: bytes, overlapped: Union[int, bool]) -> Any: ...
@overload
def WriteFile(handle: int, buffer: bytes) -> Tuple[bytes, int]: ...

class Overlapped:
    event: int = ...
    def GetOverlappedResult(self, wait: bool) -> Tuple[int, int]: ...
    def cancel(self) -> None: ...
    def getbuffer(self) -> Optional[bytes]: ...
