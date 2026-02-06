import asyncio
import socket
from _typeshed import Incomplete
from typing import ClassVar

class DirtyProtocol:
    HEADER_FORMAT: ClassVar[str]
    HEADER_SIZE: ClassVar[int]
    MAX_MESSAGE_SIZE: ClassVar[int]
    MSG_TYPE_REQUEST: ClassVar[str]
    MSG_TYPE_RESPONSE: ClassVar[str]
    MSG_TYPE_ERROR: ClassVar[str]
    MSG_TYPE_CHUNK: ClassVar[str]
    MSG_TYPE_END: ClassVar[str]

    @staticmethod
    def encode(message: dict[Incomplete, Incomplete]) -> bytes: ...
    @staticmethod
    def decode(data: bytes) -> dict[Incomplete, Incomplete]: ...
    @staticmethod
    async def read_message_async(reader: asyncio.StreamReader) -> dict[Incomplete, Incomplete]: ...
    @staticmethod
    async def write_message_async(writer: asyncio.StreamWriter, message: dict[Incomplete, Incomplete]) -> None: ...
    @staticmethod
    def read_message(sock: socket.socket) -> dict[Incomplete, Incomplete]: ...
    @staticmethod
    def write_message(sock: socket.socket, message: dict[Incomplete, Incomplete]) -> None: ...

# TODO: Use TypedDict for results
def make_request(
    request_id: str,
    app_path: str,
    action: str,
    args: tuple[Incomplete, ...] | None = None,
    kwargs: dict[str, Incomplete] | None = None,
) -> dict[str, Incomplete]: ...
def make_response(request_id: str, result) -> dict[str, Incomplete]: ...
def make_error_response(request_id: str, error) -> dict[str, Incomplete]: ...
def make_chunk_message(request_id: str, data) -> dict[str, Incomplete]: ...
def make_end_message(request_id: str) -> dict[str, Incomplete]: ...
