import asyncore
import socket
from abc import abstractmethod
from typing import Union

class simple_producer:
    def __init__(self, data: bytes, buffer_size: int = ...) -> None: ...
    def more(self) -> bytes: ...

class async_chat(asyncore.dispatcher):
    ac_in_buffer_size: int
    ac_out_buffer_size: int
    def __init__(self, sock: socket.socket | None = ..., map: asyncore._maptype | None = ...) -> None: ...
    @abstractmethod
    def collect_incoming_data(self, data: bytes) -> None: ...
    @abstractmethod
    def found_terminator(self) -> None: ...
    def set_terminator(self, term: bytes | int | None) -> None: ...
    def get_terminator(self) -> bytes | int | None: ...
    def handle_read(self) -> None: ...
    def handle_write(self) -> None: ...
    def handle_close(self) -> None: ...
    def push(self, data: bytes) -> None: ...
    def push_with_producer(self, producer: simple_producer) -> None: ...
    def readable(self) -> bool: ...
    def writable(self) -> bool: ...
    def close_when_done(self) -> None: ...
    def initiate_send(self) -> None: ...
    def discard_buffers(self) -> None: ...
