from collections.abc import Callable
from typing import IO

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey, RSAPublicNumbers
from paramiko.message import Message
from paramiko.pkey import PKey

class RSAKey(PKey):
    key: None | RSAPublicKey | RSAPrivateKey
    public_blob: None
    def __init__(
        self,
        msg: Message | None = ...,
        data: bytes | None = ...,
        filename: str | None = ...,
        password: str | None = ...,
        key: None | RSAPublicKey | RSAPrivateKey = ...,
        file_obj: IO[str] | None = ...,
    ) -> None: ...
    @property
    def size(self) -> int: ...
    @property
    def public_numbers(self) -> RSAPublicNumbers: ...
    def asbytes(self) -> bytes: ...
    def __hash__(self) -> int: ...
    def get_name(self) -> str: ...
    def get_bits(self) -> int: ...
    def can_sign(self) -> bool: ...
    def sign_ssh_data(self, data: bytes, algorithm: str = ...) -> Message: ...  # type: ignore[override]
    def verify_ssh_sig(self, data: bytes, msg: Message) -> bool: ...
    def write_private_key_file(self, filename: str, password: str | None = ...) -> None: ...
    def write_private_key(self, file_obj: IO[str], password: str | None = ...) -> None: ...
    @staticmethod
    def generate(bits: int, progress_func: Callable[..., Any] | None = ...) -> RSAKey: ...
