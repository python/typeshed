import sys
from _typeshed import structseq
from collections.abc import Callable, Iterable
from enum import IntEnum
from types import FrameType
from typing import Any, Final, final
from typing_extensions import Never, TypeAlias

NSIG: Final[int]

class Signals(IntEnum):
    SIGABRT = 6
    SIGFPE = 8
    SIGILL = 4
    SIGINT = 2
    SIGSEGV = 11
    SIGTERM = 15

    if sys.platform == "win32":
        SIGBREAK = 21
        CTRL_C_EVENT = 0
        CTRL_BREAK_EVENT = 1
    else:
        SIGALRM = 14
        SIGBUS = 7
        SIGCHLD = 17
        SIGCONT = 18
        SIGHUP = 1
        SIGIO = 29
        SIGIOT = 6
        SIGKILL = 9
        SIGPIPE = 13
        SIGPROF = 27
        SIGQUIT = 3
        SIGSTOP = 19
        SIGSYS = 31
        SIGTRAP = 5
        SIGTSTP = 20
        SIGTTIN = 21
        SIGTTOU = 22
        SIGURG = 23
        SIGUSR1 = 10
        SIGUSR2 = 12
        SIGVTALRM = 26
        SIGWINCH = 28
        SIGXCPU = 24
        SIGXFSZ = 25
        if sys.platform != "linux":
            SIGEMT = 7
            SIGINFO = 29
        if sys.platform != "darwin":
            SIGCLD = 17
            SIGPOLL = 29
            SIGPWR = 30
            SIGRTMAX = 64
            SIGRTMIN = 34
            if sys.version_info >= (3, 11):
                SIGSTKFLT = 16

class Handlers(IntEnum):
    SIG_DFL = 0
    SIG_IGN = 1

SIG_DFL: Final[Handlers]
SIG_IGN: Final[Handlers]

_SIGNUM: Final[TypeAlias] = int | Signals
_HANDLER: Final[TypeAlias] = Callable[[int, FrameType | None], Any] | int | Handlers | None

def default_int_handler(signalnum: int, frame: FrameType | None, /) -> Never: ...

if sys.version_info >= (3, 10):  # arguments changed in 3.10.2
    def getsignal(signalnum: _SIGNUM) -> _HANDLER: ...
    def signal(signalnum: _SIGNUM, handler: _HANDLER) -> _HANDLER: ...

else:
    def getsignal(signalnum: _SIGNUM, /) -> _HANDLER: ...
    def signal(signalnum: _SIGNUM, handler: _HANDLER, /) -> _HANDLER: ...

SIGABRT: Final[Signals]
SIGFPE: Final[Signals]
SIGILL: Final[Signals]
SIGINT: Final[Signals]
SIGSEGV: Final[Signals]
SIGTERM: Final[Signals]

if sys.platform == "win32":
    SIGBREAK: Final[Signals]
    CTRL_C_EVENT: Final[Signals]
    CTRL_BREAK_EVENT: Final[Signals]
else:
    if sys.platform != "linux":
        SIGINFO: Final[Signals]
        SIGEMT: Final[Signals]
    SIGALRM: Final[Signals]
    SIGBUS: Final[Signals]
    SIGCHLD: Final[Signals]
    SIGCONT: Final[Signals]
    SIGHUP: Final[Signals]
    SIGIO: Final[Signals]
    SIGIOT: Final[Signals]
    SIGKILL: Final[Signals]
    SIGPIPE: Final[Signals]
    SIGPROF: Final[Signals]
    SIGQUIT: Final[Signals]
    SIGSTOP: Final[Signals]
    SIGSYS: Final[Signals]
    SIGTRAP: Final[Signals]
    SIGTSTP: Final[Signals]
    SIGTTIN: Final[Signals]
    SIGTTOU: Final[Signals]
    SIGURG: Final[Signals]
    SIGUSR1: Final[Signals]
    SIGUSR2: Final[Signals]
    SIGVTALRM: Final[Signals]
    SIGWINCH: Final[Signals]
    SIGXCPU: Final[Signals]
    SIGXFSZ: Final[Signals]

    class ItimerError(OSError): ...
    ITIMER_PROF: Final[int]
    ITIMER_REAL: Final[int]
    ITIMER_VIRTUAL: Final[int]

    class Sigmasks(IntEnum):
        SIG_BLOCK = 0
        SIG_UNBLOCK = 1
        SIG_SETMASK = 2

    SIG_BLOCK: Final = Sigmasks.SIG_BLOCKSigmasks.SIG_BLOCK
    SIG_UNBLOCK: Final = Sigmasks.SIG_UNBLOCKSigmasks.SIG_UNBLOCK
    SIG_SETMASK: Final = Sigmasks.SIG_SETMASKSigmasks.SIG_SETMASK
    def alarm(seconds: int, /) -> int: ...
    def getitimer(which: int, /) -> tuple[float, float]: ...
    def pause() -> None: ...
    def pthread_kill(thread_id: int, signalnum: int, /) -> None: ...
    if sys.version_info >= (3, 10):  # arguments changed in 3.10.2
        def pthread_sigmask(how: int, mask: Iterable[int]) -> set[_SIGNUM]: ...
    else:
        def pthread_sigmask(how: int, mask: Iterable[int], /) -> set[_SIGNUM]: ...

    def setitimer(which: int, seconds: float, interval: float = 0.0, /) -> tuple[float, float]: ...
    def siginterrupt(signalnum: int, flag: bool, /) -> None: ...
    def sigpending() -> Any: ...
    if sys.version_info >= (3, 10):  # argument changed in 3.10.2
        def sigwait(sigset: Iterable[int]) -> _SIGNUM: ...
    else:
        def sigwait(sigset: Iterable[int], /) -> _SIGNUM: ...
    if sys.platform != "darwin":
        SIGCLD: Final[Signals]
        SIGPOLL: Final[Signals]
        SIGPWR: Final[Signals]
        SIGRTMAX: Final[Signals]
        SIGRTMIN: Final[Signals]
        if sys.version_info >= (3, 11):
            SIGSTKFLT: Final[Signals]

        @final
        class struct_siginfo(structseq[int], tuple[int, int, int, int, int, int, int]):
            if sys.version_info >= (3, 10):
                __match_args__: Final = ("si_signo", "si_code", "si_errno", "si_pid", "si_uid", "si_status", "si_band")

            @property
            def si_signo(self) -> int: ...
            @property
            def si_code(self) -> int: ...
            @property
            def si_errno(self) -> int: ...
            @property
            def si_pid(self) -> int: ...
            @property
            def si_uid(self) -> int: ...
            @property
            def si_status(self) -> int: ...
            @property
            def si_band(self) -> int: ...

        def sigtimedwait(sigset: Iterable[int], timeout: float, /) -> struct_siginfo | None: ...
        def sigwaitinfo(sigset: Iterable[int], /) -> struct_siginfo: ...

def strsignal(signalnum: _SIGNUM, /) -> str | None: ...
def valid_signals() -> set[Signals]: ...
def raise_signal(signalnum: _SIGNUM, /) -> None: ...
def set_wakeup_fd(fd: int, /, *, warn_on_full_buffer: bool = ...) -> int: ...

if sys.version_info >= (3, 9):
    if sys.platform == "linux":
        def pidfd_send_signal(pidfd: int, sig: int, siginfo: None = None, flags: int = ..., /) -> None: ...
