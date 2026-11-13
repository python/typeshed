import sys
from _typeshed import Incomplete, StrOrBytesPath
from collections.abc import Callable, Collection, Iterable, Iterator
from contextlib import AbstractContextManager
from subprocess import _CMD, _ENV, _FILE
from types import TracebackType
from typing import Any, Literal, Protocol, overload, type_check_only
from typing_extensions import Self, deprecated

from psutil._common import (
    AIX as AIX,
    BSD as BSD,
    FREEBSD as FREEBSD,
    LINUX as LINUX,
    MACOS as MACOS,
    NETBSD as NETBSD,
    OPENBSD as OPENBSD,
    POSIX as POSIX,
    SUNOS as SUNOS,
    WINDOWS as WINDOWS,
    AccessDenied as AccessDenied,
    Error as Error,
    NoSuchProcess as NoSuchProcess,
    TimeoutExpired as TimeoutExpired,
    ZombieProcess as ZombieProcess,
)
from psutil._enums import (
    BatteryTime as BatteryTime,
    ConnectionStatus as ConnectionStatus,
    NicDuplex as NicDuplex,
    ProcessStatus as ProcessStatus,
)

from . import _ntuples as _ntp

__all__ = [
    # exceptions
    "Error",
    "NoSuchProcess",
    "ZombieProcess",
    "AccessDenied",
    "TimeoutExpired",
    # constants
    "version_info",
    "__version__",
    "AF_LINK",
    "BSD",
    "FREEBSD",
    "LINUX",
    "NETBSD",
    "OPENBSD",
    "MACOS",
    "POSIX",
    "SUNOS",
    "WINDOWS",
    "AIX",
    # classes
    "Process",
    "ProcessSnapshot",
    "Popen",
    # functions
    "pid_exists",
    "pids",
    "process_iter",
    "wait_procs",
    "memory_physical",
    "memory_swap",
    "virtual_memory",
    "swap_memory",
    "cpu_times",
    "cpu_percent",
    "cpu_times_percent",
    "cpu_count",
    "cpu_stats",
    "getloadavg",
    "net_io_counters",
    "net_connections",
    "net_if_addrs",
    "net_if_stats",
    "disk_io_counters",
    "disk_partitions",
    "disk_usage",
    "users",
    "boot_time",
    "bytes2human",
    "ProcessStatus",
    "STATUS_DEAD",
    "STATUS_DISK_SLEEP",
    "STATUS_IDLE",
    "STATUS_LOCKED",
    "STATUS_PARKED",
    "STATUS_RUNNING",
    "STATUS_SLEEPING",
    "STATUS_STOPPED",
    "STATUS_SUSPENDED",
    "STATUS_TRACING_STOP",
    "STATUS_UNKNOWN",
    "STATUS_WAITING",
    "STATUS_WAKE_KILL",
    "STATUS_WAKING",
    "STATUS_ZOMBIE",
    "ConnectionStatus",
    "CONN_CLOSE",
    "CONN_CLOSE_WAIT",
    "CONN_CLOSING",
    "CONN_ESTABLISHED",
    "CONN_FIN_WAIT1",
    "CONN_FIN_WAIT2",
    "CONN_LAST_ACK",
    "CONN_LISTEN",
    "CONN_NONE",
    "CONN_SYN_RECV",
    "CONN_SYN_SENT",
    "CONN_TIME_WAIT",
    "NicDuplex",
    "NIC_DUPLEX_FULL",
    "NIC_DUPLEX_HALF",
    "NIC_DUPLEX_UNKNOWN",
    "BatteryTime",
    "POWER_TIME_UNKNOWN",
    "POWER_TIME_UNLIMITED",
    "cpu_freq",
    "sensors_battery",
    "heap_info",
    "heap_trim",
]

