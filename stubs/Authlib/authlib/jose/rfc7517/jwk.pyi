from _typeshed import Incomplete

class JsonWebKey:
    JWK_KEY_CLS: Incomplete
    @classmethod
    def generate_key(cls, kty, crv_or_size, options: Incomplete | None = None, is_private: bool = False): ...
    @classmethod
    def import_key(cls, raw, options: Incomplete | None = None): ...
    @classmethod
    def import_key_set(cls, raw): ...
