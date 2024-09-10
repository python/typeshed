from _typeshed import Incomplete

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKeyWithSerialization, RSAPublicKey

from ..rfc7517 import AsymmetricKey

class RSAKey(AsymmetricKey):
    kty: str
    PUBLIC_KEY_CLS = RSAPublicKey
    PRIVATE_KEY_CLS = RSAPrivateKeyWithSerialization
    PUBLIC_KEY_FIELDS: Incomplete
    PRIVATE_KEY_FIELDS: Incomplete
    REQUIRED_JSON_FIELDS: Incomplete
    SSH_PUBLIC_PREFIX: bytes
    def dumps_private_key(self): ...
    def dumps_public_key(self): ...
    def load_private_key(self): ...
    def load_public_key(self): ...
    @classmethod
    def generate_key(cls, key_size: int = 2048, options: Incomplete | None = None, is_private: bool = False) -> RSAKey: ...
    @classmethod
    def import_dict_key(cls, raw, options: Incomplete | None = None): ...

def has_all_prime_factors(obj): ...
