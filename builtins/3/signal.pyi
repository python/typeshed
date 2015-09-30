"""Stub file for the 'signal' module."""

from typing import Any, Callable, List, Tuple, Dict, Generic, Union

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

def alarm(time: int) -> int: ...

def default_int_handler(*args, **kwargs) -> Any:
    raise KeyboardInterrupt()

def getitimer(which: int) -> tuple: ...

def getsignal(signalnum: int) -> None:
    raise ValueError()

def pause() -> None: ...

def pthread_kill(a: int, b: int) -> None:
    raise OSError()

def pthread_sigmask(a: int, b) -> Any:
    raise OSError()

def set_wakeup_fd(fd: int) -> int: ...

def setitimer(which: int, seconds: float, internval: float = ...) -> Tuple[float, float]: ...

def siginterrupt(signalnum: int, flag: int) -> None:
    raise OSError()

def signal(signalnum: int, handler: Union[int, Callable[[int, Any], None]]) -> Any:
    raise OSError()

def sigpending() -> Any:
    raise OSError()

def sigtimedwait(a, b) -> Any:
    raise OSError()
    raise ValueError()

def sigwait(a) -> int:
    raise OSError()

def sigwaitinfo(a) -> tuple:
    raise OSError()

... # TODO frame object type
