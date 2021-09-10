import enum
import sys
from typing import Any, Callable, NamedTuple, TypeVar

POSIX: bool
WINDOWS: bool
LINUX: bool
MACOS: bool
OSX: bool
FREEBSD: bool
OPENBSD: bool
NETBSD: bool
BSD: bool
SUNOS: bool
AIX: bool
STATUS_RUNNING: str
STATUS_SLEEPING: str
STATUS_DISK_SLEEP: str
STATUS_STOPPED: str
STATUS_TRACING_STOP: str
STATUS_ZOMBIE: str
STATUS_DEAD: str
STATUS_WAKE_KILL: str
STATUS_WAKING: str
STATUS_IDLE: str
STATUS_LOCKED: str
STATUS_WAITING: str
STATUS_SUSPENDED: str
STATUS_PARKED: str
CONN_ESTABLISHED: str
CONN_SYN_SENT: str
CONN_SYN_RECV: str
CONN_FIN_WAIT1: str
CONN_FIN_WAIT2: str
CONN_TIME_WAIT: str
CONN_CLOSE: str
CONN_CLOSE_WAIT: str
CONN_LAST_ACK: str
CONN_LISTEN: str
CONN_CLOSING: str
CONN_NONE: str
NIC_DUPLEX_FULL: int
NIC_DUPLEX_HALF: int
NIC_DUPLEX_UNKNOWN: int

class NicDuplex(enum.IntEnum):
    NIC_DUPLEX_FULL: int
    NIC_DUPLEX_HALF: int
    NIC_DUPLEX_UNKNOWN: int

POWER_TIME_UNKNOWN: int
POWER_TIME_UNLIMITED: int

class BatteryTime(enum.IntEnum):
    POWER_TIME_UNKNOWN: int
    POWER_TIME_UNLIMITED: int

ENCODING: str
ENCODING_ERRS: str

class sswap(NamedTuple):
    total: int
    used: int
    free: int
    percent: float
    sin: int
    sout: int

class sdiskusage(NamedTuple):
    total: int
    used: int
    free: int
    percent: float

class sdiskio(NamedTuple):
    read_count: int
    write_count: int
    read_bytes: int
    write_bytes: int
    read_time: int
    write_time: int

class sdiskpart(NamedTuple):
    device: str
    mountpoint: str
    fstype: str
    opts: str
    maxfile: int
    maxpath: int

class snetio(NamedTuple):
    bytes_sent: int
    bytes_recv: int
    packets_sent: int
    packets_recv: int
    errin: int
    errout: int
    dropin: int
    dropout: int

class suser(NamedTuple):
    name: str
    terminal: str | None
    host: str | None
    started: float
    pid: str

class sconn(NamedTuple):
    fd: int
    family: Any
    type: Any
    laddr: str
    raddr: str
    status: str
    pid: int

class snicaddr(NamedTuple):
    family: Any
    address: str
    netmask: str | None
    broadcast: str | None
    ptp: str | None

class snicstats(NamedTuple):
    isup: bool
    duplex: Any
    speed: int
    mtu: int

class scpustats(NamedTuple):
    ctx_switches: int
    interrupts: int
    soft_interrupts: int
    syscalls: int

class scpufreq(NamedTuple):
    current: float
    min: float
    max: float

class shwtemp(NamedTuple):
    label: str
    current: float
    high: float | None
    critical: float | None

class sbattery(NamedTuple):
    percent: int
    secsleft: int
    power_plugged: bool

class sfan(NamedTuple):
    label: str
    current: int

class pcputimes(NamedTuple):
    user: float
    system: float
    children_user: float
    children_system: float

class popenfile(NamedTuple):
    path: str
    fd: int
    if sys.platform == "linux":
        position: int
        mode: str
        flags: int

class pthread(NamedTuple):
    id: int
    user_time: float
    system_time: float

class puids(NamedTuple):
    real: int
    effective: int
    saved: int

class pgids(NamedTuple):
    real: int
    effective: int
    saved: int

class pio(NamedTuple):
    read_count: int
    write_count: int
    read_bytes: int
    write_bytes: int
    if sys.platform == "linux":
        read_chars: int
        write_chars: int

class pionice(NamedTuple):
    ioclass: Any
    value: int

class pctxsw(NamedTuple):
    voluntary: int
    involuntary: int

class pconn(NamedTuple):
    fd: int
    family: Any
    type: Any
    laddr: addr
    raddr: addr
    status: str

class addr(NamedTuple):
    ip: str
    port: int

conn_tmap: Any

class Error(Exception):
    __module__: str
    msg: Any
    def __init__(self, msg: str = ...) -> None: ...

class NoSuchProcess(Error):
    __module__: str
    pid: Any
    name: Any
    msg: Any
    def __init__(self, pid, name: Any | None = ..., msg: Any | None = ...) -> None: ...

class ZombieProcess(NoSuchProcess):
    __module__: str
    pid: Any
    ppid: Any
    name: Any
    msg: Any
    def __init__(self, pid, name: Any | None = ..., ppid: Any | None = ..., msg: Any | None = ...) -> None: ...

class AccessDenied(Error):
    __module__: str
    pid: Any
    name: Any
    msg: Any
    def __init__(self, pid: Any | None = ..., name: Any | None = ..., msg: Any | None = ...) -> None: ...

class TimeoutExpired(Error):
    __module__: str
    seconds: Any
    pid: Any
    name: Any
    def __init__(self, seconds, pid: Any | None = ..., name: Any | None = ...) -> None: ...

_Func = TypeVar("_Func", bound=Callable[..., Any])

def usage_percent(used, total, round_: int | None = ...) -> float: ...
def memoize(fun: _Func) -> _Func: ...
def memoize_when_activated(fun: _Func) -> _Func: ...
def isfile_strict(path) -> bool: ...
def path_exists_strict(path) -> bool: ...
def supports_ipv6() -> bool: ...
def parse_environ_block(data): ...
def sockfam_to_enum(num): ...
def socktype_to_enum(num): ...
def conn_to_ntuple(fd, fam, type_, laddr, raddr, status, status_map, pid: Any | None = ...): ...
def deprecated_method(replacement: str) -> Callable[[_Func], _Func]: ...

class _WrapNumbers:
    lock: Any
    cache: Any
    reminders: Any
    reminder_keys: Any
    def __init__(self) -> None: ...
    def run(self, input_dict, name): ...
    def cache_clear(self, name: Any | None = ...) -> None: ...
    def cache_info(self): ...

def wrap_numbers(input_dict, name): ...
def bytes2human(n: int, format: str = ...) -> str: ...
def get_procfs_path(): ...
def term_supports_colors(file=...) -> bool: ...
def hilite(s: str, color: str | None = ..., bold: bool = ...) -> str: ...
def print_color(s: str, color: str | None = ..., bold: bool = ..., file=...) -> None: ...
def debug(msg) -> None: ...
