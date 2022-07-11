from typing import Any, NamedTuple

from ._common import (
    AccessDenied as AccessDenied,
    NoSuchProcess as NoSuchProcess,
    ZombieProcess as ZombieProcess,
    conn_tmap as conn_tmap,
    conn_to_ntuple as conn_to_ntuple,
    isfile_strict as isfile_strict,
    parse_environ_block as parse_environ_block,
    usage_percent as usage_percent,
)

__extra__all__: Any
PAGESIZE: Any
AF_LINK: Any
TCP_STATUSES: Any
PROC_STATUSES: Any
kinfo_proc_map: Any
pidtaskinfo_map: Any

class scputimes(NamedTuple):
    user: Any
    nice: Any
    system: Any
    idle: Any

class svmem(NamedTuple):
    total: Any
    available: Any
    percent: Any
    used: Any
    free: Any
    active: Any
    inactive: Any
    wired: Any

class pmem(NamedTuple):
    rss: Any
    vms: Any
    pfaults: Any
    pageins: Any

pfullmem: Any

def virtual_memory(): ...
def swap_memory(): ...
def cpu_times(): ...
def per_cpu_times(): ...
def cpu_count_logical(): ...
def cpu_count_cores() -> int | None: ...
def cpu_stats(): ...
def cpu_freq(): ...

disk_usage: Any
disk_io_counters: Any

def disk_partitions(all: bool = ...): ...
def sensors_battery(): ...

net_io_counters: Any
net_if_addrs: Any

def net_connections(kind: str = ...): ...
def net_if_stats(): ...
def boot_time(): ...
def users(): ...
def pids(): ...

pid_exists: Any

def is_zombie(pid): ...
def wrap_exceptions(fun): ...

class Process:
    pid: Any
    def __init__(self, pid) -> None: ...
    def oneshot_enter(self) -> None: ...
    def oneshot_exit(self) -> None: ...
    def name(self): ...
    def exe(self): ...
    def cmdline(self): ...
    def environ(self): ...
    def ppid(self): ...
    def cwd(self): ...
    def uids(self): ...
    def gids(self): ...
    def terminal(self): ...
    def memory_info(self): ...
    def memory_full_info(self): ...
    def cpu_times(self): ...
    def create_time(self): ...
    def num_ctx_switches(self): ...
    def num_threads(self): ...
    def open_files(self): ...
    def connections(self, kind: str = ...): ...
    def num_fds(self): ...
    def wait(self, timeout: Any | None = ...): ...
    def nice_get(self): ...
    def nice_set(self, value): ...
    def status(self): ...
    def threads(self): ...
