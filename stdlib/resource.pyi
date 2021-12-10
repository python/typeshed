import sys
from _typeshed import structseq
from typing import Tuple, overload
from typing_extensions import final

RLIMIT_AS: int
RLIMIT_CORE: int
RLIMIT_CPU: int
RLIMIT_DATA: int
RLIMIT_FSIZE: int
RLIMIT_MEMLOCK: int
RLIMIT_NOFILE: int
RLIMIT_NPROC: int
RLIMIT_RSS: int
RLIMIT_STACK: int
RLIM_INFINITY: int
RUSAGE_CHILDREN: int
RUSAGE_SELF: int
if sys.platform == "linux":
    RLIMIT_MSGQUEUE: int
    RLIMIT_NICE: int
    RLIMIT_OFILE: int
    RLIMIT_RTPRIO: int
    RLIMIT_RTTIME: int
    RLIMIT_SIGPENDING: int
    RUSAGE_THREAD: int

_Tuple16 = Tuple[float, float, int, int, int, int, int, int, int, int, int, int, int, int, int, int]

@final
class struct_rusage(structseq[float], _Tuple16):
    @property
    def ru_utime(self) -> float: ...
    @property
    def ru_stime(self) -> float: ...
    @property
    def ru_maxrss(self) -> int: ...
    @property
    def ru_ixrss(self) -> int: ...
    @property
    def ru_idrss(self) -> int: ...
    @property
    def ru_isrss(self) -> int: ...
    @property
    def ru_minflt(self) -> int: ...
    @property
    def ru_majflt(self) -> int: ...
    @property
    def ru_nswap(self) -> int: ...
    @property
    def ru_inblock(self) -> int: ...
    @property
    def ru_oublock(self) -> int: ...
    @property
    def ru_msgsnd(self) -> int: ...
    @property
    def ru_msgrcv(self) -> int: ...
    @property
    def ru_nsignals(self) -> int: ...
    @property
    def ru_nvcsw(self) -> int: ...
    @property
    def ru_nivcsw(self) -> int: ...

def getpagesize() -> int: ...
def getrlimit(__resource: int) -> tuple[int, int]: ...
def getrusage(__who: int) -> struct_rusage: ...
def setrlimit(__resource: int, __limits: tuple[int, int]) -> None: ...

if sys.platform == "linux":
    @overload
    def prlimit(pid: int, resource: int, limits: tuple[int, int]) -> tuple[int, int]: ...
    @overload
    def prlimit(pid: int, resource: int) -> tuple[int, int]: ...

error = OSError
