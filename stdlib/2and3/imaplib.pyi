# Stubs for imaplib (Python 2)

import imaplib
import subprocess
import sys
import time
from socket import socket as _socket
from ssl import SSLSocket
from typing import Any, Callable, Dict, IO, List, Optional, Pattern, Text, Tuple, Type, Union

CommandResults = Tuple[str, List[Any]]


class IMAP4:
    error: Type[Exception] = ...
    abort: Type[Exception] = ...
    readonly: Type[Exception] = ...
    mustquote: Pattern[Text] = ...
    debug: int = ...
    state: str = ...
    literal: Optional[Text] = ...
    tagged_commands: Dict[str, str] = ...
    untagged_responses: Dict[str, str] = ...
    continuation_response: str = ...
    is_readonly: bool = ...
    tagnum: int = ...
    tagpre: str = ...
    tagre: Pattern[Text] = ...
    welcome: bytes = ...
    capabilities: Tuple[str] = ...
    PROTOCOL_VERSION: str = ...
    def __init__(self, host: str, port: int) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...
    host: str = ...
    port: int = ...
    sock: _socket = ...
    file: Union[IO[Text], IO[bytes]] = ...
    def open(self, host: str = ..., port: int = ...) -> None: ...
    def read(self, size: int) -> bytes: ...
    def readline(self) -> bytes: ...
    def send(self, data: bytes) -> None: ...
    def shutdown(self) -> None: ...
    def socket(self) -> _socket: ...
    def recent(self) -> CommandResults: ...
    def response(self, code: str) -> CommandResults: ...
    def append(self, mailbox: str, flags: str, date_time: str, message: str) -> str: ...
    def authenticate(self, mechanism: str, authobject: Callable[[bytes], Optional[bytes]]) -> Tuple[str, str]: ...
    def capability(self) -> CommandResults: ...
    def check(self) -> CommandResults: ...
    def close(self) -> CommandResults: ...
    def copy(self, message_set: str, new_mailbox: str) -> CommandResults: ...
    def create(self, mailbox: str) -> CommandResults: ...
    def delete(self, mailbox: str) -> CommandResults: ...
    def deleteacl(self, mailbox: str, who: str) -> CommandResults: ...
    def expunge(self) -> CommandResults: ...
    def fetch(self, message_set: str, message_parts: str) -> CommandResults: ...
    def getacl(self, mailbox: str) -> CommandResults: ...
    def getannotation(self, mailbox: str, entry: str, attribute: str) -> CommandResults: ...
    def getquota(self, root: str) -> CommandResults: ...
    def getquotaroot(self, mailbox: str) -> CommandResults: ...
    def list(self, directory: str = ..., pattern: str = ...) -> CommandResults: ...
    def login(self, user: str, password: str) -> CommandResults: ...
    def login_cram_md5(self, user: str, password: str) -> CommandResults: ...
    def logout(self) -> CommandResults: ...
    def lsub(self, directory: str = ..., pattern: str = ...) -> CommandResults: ...
    def myrights(self, mailbox: str) -> CommandResults: ...
    def namespace(self) -> CommandResults: ...
    def noop(self) -> CommandResults: ...
    def partial(self, message_num: str, message_part: str, start: str, length: str) -> CommandResults: ...
    def proxyauth(self, user: str) -> CommandResults: ...
    def rename(self, oldmailbox: str, newmailbox: str) -> CommandResults: ...
    def search(self, charset: Optional[str], *criteria: str) -> CommandResults: ...
    def select(self, mailbox: str = ..., readonly: bool = ...) -> CommandResults: ...
    def setacl(self, mailbox: str, who: str, what: str) -> CommandResults: ...
    def setannotation(self, *args: List[str]) -> CommandResults: ...
    def setquota(self, root: str, limits: str) -> CommandResults: ...
    def sort(self, sort_criteria: str, charset: str, *search_criteria: List[str]) -> CommandResults: ...
    if sys.version_info >= (3,):
        def starttls(self, ssl_context: Optional[Any] = ...) -> CommandResults: ...
    def status(self, mailbox: str, names: str) -> CommandResults: ...
    def store(self, message_set: str, command: str, flags: str) -> CommandResults: ...
    def subscribe(self, mailbox: str) -> CommandResults: ...
    def thread(self, threading_algorithm: str, charset: str, *search_criteria: List[str]) -> CommandResults: ...
    def uid(self, command: str, *args: List[str]) -> CommandResults: ...
    def unsubscribe(self, mailbox: str) -> CommandResults: ...
    def xatom(self, name: str, *args: List[str]) -> CommandResults: ...
    def print_log(self) -> None: ...

class IMAP4_SSL(IMAP4):
    keyfile: str = ...
    certfile: str = ...
    def __init__(self, host: str = ..., port: int = ..., keyfile: Optional[str] = ..., certfile: Optional[str] = ...) -> None: ...
    host: str = ...
    port: int = ...
    sock: _socket = ...
    sslobj: SSLSocket = ...
    file: IO[Any] = ...
    def open(self, host: str = ..., port: Optional[int] = ...) -> None: ...
    def read(self, size: int) -> bytes: ...
    def readline(self) -> bytes: ...
    def send(self, data: bytes) -> None: ...
    def shutdown(self) -> None: ...
    def socket(self) -> _socket: ...
    def ssl(self) -> SSLSocket: ...


class IMAP4_stream(IMAP4):
    command: str = ...
    def __init__(self, command: str) -> None: ...
    host: str = ...
    port: int = ...
    sock: _socket = ...
    file: IO[Any] = ...
    process: subprocess.Popen[bytes] = ...
    writefile: IO[Any] = ...
    readfile: IO[Any] = ...
    def open(self, host: str = ..., port: Optional[int] = ...) -> None: ...
    def read(self, size: int) -> bytes: ...
    def readline(self) -> bytes: ...
    def send(self, data: bytes) -> None: ...
    def shutdown(self) -> None: ...

class _Authenticator:
    mech: Callable[[bytes], bytes] = ...
    def __init__(self, mechinst: Callable[[bytes], bytes]) -> None: ...
    def process(self, data: str) -> str: ...
    def encode(self, inp: bytes) -> str: ...
    def decode(self, inp: str) -> bytes: ...

def Internaldate2tuple(resp: str) -> time.struct_time: ...
def Int2AP(num: int) -> str: ...
def ParseFlags(resp: str) -> Tuple[str]: ...
def Time2Internaldate(date_time: Union[float, time.struct_time, str]) -> str: ...
