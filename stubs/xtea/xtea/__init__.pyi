from _typeshed import ReadableBuffer
from collections.abc import Callable

from pep272_encryption import PEP272Cipher

MODE_ECB: int
MODE_CBC: int
MODE_CFB: int
MODE_PGP: int
MODE_OFB: int
MODE_CTR: int
block_size: int
key_size: int

def new(key, **kwargs): ...

class XTEACipher(PEP272Cipher):
    block_size: int
    IV: bytes | None
    counter: Callable[[], bytes] | None
    rounds: int
    cycles: int
    endian: str
    def __init__(self, key: ReadableBuffer, mode: int | None = ..., **kwargs) -> None: ...
    def encrypt_block(self, key: ReadableBuffer, block: ReadableBuffer, **kwargs): ...
    def decrypt_block(self, key: ReadableBuffer, block: ReadableBuffer, **kwargs): ...
