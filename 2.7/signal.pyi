from typing import Callable, Any, Tuple, Union

SIG_DFL = ...  # type: long
SIG_IGN = ...  # type: long
ITIMER_REAL = ...  # type: long
ITIMER_VIRTUAL = ...  # type: long
ITIMER_PROF = ...  # type: long

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
NSIG = ...  # type: int

# Python 3 only:
CTRL_C_EVENT = 0
CTRL_BREAK_EVENT = 0
GSIG = 0

class ItimerError(IOError): ...

_HANDLER = Union[Callable[[int, Any], Any], int, None]

def alarm(time: int) -> int: ...
def getsignal(signalnum: int) -> _HANDLER: ...
def pause() -> None: ...
def setitimer(which: int, seconds: float, interval: float = None) -> Tuple[float, float]: ...
def getitimer(which: int) -> Tuple[float, float]: ...
def set_wakeup_fd(fd: int) -> long: ...
def siginterrupt(signalnum: int, flag: bool) -> None:
    raise RuntimeError()
def signal(signalnum: int, handler: _HANDLER) -> None:
    raise RuntimeError()
def default_int_handler(*args, **kwargs) -> Any:
    raise KeyboardInterrupt()
