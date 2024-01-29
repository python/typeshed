#

import sys

if sys.platform != "win32":
    from _resource_rusage import struct_rusage as struct_rusage

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

    def getpagesize() -> int: ...
    def getrlimit(__resource: int) -> tuple[int, int]: ...
    def getrusage(__who: int) -> struct_rusage: ...
    def setrlimit(__resource: int, __limits: tuple[int, int]) -> None: ...
    if sys.platform == "linux":
        if sys.version_info >= (3, 12):
            def prlimit(__pid: int, __resource: int, __limits: tuple[int, int] | None = None) -> tuple[int, int]: ...
        else:
            def prlimit(__pid: int, __resource: int, __limits: tuple[int, int] = ...) -> tuple[int, int]: ...
    error = OSError
