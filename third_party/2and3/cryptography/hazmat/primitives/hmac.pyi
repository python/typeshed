from cryptography.hazmat.backends.interfaces import HMACBackend
from cryptography.hazmat.primitives.hashes import HashAlgorithm

class HMAC:
    def __init__(self, key: bytes, algorithm: HashAlgorithm, backend: HMACBackend): ...
    def finalize(self) -> bytes: ...
    def update(self, msg: bytes) -> None: ...
