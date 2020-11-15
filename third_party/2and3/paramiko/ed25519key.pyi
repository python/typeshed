from typing import IO, Any, Optional, Tuple

from paramiko.message import Message
from paramiko.pkey import PKey

OPENSSH_AUTH_MAGIC: bytes

class Ed25519Key(PKey):
    public_blob: None
    def __init__(
        self,
        msg: Optional[Message] = ...,
        data: Optional[bytes] = ...,
        filename: Optional[str] = ...,
        password: Optional[str] = ...,
        file_obj: Optional[IO[bytes]] = ...,
    ) -> None: ...
    def asbytes(self) -> bytes: ...
    def __hash__(self) -> int: ...
    def get_name(self) -> str: ...
    def get_bits(self) -> int: ...
    def can_sign(self) -> bool: ...
    def sign_ssh_data(self, data: bytes) -> bytes: ...
    def verify_ssh_sig(self, data: bytes, msg: Message) -> bool: ...
