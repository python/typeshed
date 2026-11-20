import enum
import sys

if sys.version_info >= (3, 11):
    from enum import StrEnum as StrEnum
else:
    class StrEnum(str, enum.Enum): ...  # type: ignore[misc]

class ProcessStatus(StrEnum):
    STATUS_DEAD = "dead"
    STATUS_DISK_SLEEP = "disk-sleep"
    STATUS_IDLE = "idle"
    STATUS_LOCKED = "locked"
    STATUS_PARKED = "parked"
    STATUS_RUNNING = "running"
    STATUS_SLEEPING = "sleeping"
    STATUS_STOPPED = "stopped"
    STATUS_SUSPENDED = "suspended"
    STATUS_TRACING_STOP = "tracing-stop"
    STATUS_UNKNOWN = "unknown"
    STATUS_WAITING = "waiting"
    STATUS_WAKE_KILL = "wake-kill"
    STATUS_WAKING = "waking"
    STATUS_ZOMBIE = "zombie"

class ConnectionStatus(StrEnum):
    CONN_CLOSE = "CLOSE"
    CONN_CLOSE_WAIT = "CLOSE_WAIT"
    CONN_CLOSING = "CLOSING"
    CONN_ESTABLISHED = "ESTABLISHED"
    CONN_FIN_WAIT1 = "FIN_WAIT1"
    CONN_FIN_WAIT2 = "FIN_WAIT2"
    CONN_LAST_ACK = "LAST_ACK"
    CONN_LISTEN = "LISTEN"
    CONN_NONE = "NONE"
    CONN_SYN_RECV = "SYN_RECV"
    CONN_SYN_SENT = "SYN_SENT"
    CONN_TIME_WAIT = "TIME_WAIT"
    if sys.platform == "win32":
        CONN_DELETE_TCB = "DELETE_TCB"
    if sys.platform == "sunos5":  # noqa: Y008
        CONN_BOUND = "BOUND"
        CONN_IDLE = "IDLE"

class NicDuplex(enum.IntEnum):
    NIC_DUPLEX_FULL = 2
    NIC_DUPLEX_HALF = 1
    NIC_DUPLEX_UNKNOWN = 0

class BatteryTime(enum.IntEnum):
    POWER_TIME_UNKNOWN = -1
    POWER_TIME_UNLIMITED = -2

if sys.platform == "linux":
    class ProcessIOPriority(enum.IntEnum):
        IOPRIO_CLASS_NONE = 0
        IOPRIO_CLASS_RT = 1
        IOPRIO_CLASS_BE = 2
        IOPRIO_CLASS_IDLE = 3

elif sys.platform == "win32":
    class ProcessIOPriority(enum.IntEnum):
        IOPRIO_VERYLOW = 0
        IOPRIO_LOW = 1
        IOPRIO_NORMAL = 2
        IOPRIO_HIGH = 3

    class ProcessPriority(enum.IntEnum):
        ABOVE_NORMAL_PRIORITY_CLASS = 32768
        BELOW_NORMAL_PRIORITY_CLASS = 16384
        HIGH_PRIORITY_CLASS = 128
        IDLE_PRIORITY_CLASS = 64
        NORMAL_PRIORITY_CLASS = 32
        REALTIME_PRIORITY_CLASS = 256

if sys.platform == "linux":
    class ProcessRlimit(enum.IntEnum):
        RLIMIT_AS = 9
        RLIMIT_CORE = 4
        RLIMIT_CPU = 0
        RLIMIT_DATA = 2
        RLIMIT_FSIZE = 1
        RLIMIT_LOCKS = 10
        RLIMIT_MEMLOCK = 8
        RLIMIT_MSGQUEUE = 12
        RLIMIT_NICE = 13
        RLIMIT_NOFILE = 7
        RLIMIT_NPROC = 6
        RLIMIT_RSS = 5
        RLIMIT_RTPRIO = 14
        RLIMIT_RTTIME = 15
        RLIMIT_SIGPENDING = 11
        RLIMIT_STACK = 3

elif sys.platform != "win32" and sys.platform != "darwin":  # Linux or FreeBSD
    class ProcessRlimit(enum.IntEnum):
        RLIMIT_AS = 10
        RLIMIT_CORE = 4
        RLIMIT_CPU = 0
        RLIMIT_DATA = 2
        RLIMIT_FSIZE = 1
        RLIMIT_MEMLOCK = 6
        RLIMIT_NOFILE = 8
        RLIMIT_NPROC = 7
        RLIMIT_NPTS = 11
        RLIMIT_RSS = 5
        RLIMIT_SBSIZE = 9
        RLIMIT_STACK = 3
        RLIMIT_SWAP = 12
