from typing import Optional, Tuple
from cryptography.hazmat.primitives.hashes import HashAlgorithm

def decode_dss_signature(signature: bytes) -> Tuple[int, int]: ...
def encode_dss_signature(r: int, s: int) -> bytes: ...

class Prehashed(object):
    _algorithm: HashAlgorithm
    _digest_size: int
    def __init__(self, algorithm: Optional[HashAlgorithm]) -> None: ...
