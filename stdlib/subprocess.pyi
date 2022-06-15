import sys
from _typeshed import Self, StrOrBytesPath
from collections.abc import Callable, Iterable, Mapping, Sequence
from types import TracebackType
from typing import IO, Any, AnyStr, Generic, TypeVar, overload
from typing_extensions import Literal, TypeAlias

if sys.version_info >= (3, 9):
    from types import GenericAlias

__all__ = [
    "Popen",
    "PIPE",
    "STDOUT",
    "call",
    "check_call",
    "getstatusoutput",
    "getoutput",
    "check_output",
    "run",
    "CalledProcessError",
    "DEVNULL",
    "SubprocessError",
    "TimeoutExpired",
    "CompletedProcess",
]

if sys.platform == "win32":
    __all__ += [
        "CREATE_NEW_CONSOLE",
        "CREATE_NEW_PROCESS_GROUP",
        "STARTF_USESHOWWINDOW",
        "STARTF_USESTDHANDLES",
        "STARTUPINFO",
        "STD_ERROR_HANDLE",
        "STD_INPUT_HANDLE",
        "STD_OUTPUT_HANDLE",
        "SW_HIDE",
    ]

    if sys.version_info >= (3, 7):
        __all__ += [
            "ABOVE_NORMAL_PRIORITY_CLASS",
            "BELOW_NORMAL_PRIORITY_CLASS",
            "CREATE_BREAKAWAY_FROM_JOB",
            "CREATE_DEFAULT_ERROR_MODE",
            "CREATE_NO_WINDOW",
            "DETACHED_PROCESS",
            "HIGH_PRIORITY_CLASS",
            "IDLE_PRIORITY_CLASS",
            "NORMAL_PRIORITY_CLASS",
            "REALTIME_PRIORITY_CLASS",
        ]

# We prefer to annotate inputs to methods (eg subprocess.check_call) with these
# union types.
# For outputs we use laborious literal based overloads to try to determine
# which specific return types to use, and prefer to fall back to Any when
# this does not work, so the caller does not have to use an assertion to confirm
# which type.
#
# For example:
#
# try:
#    x = subprocess.check_output(["ls", "-l"])
#    reveal_type(x)  # bytes, based on the overloads
# except TimeoutError as e:
#    reveal_type(e.cmd)  # Any, but morally is _CMD
_FILE: TypeAlias = None | int | IO[Any]
_TXT: TypeAlias = bytes | str
if sys.version_info >= (3, 8):
    _CMD: TypeAlias = StrOrBytesPath | Sequence[StrOrBytesPath]
else:
    # Python 3.6 doesn't support _CMD being a single PathLike.
    # See: https://bugs.python.org/issue31961
    _CMD: TypeAlias = _TXT | Sequence[StrOrBytesPath]
if sys.platform == "win32":
    _ENV: TypeAlias = Mapping[str, str]
else:
    _ENV: TypeAlias = Mapping[bytes, StrOrBytesPath] | Mapping[str, StrOrBytesPath]

_T = TypeVar("_T")

# These two are private but documented
if sys.version_info >= (3, 11):
    _USE_VFORK: bool
if sys.version_info >= (3, 8):
    _USE_POSIX_SPAWN: bool

class CompletedProcess(Generic[_T]):
    # morally: _CMD
    args: Any
    returncode: int
    # These can both be None, but requiring checks for None would be tedious
    # and writing all the overloads would be horrific.
    stdout: _T
    stderr: _T
    def __init__(self, args: _CMD, returncode: int, stdout: _T | None = ..., stderr: _T | None = ...) -> None: ...
    def check_returncode(self) -> None: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

