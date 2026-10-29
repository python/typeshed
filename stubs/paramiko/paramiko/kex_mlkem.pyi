from _typeshed import Incomplete, ReadableBuffer
from collections.abc import Callable
from hashlib import _Hash

from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from paramiko.message import Message
from paramiko.transport import Transport

c_MSG_KEX_HYBRID_INIT: bytes
c_MSG_KEX_HYBRID_REPLY: bytes

class KexMLKEM768X25519:
    name: str
    hash_algo: Callable[[ReadableBuffer], _Hash]
    transport: Transport
    # cryptography.hazmat.primitives.asymmetric.mlkem.MLKEM768PrivateKey, added in cryptography 48
    mlkem_key: Incomplete | None
    x25519_key: X25519PrivateKey | None
    def __init__(self, transport: Transport) -> None: ...
    @classmethod
    def is_available(cls) -> bool: ...
    def start_kex(self) -> None: ...
    def parse_next(self, ptype: int, m: Message) -> None: ...
