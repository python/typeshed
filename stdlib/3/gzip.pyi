from typing import Any, Optional
import _compression

def open(filename, mode: str = ..., compresslevel: int = ..., encoding=None, errors=None, newline=None): ...

class _PaddedFile:
    file = ...  # type: Any
    def __init__(self, f, prepend: bytes = ...) -> None : ...
    def read(self, size): ...
    def prepend(self, prepend: bytes = ...): ...
    def seek(self, off): ...
    def seekable(self): ...

class GzipFile(_compression.BaseStream):
    myfileobj = ...  # type: Any
    mode = ...  # type: Any
    name = ...  # type: Any
    compress = ...  # type: Any
    fileobj = ...  # type: Any
    def __init__(self, filename=None, mode=None, compresslevel: int = ..., fileobj=None, mtime=None) -> None: ...
    @property
    def filename(self): ...
    @property
    def mtime(self): ...
    crc = ...  # type: Any
    def write(self, data): ...
    def read(self, size: Optional[int] = ...): ...
    def read1(self, size: int = ...): ...
    def peek(self, n): ...
    @property
    def closed(self): ...
    def close(self): ...
    def flush(self, zlib_mode=...): ...
    def fileno(self): ...
    def rewind(self): ...
    def readable(self): ...
    def writable(self): ...
    def seekable(self): ...
    def seek(self, offset, whence=...): ...
    def readline(self, size: int = ...): ...

class _GzipReader(_compression.DecompressReader):
    def __init__(self, fp) -> None: ...
    def read(self, size: int = ...): ...

def compress(data, compresslevel: int = ...): ...
def decompress(data): ...