if sys.version_info >= (3, 7):
    # Nearly the same args as for 3.6, except for capture_output and text
    @overload
    def run(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        capture_output: bool = ...,
        check: bool = ...,
        encoding: str | None = ...,
        errors: str | None = ...,
        input: str | None = ...,
        text: Literal[True],
        timeout: float | None = ...,
    ) -> CompletedProcess[str]: ...
    @overload
    def run(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        capture_output: bool = ...,
        check: bool = ...,
        encoding: str,
        errors: str | None = ...,
        input: str | None = ...,
        text: bool | None = ...,
        timeout: float | None = ...,
    ) -> CompletedProcess[str]: ...
    @overload
    def run(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        capture_output: bool = ...,
        check: bool = ...,
        encoding: str | None = ...,
        errors: str,
        input: str | None = ...,
        text: bool | None = ...,
        timeout: float | None = ...,
    ) -> CompletedProcess[str]: ...
    @overload
    def run(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        *,
        universal_newlines: Literal[True],
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        # where the *real* keyword only args start
        capture_output: bool = ...,
        check: bool = ...,
        encoding: str | None = ...,
        errors: str | None = ...,
        input: str | None = ...,
        text: bool | None = ...,
        timeout: float | None = ...,
    ) -> CompletedProcess[str]: ...
    @overload
    def run(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: Literal[False] = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        capture_output: bool = ...,
        check: bool = ...,
        encoding: None = ...,
        errors: None = ...,
        input: bytes | None = ...,
        text: Literal[None, False] = ...,
        timeout: float | None = ...,
    ) -> CompletedProcess[bytes]: ...
    @overload
    def run(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        capture_output: bool = ...,
        check: bool = ...,
        encoding: str | None = ...,
        errors: str | None = ...,
        input: _TXT | None = ...,
        text: bool | None = ...,
        timeout: float | None = ...,
    ) -> CompletedProcess[Any]: ...

else:
    # Nearly same args as Popen.__init__ except for timeout, input, and check
    @overload
    def run(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        check: bool = ...,
        encoding: str,
        errors: str | None = ...,
        input: str | None = ...,
        timeout: float | None = ...,
    ) -> CompletedProcess[str]: ...
    @overload
    def run(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        check: bool = ...,
        encoding: str | None = ...,
        errors: str,
        input: str | None = ...,
        timeout: float | None = ...,
    ) -> CompletedProcess[str]: ...
    @overload
    def run(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        *,
        universal_newlines: Literal[True],
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        # where the *real* keyword only args start
        check: bool = ...,
        encoding: str | None = ...,
        errors: str | None = ...,
        input: str | None = ...,
        timeout: float | None = ...,
    ) -> CompletedProcess[str]: ...
    @overload
    def run(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: Literal[False] = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        check: bool = ...,
        encoding: None = ...,
        errors: None = ...,
        input: bytes | None = ...,
        timeout: float | None = ...,
    ) -> CompletedProcess[bytes]: ...
    @overload
    def run(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        check: bool = ...,
        encoding: str | None = ...,
        errors: str | None = ...,
        input: _TXT | None = ...,
        timeout: float | None = ...,
    ) -> CompletedProcess[Any]: ...

# Same args as Popen.__init__
if sys.version_info >= (3, 7):
    def call(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        timeout: float | None = ...,
        text: bool | None = ...,
    ) -> int: ...

else:
    def call(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        timeout: float | None = ...,
    ) -> int: ...

# Same args as Popen.__init__
if sys.version_info >= (3, 7):
    def check_call(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        timeout: float | None = ...,
        *,
        text: bool | None = ...,
    ) -> int: ...

else:
    def check_call(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath = ...,
        stdin: _FILE = ...,
        stdout: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        timeout: float | None = ...,
    ) -> int: ...

