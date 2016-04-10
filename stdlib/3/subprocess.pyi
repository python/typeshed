# Stubs for subprocess

# Based on http://docs.python.org/3.2/library/subprocess.html

from typing import Sequence, Any, Mapping, Callable, Tuple, IO

# TODO force keyword arguments
# TODO more keyword arguments
def call(args: Sequence[str], *, stdin: Any = ..., stdout: Any = ...,
         stderr: Any = ..., shell: bool = ...,
         env: Mapping[str, str] = ...,
         cwd: str = ...) -> int: ...
def check_call(args: Sequence[str], *, stdin: Any = ..., stdout: Any = ...,
               stderr: Any = ..., shell: bool = ...,
               env: Mapping[str, str] = ...,
               cwd: str = ...) -> int: ...
# Return str/bytes
def check_output(args: Sequence[str], *, stdin: Any = ..., stderr: Any = ...,
                 shell: bool = ..., universal_newlines: bool = ...,
                 env: Mapping[str, str] = ...,
                 cwd: str = ...) -> Any: ...

# TODO types
PIPE = ... # type: Any
STDOUT = ... # type: Any

class CalledProcessError(Exception):
    returncode = 0
    cmd = ...  # type: str
    output = b'' # May be None

    def __init__(self, returncode: int, cmd: str, output: str = ...) -> None: ...

class Popen:
    stdin = ... # type: IO[Any]
    stdout = ... # type: IO[Any]
    stderr = ... # type: IO[Any]
    pid = 0
    returncode = 0

    def __init__(self,
                  args: Sequence[str],
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
    def communicate(self, input=...) -> Tuple[Any, Any]: ...
    def send_signal(self, signal: int) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    def __enter__(self) -> 'Popen': ...
    def __exit__(self, type, value, traceback) -> bool: ...

def getstatusoutput(cmd: str) -> Tuple[int, str]: ...
def getoutput(cmd: str) -> str: ...

# Windows-only: STARTUPINFO etc.
