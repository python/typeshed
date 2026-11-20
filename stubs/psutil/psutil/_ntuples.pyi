import sys
from _typeshed import Incomplete
from socket import AddressFamily, SocketKind
from typing import Any, NamedTuple

from ._enums import ConnectionStatus

# All named tuples are defined in this file, but due to the inability to detect some platforms,
# it was decided to store the correct named tuples inside platform-specific files.

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

# redefine for linux:
if sys.platform != "linux":
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
    pid: int | None

class sconn(NamedTuple):
    fd: int
    family: AddressFamily
    type: SocketKind
    laddr: addr | tuple[()]
    raddr: addr | tuple[()]
    status: ConnectionStatus
    pid: int | None

class snicaddr(NamedTuple):
    family: AddressFamily
    address: str
    netmask: str | None
    broadcast: str | None
    ptp: str | None

class snicstats(NamedTuple):
    isup: bool
    duplex: int
    speed: int
    mtu: int
    flags: str

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

if sys.platform == "win32":
    class pheap(NamedTuple):
        heap_used: int
        mmap_used: int
        heap_count: int

else:
    # if LINUX or MACOS or BSD:
    class pheap(NamedTuple):
        heap_used: int
        mmap_used: int

# redefine for linux:
if sys.platform != "linux":
    class pcputimes(NamedTuple):
        user: float
        system: float
        children_user: float
        children_system: float

    class popenfile(NamedTuple):
        path: str
        fd: int

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

# redefine for linux and windows:
if sys.platform != "linux" and sys.platform != "win32":
    class pio(NamedTuple):
        read_count: int
        write_count: int
        read_bytes: int
        write_bytes: int

class pionice(NamedTuple):
    ioclass: int
    value: int

class pctxsw(NamedTuple):
    voluntary: int
    involuntary: int

class ppagefaults(NamedTuple):
    minor: int
    major: int

class pconn(NamedTuple):
    fd: int
    family: AddressFamily
    type: SocketKind
    laddr: addr
    raddr: addr
    status: ConnectionStatus

class addr(NamedTuple):
    ip: str
    port: int

if sys.platform == "linux":
    class scputimes(NamedTuple):
        # Note: scputimes has different fields depending on exactly how Linux
        # is setup, but we'll include the "complete" set of fields
        user: float
        system: float
        idle: float
        nice: float
        iowait: float
        irq: float
        softirq: float
        steal: float
        guest: float
        guest_nice: float

    class smem(NamedTuple):
        total: int
        available: int
        percent: float
        used: int
        free: int
        active: int
        inactive: int
        buffers: int
        cached: int
        shared: int
        slab: int

    class sdiskio(NamedTuple):
        read_count: int
        write_count: int
        read_bytes: int
        write_bytes: int
        read_time: int
        write_time: int
        read_merged_count: int
        write_merged_count: int
        busy_time: int

    class popenfile(NamedTuple):
        path: str
        fd: int
        position: int
        mode: str
        flags: int

    class pmem(NamedTuple):
        rss: int
        vms: int
        shared: int
        text: int
        data: int

    class pmem_extras(NamedTuple):
        peak_rss: int
        peak_vms: int
        rss_anon: int
        rss_file: int
        rss_shmem: int
        swap_anon: int
        locked: int

    class pfootprint(NamedTuple):
        uss: int
        shared: int
        pss: int
        swap: int

    class pfullmem(NamedTuple):
        rss: int
        vms: int
        shared: int
        text: int
        data: int
        uss: int
        pss: int
        swap: int

    class pmmap_grouped(NamedTuple):
        path: str
        rss: int
        size: int
        pss: int
        shared_clean: int
        shared_dirty: int
        private_clean: int
        private_dirty: int
        referenced: int
        anonymous: int
        swap: int

    class pmmap_ext(NamedTuple):
        addr: str
        perms: str
        path: str
        rss: int
        size: int
        pss: int
        shared_clean: int
        shared_dirty: int
        private_clean: int
        private_dirty: int
        referenced: int
        anonymous: int
        swap: int

    class pio(NamedTuple):
        read_count: int
        write_count: int
        read_bytes: int
        write_bytes: int
        read_chars: int
        write_chars: int

    class pcputimes(NamedTuple):
        user: float
        system: float
        children_user: float
        children_system: float
        iowait: float

elif sys.platform == "win32":
    class scputimes(NamedTuple):
        user: float
        system: float
        idle: float
        interrupt: float
        dpc: float

    class smem(NamedTuple):
        total: int
        available: int
        percent: float
        used: int
        free: int

    class pmem(NamedTuple):
        rss: int
        vms: int
        peak_rss: int
        peak_vms: int

    class pmem_extras(NamedTuple):
        virtual: int
        peak_virtual: int
        paged_pool: int
        nonpaged_pool: int
        peak_paged_pool: int
        peak_nonpaged_pool: int

    class pfootprint(NamedTuple):
        uss: int
        shared: int

    class pfullmem(NamedTuple):
        rss: int
        vms: int
        peak_rss: int
        peak_vms: int
        uss: int

    class pmmap_grouped(NamedTuple):
        path: str
        rss: int

    class pmmap_ext(NamedTuple):
        addr: str
        perms: str
        path: str
        rss: int

    class pio(NamedTuple):
        read_count: int
        write_count: int
        read_bytes: int
        write_bytes: int
        other_count: int
        other_bytes: int

elif sys.platform == "darwin":
    class scputimes(NamedTuple):
        user: float
        system: float
        idle: float
        nice: float

    class smem(NamedTuple):
        total: int
        available: int
        percent: float
        used: int
        free: int
        active: int
        inactive: int
        wired: int

    class pmem(NamedTuple):
        rss: int
        vms: int

    class pmem_extras(NamedTuple):
        phys_footprint: int
        peak_phys_footprint: int

    class pfootprint(NamedTuple):
        uss: int
        shared: int

    class pfullmem(NamedTuple):
        rss: int
        vms: int
        uss: int

    class pmmap_grouped(NamedTuple):
        path: str
        rss: int

    class pmmap_ext(NamedTuple):
        addr: str
        perms: str
        path: str
        rss: int

else:
    # See _psbsd.pyi, _pssunos.pyi or _psaix.pyi
    # BSD: smem, scputimes, pmem, pfullmem, pcputimes, pmmap_grouped, pmmap_ext, sdiskio
    # SUNOS: scputimes, pcputimes, smem, pmem, pfullmem, pmmap_grouped, pmmap_ext
    # AIX: pmem, pfullmem, scputimes, smem

    scputimes = Incomplete

    class pmem(Any): ...
    class pmem_extras(Any): ...
    class pfootprint(Any): ...
    class pfullmem(Any): ...
    class smem(Any): ...
