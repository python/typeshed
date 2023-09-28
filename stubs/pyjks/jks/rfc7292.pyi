from _typeshed import Incomplete
from hashlib import _Hash
from typing_extensions import TypeAlias, Literal

from pyasn1.type import univ

PBE_WITH_SHA1_AND_TRIPLE_DES_CBC_OID: tuple[int, ...]
PURPOSE_KEY_MATERIAL: Literal[1]
PURPOSE_IV_MATERIAL: Literal[2]
PURPOSE_MAC_MATERIAL: Literal[3]

_Purpose: TypeAlias = Literal[1, 2, 3]

class Pkcs12PBEParams(univ.Sequence):
    componentType: Incomplete

def derive_key(
    hashfn: _Hash, purpose_byte: _Purpose, password_str: str, salt: bytes, iteration_count: int, desired_key_size: int
) -> bytes: ...
def decrypt_PBEWithSHAAnd3KeyTripleDESCBC(
    data: bytes | bytearray, password_str: str, salt: bytes, iteration_count: int
) -> bytes: ...
def decrypt_PBEWithSHAAndTwofishCBC(
    encrypted_data: bytes | bytearray, password: str, salt: bytes, iteration_count: int
) -> bytes: ...
def encrypt_PBEWithSHAAndTwofishCBC(
    plaintext_data: bytes | bytearray, password: str, salt: bytes, iteration_count: int
) -> bytes: ...
