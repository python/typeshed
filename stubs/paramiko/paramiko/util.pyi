from _typeshed import ReadableBuffer
from collections.abc import Iterable
from hashlib import _Hash
from logging import Logger, LogRecord
from types import TracebackType
from typing import IO, AnyStr, Protocol
from typing_extensions import Self

from paramiko.config import SSHConfig, SSHConfigDict
from paramiko.hostkeys import HostKeys

class SupportsClose(Protocol):
    def close(self) -> None: ...

def inflate_long(s: bytes | bytearray, always_positive: bool = False) -> int: ...
def deflate_long(n: int, add_sign_padding: bool = True) -> bytes: ...
def format_binary(data: bytes | bytearray, prefix: str = "") -> list[str]: ...
def format_binary_line(data: bytes | bytearray) -> str: ...
def safe_string(s: Iterable[int | str]) -> bytes: ...
def bit_length(n: int) -> int: ...
def tb_strings() -> list[str]: ...
def generate_key_bytes(hash_alg: type[_Hash], salt: ReadableBuffer, key: bytes | str, nbytes: int) -> bytes: ...
def load_host_keys(filename: str) -> HostKeys: ...
def parse_ssh_config(file_obj: IO[str]) -> SSHConfig: ...
def lookup_ssh_host_config(hostname: str, config: SSHConfig) -> SSHConfigDict: ...
def mod_inverse(x: int, m: int) -> int: ...
def get_thread_id() -> int: ...
def log_to_file(filename: str, level: int = 10) -> None: ...

class PFilter:
    def filter(self, record: LogRecord) -> bool: ...

def get_logger(name: str) -> Logger: ...
def constant_time_bytes_eq(a: AnyStr, b: AnyStr) -> bool: ...

class ClosingContextManager:
    def __enter__(self) -> Self: ...
    def __exit__(
        self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...

def clamp_value(minimum: int, val: int, maximum: int) -> int: ...

# This function attempts to convert objects to bytes,
# *but* just returns the object unchanged if that was unsuccessful!
def asbytes(s: object) -> object: ...
def b(s: str | bytes, encoding: str = "utf8") -> bytes: ...
def u(s: str | bytes, encoding: str = "utf8") -> str: ...
