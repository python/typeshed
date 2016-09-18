"""Stub file for the 'signal' module."""

import sys
from enum import IntEnum
from typing import Any, Callable, List, Tuple, Dict, Generic, Union, Optional, Iterable, Set
from types import FrameType

class ItimerError(IOError): ...

ITIMER_PROF = ...  # type: int
ITIMER_REAL = ...  # type: int
ITIMER_VIRTUAL = ...  # type: int

NSIG = ...  # type: int

if sys.version_info >= (3, 5):
    class Signals(IntEnum):
        SIGABRT = ...  # type: Signals
        SIGALRM = ...  # type: Signals
        SIGBUS = ...  # type: Signals
        SIGCHLD = ...  # type: Signals
        SIGCLD = ...  # type: Signals
        SIGCONT = ...  # type: Signals
        SIGFPE = ...  # type: Signals
        SIGHUP = ...  # type: Signals
        SIGILL = ...  # type: Signals
        SIGINT = ...  # type: Signals
        SIGIO = ...  # type: Signals
        SIGIOT = ...  # type: Signals
        SIGKILL = ...  # type: Signals
        SIGPIPE = ...  # type: Signals
        SIGPOLL = ...  # type: Signals
        SIGPROF = ...  # type: Signals
        SIGPWR = ...  # type: Signals
        SIGQUIT = ...  # type: Signals
        SIGRTMAX = ...  # type: Signals
        SIGRTMIN = ...  # type: Signals
        SIGSEGV = ...  # type: Signals
        SIGSTOP = ...  # type: Signals
        SIGSYS = ...  # type: Signals
        SIGTERM = ...  # type: Signals
        SIGTRAP = ...  # type: Signals
        SIGTSTP = ...  # type: Signals
        SIGTTIN = ...  # type: Signals
        SIGTTOU = ...  # type: Signals
        SIGURG = ...  # type: Signals
        SIGUSR1 = ...  # type: Signals
        SIGUSR2 = ...  # type: Signals
        SIGVTALRM = ...  # type: Signals
        SIGWINCH = ...  # type: Signals
        SIGXCPU = ...  # type: Signals
        SIGXFSZ = ...  # type: Signals

    SIGABRT = Signals.SIGABRT
    SIGALRM = Signals.SIGALRM
    SIGBUS = Signals.SIGBUS
    SIGCHLD = Signals.SIGCHLD
    SIGCLD = Signals.SIGCLD
    SIGCONT = Signals.SIGCONT
    SIGFPE = Signals.SIGFPE
    SIGHUP = Signals.SIGHUP
    SIGILL = Signals.SIGILL
    SIGINT = Signals.SIGINT
    SIGIO = Signals.SIGIO
    SIGIOT = Signals.SIGIOT
    SIGKILL = Signals.SIGKILL
    SIGPIPE = Signals.SIGPIPE
    SIGPOLL = Signals.SIGPOLL
    SIGPROF = Signals.SIGPROF
    SIGPWR = Signals.SIGPWR
    SIGQUIT = Signals.SIGQUIT
    SIGRTMAX = Signals.SIGRTMAX
    SIGRTMIN = Signals.SIGRTMIN
    SIGSEGV = Signals.SIGSEGV
    SIGSTOP = Signals.SIGSTOP
    SIGSYS = Signals.SIGSYS
    SIGTERM = Signals.SIGTERM
    SIGTRAP = Signals.SIGTRAP
    SIGTSTP = Signals.SIGTSTP
    SIGTTIN = Signals.SIGTTIN
    SIGTTOU = Signals.SIGTTOU
    SIGURG = Signals.SIGURG
    SIGUSR1 = Signals.SIGUSR1
    SIGUSR2 = Signals.SIGUSR2
    SIGVTALRM = Signals.SIGVTALRM
    SIGWINCH = Signals.SIGWINCH
    SIGXCPU = Signals.SIGXCPU
    SIGXFSZ = Signals.SIGXFSZ

    class Handlers(IntEnum):
        SIG_DFL = ...  # type: Handlers
        SIG_IGN = ...  # type: Handlers

    SIG_DFL = Handlers.SIG_DFL
    SIG_IGN = Handlers.SIG_IGN

    class Sigmasks(IntEnum):
        SIG_BLOCK = ...  # type: Sigmasks
        SIG_UNBLOCK = ...  # type: Sigmasks
        SIG_SETMASK = ...  # type: Sigmasks

    SIG_BLOCK = Sigmasks.SIG_BLOCK
    SIG_UNBLOCK = Sigmasks.SIG_UNBLOCK
    SIG_SETMASK = Sigmasks.SIG_SETMASK

    _HANDLER = Union[Callable[[Signals, FrameType], None], int, Handlers, None]
    _SIGNUM = Union[int, Signals]
else:
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

    SIG_BLOCK = ...  # type: int
    SIG_UNBLOCK = ...  # type: int
    SIG_SETMASK = ...  # type: int

    _HANDLER = Union[Callable[[int, FrameType], None], int, None]
    _SIGNUM = int

CTRL_C_EVENT = 0 # Windows
CTRL_BREAK_EVENT = 0 # Windows

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

def getsignal(signalnum: _SIGNUM) -> _HANDLER:
    raise ValueError()

def pause() -> None: ...

def pthread_kill(thread_id: int, signum: int) -> None:
    raise OSError()

def pthread_sigmask(how: int, mask: Iterable[int]) -> Set[_SIGNUM]:
    raise OSError()

def set_wakeup_fd(fd: int) -> int: ...

def setitimer(which: int, seconds: float, interval: float = ...) -> Tuple[float, float]: ...

def siginterrupt(signalnum: int, flag: bool) -> None:
    raise OSError()

def signal(signalnum: _SIGNUM, handler: _HANDLER) -> _HANDLER:
    raise OSError()

def sigpending() -> Any:
    raise OSError()

def sigtimedwait(sigset: Iterable[int], timeout: float) -> Optional[struct_siginfo]:
    raise OSError()
    raise ValueError()

def sigwait(sigset: Iterable[int]) -> _SIGNUM:
    raise OSError()

def sigwaitinfo(sigset: Iterable[int]) -> struct_siginfo:
    raise OSError()
