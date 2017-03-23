# Stubs for subprocess

# Based on http://docs.python.org/2/library/subprocess.html and Python 3 stub

from typing import Sequence, Any, AnyStr, Mapping, Callable, Tuple, IO, Union, Optional, List, Text

_FILE = Union[int, IO[Any]]
_TXT = Union[bytes, Text]
_CMD = Union[_TXT, Sequence[_TXT]]

# Same args as Popen.__init__
def call(args: _CMD,
         bufsize: int = ...,
         executable: _TXT = ...,
         stdin: _FILE = ...,
         stdout: _FILE = ...,
         stderr: _FILE = ...,
         preexec_fn: Callable[[], Any] = ...,
         close_fds: bool = ...,
         shell: bool = ...,
         cwd: _TXT = ...,
         env: Mapping[_TXT, _TXT] = ...,
         universal_newlines: bool = ...,
         startupinfo: Any = ...,
         creationflags: int = ...) -> int: ...

def check_call(args: _CMD,
               bufsize: int = ...,
               executable: _TXT = ...,
               stdin: _FILE = ...,
               stdout: _FILE = ...,
               stderr: _FILE = ...,
               preexec_fn: Callable[[], Any] = ...,
               close_fds: bool = ...,
               shell: bool = ...,
               cwd: _TXT = ...,
               env: Mapping[_TXT, _TXT] = ...,
               universal_newlines: bool = ...,
               startupinfo: Any = ...,
               creationflags: int = ...) -> int: ...

# Same args as Popen.__init__ except for stdout
def check_output(args: _CMD,
                 bufsize: int = ...,
                 executable: _TXT = ...,
                 stdin: _FILE = ...,
                 stderr: _FILE = ...,
                 preexec_fn: Callable[[], Any] = ...,
                 close_fds: bool = ...,
                 shell: bool = ...,
                 cwd: _TXT = ...,
                 env: Mapping[_TXT, _TXT] = ...,
                 universal_newlines: bool = ...,
                 startupinfo: Any = ...,
                 creationflags: int = ...
                 ) -> Any: ...  # morally: _TXT

PIPE = ...  # type: int
STDOUT = ...  # type: int

class CalledProcessError(Exception):
    returncode = 0
    # morally: _CMD
    cmd = ...  # type: Any
    # morally: Optional[_TXT]
    output = ...  # type: Any

    def __init__(self,
                 returncode: int,
                 cmd: _CMD,
                 output: Optional[_TXT] = ...) -> None: ...

class Popen:
    stdin = ...  # type: Optional[IO[Any]]
    stdout = ...  # type: Optional[IO[Any]]
    stderr = ...  # type: Optional[IO[Any]]
    pid = 0
    returncode = 0

    def __init__(self,
                 args: _CMD,
                 bufsize: int = ...,
                 executable: Optional[_TXT] = ...,
                 stdin: Optional[_FILE] = ...,
                 stdout: Optional[_FILE] = ...,
                 stderr: Optional[_FILE] = ...,
                 preexec_fn: Optional[Callable[[], Any]] = ...,
                 close_fds: bool = ...,
                 shell: bool = ...,
                 cwd: Optional[_TXT] = ...,
                 env: Optional[Mapping[_TXT, _TXT]] = ...,
                 universal_newlines: bool = ...,
                 startupinfo: Optional[Any] = ...,
                 creationflags: int = ...) -> None: ...

    def poll(self) -> int: ...
    def wait(self) -> int: ...
    # morally: -> Tuple[_TXT, _TXT]
    def communicate(self, input: Optional[_TXT] = ...) -> Tuple[Any, Any]: ...
    def send_signal(self, signal: int) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    def __enter__(self) -> 'Popen': ...
    def __exit__(self, type, value, traceback) -> bool: ...

# Windows-only: STARTUPINFO etc.

STD_INPUT_HANDLE = ...  # type: Any
STD_OUTPUT_HANDLE = ...  # type: Any
STD_ERROR_HANDLE = ...  # type: Any
SW_HIDE = ...  # type: Any
STARTF_USESTDHANDLES = ...  # type: Any
STARTF_USESHOWWINDOW = ...  # type: Any
CREATE_NEW_CONSOLE = ...  # type: Any
CREATE_NEW_PROCESS_GROUP = ...  # type: Any
