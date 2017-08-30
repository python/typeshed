import logging
import logging.handlers
import datetime
import subprocess
import thread
import time

import boto.provider
import boto.connection
import six
from typing import Any, List, Hashable, Optional, Text, Union, Tuple


JSONDecodeError = ...  # type: Exception
qsa_of_interest = ...  # type: List[Text]

def unquote_v(nv: Text) -> Union[Text, Tuple[Text, Text]]: ...
def canonical_string(
    method: Text,
    path: Text,
    headers: Dict[Text, Text],
    expires: Optional[int] = ...,
    provider: Optional[boto.provider.Provider] = ...,
): ...
def merge_meta(
    headers: Dict[Text, Text],
    metadata: Dict[Text, Text],
    provider: Optional[boto.provider.Provider] = ...,
): ...
def get_aws_metadata(headers: Dict[Text, Text], provider: Optional[boto.provider.Provider] = ...): ...
def retry_url(
    url: Text,
    retry_on_404: bool = ...,
    num_retries: int = ...,
    timeout: Optional[int] = ...,
): ...

class LazyLoadMetadata(dict):
    def __init__(
        self,
        url: Text,
        num_retries: int,
        timeout: Optional[int] = ...,
    ) -> None: ...
    def __getitem__(self, key: Hashable): ...
    def get(self, key: Hashable, default: Optional[Any] = ...) -> Any: ...
    def values(self) -> List[Any]: ...
    def items(self) -> List[Tuple[Any, Any]]: ...

def get_instance_metadata(
    version: Text = ...,
    url: Text = ...,
    data: Text = ...,
    timeout: Optional[int] = ...,
    num_retries: int = ...
) -> Optional[LazyLoadMetadata]: ...
def get_instance_identity(
    version: Text = ...,
    url: Text = ...,
    timeout: Optional[int] = ...,
    num_retries: int = ...,
) -> Optional[Dict[Text, Any]]: ...
def get_instance_userdata(
    version: Text = ...,
    sep: Optional[Text] = ...,
    url: Text = ...,
    timeout: Optional[int] = ...,
    num_retries: int = ...,
) -> Dict[Text, Text]: ...

ISO8601 = ...  # type: Text
ISO8601_MS = ...  # type: Text
RFC1123 = ...  # type: Text
LOCALE_LOCK = ...  # type: therad.LockType

def setlocale(name: Union[Text, Tuple[Text, Text]]): ...
def get_ts(ts: Optional[time.struct_time] = ...) -> Text: ...
def parse_ts(ts: Text) -> datetime.datetime: ...
def find_class(module_name: Text, class_name: Optional[Text] = ...) -> Optional[Any]: ...
def update_dme(username: Text, password: Text, dme_id: Text, ip_address: Text) -> Text: ...
def fetch_file(
    uri: Text,
    file: Optional[file] = ...,
    username: Optional[Text] = ...,
    password: Optional[Text] = ...,
) -> file: ...

class ShellCommand:
    exit_code = ...  # type: int
    command = ...  # type: subprocess._CMD
    log_fp = ...  # type: six.StringIO
    wait = ...  # type: bool
    fail_fast = ...  # type: bool

    def __init__(
        self,
        command: subprocess._CMD,
        wait: bool = ...,
        fail_fast: bool = ...,
        cwd: Optional[subprocess._TXT] = ...,
    ) -> None: ....

    process = ...  # type: subprocess.Popen

    def run(self, cwd: Optional[subprocess._CMD] = ...) -> Optional[int]: ...
    def setReadOnly(self, value) -> None: ...
    def getStatus(self) -> Optional[int]: ...

    status = ...  # type: Any

    def getOutput(self) -> Text: ...

    output = ...  # type: Any

class AuthSMTPHandler(logging.handlers.SMTPHandler):
    username = ...  # type: Text
    password = ...  # type: Text
    def __init__(
        self,
        mailhost: Text,
        username: Text,
        password: Text,
        fromaddr: Text,
        toaddrs: Sequence[Text],
        subject: Text,
    ) -> None: ...
    def emit(self, record: logging.Record) -> None: ...

class LRUCache(dict):
    class _Item:
        previous = ...  # type: Optional[_Item]
        key = ...  # type: Hashable
        value = ...  # type: Any
        def __init__(self, key, value) -> None: ...

    capacity = ...  # type: int
    head = ...  # type: Optional[_Item]
    tail = ...  # type: Optional[_Item]

    def __init__(self, capacity: int) -> None: ...
    def __contains__(self, key: Hashable) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: Hashable) -> Any: ...
    def __setitem__(self, key: Hashable, value: Any): ...

class Password:
    hashfunc = ...  # type: Callable
    str = ...  # type: Optional[Text]

    def __init__(
        self,
        str: Optional[Text] = ...,
        hashfunc: Optional[Callable] = ...,
    ) -> None: ...
    def set(self, value: Optional[bytes, Text]): ...
    def __eq__(self, other: Any) -> bool: ...
    def __len__(self) -> bool: ...

def notify(
    subject: Text,
    body: Optional[Text] = ...,
    html_body: Optional[Union[Sequence[Text], Text]] = ...,
    to_string: Optional[Text] = ...,
    attachments: Optional[Iterable] = ...,
    append_instance_id: bool = ...,
): ...
def get_utf8_value(value: Text) -> Text: ...
def mklist(value: Any) -> List: ...
def pythonize_name(name: Text) -> Text: ...
def write_mime_multipart(
    content: List[Tuple[Text, Text]],
    compress: bool = ...,
    deftype: Text = ...,
    delimiter: Text = ...,
): ...
def guess_mime_type(content: Text, deftype: Text) -> Text: ...
def compute_md5(
    fp: file,
    buf_size: int = ...,
    size: Optional[int] = ...,
) -> Tuple[Text, Text, int]: ...
def compute_hash(
    fp: file,
    buf_size: int = ...,
    size: Optional[int] = ...,
    hash_algorithm: Any = ...,
) -> Tuple[Text, Text, int]: ...
def find_matching_headers(name: Text, headers: Dict[Text, Text]) -> List[Text]: ...
def merge_headers_by_name(name: Text, headers: Dict[Text, Text]) -> Text: ...

class RequestHook:
    def handle_request_data(
        self,
        request: boto.connection.HTTPRequest,
        response: boto.connection.HTTPResponse,
        error: bool = ...,
    ): ...

def host_is_ipv6(hostname: Text) -> bool: ...
def parse_host(hostname: Text) -> Text: ...
