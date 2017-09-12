import datetime
import logging
import logging.handlers
import subprocess
import time

import boto.connection
from typing import (
    _KT,
    _VT,
    Any,
    Callable,
    Dict,
    IO,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

_Provider = Any  # TODO replace this with boto.provider.Provider once stubs exist
_LockType = Any  # TODO replace this with _thread.LockType once stubs exist

JSONDecodeError = ...  # type: Type[ValueError]
qsa_of_interest = ...  # type: List[str]


def unquote_v(nv: str) -> Union[str, Tuple[str, str]]: ...
def canonical_string(
    method: str,
    path: str,
    headers: Dict[str, str],
    expires: Optional[int] = ...,
    provider: Optional[_Provider] = ...,
): ...
def merge_meta(
    headers: Dict[str, str],
    metadata: Dict[str, str],
    provider: Optional[_Provider] = ...,
): ...
def get_aws_metadata(headers: Dict[str, str], provider: Optional[_Provider] = ...): ...
def retry_url(
    url: str,
    retry_on_404: bool = ...,
    num_retries: int = ...,
    timeout: Optional[int] = ...,
): ...

class LazyLoadMetadata(Dict[_KT, _VT]):
    def __init__(
        self,
        url: str,
        num_retries: int,
        timeout: Optional[int] = ...,
    ) -> None: ...
    def get(self, key: _KT, default: Optional[Any] = ...) -> Any: ...

def get_instance_metadata(
    version: str = ...,
    url: str = ...,
    data: str = ...,
    timeout: Optional[int] = ...,
    num_retries: int = ...,
) -> Optional[LazyLoadMetadata]: ...
def get_instance_identity(
    version: str = ...,
    url: str = ...,
    timeout: Optional[int] = ...,
    num_retries: int = ...,
) -> Optional[Dict[str, Any]]: ...
def get_instance_userdata(
    version: str = ...,
    sep: Optional[str] = ...,
    url: str = ...,
    timeout: Optional[int] = ...,
    num_retries: int = ...,
) -> Dict[str, str]: ...

ISO8601 = ...  # type: str
ISO8601_MS = ...  # type: str
RFC1123 = ...  # type: str
LOCALE_LOCK = ...  # type: _LockType

def setlocale(name: Union[str, Tuple[str, str]]): ...
def get_ts(ts: Optional[time.struct_time] = ...) -> str: ...
def parse_ts(ts: str) -> datetime.datetime: ...
def find_class(module_name: str, class_name: Optional[str] = ...) -> Optional[Type[Any]]: ...
def update_dme(username: str, password: str, dme_id: str, ip_address: str) -> str: ...
def fetch_file(
    uri: str,
    file: Optional[IO] = ...,
    username: Optional[str] = ...,
    password: Optional[str] = ...,
) -> IO: ...

class ShellCommand:
    exit_code = ...  # type: int
    command = ...  # type: subprocess._CMD
    log_fp = ...  # type: IO
    wait = ...  # type: bool
    fail_fast = ...  # type: bool

    def __init__(
        self,
        command: subprocess._CMD,
        wait: bool = ...,
        fail_fast: bool = ...,
        cwd: Optional[subprocess._TXT] = ...,
    ) -> None: ...

    process = ...  # type: subprocess.Popen

    def run(self, cwd: Optional[subprocess._CMD] = ...) -> Optional[int]: ...
    def setReadOnly(self, value) -> None: ...
    def getStatus(self) -> Optional[int]: ...

    status = ...  # type: Optional[int]

    def getOutput(self) -> str: ...

    output = ...  # type: str

class AuthSMTPHandler(logging.handlers.SMTPHandler):
    username = ...  # type: str
    password = ...  # type: str
    def __init__(
        self,
        mailhost: str,
        username: str,
        password: str,
        fromaddr: str,
        toaddrs: Sequence[str],
        subject: str,
    ) -> None: ...
    def emit(self, record: logging.LogRecord) -> None: ...

class LRUCache(Dict[_KT, _VT]):
    class _Item:
        previous = ...  # type: Optional[LRUCache._Item]
        key = ...  # type: _KT
        value = ...  # type: _VT
        def __init__(self, key: _KT, value: _VT) -> None: ...

    capacity = ...  # type: int
    head = ...  # type: Optional[LRUCache._Item]
    tail = ...  # type: Optional[LRUCache._Item]

    def __init__(self, capacity: int) -> None: ...


# This exists to work around Password.str's name shadowing the str type
_str = str

class Password:
    hashfunc = ...  # type: Callable
    str = ...  # type: Optional[_str]

    def __init__(
        self,
        str: Optional[_str] = ...,
        hashfunc: Optional[Callable] = ...,
    ) -> None: ...
    def set(self, value: Union[bytes, _str]): ...
    def __eq__(self, other: Any) -> bool: ...
    def __len__(self) -> bool: ...

def notify(
    subject: str,
    body: Optional[str] = ...,
    html_body: Optional[Union[Sequence[str], str]] = ...,
    to_string: Optional[str] = ...,
    attachments: Optional[Iterable] = ...,
    append_instance_id: bool = ...,
): ...
def get_utf8_value(value: str) -> str: ...
def mklist(value: Any) -> List: ...
def pythonize_name(name: str) -> str: ...
def write_mime_multipart(
    content: List[Tuple[str, str]],
    compress: bool = ...,
    deftype: str = ...,
    delimiter: str = ...,
): ...
def guess_mime_type(content: str, deftype: str) -> str: ...
def compute_md5(
    fp: IO,
    buf_size: int = ...,
    size: Optional[int] = ...,
) -> Tuple[str, str, int]: ...
def compute_hash(
    fp: IO,
    buf_size: int = ...,
    size: Optional[int] = ...,
    hash_algorithm: Any = ...,
) -> Tuple[str, str, int]: ...
def find_matching_headers(name: str, headers: Dict[str, str]) -> List[str]: ...
def merge_headers_by_name(name: str, headers: Dict[str, str]) -> str: ...

class RequestHook:
    def handle_request_data(
        self,
        request: boto.connection.HTTPRequest,
        response: boto.connection.HTTPResponse,
        error: bool = ...,
    ): ...

def host_is_ipv6(hostname: str) -> bool: ...
def parse_host(hostname: str) -> str: ...
