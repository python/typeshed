# created from https://docs.python.org/2/library/os.html

from typing import (
    List, Tuple, Union, Sequence, Mapping, IO, Any, Optional, AnyStr, Iterator,
    MutableMapping, NamedTuple
)
import posixpath as path

error = OSError
name = ... # type: str

class _Environ(MutableMapping[str, str]):
    def copy(self) -> Dict[str, str]: ...

environ = ... # type: _Environ

def chdir(path: unicode) -> None: ...
def fchdir(fd: int) -> None: ...
def getcwd() -> str: ...
def ctermid() -> str: ...
def getegid() -> int: ...
def geteuid() -> int: ...
def getgid() -> int: ...
def getgroups() -> List[int]: ...
def initgroups(username: str, gid: int) -> None: ...
def getlogin() -> str: ...
def getpgid(pid: int) -> int: ...
def getpgrp() -> int: ...
def getpid() -> int: ...
def getppid() -> int: ...
def getresuid() -> Tuple[int, int, int]: ...
def getresgid() -> Tuple[int, int, int]: ...
def getuid() -> int: ...
def getenv(varname: unicode, value: unicode = ...) -> str: ...
def putenv(varname: unicode, value: unicode) -> None: ...
def setegid(egid: int) -> None: ...
def seteuid(euid: int) -> None: ...
def setgid(gid: int) -> None: ...
def setgroups(groups: Sequence[int]) -> None: ...

# TODO(MichalPokorny)
def setpgrp(*args) -> None: ...

def setpgid(pid: int, pgrp: int) -> None: ...
def setregid(rgid: int, egid: int) -> None: ...
def setresgid(rgid: int, egid: int, sgid: int) -> None: ...
def setresuid(ruid: int, euid: int, suid: int) -> None: ...
def setreuid(ruid: int, euid: int) -> None: ...
def getsid(pid: int) -> int: ...
def setsid() -> None: ...
def setuid(pid: int) -> None: ...

def strerror(code: int) -> str:
    raise ValueError()

def umask(mask: int) -> int: ...
def uname() -> Tuple[str, str, str, str, str]: ...
def unsetenv(varname: str) -> None: ...

# TODO(MichalPokorny)
def fdopen(fd: int, *args, **kwargs) -> IO[Any]: ...
def popen(command: str, *args, **kwargs) -> Optional[IO[Any]]: ...
def tmpfile() -> IO[Any]: ...

def popen2(cmd: str, *args, **kwargs) -> Tuple[IO[Any], IO[Any]]: ...
def popen3(cmd: str, *args, **kwargs) -> Tuple[IO[Any], IO[Any], IO[Any]]: ...
def popen4(cmd: str, *args, **kwargs) -> Tuple[IO[Any], IO[Any]]: ...

def close(fd: int) -> None: ...
def closerange(fd_low: int, fd_high: int) -> None: ...
def dup(fd: int) -> int: ...
def dup2(fd: int, fd2: int) -> None: ...
def fchmod(fd: int, mode: int) -> None: ...
def fchown(fd: int, uid: int, gid: int) -> None: ...
def fdatasync(fd: int) -> None: ...
def fpathconf(fd: int, name: str) -> None: ...

# TODO(prvak)
def fstat(fd: int) -> Any: ...
def fsync(fd: int) -> None: ...
def ftruncate(fd: int, length: int) -> None: ...
def isatty(fd: int) -> bool: ...

def lseek(fd: int, pos: int, how: int) -> None: ...
SEEK_SET = 0
SEEK_CUR = 0
SEEK_END = 0

# TODO(prvak): maybe file should be unicode? (same with all other paths...)
def open(file: unicode, flags: int, mode: int = ...) -> int: ...
def openpty() -> Tuple[int, int]: ...
def pipe() -> Tuple[int, int]: ...
def read(fd: int, n: int) -> str: ...
def tcgetpgrp(fd: int) -> int: ...
def tcsetpgrp(fd: int, pg: int) -> None: ...
def ttyname(fd: int) -> str: ...
def write(fd: int, str: str) -> int: ...

# TODO: O_*

