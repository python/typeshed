# Stubs for posix

# NOTE: These are incomplete!

import sys
from typing import NamedTuple, Tuple

class stat_result:
    # For backward compatibility, the return value of stat() is also
    # accessible as a tuple of at least 10 integers giving the most important
    # (and portable) members of the stat structure, in the order st_mode,
    # st_ino, st_dev, st_nlink, st_uid, st_gid, st_size, st_atime, st_mtime,
    # st_ctime. More items may be added at the end by some implementations.

    st_mode: int  # protection bits,
    st_ino: int  # inode number,
    st_dev: int  # device,
    st_nlink: int  # number of hard links,
    st_uid: int  # user id of owner,
    st_gid: int  # group id of owner,
    st_size: int  # size of file, in bytes,
    st_atime: float  # time of most recent access,
    st_mtime: float  # time of most recent content modification,
    st_ctime: float  # platform dependent (time of most recent metadata change on Unix, or the time of creation on Windows)
    st_atime_ns: int  # time of most recent access, in nanoseconds
    st_mtime_ns: int  # time of most recent content modification in nanoseconds
    st_ctime_ns: int  # platform dependent (time of most recent metadata change on Unix, or the time of creation on Windows) in nanoseconds

    # not documented
    def __init__(self, tuple: Tuple[int, ...]) -> None: ...

    # On some Unix systems (such as Linux), the following attributes may also
    # be available:
    st_blocks: int  # number of blocks allocated for file
    st_blksize: int  # filesystem blocksize
    st_rdev: int  # type of device if an inode device
    st_flags: int  # user defined flags for file

    # On other Unix systems (such as FreeBSD), the following attributes may be
    # available (but may be only filled out if root tries to use them):
    st_gen: int  # file generation number
    st_birthtime: int  # time of file creation

    # On Mac OS systems, the following attributes may also be available:
    st_rsize: int
    st_creator: int
    st_type: int

uname_result = NamedTuple('uname_result', [
    ('sysname', str),
    ('nodename', str),
    ('release', str),
    ('version', str),
    ('machine', str),
])

times_result = NamedTuple('times_result', [
    ('user', float),
    ('system', float),
    ('children_user', float),
    ('children_system', float),
    ('elapsed', float),
])

waitid_result = NamedTuple('waitid_result', [
    ('si_pid', int),
    ('si_uid', int),
    ('si_signo', int),
    ('si_status', int),
    ('si_code', int),
])

sched_param = NamedTuple('sched_priority', [
    ('sched_priority', int),
])


EX_CANTCREAT: int
EX_CONFIG: int
EX_DATAERR: int
EX_IOERR: int
EX_NOHOST: int
EX_NOINPUT: int
EX_NOPERM: int
EX_NOTFOUND: int
EX_NOUSER: int
EX_OK: int
EX_OSERR: int
EX_OSFILE: int
EX_PROTOCOL: int
EX_SOFTWARE: int
EX_TEMPFAIL: int
EX_UNAVAILABLE: int
EX_USAGE: int

F_OK: int
R_OK: int
W_OK: int
X_OK: int

if sys.version_info >= (3, 6):
    GRND_NONBLOCK: int
    GRND_RANDOM: int
NGROUPS_MAX: int

O_APPEND: int
if sys.version_info >= (3, 4):
    O_ACCMODE: int
O_ASYNC: int
O_CREAT: int
O_DIRECT: int
O_DIRECTORY: int
O_DSYNC: int
O_EXCL: int
O_LARGEFILE: int
O_NDELAY: int
O_NOATIME: int
O_NOCTTY: int
O_NOFOLLOW: int
O_NONBLOCK: int
O_RDONLY: int
O_RDWR: int
O_RSYNC: int
O_SYNC: int
O_TRUNC: int
O_WRONLY: int

ST_APPEND: int
ST_MANDLOCK: int
ST_NOATIME: int
ST_NODEV: int
ST_NODIRATIME: int
ST_NOEXEC: int
ST_NOSUID: int
ST_RDONLY: int
ST_RELATIME: int
ST_SYNCHRONOUS: int
ST_WRITE: int

TMP_MAX: int
WCONTINUED: int
WCOREDUMP: int
WEXITSTATUS: int
WIFCONTINUED: int
WIFEXITED: int
WIFSIGNALED: int
WIFSTOPPED: int
WNOHANG: int
WSTOPSIG: int
WTERMSIG: int
WUNTRACED: int