if sys.platform == "linux":
    __all__ += [
        "PROCFS_PATH",
        "IOPRIO_CLASS_NONE",
        "IOPRIO_CLASS_RT",
        "IOPRIO_CLASS_BE",
        "IOPRIO_CLASS_IDLE",
        "RLIMIT_AS",
        "RLIMIT_CORE",
        "RLIMIT_CPU",
        "RLIMIT_DATA",
        "RLIMIT_FSIZE",
        "RLIMIT_LOCKS",
        "RLIMIT_MEMLOCK",
        "RLIMIT_MSGQUEUE",
        "RLIMIT_NICE",
        "RLIMIT_NOFILE",
        "RLIMIT_NPROC",
        "RLIMIT_RSS",
        "RLIMIT_RTPRIO",
        "RLIMIT_RTTIME",
        "RLIMIT_SIGPENDING",
        "RLIMIT_STACK",
        "RLIM_INFINITY",
        "sensors_temperatures",
        "sensors_fans",
    ]
elif sys.platform == "win32":
    __all__ += [
        "win_service_iter",
        "win_service_get",
        "ABOVE_NORMAL_PRIORITY_CLASS",
        "BELOW_NORMAL_PRIORITY_CLASS",
        "HIGH_PRIORITY_CLASS",
        "IDLE_PRIORITY_CLASS",
        "NORMAL_PRIORITY_CLASS",
        "REALTIME_PRIORITY_CLASS",
        "IOPRIO_VERYLOW",
        "IOPRIO_LOW",
        "IOPRIO_NORMAL",
        "IOPRIO_HIGH",
        "CONN_DELETE_TCB",
    ]

if sys.platform == "linux":
    from ._enums import ProcessIOPriority as ProcessIOPriority, ProcessRlimit as ProcessRlimit

    IOPRIO_CLASS_NONE: ProcessIOPriority
    IOPRIO_CLASS_RT: ProcessIOPriority
    IOPRIO_CLASS_BE: ProcessIOPriority
    IOPRIO_CLASS_IDLE: ProcessIOPriority
    def sensors_temperatures(fahrenheit: bool = False) -> dict[str, list[_ntp.shwtemp]]: ...
    def sensors_fans() -> dict[str, list[_ntp.sfan]]: ...
    PROCFS_PATH: str
    RLIMIT_AS: int
    RLIMIT_CORE: int
    RLIMIT_CPU: int
    RLIMIT_DATA: int
    RLIMIT_FSIZE: int
    RLIMIT_LOCKS: int
    RLIMIT_MEMLOCK: int
    RLIMIT_MSGQUEUE: int
    RLIMIT_NICE: int
    RLIMIT_NOFILE: int
    RLIMIT_NPROC: int
    RLIMIT_RSS: int
    RLIMIT_RTPRIO: int
    RLIMIT_RTTIME: int
    RLIMIT_SIGPENDING: int
    RLIMIT_STACK: int
    RLIM_INFINITY: int
if sys.platform == "win32":
    from ._enums import ProcessIOPriority as ProcessIOPriority, ProcessPriority as ProcessPriority
    from ._pswindows import WindowsService as WindowsService

    IOPRIO_VERYLOW: ProcessIOPriority
    IOPRIO_LOW: ProcessIOPriority
    IOPRIO_NORMAL: ProcessIOPriority
    IOPRIO_HIGH: ProcessIOPriority
    ABOVE_NORMAL_PRIORITY_CLASS: ProcessPriority
    BELOW_NORMAL_PRIORITY_CLASS: ProcessPriority
    HIGH_PRIORITY_CLASS: ProcessPriority
    IDLE_PRIORITY_CLASS: ProcessPriority
    NORMAL_PRIORITY_CLASS: ProcessPriority
    REALTIME_PRIORITY_CLASS: ProcessPriority
    CONN_DELETE_TCB: ConnectionStatus
    def win_service_get(name: str) -> WindowsService: ...
    def win_service_iter() -> Iterator[WindowsService]: ...

# Linux + glibc, Windows, macOS, FreeBSD, NetBSD:
def heap_info() -> _ntp.pheap: ...
def heap_trim() -> None: ...

if sys.platform == "linux":
    from ._pslinux import sensors_battery as sensors_battery
elif sys.platform == "darwin":
    from ._psosx import sensors_battery as sensors_battery
elif sys.platform == "win32":
    from ._pswindows import sensors_battery as sensors_battery
else:
    def sensors_battery(): ...