def access(path: unicode, mode: int) -> bool: ...
F_OK = 0
R_OK = 0
W_OK = 0
X_OK = 0

def getcwdu() -> unicode: ...
def chflags(path: unicode, flags: int) -> None: ...
def chroot(path: unicode) -> None: ...
def chmod(path: unicode, mode: int) -> None: ...
def chown(path: unicode, uid: int, gid: int) -> None: ...
def lchflags(path: unicode, flags: int) -> None: ...
def lchmod(path: unicode, uid: int, gid: int) -> None: ...
def lchown(path: unicode, uid: int, gid: int) -> None: ...
def link(source: unicode, link_name: unicode) -> None: ...
def listdir(path: AnyStr) -> List[AnyStr]: ...

# TODO(MichalPokorny)
def lstat(path: unicode) -> Any: ...

def mkfifo(path: unicode, mode: int = ...) -> None: ...
def mknod(filename: unicode, mode: int = ..., device: int = ...) -> None: ...
def major(device: int) -> int: ...
def minor(device: int) -> int: ...
def makedev(major: int, minor: int) -> int: ...
def mkdir(path: unicode, mode: int = ...) -> None: ...
def makedirs(path: unicode, mode: int = ...) -> None: ...
def pathconf(path: unicode, name: str) -> str: ...

pathconf_names = ... # type: Mapping[str, int]

def readlink(path: AnyStr) -> AnyStr: ...
def remove(path: unicode) -> None: ...
def removedirs(path: unicode) -> None:
    raise OSError()
def rename(src: unicode, dst: unicode) -> None: ...
def renames(old: unicode, new: unicode) -> None: ...
def rmdir(path: unicode) -> None: ...

# TODO(MichalPokorny)
def stat(path: unicode) -> Any: ...

_StatVFS = NamedTuple('_StatVFS', [('f_bsize', int), ('f_frsize', int), ('f_blocks', int),
                                   ('f_bfree', int), ('f_bavail', int), ('f_files', int),
                                   ('f_ffree', int), ('f_favail', int), ('f_flag', int),
                                   ('f_namemax', int)])

def fstatvfs(fd: int) -> _StatVFS: ...
def statvfs(path: unicode) -> _StatVFS: ...

# TODO: stat_float_times, tempnam, tmpnam, TMP_MAX
def walk(top: AnyStr, topdown: bool = ..., onerror: Any = ...,
         followlinks: bool = ...) -> Iterator[Tuple[AnyStr, List[AnyStr],
                                                    List[AnyStr]]]: ...

def symlink(source: unicode, link_name: unicode) -> None: ...
def unlink(path: unicode) -> None: ...
def utime(path: unicode, times: Optional[Tuple[int, int]]) -> None: ...

def abort() -> None: ...

EX_OK = 0        # Unix only
EX_USAGE = 0     # Unix only
EX_DATAERR = 0   # Unix only
EX_NOINPUT = 0   # Unix only
EX_NOUSER = 0    # Unix only
EX_NOHOST = 0    # Unix only
EX_UNAVAILABLE = 0  # Unix only
EX_SOFTWARE = 0  # Unix only
EX_OSERR = 0     # Unix only
EX_OSFILE = 0    # Unix only
EX_CANTCREAT = 0 # Unix only
EX_IOERR = 0     # Unix only
EX_TEMPFAIL = 0  # Unix only
EX_PROTOCOL = 0  # Unix only
EX_NOPERM = 0    # Unix only
EX_CONFIG = 0    # Unix only

def execl(file: AnyStr, *args) -> None: ...
def execle(file: AnyStr, *args) -> None: ...
def execlp(file: AnyStr, *args) -> None: ...
def execlpe(file: AnyStr, *args) -> None: ...
def execvp(file: AnyStr, args: Union[Tuple[AnyStr], List[AnyStr]]) -> None: ...
def execvpe(file: AnyStr, args: Union[Tuple[AnyStr], List[AnyStr]], env: Mapping[AnyStr, AnyStr]) -> None: ...
def execv(path: AnyStr, args: Union[Tuple[AnyStr], List[AnyStr]]) -> None: ...
def execve(path: AnyStr, args: Union[Tuple[AnyStr], List[AnyStr]], env: Mapping[AnyStr, AnyStr]) -> None: ...

