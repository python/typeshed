from collections.abc import Callable
from typing import IO

from paramiko.message import Message
from paramiko.pkey import PKey

class DSSKey(PKey):
    p: int | None
    q: int | None
    g: int | None
    y: int | None
    x: int | None
    public_blob: None
    size: int
    def __init__(
        self,
        msg: Message | None = ...,
        data: bytes | None = ...,
        filename: str | None = ...,
        password: str | None = ...,
        vals: tuple[int, int, int, int] | None = ...,
        file_obj: IO[str] | None = ...,
    ) -> None: ...
    def asbytes(self) -> bytes: ...
    def __hash__(self) -> int: ...
    def get_name(self) -> str: ...
    def get_bits(self) -> int: ...
    def can_sign(self) -> bool: ...
    def sign_ssh_data(self, data: bytes, algorithm: str | None = ...) -> Message: ...
    def verify_ssh_sig(self, data: bytes, msg: Message) -> bool: ...
    def write_private_key_file(self, filename: str, password: str | None = ...) -> None: ...
    def write_private_key(self, file_obj: IO[str], password: str | None = ...) -> None: ...
    @staticmethod
    def generate(bits: int = ..., progress_func: Callable[..., object] | None = ...) -> DSSKey: ...
