from typing import Any

PSUTIL_CONN_NONE: int
SIDL: int
SRUN: int
SSLEEP: int
SSTOP: int
SZOMB: int
TCPS_CLOSED: int
TCPS_CLOSE_WAIT: int
TCPS_CLOSING: int
TCPS_ESTABLISHED: int
TCPS_FIN_WAIT_1: int
TCPS_FIN_WAIT_2: int
TCPS_LAST_ACK: int
TCPS_LISTEN: int
TCPS_SYN_RECEIVED: int
TCPS_SYN_SENT: int
TCPS_TIME_WAIT: int
version: int

def boot_time(*args, **kwargs) -> Any: ...
def check_pid_range(pid: int, /) -> None: ...
def cpu_count_cores(*args, **kwargs) -> Any: ...
def cpu_count_logical(*args, **kwargs) -> Any: ...
def cpu_freq(*args, **kwargs) -> Any: ...
def cpu_stats(*args, **kwargs) -> Any: ...
def cpu_times(*args, **kwargs) -> Any: ...
def disk_io_counters(*args, **kwargs) -> Any: ...
def disk_partitions(*args, **kwargs) -> Any: ...
def disk_usage_used(*args, **kwargs) -> Any: ...
def net_io_counters(*args, **kwargs) -> Any: ...
def per_cpu_times(*args, **kwargs) -> Any: ...
def pids(*args, **kwargs) -> Any: ...
def proc_cmdline(*args, **kwargs) -> Any: ...
def proc_net_connections(*args, **kwargs) -> Any: ...
def proc_cwd(*args, **kwargs) -> Any: ...
def proc_environ(*args, **kwargs) -> Any: ...
def proc_exe(*args, **kwargs) -> Any: ...
def proc_kinfo_oneshot(*args, **kwargs) -> Any: ...
def proc_memory_uss(*args, **kwargs) -> Any: ...
def proc_name(*args, **kwargs) -> Any: ...
def proc_num_fds(*args, **kwargs) -> Any: ...
def proc_open_files(*args, **kwargs) -> Any: ...
def proc_pidtaskinfo_oneshot(*args, **kwargs) -> Any: ...
def proc_threads(*args, **kwargs) -> Any: ...
def sensors_battery(*args, **kwargs) -> Any: ...
def set_debug(*args, **kwargs) -> Any: ...
def swap_mem(*args, **kwargs) -> Any: ...
def users(*args, **kwargs) -> Any: ...
def virtual_mem(*args, **kwargs) -> Any: ...
