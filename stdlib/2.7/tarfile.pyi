# Stubs for tarfile (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class TarError(Exception): ...
class ExtractError(TarError): ...
class ReadError(TarError): ...
class CompressionError(TarError): ...
class StreamError(TarError): ...
class HeaderError(TarError): ...
class EmptyHeaderError(HeaderError): ...
class TruncatedHeaderError(HeaderError): ...
class EOFHeaderError(HeaderError): ...
class InvalidHeaderError(HeaderError): ...
class SubsequentHeaderError(HeaderError): ...

class _LowLevelFile:
    fd = ... # type: Any
    def __init__(self, name, mode) -> None: ...
    def close(self): ...
    def read(self, size): ...
    def write(self, s): ...

class _Stream:
    name = ... # type: Any
    mode = ... # type: Any
    comptype = ... # type: Any
    fileobj = ... # type: Any
    bufsize = ... # type: Any
    buf = ... # type: Any
    pos = ... # type: Any
    closed = ... # type: Any
    zlib = ... # type: Any
    crc = ... # type: Any
    dbuf = ... # type: Any
    cmp = ... # type: Any
    def __init__(self, name, mode, comptype, fileobj, bufsize) -> None: ...
    def __del__(self): ...
    def write(self, s): ...
    def close(self): ...
    def tell(self): ...
    def seek(self, pos=...): ...
    def read(self, size=...): ...

class _StreamProxy:
    fileobj = ... # type: Any
    buf = ... # type: Any
    def __init__(self, fileobj) -> None: ...
    def read(self, size): ...
    def getcomptype(self): ...
    def close(self): ...

class _BZ2Proxy:
    blocksize = ... # type: Any
    fileobj = ... # type: Any
    mode = ... # type: Any
    name = ... # type: Any
    def __init__(self, fileobj, mode) -> None: ...
    pos = ... # type: Any
    bz2obj = ... # type: Any
    buf = ... # type: Any
    def init(self): ...
    def read(self, size): ...
    def seek(self, pos): ...
    def tell(self): ...
    def write(self, data): ...
    def close(self): ...

class _FileInFile:
    fileobj = ... # type: Any
    offset = ... # type: Any
    size = ... # type: Any
    sparse = ... # type: Any
    position = ... # type: Any
    def __init__(self, fileobj, offset, size, sparse=...) -> None: ...
    def tell(self): ...
    def seek(self, position): ...
    def read(self, size=...): ...
    def readnormal(self, size): ...
    def readsparse(self, size): ...
    def readsparsesection(self, size): ...

class ExFileObject:
    blocksize = ... # type: Any
    fileobj = ... # type: Any
    name = ... # type: Any
    mode = ... # type: Any
    closed = ... # type: Any
    size = ... # type: Any
    position = ... # type: Any
    buffer = ... # type: Any
    def __init__(self, tarfile, tarinfo) -> None: ...
    def read(self, size=...): ...
    def readline(self, size=...): ...
    def readlines(self): ...
    def tell(self): ...
    def seek(self, pos, whence=...): ...
    def close(self): ...
    def __iter__(self): ...

class TarInfo:
    name = ... # type: Any
    mode = ... # type: Any
    uid = ... # type: Any
    gid = ... # type: Any
    size = ... # type: Any
    mtime = ... # type: Any
    chksum = ... # type: Any
    type = ... # type: Any
    linkname = ... # type: Any
    uname = ... # type: Any
    gname = ... # type: Any
    devmajor = ... # type: Any
    devminor = ... # type: Any
    offset = ... # type: Any
    offset_data = ... # type: Any
    pax_headers = ... # type: Any
    def __init__(self, name=...) -> None: ...
    path = ... # type: Any
    linkpath = ... # type: Any
    def get_info(self, encoding, errors): ...
    def tobuf(self, format=..., encoding=..., errors=...): ...
    def create_ustar_header(self, info): ...
    def create_gnu_header(self, info): ...
    def create_pax_header(self, info, encoding, errors): ...
    @classmethod
    def create_pax_global_header(cls, pax_headers): ...
    @classmethod
    def frombuf(cls, buf): ...
    @classmethod
    def fromtarfile(cls, tarfile): ...
    def isreg(self): ...
    def isfile(self): ...
    def isdir(self): ...
    def issym(self): ...
    def islnk(self): ...
    def ischr(self): ...
    def isblk(self): ...
    def isfifo(self): ...
    def issparse(self): ...
    def isdev(self): ...