def _exit(n: int) -> None: ...

def fork() -> int:
    raise OSError()

def forkpty() -> Tuple[int, int]:
    raise OSError()

def kill(pid: int, sig: int) -> None: ...
def killpg(pgid: int, sig: int) -> None: ...
def nice(increment: int) -> int: ...

# TODO: plock, popen*, P_*

def spawnl(mode: int, path: AnyStr, arg0: AnyStr, *args: AnyStr) -> int: ...
def spawnle(mode: int, path: AnyStr, arg0: AnyStr,
            *args: Any) -> int: ... # Imprecise sig
def spawnlp(mode: int, file: AnyStr, arg0: AnyStr,
            *args: AnyStr) -> int: ...  # Unix only TODO
def spawnlpe(mode: int, file: AnyStr, arg0: AnyStr, *args: Any) -> int:
    ... # Imprecise signature; Unix only TODO
def spawnv(mode: int, path: AnyStr, args: List[AnyStr]) -> int: ...
def spawnve(mode: int, path: AnyStr, args: List[AnyStr],
            env: Mapping[str, str]) -> int: ...
def spawnvp(mode: int, file: AnyStr, args: List[AnyStr]) -> int: ...  # Unix only
def spawnvpe(mode: int, file: AnyStr, args: List[AnyStr],
             env: Mapping[str, str]) -> int:
    ...  # Unix only
def startfile(path: unicode, operation: str = ...) -> None: ... # Windows only
def system(command: unicode) -> int: ...
def times() -> Tuple[float, float, float, float, float]: ...
def wait() -> Tuple[int, int]: ... # Unix only
def waitpid(pid: int, options: int) -> Tuple[int, int]:
    raise OSError()
# TODO: wait3, wait4, W...
def confstr(name: Union[str, int]) -> Optional[str]: ...
confstr_names = ... # type: Mapping[str, int]

def getloadavg() -> Tuple[float, float, float]:
    raise OSError()

def sysconf(name: Union[str, int]) -> int: ...
sysconf_names = ... # type: Mapping[str, int]

curdir = ... # type: str
pardir = ... # type: str
sep = ... # type: str
altsep = ... # type: str
extsep = ... # type: str
pathsep = ... # type: str
defpath = ... # type: str
linesep = ... # type: str
devnull = ... # type: str

def urandom(n: int) -> str: ...

# More constants, copied from stdlib/3/os/__init__.pyi

O_RDONLY = 0
O_WRONLY = 0
O_RDWR = 0
O_APPEND = 0
O_CREAT = 0
O_EXCL = 0
O_TRUNC = 0
O_DSYNC = 0    # Unix only
O_RSYNC = 0    # Unix only
O_SYNC = 0     # Unix only
O_NDELAY = 0   # Unix only
O_NONBLOCK = 0 # Unix only
O_NOCTTY = 0   # Unix only
O_SHLOCK = 0   # Unix only
O_EXLOCK = 0   # Unix only
O_BINARY = 0     # Windows only
O_NOINHERIT = 0  # Windows only
O_SHORT_LIVED = 0# Windows only
O_TEMPORARY = 0  # Windows only
O_RANDOM = 0     # Windows only
O_SEQUENTIAL = 0 # Windows only
O_TEXT = 0       # Windows only
O_ASYNC = 0      # Gnu extension if in C library
O_DIRECT = 0     # Gnu extension if in C library
O_DIRECTORY = 0  # Gnu extension if in C library
O_NOFOLLOW = 0   # Gnu extension if in C library
O_NOATIME = 0    # Gnu extension if in C library

P_NOWAIT = 0
P_NOWAITO = 0
P_WAIT = 0
#P_DETACH = 0  # Windows only
#P_OVERLAY = 0  # Windows only

# wait()/waitpid() options
WNOHANG = 0  # Unix only
#WCONTINUED = 0  # some Unix systems
#WUNTRACED = 0  # Unix only

P_ALL = 0
WEXITED = 0
WNOWAIT = 0
