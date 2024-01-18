from _typeshed import Incomplete
from re import Pattern
from typing import AnyStr, Protocol

PY3: bool
text_type: type

class _NullCoder:
    @staticmethod
    def encode(b: str, final: bool = False): ...
    @staticmethod
    def decode(b: str, final: bool = False): ...

class _Logfile(Protocol):
    def write(self, __s) -> object: ...
    def flush(self) -> object: ...

class SpawnBase:
    encoding: Incomplete
    pid: Incomplete
    flag_eof: bool
    stdin: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    searcher: Incomplete
    ignorecase: bool
    before: Incomplete
    after: Incomplete
    match: Incomplete
    match_index: Incomplete
    terminated: bool
    exitstatus: Incomplete
    signalstatus: Incomplete
    status: Incomplete
    child_fd: int
    timeout: float | None
    delimiter: Incomplete
    logfile: _Logfile
    logfile_read: _Logfile
    logfile_send: _Logfile
    maxread: Incomplete
    searchwindowsize: int | None
    delaybeforesend: float | None
    delayafterclose: float
    delayafterterminate: float
    delayafterread: float
    softspace: bool
    name: Incomplete
    closed: bool
    codec_errors: Incomplete
    string_type: Incomplete
    buffer_type: Incomplete
    crlf: bytes
    allowed_string_types: Incomplete
    linesep: Incomplete
    write_to_stdout: Incomplete
    async_pw_transport: Incomplete
    def __init__(
        self,
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _Logfile | None = None,
        encoding: str | None = None,
        codec_errors: str = "strict",
    ) -> None: ...
    buffer: Incomplete
    def read_nonblocking(self, size: int = 1, timeout: float | None = None) -> bytes: ...
    def compile_pattern_list(self, patterns) -> list[Pattern[AnyStr]]: ...
    def expect(self, pattern, timeout: float | None = -1, searchwindowsize: int | None = -1, async_: bool = False, **kw) -> int: ...
    def expect_list(self, pattern_list, timeout: float | None = -1, searchwindowsize: int | None = -1, async_: bool = False, **kw) -> int: ...
    def expect_exact(self, pattern_list, timeout: float | None = -1, searchwindowsize: int | None = -1, async_: bool = False, **kw) -> int: ...
    def expect_loop(self, searcher, timeout: float | None = -1, searchwindowsize: int | None = -1) -> int: ...
    def read(self, size: int = -1) -> bytes: ...
    def readline(self, size: int = -1) -> bytes: ...
    def __iter__(self): ...
    def readlines(self, sizehint: int = -1) -> list[str]: ...
    def fileno(self): ...
    def flush(self) -> None: ...
    def isatty(self): ...
    def __enter__(self): ...
    def __exit__(self, etype, evalue, tb) -> None: ...