class TarFile:
    debug = ... # type: Any
    dereference = ... # type: Any
    ignore_zeros = ... # type: Any
    errorlevel = ... # type: Any
    format = ... # type: Any
    encoding = ... # type: Any
    errors = ... # type: Any
    tarinfo = ... # type: Any
    fileobject = ... # type: Any
    mode = ... # type: Any
    name = ... # type: Any
    fileobj = ... # type: Any
    pax_headers = ... # type: Any
    closed = ... # type: Any
    members = ... # type: Any
    offset = ... # type: Any
    inodes = ... # type: Any
    firstmember = ... # type: Any
    def __init__(self, name=..., mode=..., fileobj=..., format=..., tarinfo=..., dereference=..., ignore_zeros=..., encoding=..., errors=..., pax_headers=..., debug=..., errorlevel=...) -> None: ...
    posix = ... # type: Any
    @classmethod
    def open(cls, name=..., mode=..., fileobj=..., bufsize=..., **kwargs): ...
    @classmethod
    def taropen(cls, name, mode=..., fileobj=..., **kwargs): ...
    @classmethod
    def gzopen(cls, name, mode=..., fileobj=..., compresslevel=..., **kwargs): ...
    @classmethod
    def bz2open(cls, name, mode=..., fileobj=..., compresslevel=..., **kwargs): ...
    OPEN_METH = ... # type: Any
    def close(self): ...
    def getmember(self, name): ...
    def getmembers(self): ...
    def getnames(self): ...
    def gettarinfo(self, name=..., arcname=..., fileobj=...): ...
    def list(self, verbose=...): ...
    def add(self, name, arcname=..., recursive=..., exclude=..., filter=...): ...
    def addfile(self, tarinfo, fileobj=...): ...
    def extractall(self, path=..., members=...): ...
    def extract(self, member, path=...): ...
    def extractfile(self, member): ...
    def makedir(self, tarinfo, targetpath): ...
    def makefile(self, tarinfo, targetpath): ...
    def makeunknown(self, tarinfo, targetpath): ...
    def makefifo(self, tarinfo, targetpath): ...
    def makedev(self, tarinfo, targetpath): ...
    def makelink(self, tarinfo, targetpath): ...
    def chown(self, tarinfo, targetpath): ...
    def chmod(self, tarinfo, targetpath): ...
    def utime(self, tarinfo, targetpath): ...
    def next(self): ...
    def __iter__(self): ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback): ...

class TarIter:
    tarfile = ... # type: Any
    index = ... # type: Any
    def __init__(self, tarfile) -> None: ...
    def __iter__(self): ...
    def next(self): ...

class _section:
    offset = ... # type: Any
    size = ... # type: Any
    def __init__(self, offset, size) -> None: ...
    def __contains__(self, offset): ...

class _data(_section):
    realpos = ... # type: Any
    def __init__(self, offset, size, realpos) -> None: ...

class _hole(_section): ...

class _ringbuffer(list):
    idx = ... # type: Any
    def __init__(self) -> None: ...
    def find(self, offset): ...

class TarFileCompat:
    tarfile = ... # type: Any
    def __init__(self, file, mode=..., compression=...) -> None: ...
    def namelist(self): ...
    def infolist(self): ...
    def printdir(self): ...
    def testzip(self): ...
    def getinfo(self, name): ...
    def read(self, name): ...
    def write(self, filename, arcname=..., compress_type=...): ...
    def writestr(self, zinfo, bytes): ...
    def close(self): ...

def is_tarfile(name): ...

open = TarFile.open
