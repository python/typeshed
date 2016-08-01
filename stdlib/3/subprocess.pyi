# Stubs for subprocess

# Based on http://docs.python.org/3.5/library/subprocess.html
import sys

from typing import Sequence, Any, Mapping, Callable, Tuple, IO, Optional, Union

# Same args as Popen.__init__
if sys.version_info >= (3, 3):
    def call(args: Union[str, Sequence[str]],
             bufsize: int = ...,
             executable: str = ...,
             stdin: Any = ...,
             stdout: Any = ...,
             stderr: Any = ...,
             preexec_fn: Callable[[], Any] = ...,
             close_fds: bool = ...,
             shell: bool = ...,
             cwd: str = ...,
             env: Mapping[str, str] = ...,
             universal_newlines: bool = ...,
             startupinfo: Any = ...,
             creationflags: int = ...,
             restore_signals: bool = ...,
             start_new_session: bool = ...,
             pass_fds: Any = ...,
             timeout: int = ...) -> int: ...
else:
    def call(args: Union[str, Sequence[str]],
             bufsize: int = ...,
             executable: str = ...,
             stdin: Any = ...,
             stdout: Any = ...,
             stderr: Any = ...,
             preexec_fn: Callable[[], Any] = ...,
             close_fds: bool = ...,
             shell: bool = ...,
             cwd: str = ...,
             env: Mapping[str, str] = ...,
             universal_newlines: bool = ...,
             startupinfo: Any = ...,
             creationflags: int = ...,
             restore_signals: bool = ...,
             start_new_session: bool = ...,
             pass_fds: Any = ...) -> int: ...

# Same args as Popen.__init__
if sys.version_info >= (3, 3):
    def check_call(args: Union[str, Sequence[str]],
                   bufsize: int = ...,
                   executable: str = ...,
                   stdin: Any = ...,
                   stdout: Any = ...,
                   stderr: Any = ...,
                   preexec_fn: Callable[[], Any] = ...,
                   close_fds: bool = ...,
                   shell: bool = ...,
                   cwd: str = ...,
                   env: Mapping[str, str] = ...,
                   universal_newlines: bool = ...,
                   startupinfo: Any = ...,
                   creationflags: int = ...,
                   restore_signals: bool = ...,
                   start_new_session: bool = ...,
                   pass_fds: Any = ...,
                   timeout: int = ...) -> int: ...
else:
    def check_call(args: Union[str, Sequence[str]],
                   bufsize: int = ...,
                   executable: str = ...,
                   stdin: Any = ...,
                   stdout: Any = ...,
                   stderr: Any = ...,
                   preexec_fn: Callable[[], Any] = ...,
                   close_fds: bool = ...,
                   shell: bool = ...,
                   cwd: str = ...,
                   env: Mapping[str, str] = ...,
                   universal_newlines: bool = ...,
                   startupinfo: Any = ...,
                   creationflags: int = ...,
                   restore_signals: bool = ...,
                   start_new_session: bool = ...,
                   pass_fds: Any = ...) -> int: ...

if sys.version_info >= (3, 4):
    # the input= keyword was added in 3.4
    def check_output(args: Union[str, Sequence[str]],
                     bufsize: int = ...,
                     executable: str = ...,
                     stdin: Any = ...,
                     stderr: Any = ...,
                     preexec_fn: Callable[[], Any] = ...,
                     close_fds: bool = ...,
                     shell: bool = ...,
                     cwd: str = ...,
                     env: Mapping[str, str] = ...,
                     universal_newlines: bool = ...,
                     startupinfo: Any = ...,
                     creationflags: int = ...,
                     restore_signals: bool = ...,
                     start_new_session: bool = ...,
                     pass_fds: Any = ...,
                     timeout: int = ...,
                     input: Union[str, bytes] = ...) -> Any: ...
