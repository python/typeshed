from _typeshed import Incomplete
from collections.abc import Collection, Mapping

from .. import Key
from .key_set import KeySet

class JsonWebKey:
    JWK_KEY_CLS: Incomplete
    @classmethod
    def generate_key(cls, kty, crv_or_size, options: Incomplete | None = None, is_private: bool = False): ...
    @classmethod
    def import_key(cls, raw: Mapping[str, object], options: Mapping[str, object] | None = None) -> Key: ...
    @classmethod
    def import_key_set(cls, raw: str | Collection | dict[str, object]) -> KeySet: ...
