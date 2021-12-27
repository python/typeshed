import datetime
import logging.handlers
import subprocess
import sys
import time
from typing import IO, Any, Callable, ContextManager, Iterable, Mapping, Sequence, Type, TypeVar

import boto.connection

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

if sys.version_info >= (3,):
    # TODO move _StringIO definition into boto.compat once stubs exist and rename to StringIO
    import io

    _StringIO = io.StringIO

    from hashlib import _Hash

    _HashType = _Hash

    from email.message import Message as _Message
else:
    # TODO move _StringIO definition into boto.compat once stubs exist and rename to StringIO
    import StringIO

    _StringIO = StringIO.StringIO[Any]

    from hashlib import _hash

    _HashType = _hash

    # TODO use email.message.Message once stubs exist
    _Message = Any

_Provider = Any  # TODO replace this with boto.provider.Provider once stubs exist
_LockType = Any  # TODO replace this with _thread.LockType once stubs exist

JSONDecodeError: Type[ValueError]
qsa_of_interest: list[str]

def unquote_v(nv: str) -> str | tuple[str, str]: ...
def canonical_string(
    method: str, path: str, headers: Mapping[str, str | None], expires: int | None = ..., provider: _Provider | None = ...
) -> str: ...
def merge_meta(
    headers: Mapping[str, str], metadata: Mapping[str, str], provider: _Provider | None = ...
) -> Mapping[str, str]: ...
def get_aws_metadata(headers: Mapping[str, str], provider: _Provider | None = ...) -> Mapping[str, str]: ...
def retry_url(url: str, retry_on_404: bool = ..., num_retries: int = ..., timeout: int | None = ...) -> str: ...

class LazyLoadMetadata(dict[_KT, _VT]):
    def __init__(self, url: str, num_retries: int, timeout: int | None = ...) -> None: ...

def get_instance_metadata(
    version: str = ..., url: str = ..., data: str = ..., timeout: int | None = ..., num_retries: int = ...
) -> LazyLoadMetadata[Any, Any] | None: ...
def get_instance_identity(
    version: str = ..., url: str = ..., timeout: int | None = ..., num_retries: int = ...
) -> Mapping[str, Any] | None: ...
def get_instance_userdata(
    version: str = ..., sep: str | None = ..., url: str = ..., timeout: int | None = ..., num_retries: int = ...
) -> Mapping[str, str]: ...

ISO8601: str
ISO8601_MS: str
RFC1123: str
LOCALE_LOCK: _LockType

def setlocale(name: str | tuple[str, str]) -> ContextManager[str]: ...
def get_ts(ts: time.struct_time | None = ...) -> str: ...
def parse_ts(ts: str) -> datetime.datetime: ...
def find_class(module_name: str, class_name: str | None = ...) -> Type[Any] | None: ...
def update_dme(username: str, password: str, dme_id: str, ip_address: str) -> str: ...
def fetch_file(
    uri: str, file: IO[str] | None = ..., username: str | None = ..., password: str | None = ...
) -> IO[str] | None: ...

class ShellCommand:
    exit_code: int
    command: subprocess._CMD
    log_fp: _StringIO
    wait: bool
    fail_fast: bool
    def __init__(
        self, command: subprocess._CMD, wait: bool = ..., fail_fast: bool = ..., cwd: subprocess._TXT | None = ...
    ) -> None: ...
    process: subprocess.Popen[Any]
    def run(self, cwd: subprocess._CMD | None = ...) -> int | None: ...
    def setReadOnly(self, value) -> None: ...
    def getStatus(self) -> int | None: ...
    status: int | None
    def getOutput(self) -> str: ...
    output: str

class AuthSMTPHandler(logging.handlers.SMTPHandler):
    username: str
    password: str
    def __init__(
        self, mailhost: str, username: str, password: str, fromaddr: str, toaddrs: Sequence[str], subject: str
    ) -> None: ...

class LRUCache(dict[_KT, _VT]):
    class _Item:
        previous: LRUCache._Item | None
        next: LRUCache._Item | None
        key = ...
        value = ...
        def __init__(self, key, value) -> None: ...
    _dict: dict[_KT, LRUCache._Item]
    capacity: int
    head: LRUCache._Item | None
    tail: LRUCache._Item | None
    def __init__(self, capacity: int) -> None: ...

# This exists to work around Password.str's name shadowing the str type
_str = str

class Password:
    hashfunc: Callable[[bytes], _HashType]
    str: _str | None
    def __init__(self, str: _str | None = ..., hashfunc: Callable[[bytes], _HashType] | None = ...) -> None: ...
    def set(self, value: bytes | _str) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __len__(self) -> int: ...

def notify(
    subject: str,
    body: str | None = ...,
    html_body: Sequence[str] | str | None = ...,
    to_string: str | None = ...,
    attachments: Iterable[_Message] | None = ...,
    append_instance_id: bool = ...,
) -> None: ...
def get_utf8_value(value: str) -> bytes: ...
def mklist(value: Any) -> list[Any]: ...
def pythonize_name(name: str) -> str: ...
def write_mime_multipart(
    content: list[tuple[str, str]], compress: bool = ..., deftype: str = ..., delimiter: str = ...
) -> str: ...
def guess_mime_type(content: str, deftype: str) -> str: ...
def compute_md5(fp: IO[Any], buf_size: int = ..., size: int | None = ...) -> tuple[str, str, int]: ...
def compute_hash(fp: IO[Any], buf_size: int = ..., size: int | None = ..., hash_algorithm: Any = ...) -> tuple[str, str, int]: ...
def find_matching_headers(name: str, headers: Mapping[str, str | None]) -> list[str]: ...
def merge_headers_by_name(name: str, headers: Mapping[str, str | None]) -> str: ...

class RequestHook:
    def handle_request_data(
        self, request: boto.connection.HTTPRequest, response: boto.connection.HTTPResponse, error: bool = ...
    ) -> Any: ...

def host_is_ipv6(hostname: str) -> bool: ...
def parse_host(hostname: str) -> str: ...
