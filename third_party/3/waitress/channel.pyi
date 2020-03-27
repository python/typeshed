from . import wasyncore as wasyncore
from socket import SocketType
from threading import Condition, Lock
from typing import Dict, List, Optional
from waitress.adjustments import Adjustments
from waitress.buffers import OverflowableBuffer, ReadOnlyFileBasedBuffer
from waitress.parser import HTTPRequestParser
from waitress.server import BaseWSGIServer
from waitress.task import ErrorTask, WSGITask, Task
from waitress.utilities import InternalServerError

class ClientDisconnected(Exception): ...

class HTTPChannel(wasyncore.dispatcher):
    task_class: WSGITask = ...
    error_task_class: ErrorTask = ...
    parser_class: HTTPRequestParser = ...
    request: HTTPRequestParser = ...
    last_activity: float = ...
    will_close: bool = ...
    close_when_flushed: bool = ...
    requests: List[HTTPRequestParser] = ...
    sent_continue: bool = ...
    total_outbufs_len: int = ...
    current_outbuf_count: int = ...
    server: BaseWSGIServer = ...
    adj: Adjustments = ...
    outbufs: List[OverflowableBuffer] = ...
    creation_time: float = ...
    sendbuf_len: int = ...
    task_lock: Lock = ...
    outbuf_lock: Condition = ...
    addr: str = ...
    def __init__(self, server: BaseWSGIServer, sock: SocketType, addr: str, adj: Adjustments, map: Optional[Dict[int, SocketType]] = ...) -> None: ...
    def writable(self) -> bool: ...
    def handle_write(self) -> None: ...
    def readable(self) -> bool: ...
    def handle_read(self) -> None: ...
    def received(self, data: bytes) -> bool: ...
    connected: bool = ...
    def handle_close(self) -> None: ...
    def add_channel(self, map: Optional[Dict[int, SocketType]] = ...) -> None: ...
    def del_channel(self, map: Optional[Dict[int, SocketType]] = ...) -> None: ...
    def write_soon(self, data: bytes) -> int: ...
    def service(self) -> None: ...
    def cancel(self) -> None: ...
