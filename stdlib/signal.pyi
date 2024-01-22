import sys
from _typeshed import structseq
from collections.abc import Callable, Iterable
from enum import IntEnum
from types import FrameType
from typing import Any, Final, final
from typing_extensions import Never, TypeAlias

NSIG: int

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

SIG_DFL: Handlers
SIG_IGN: Handlers

_SIGNUM: TypeAlias = int | Signals
_HANDLER: TypeAlias = Callable[[int, FrameType | None], Any] | int | Handlers | None

def default_int_handler(__signalnum: int, __frame: FrameType | None) -> Never: ...

if sys.version_info >= (3, 10):  # arguments changed in 3.10.2
    def getsignal(signalnum: _SIGNUM) -> _HANDLER: ...
    def signal(signalnum: _SIGNUM, handler: _HANDLER) -> _HANDLER: ...

else:
    def getsignal(__signalnum: _SIGNUM) -> _HANDLER: ...
    def signal(__signalnum: _SIGNUM, __handler: _HANDLER) -> _HANDLER: ...

SIGABRT: Signals
SIGFPE: Signals
SIGILL: Signals
SIGINT: Signals
SIGSEGV: Signals
SIGTERM: Signals

if sys.platform == "win32":
    SIGBREAK: Signals
    CTRL_C_EVENT: Signals
    CTRL_BREAK_EVENT: Signals
else:
    if sys.platform != "linux":
        SIGINFO: Signals
        SIGEMT: Signals
    SIGALRM: Signals
    SIGBUS: Signals
    SIGCHLD: Signals
    SIGCONT: Signals
    SIGHUP: Signals
    SIGIO: Signals
    SIGIOT: Signals
    SIGKILL: Signals
    SIGPIPE: Signals
    SIGPROF: Signals
    SIGQUIT: Signals
    SIGSTOP: Signals
    SIGSYS: Signals
    SIGTRAP: Signals
    SIGTSTP: Signals
    SIGTTIN: Signals
    SIGTTOU: Signals
    SIGURG: Signals
    SIGUSR1: Signals
    SIGUSR2: Signals
    SIGVTALRM: Signals
    SIGWINCH: Signals
    SIGXCPU: Signals
    SIGXFSZ: Signals

    class ItimerError(OSError): ...
    ITIMER_PROF: int
    ITIMER_REAL: int
    ITIMER_VIRTUAL: int

    class Sigmasks(IntEnum):
        SIG_BLOCK = 0
        SIG_UNBLOCK = 1
        SIG_SETMASK = 2
    SIG_BLOCK = Sigmasks.SIG_BLOCK
    SIG_UNBLOCK = Sigmasks.SIG_UNBLOCK
    SIG_SETMASK = Sigmasks.SIG_SETMASK
    def alarm(__seconds: int) -> int: ...
    def getitimer(__which: int) -> tuple[float, float]: ...
    def pause() -> None: ...
    def pthread_kill(__thread_id: int, __signalnum: int) -> None: ...
    if sys.version_info >= (3, 10):  # arguments changed in 3.10.2
        def pthread_sigmask(how: int, mask: Iterable[int]) -> set[_SIGNUM]: ...
    else:
        def pthread_sigmask(__how: int, __mask: Iterable[int]) -> set[_SIGNUM]: ...

    def setitimer(__which: int, __seconds: float, __interval: float = 0.0) -> tuple[float, float]: ...
    def siginterrupt(__signalnum: int, __flag: bool) -> None: ...
    def sigpending() -> Any: ...
    if sys.version_info >= (3, 10):  # argument changed in 3.10.2
        def sigwait(sigset: Iterable[int]) -> _SIGNUM: ...
    else:
        def sigwait(__sigset: Iterable[int]) -> _SIGNUM: ...
    if sys.platform != "darwin":
        SIGCLD: Signals
        SIGPOLL: Signals
        SIGPWR: Signals
        SIGRTMAX: Signals
        SIGRTMIN: Signals
        if sys.version_info >= (3, 11):
            SIGSTKFLT: Signals
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

        if sys.version_info >= (3, 10):
            def sigtimedwait(__sigset: Iterable[int], __timeout: float) -> struct_siginfo | None: ...
            def sigwaitinfo(__sigset: Iterable[int]) -> struct_siginfo: ...
        else:
            def sigtimedwait(sigset: Iterable[int], timeout: float) -> struct_siginfo | None: ...
            def sigwaitinfo(sigset: Iterable[int]) -> struct_siginfo: ...

def strsignal(__signalnum: _SIGNUM) -> str | None: ...
def valid_signals() -> set[Signals]: ...
def raise_signal(__signalnum: _SIGNUM) -> None: ...
def set_wakeup_fd(fd: int, *, warn_on_full_buffer: bool = ...) -> int: ...

if sys.version_info >= (3, 9):
    if sys.platform == "linux":
        def pidfd_send_signal(__pidfd: int, __sig: int, __siginfo: None = None, __flags: int = ...) -> None: ...