AF_LINK: int
version_info: tuple[int, int, int]
__version__: str
__author__: str
bytes2human: Callable[[int], str]

STATUS_DEAD: ProcessStatus
STATUS_DISK_SLEEP: ProcessStatus
STATUS_IDLE: ProcessStatus
STATUS_LOCKED: ProcessStatus
STATUS_PARKED: ProcessStatus
STATUS_RUNNING: ProcessStatus
STATUS_SLEEPING: ProcessStatus
STATUS_STOPPED: ProcessStatus
STATUS_SUSPENDED: ProcessStatus
STATUS_TRACING_STOP: ProcessStatus
STATUS_UNKNOWN: ProcessStatus
STATUS_WAITING: ProcessStatus
STATUS_WAKE_KILL: ProcessStatus
STATUS_WAKING: ProcessStatus
STATUS_ZOMBIE: ProcessStatus

CONN_CLOSE: ConnectionStatus
CONN_CLOSE_WAIT: ConnectionStatus
CONN_CLOSING: ConnectionStatus
CONN_ESTABLISHED: ConnectionStatus
CONN_FIN_WAIT1: ConnectionStatus
CONN_FIN_WAIT2: ConnectionStatus
CONN_LAST_ACK: ConnectionStatus
CONN_LISTEN: ConnectionStatus
CONN_NONE: ConnectionStatus
CONN_SYN_RECV: ConnectionStatus
CONN_SYN_SENT: ConnectionStatus
CONN_TIME_WAIT: ConnectionStatus

NIC_DUPLEX_FULL: NicDuplex
NIC_DUPLEX_HALF: NicDuplex
NIC_DUPLEX_UNKNOWN: NicDuplex

POWER_TIME_UNKNOWN: BatteryTime
POWER_TIME_UNLIMITED: BatteryTime

class ProcessSnapshot:
    cmdline: list[str]
    cpu_affinity: list[int]
    cpu_num: int
    cpu_percent: float
    cpu_times: _ntp.pcputimes
    create_time: float
    ctx_switches: _ntp.pctxsw
    cwd: str
    environ: dict[str, str]
    exe: str
    gids: _ntp.pgids
    io_counters: _ntp.pio
    ionice: _ntp.pionice
    memory_extras: _ntp.pmem_extras
    memory_footprint: _ntp.pfootprint
    memory_info: _ntp.pmem
    memory_maps: list[_ntp.pmmap_grouped] | list[_ntp.pmmap_ext]
    memory_percent: float
    name: str
    net_connections: list[_ntp.pconn]
    nice: int
    num_fds: int
    num_handles: int
    num_threads: int
    open_files: list[_ntp.popenfile]
    page_faults: _ntp.ppagefaults
    pid: int
    ppid: int
    status: ProcessStatus
    terminal: str | None
    threads: list[_ntp.pthread]
    uids: _ntp.puids
    username: str

    def __init__(self, data: dict[str, Any]) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    __hash__: None  # type: ignore[assignment]  # unhashable
    def __bool__(self) -> bool: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...

