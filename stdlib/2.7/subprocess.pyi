# Stubs for subprocess

# Based on http://docs.python.org/2/library/subprocess.html and Python 3 stub

from typing import Sequence, Any, Mapping, Callable, Tuple, IO, Union, Optional

_FILE = Union[int, IO[Any]]

# TODO force keyword arguments
# TODO more keyword arguments (from Popen)
def call(args: Sequence[str], *,
         stdin: _FILE = ..., stdout: _FILE = ..., stderr: _FILE = ...,
         shell: bool = ..., env: Mapping[str, str] = ...,
         cwd: str = ...) -> int: ...
def check_call(args: Sequence[str], *,
               stdin: _FILE = ..., stdout: _FILE = ..., stderr: _FILE = ...,
               shell: bool = ..., env: Mapping[str, str] = ..., cwd: str = ...,
               close_fds: Sequence[_FILE] = ..., preexec_fn: Callable[[], Any] = ...) -> int: ...
def check_output(args: Sequence[str], *,
                 stdin: _FILE = ..., stderr: _FILE = ...,
                 shell: bool = ..., universal_newlines: bool = ...,
                 env: Mapping[str, str] = ..., cwd: str = ...) -> str: ...

PIPE = ... # type: int
STDOUT = ... # type: int

class CalledProcessError(Exception):
    returncode = 0
    cmd = ...  # type: str
    output = ...  # type: str # May be None

    def __init__(self, returncode: int, cmd: str, output: str = ...) -> None: ...

class Popen:
    stdin = ... # type: Optional[IO[Any]]
    stdout = ... # type: Optional[IO[Any]]
    stderr = ... # type: Optional[IO[Any]]
    pid = 0
    returncode = 0

    def __init__(self,
                 args: Sequence[str],
                 bufsize: int = ...,
                 executable: str = ...,
                 stdin: _FILE = ...,
                 stdout: _FILE = ...,
                 stderr: _FILE = ...,
                 preexec_fn: Callable[[], Any] = ...,
                 close_fds: bool = ...,
                 shell: bool = ...,
                 cwd: str = ...,
                 env: Mapping[str, str] = ...,
                 universal_newlines: bool = ...,
                 startupinfo: Any = ...,
                 creationflags: int = ...) -> None: ...

    def poll(self) -> int: ...
    def wait(self) -> int: ...
    # Return str/bytes
    def communicate(self, input: Union[str, unicode] = ...) -> Tuple[str, str]: ...
    def send_signal(self, signal: int) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    def __enter__(self) -> 'Popen': ...
    def __exit__(self, type, value, traceback) -> bool: ...

def getstatusoutput(cmd: str) -> Tuple[int, str]: ...
def getoutput(cmd: str) -> str: ...

# Windows-only: STARTUPINFO etc.

STD_INPUT_HANDLE = ... # type: Any
STD_OUTPUT_HANDLE = ... # type: Any
STD_ERROR_HANDLE = ... # type: Any
SW_HIDE = ... # type: Any
STARTF_USESTDHANDLES = ... # type: Any
STARTF_USESHOWWINDOW = ... # type: Any
CREATE_NEW_CONSOLE = ... # type: Any
CREATE_NEW_PROCESS_GROUP = ... # type: Any
