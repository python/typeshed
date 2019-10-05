from cryptography.hazmat.backends.interfaces import HMACBackend
from cryptography.hazmat.primitives.hashes import HashAlgorithm

class Poly1305:
    def __init__(self, key: bytes) -> None: ...
    def finalize(self) -> bytes: ...
    @classmethod
    def generate_tag(cls, key: bytes, data: bytes) -> bytes: ...
    def update(self, data: bytes) -> None: ...
    def verify(self, tag: bytes) -> None: ...
    @classmethod
    def verify_tag(cls, key: bytes, data: bytes, tag: bytes) -> None: ...
