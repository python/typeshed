"""Stub file for the 'signal' module."""

from typing import Any, Callable, List, Tuple, Dict, Generic, Union, Optional, Iterable, Set
from types import FrameType

class ItimerError(IOError): ...

ITIMER_PROF = ...  # type: int
ITIMER_REAL = ...  # type: int
ITIMER_VIRTUAL = ...  # type: int

NSIG = ...  # type: int
SIGABRT = ...  # type: int
SIGALRM = ...  # type: int
SIGBUS = ...  # type: int
SIGCHLD = ...  # type: int
SIGCLD = ...  # type: int
SIGCONT = ...  # type: int
SIGFPE = ...  # type: int
SIGHUP = ...  # type: int
SIGILL = ...  # type: int
SIGINT = ...  # type: int
SIGIO = ...  # type: int
SIGIOT = ...  # type: int
SIGKILL = ...  # type: int
SIGPIPE = ...  # type: int
SIGPOLL = ...  # type: int
SIGPROF = ...  # type: int
SIGPWR = ...  # type: int
SIGQUIT = ...  # type: int
SIGRTMAX = ...  # type: int
SIGRTMIN = ...  # type: int
SIGSEGV = ...  # type: int
SIGSTOP = ...  # type: int
SIGSYS = ...  # type: int
SIGTERM = ...  # type: int
SIGTRAP = ...  # type: int
SIGTSTP = ...  # type: int
SIGTTIN = ...  # type: int
SIGTTOU = ...  # type: int
SIGURG = ...  # type: int
SIGUSR1 = ...  # type: int
SIGUSR2 = ...  # type: int
SIGVTALRM = ...  # type: int
SIGWINCH = ...  # type: int
SIGXCPU = ...  # type: int
SIGXFSZ = ...  # type: int

SIG_DFL = ...  # type: int
SIG_IGN = ...  # type: int

CTRL_C_EVENT = 0 # Windows
CTRL_BREAK_EVENT = 0 # Windows

SIG_BLOCK = ...  # type: int
SIG_UNBLOCK = ...  # type: int
SIG_SETMASK = ...  # type: int

_HANDLER = Union[Callable[[int, FrameType], None], int, None]

class struct_siginfo(Tuple[int, int, int, int, int, int, int]):
    def __init__(self, sequence: Iterable[int]) -> None: ...
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

def alarm(time: int) -> int: ...

def default_int_handler(signum: int, frame: FrameType) -> None:
    raise KeyboardInterrupt()

def getitimer(which: int) -> Tuple[float, float]: ...

def getsignal(signalnum: int) -> _HANDLER:
    raise ValueError()

def pause() -> None: ...

def pthread_kill(thread_id: int, signum: int) -> None:
    raise OSError()

def pthread_sigmask(how: int, mask: Iterable[int]) -> Set[int]:
    raise OSError()

def set_wakeup_fd(fd: int) -> int: ...

def setitimer(which: int, seconds: float, interval: float = ...) -> Tuple[float, float]: ...

def siginterrupt(signalnum: int, flag: bool) -> None:
    raise OSError()

def signal(signalnum: int, handler: _HANDLER) -> _HANDLER:
    raise OSError()

def sigpending() -> Any:
    raise OSError()

def sigtimedwait(sigset: Iterable[int], timeout: float) -> Optional[struct_siginfo]:
    raise OSError()
    raise ValueError()

def sigwait(sigset: Iterable[int]) -> int:
    raise OSError()

def sigwaitinfo(sigset: Iterable[int]) -> struct_siginfo:
    raise OSError()