if sys.version_info >= (3, 7):
    # 3.7 added text
    @overload
    def check_output(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        timeout: float | None = ...,
        input: _TXT | None = ...,
        encoding: str | None = ...,
        errors: str | None = ...,
        text: Literal[True],
    ) -> str: ...
    @overload
    def check_output(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        timeout: float | None = ...,
        input: _TXT | None = ...,
        encoding: str,
        errors: str | None = ...,
        text: bool | None = ...,
    ) -> str: ...
    @overload
    def check_output(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        timeout: float | None = ...,
        input: _TXT | None = ...,
        encoding: str | None = ...,
        errors: str,
        text: bool | None = ...,
    ) -> str: ...
    @overload
    def check_output(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        *,
        universal_newlines: Literal[True],
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        # where the real keyword only ones start
        timeout: float | None = ...,
        input: _TXT | None = ...,
        encoding: str | None = ...,
        errors: str | None = ...,
        text: bool | None = ...,
    ) -> str: ...
    @overload
    def check_output(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: Literal[False] = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        timeout: float | None = ...,
        input: _TXT | None = ...,
        encoding: None = ...,
        errors: None = ...,
        text: Literal[None, False] = ...,
    ) -> bytes: ...
    @overload
    def check_output(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        timeout: float | None = ...,
        input: _TXT | None = ...,
        encoding: str | None = ...,
        errors: str | None = ...,
        text: bool | None = ...,
    ) -> Any: ...  # morally: -> _TXT

else:
    @overload
    def check_output(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        timeout: float | None = ...,
        input: _TXT | None = ...,
        encoding: str,
        errors: str | None = ...,
    ) -> str: ...
    @overload
    def check_output(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        timeout: float | None = ...,
        input: _TXT | None = ...,
        encoding: str | None = ...,
        errors: str,
    ) -> str: ...
    @overload
    def check_output(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        universal_newlines: Literal[True],
        timeout: float | None = ...,
        input: _TXT | None = ...,
        encoding: str | None = ...,
        errors: str | None = ...,
    ) -> str: ...
    @overload
    def check_output(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: Literal[False] = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        timeout: float | None = ...,
        input: _TXT | None = ...,
        encoding: None = ...,
        errors: None = ...,
    ) -> bytes: ...
    @overload
    def check_output(
        args: _CMD,
        bufsize: int = ...,
        executable: StrOrBytesPath | None = ...,
        stdin: _FILE = ...,
        stderr: _FILE = ...,
        preexec_fn: Callable[[], Any] | None = ...,
        close_fds: bool = ...,
        shell: bool = ...,
        cwd: StrOrBytesPath | None = ...,
        env: _ENV | None = ...,
        universal_newlines: bool = ...,
        startupinfo: Any = ...,
        creationflags: int = ...,
        restore_signals: bool = ...,
        start_new_session: bool = ...,
        pass_fds: Any = ...,
        *,
        timeout: float | None = ...,
        input: _TXT | None = ...,
        encoding: str | None = ...,
        errors: str | None = ...,
    ) -> Any: ...  # morally: -> _TXT

PIPE: int
STDOUT: int
DEVNULL: int

class SubprocessError(Exception): ...

class TimeoutExpired(SubprocessError):
    def __init__(self, cmd: _CMD, timeout: float, output: _TXT | None = ..., stderr: _TXT | None = ...) -> None: ...
    # morally: _CMD
    cmd: Any
    timeout: float
    # morally: _TXT | None
    output: Any
    stdout: Any
    stderr: Any

class CalledProcessError(SubprocessError):
    returncode: int
    # morally: _CMD
    cmd: Any
    # morally: _TXT | None
    output: Any

    # morally: _TXT | None
    stdout: Any
    stderr: Any
    def __init__(self, returncode: int, cmd: _CMD, output: _TXT | None = ..., stderr: _TXT | None = ...) -> None: ...

