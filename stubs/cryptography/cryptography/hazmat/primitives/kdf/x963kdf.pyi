from typing import Optional

from cryptography.hazmat.backends.interfaces import HashBackend
from cryptography.hazmat.primitives.hashes import HashAlgorithm
from cryptography.hazmat.primitives.kdf import KeyDerivationFunction

class X963KDF(KeyDerivationFunction):
    def __init__(self, algorithm: HashAlgorithm, length: int, sharedinfo: bytes | None, backend: HashBackend | None = ...): ...
    def derive(self, key_material: bytes) -> bytes: ...
    def verify(self, key_material: bytes, expected_key: bytes) -> None: ...
