from typing import List, Optional, Union

from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateKeyWithSerialization
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKeyWithSerialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKeyWithSerialization
from cryptography.hazmat.primitives.serialization import KeySerializationEncryption
from cryptography.x509 import Certificate

def load_key_and_certificates(data: bytes, password: Optional[bytes], backend): ...
def serialize_key_and_certificates(
    name: bytes,
    key: Union[RSAPrivateKeyWithSerialization, EllipticCurvePrivateKeyWithSerialization, DSAPrivateKeyWithSerialization],
    cert: Optional[Certificate],
    cas: Optional[List[Certificate]],
    enc: KeySerializationEncryption,
) -> bytes: ...