class Process:
    attrs: frozenset[str]
    def __init__(self, pid: int | None = None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object, /) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def pid(self) -> int: ...
    @property
    def snapshot(self) -> ProcessSnapshot: ...

    @property
    @deprecated("use Process.snapshot.as_dict() instead")
    def info(self) -> dict[str, Any]: ...
    @info.setter
    def info(self, value: dict[str, Any]) -> None: ...

    def oneshot(self) -> AbstractContextManager[None]: ...
    def as_dict(
        self, attrs: list[str] | tuple[str, ...] | set[str] | frozenset[str] | None = None, ad_value=None
    ) -> dict[str, Incomplete]: ...
    def parent(self) -> Process | None: ...
    def parents(self) -> list[Process]: ...
    def is_running(self) -> bool: ...
    def ppid(self) -> int: ...
    def name(self) -> str: ...
    def exe(self) -> str: ...
    def cmdline(self) -> list[str]: ...
    def status(self) -> ProcessStatus: ...
    def username(self) -> str: ...
    def create_time(self) -> float: ...
    def cwd(self) -> str: ...

    @overload
    def nice(self, value: None = None) -> int: ...
    @overload
    def nice(self, value: int) -> None: ...

    if sys.platform != "win32":
        def uids(self) -> _ntp.puids: ...
        def gids(self) -> _ntp.pgids: ...
        def terminal(self) -> str | None: ...
        def num_fds(self) -> int: ...
    if sys.platform != "darwin":
        def io_counters(self) -> _ntp.pio: ...
        def ionice(self, ioclass: int | None = None, value: int | None = None) -> _ntp.pionice: ...

        @overload
        def cpu_affinity(self, cpus: None = None) -> list[int]: ...
        @overload
        def cpu_affinity(self, cpus: list[int]) -> None: ...

        @overload
        def memory_maps(self, grouped: Literal[True] = True) -> list[_ntp.pmmap_grouped]: ...
        @overload
        def memory_maps(self, grouped: Literal[False]) -> list[_ntp.pmmap_ext]: ...
        @overload
        def memory_maps(self, grouped: bool) -> list[_ntp.pmmap_grouped] | list[_ntp.pmmap_ext]: ...

    if sys.platform == "linux":
        def rlimit(self, resource: int, limits: tuple[int, int] | None = None) -> tuple[int, int]: ...
        def cpu_num(self) -> int: ...

    def environ(self) -> dict[str, str]: ...
    if sys.platform == "win32":
        def num_handles(self) -> int: ...

    def ctx_switches(self) -> _ntp.pctxsw: ...
    @deprecated("use ctx_switches() method instead")
    def num_ctx_switches(self) -> _ntp.pctxsw: ...
    def num_threads(self) -> int: ...
    def threads(self) -> list[_ntp.pthread]: ...
    def children(self, recursive: bool = False) -> list[Process]: ...
    def cpu_percent(self, interval: float | None = None) -> float: ...
    def cpu_times(self) -> _ntp.pcputimes: ...
    def memory_info(self) -> _ntp.pmem: ...
    if sys.platform == "linux" or sys.platform == "darwin" or sys.platform == "win32":
        def memory_extras(self) -> _ntp.pmem_extras: ...
        def memory_footprint(self) -> _ntp.pfootprint: ...

    @deprecated("use memory_footprint() method instead")
    def memory_full_info(self) -> _ntp.pfullmem: ...
    def memory_percent(self, memtype: str = "rss") -> float: ...
    def page_faults(self) -> _ntp.ppagefaults: ...
    def open_files(self) -> list[_ntp.popenfile]: ...
    @deprecated('use "net_connections" method instead')
    def connections(self, kind: str = "inet") -> list[_ntp.pconn]: ...
    def send_signal(self, sig: int) -> None: ...
    def suspend(self) -> None: ...
    def resume(self) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    def wait(self, timeout: float | None = None) -> int: ...
    def net_connections(self, kind: str = "inet") -> list[_ntp.pconn]: ...

class Popen(Process):
    # sync with subprocess.Popen.__init__:
    if sys.version_info >= (3, 11):
        def __init__(
            self,
            args: _CMD,
            bufsize: int = -1,
            executable: StrOrBytesPath | None = None,
            stdin: _FILE | None = None,
            stdout: _FILE | None = None,
            stderr: _FILE | None = None,
            preexec_fn: Callable[[], object] | None = None,
            close_fds: bool = True,
            shell: bool = False,
            cwd: StrOrBytesPath | None = None,
            env: _ENV | None = None,
            universal_newlines: bool | None = None,
            startupinfo: Any | None = None,
            creationflags: int = 0,
            restore_signals: bool = True,
            start_new_session: bool = False,
            pass_fds: Collection[int] = (),
            *,
            text: bool | None = None,
            encoding: str | None = None,
            errors: str | None = None,
            user: str | int | None = None,
            group: str | int | None = None,
            extra_groups: Iterable[str | int] | None = None,
            umask: int = -1,
            pipesize: int = -1,
            process_group: int | None = None,
        ) -> None: ...
    else:
        def __init__(
            self,
            args: _CMD,
            bufsize: int = -1,
            executable: StrOrBytesPath | None = None,
            stdin: _FILE | None = None,
            stdout: _FILE | None = None,
            stderr: _FILE | None = None,
            preexec_fn: Callable[[], object] | None = None,
            close_fds: bool = True,
            shell: bool = False,
            cwd: StrOrBytesPath | None = None,
            env: _ENV | None = None,
            universal_newlines: bool | None = None,
            startupinfo: Any | None = None,
            creationflags: int = 0,
            restore_signals: bool = True,
            start_new_session: bool = False,
            pass_fds: Collection[int] = (),
            *,
            text: bool | None = None,
            encoding: str | None = None,
            errors: str | None = None,
            user: str | int | None = None,
            group: str | int | None = None,
            extra_groups: Iterable[str | int] | None = None,
            umask: int = -1,
            pipesize: int = -1,
        ) -> None: ...

    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __getattribute__(self, name: str) -> Any: ...
    def __dir__(self) -> list[str]: ...