elif sys.version_info >= (3, 3):
    def check_output(args: Union[str, Sequence[str]],
                     bufsize: int = ...,
                     executable: str = ...,
                     stdin: Any = ...,
                     stderr: Any = ...,
                     preexec_fn: Callable[[], Any] = ...,
                     close_fds: bool = ...,
                     shell: bool = ...,
                     cwd: str = ...,
                     env: Mapping[str, str] = ...,
                     universal_newlines: bool = ...,
                     startupinfo: Any = ...,
                     creationflags: int = ...,
                     restore_signals: bool = ...,
                     start_new_session: bool = ...,
                     pass_fds: Any = ...,
                     timeout: int = ...) -> Any: ...
else:
    # Same args as Popen.__init__, except for stdout
    def check_output(args: Union[str, Sequence[str]],
                     bufsize: int = ...,
                     executable: str = ...,
                     stdin: Any = ...,
                     stderr: Any = ...,
                     preexec_fn: Callable[[], Any] = ...,
                     close_fds: bool = ...,
                     shell: bool = ...,
                     cwd: str = ...,
                     env: Mapping[str, str] = ...,
                     universal_newlines: bool = ...,
                     startupinfo: Any = ...,
                     creationflags: int = ...,
                     restore_signals: bool = ...,
                     start_new_session: bool = ...,
                     pass_fds: Any = ...) -> Any: ...


if sys.version_info >= (3, 5):
    # Same args as Popen.__init__, except for timeout, input and check
    def run(args: Union[str, Sequence[str]],
            bufsize: int = ...,
            executable: str = ...,
            stdin: Any = ...,
            stderr: Any = ...,
            preexec_fn: Callable[[], Any] = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: str = ...,
            env: Mapping[str, str] = ...,
            universal_newlines: bool = ...,
            startupinfo: Any = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            input: Union[str, bytes] = ...,
            timeout: int = None,
            check: bool = False) -> Any: ...


# TODO types
PIPE = ... # type: Any
STDOUT = ... # type: Any

if sys.version_info >= (3, 3):
    DEVNULL = ...  # type: Any
    class SubprocessError(Exception): ...


class CalledProcessError(Exception):
    returncode = 0
    cmd = ...  # type: str
    output = b'' # May be None

    if sys.version_info >= (3, 5):
        stdout = b''
        stderr = b''

    def __init__(self, returncode: int, cmd: str, output: Optional[str] = ...,
                 stderr: Optional[str] = ...) -> None: ...

class Popen:
    stdin = ... # type: IO[Any]
    stdout = ... # type: IO[Any]
    stderr = ... # type: IO[Any]
    pid = 0
    returncode = 0

    if sys.version_info >= (3, 3):
        args = Union[str, Sequence[str]]

    def __init__(self,
                  args: Union[str, Sequence[str]],
                  bufsize: int = ...,
                  executable: str = ...,
                  stdin: Any = ...,
                  stdout: Any = ...,
                  stderr: Any = ...,
                  preexec_fn: Callable[[], Any] = ...,
                  close_fds: bool = ...,
                  shell: bool = ...,
                  cwd: str = ...,
                  env: Mapping[str, str] = ...,
                  universal_newlines: bool = ...,
                  startupinfo: Any = ...,
                  creationflags: int = ...,
                  restore_signals: bool = ...,
                  start_new_session: bool = ...,
                  pass_fds: Any = ...) -> None: ...

    def poll(self) -> int: ...
    def wait(self) -> int: ...
    # Return str/bytes
    if sys.version_info >= (3, 3):
        def communicate(self, input: Union[str, bytes]=..., timeout: int=...) -> Tuple[Any, Any]: ...
    else:
        def communicate(self, input: Union[str, bytes]=...) -> Tuple[Any, Any]: ...
    def send_signal(self, signal: int) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    def __enter__(self) -> 'Popen': ...
    def __exit__(self, type, value, traceback) -> bool: ...

def getstatusoutput(cmd: str) -> Tuple[int, str]: ...
def getoutput(cmd: str) -> str: ...

# Windows-only: STARTUPINFO etc.