class Popen(Generic[AnyStr]):
    args: _CMD
    stdin: IO[AnyStr] | None
    stdout: IO[AnyStr] | None
    stderr: IO[AnyStr] | None
    pid: int
    returncode: int | Any
    universal_newlines: bool

    # Technically it is wrong that Popen provides __new__ instead of __init__
    # but this shouldn't come up hopefully?

    if sys.version_info >= (3, 11):
        # process_group is added in 3.11
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: bool | None = ...,
            encoding: str,
            errors: str | None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
            pipesize: int = ...,
            process_group: int | None = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: bool | None = ...,
            encoding: str | None = ...,
            errors: str,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
            pipesize: int = ...,
            process_group: int | None = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            *,
            universal_newlines: Literal[True],
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            # where the *real* keyword only args start
            text: bool | None = ...,
            encoding: str | None = ...,
            errors: str | None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
            pipesize: int = ...,
            process_group: int | None = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: Literal[True],
            encoding: str | None = ...,
            errors: str | None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
            pipesize: int = ...,
            process_group: int | None = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: Literal[False] = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: Literal[None, False] = ...,
            encoding: None = ...,
            errors: None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
            pipesize: int = ...,
            process_group: int | None = ...,
        ) -> Popen[bytes]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: bool | None = ...,
            encoding: str | None = ...,
            errors: str | None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
            pipesize: int = ...,
            process_group: int | None = ...,
        ) -> Popen[Any]: ...
    elif sys.version_info >= (3, 10):
        # pipesize is added in 3.10
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: bool | None = ...,
            encoding: str,
            errors: str | None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
            pipesize: int = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: bool | None = ...,
            encoding: str | None = ...,
            errors: str,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
            pipesize: int = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            *,
            universal_newlines: Literal[True],
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            # where the *real* keyword only args start
            text: bool | None = ...,
            encoding: str | None = ...,
            errors: str | None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
            pipesize: int = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: Literal[True],
            encoding: str | None = ...,
            errors: str | None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
            pipesize: int = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: Literal[False] = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: Literal[None, False] = ...,
            encoding: None = ...,
            errors: None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
            pipesize: int = ...,
        ) -> Popen[bytes]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: bool | None = ...,
            encoding: str | None = ...,
            errors: str | None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
            pipesize: int = ...,
        ) -> Popen[Any]: ...
    elif sys.version_info >= (3, 9):
        # user, group, extra_groups, umask were added in 3.9
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: bool | None = ...,
            encoding: str,
            errors: str | None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: bool | None = ...,
            encoding: str | None = ...,
            errors: str,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            *,
            universal_newlines: Literal[True],
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            # where the *real* keyword only args start
            text: bool | None = ...,
            encoding: str | None = ...,
            errors: str | None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: Literal[True],
            encoding: str | None = ...,
            errors: str | None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: Literal[False] = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: Literal[None, False] = ...,
            encoding: None = ...,
            errors: None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
        ) -> Popen[bytes]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: bool | None = ...,
            encoding: str | None = ...,
            errors: str | None = ...,
            user: str | int | None = ...,
            group: str | int | None = ...,
            extra_groups: Iterable[str | int] | None = ...,
            umask: int = ...,
        ) -> Popen[Any]: ...
    elif sys.version_info >= (3, 7):
        # text is added in 3.7
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: bool | None = ...,
            encoding: str,
            errors: str | None = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: bool | None = ...,
            encoding: str | None = ...,
            errors: str,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            *,
            universal_newlines: Literal[True],
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            # where the *real* keyword only args start
            text: bool | None = ...,
            encoding: str | None = ...,
            errors: str | None = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: Literal[True],
            encoding: str | None = ...,
            errors: str | None = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: Literal[False] = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: Literal[None, False] = ...,
            encoding: None = ...,
            errors: None = ...,
        ) -> Popen[bytes]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            text: bool | None = ...,
            encoding: str | None = ...,
            errors: str | None = ...,
        ) -> Popen[Any]: ...
    else:
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            encoding: str,
            errors: str | None = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            encoding: str | None = ...,
            errors: str,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            *,
            universal_newlines: Literal[True],
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            # where the *real* keyword only args start
            encoding: str | None = ...,
            errors: str | None = ...,
        ) -> Popen[str]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: Literal[False] = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            encoding: None = ...,
            errors: None = ...,
        ) -> Popen[bytes]: ...
        @overload
        def __new__(
            cls,
            args: _CMD,
            bufsize: int = ...,
            executable: StrOrBytesPath | None = ...,
            stdin: _FILE | None = ...,
            stdout: _FILE | None = ...,
            stderr: _FILE | None = ...,
            preexec_fn: Callable[[], Any] | None = ...,
            close_fds: bool = ...,
            shell: bool = ...,
            cwd: StrOrBytesPath | None = ...,
            env: _ENV | None = ...,
            universal_newlines: bool = ...,
            startupinfo: Any | None = ...,
            creationflags: int = ...,
            restore_signals: bool = ...,
            start_new_session: bool = ...,
            pass_fds: Any = ...,
            *,
            encoding: str | None = ...,
            errors: str | None = ...,
        ) -> Popen[Any]: ...

    def poll(self) -> int | None: ...
    if sys.version_info >= (3, 7):
        def wait(self, timeout: float | None = ...) -> int: ...
    else:
        def wait(self, timeout: float | None = ..., endtime: float | None = ...) -> int: ...
    # Return str/bytes
    def communicate(
        self,
        input: AnyStr | None = ...,
        timeout: float | None = ...,
        # morally this should be optional
    ) -> tuple[AnyStr, AnyStr]: ...
    def send_signal(self, sig: int) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