@type_check_only
class _ProcessIterCallable(Protocol):
    def __call__(
        self, attrs: list[str] | tuple[str, ...] | set[str] | frozenset[str] | None = None, ad_value=None
    ) -> Iterator[Process]: ...
    def cache_clear(self) -> None: ...

def pids() -> list[int]: ...
def pid_exists(pid: int) -> bool: ...

process_iter: _ProcessIterCallable

def wait_procs(
    procs: Iterable[Process], timeout: float | None = None, callback: Callable[[Process], object] | None = None
) -> tuple[list[Process], list[Process]]: ...
def cpu_count(logical: bool = True) -> int | None: ...

@overload
def cpu_freq(percpu: Literal[False] = False) -> _ntp.scpufreq: ...
@overload
def cpu_freq(percpu: Literal[True]) -> list[_ntp.scpufreq]: ...

@overload
def cpu_times(percpu: Literal[False] = False) -> _ntp.scputimes: ...
@overload
def cpu_times(percpu: Literal[True]) -> list[_ntp.scputimes]: ...

@overload
def cpu_percent(interval: float | None = None, percpu: Literal[False] = False) -> float: ...
@overload
def cpu_percent(interval: float | None, percpu: Literal[True]) -> list[float]: ...
@overload
def cpu_percent(*, percpu: Literal[True]) -> list[float]: ...

@overload
def cpu_times_percent(interval: float | None = None, percpu: Literal[False] = False) -> _ntp.scputimes: ...
@overload
def cpu_times_percent(interval: float | None, percpu: Literal[True]) -> list[_ntp.scputimes]: ...
@overload
def cpu_times_percent(*, percpu: Literal[True]) -> list[_ntp.scputimes]: ...

def cpu_stats() -> _ntp.scpustats: ...
def getloadavg() -> tuple[float, float, float]: ...
def memory_physical() -> _ntp.smem: ...
def memory_swap() -> _ntp.sswap: ...
@deprecated("use memory_physical() function instead")
def virtual_memory() -> _ntp.smem: ...
@deprecated("use memory_swap() function instead")
def swap_memory() -> _ntp.sswap: ...
def disk_usage(path: str) -> _ntp.sdiskusage: ...
def disk_partitions(all: bool = False) -> list[_ntp.sdiskpart]: ...

# TODO: Incorrect sdiskio for BSD systems:
@overload
def disk_io_counters(perdisk: Literal[False] = False, nowrap: bool = True) -> _ntp.sdiskio | None: ...
@overload
def disk_io_counters(perdisk: Literal[True], nowrap: bool = True) -> dict[str, _ntp.sdiskio]: ...

@overload
def net_io_counters(pernic: Literal[False] = False, nowrap: bool = True) -> _ntp.snetio: ...
@overload
def net_io_counters(pernic: Literal[True], nowrap: bool = True) -> dict[str, _ntp.snetio]: ...

def net_connections(kind: str = "inet") -> list[_ntp.sconn]: ...
def net_if_addrs() -> dict[str, list[_ntp.snicaddr]]: ...
def net_if_stats() -> dict[str, _ntp.snicstats]: ...
def boot_time() -> float: ...
def users() -> list[_ntp.suser]: ...