# The result really is always a str.
if sys.version_info >= (3, 11):
    def getstatusoutput(cmd: _TXT, *, encoding: str | None = ..., errors: str | None = ...) -> tuple[int, str]: ...
    def getoutput(cmd: _TXT, *, encoding: str | None = ..., errors: str | None = ...) -> str: ...

else:
    def getstatusoutput(cmd: _TXT) -> tuple[int, str]: ...
    def getoutput(cmd: _TXT) -> str: ...

if sys.version_info >= (3, 8):
    def list2cmdline(seq: Iterable[StrOrBytesPath]) -> str: ...  # undocumented

else:
    def list2cmdline(seq: Iterable[str]) -> str: ...  # undocumented

if sys.platform == "win32":
    class STARTUPINFO:
        if sys.version_info >= (3, 7):
            def __init__(
                self,
                *,
                dwFlags: int = ...,
                hStdInput: Any | None = ...,
                hStdOutput: Any | None = ...,
                hStdError: Any | None = ...,
                wShowWindow: int = ...,
                lpAttributeList: Mapping[str, Any] | None = ...,
            ) -> None: ...
        dwFlags: int
        hStdInput: Any | None
        hStdOutput: Any | None
        hStdError: Any | None
        wShowWindow: int
        if sys.version_info >= (3, 7):
            lpAttributeList: Mapping[str, Any]
    from _winapi import (
        CREATE_NEW_CONSOLE as CREATE_NEW_CONSOLE,
        CREATE_NEW_PROCESS_GROUP as CREATE_NEW_PROCESS_GROUP,
        STARTF_USESHOWWINDOW as STARTF_USESHOWWINDOW,
        STARTF_USESTDHANDLES as STARTF_USESTDHANDLES,
        STD_ERROR_HANDLE as STD_ERROR_HANDLE,
        STD_INPUT_HANDLE as STD_INPUT_HANDLE,
        STD_OUTPUT_HANDLE as STD_OUTPUT_HANDLE,
        SW_HIDE as SW_HIDE,
    )

    if sys.version_info >= (3, 7):
        from _winapi import (
            ABOVE_NORMAL_PRIORITY_CLASS as ABOVE_NORMAL_PRIORITY_CLASS,
            BELOW_NORMAL_PRIORITY_CLASS as BELOW_NORMAL_PRIORITY_CLASS,
            CREATE_BREAKAWAY_FROM_JOB as CREATE_BREAKAWAY_FROM_JOB,
            CREATE_DEFAULT_ERROR_MODE as CREATE_DEFAULT_ERROR_MODE,
            CREATE_NO_WINDOW as CREATE_NO_WINDOW,
            DETACHED_PROCESS as DETACHED_PROCESS,
            HIGH_PRIORITY_CLASS as HIGH_PRIORITY_CLASS,
            IDLE_PRIORITY_CLASS as IDLE_PRIORITY_CLASS,
            NORMAL_PRIORITY_CLASS as NORMAL_PRIORITY_CLASS,
            REALTIME_PRIORITY_CLASS as REALTIME_PRIORITY_CLASS,
        )
