from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Any, Literal
from typing_extensions import Self

from jwcrypto.common import JWException, JWSEHeaderParameter
from jwcrypto.jwa import JWAAlgorithm
from jwcrypto.jwk import JWK, JWKSet

JWSHeaderRegistry: Mapping[str, JWSEHeaderParameter]
default_allowed_algs: list[str]

class InvalidJWSSignature(JWException):
    def __init__(self, message: str | None = None, exception: BaseException | None = None) -> None: ...

class InvalidJWSObject(JWException):
    def __init__(self, message: str | None = None, exception: BaseException | None = None) -> None: ...

class InvalidJWSOperation(JWException):
    def __init__(self, message: str | None = None, exception: BaseException | None = None) -> None: ...

class JWSCore:
    alg: str
    engine: JWAAlgorithm
    key: JWK | JWKSet
    header: dict[str, Any]
    protected: str
    payload: bytes
    def __init__(
        self,
        alg: str,
        key: JWK | JWKSet,
        header: dict[str, Any] | str | None,
        payload: str | bytes,
        algs: list[str] | None = None,
    ) -> None: ...
    def sign(self) -> dict[str, str | bytes]: ...
    def verify(self, signature: bytes) -> Literal[True]: ...

class JWS:
    objects: Incomplete
    verifylog: list[str] | None
    header_registry: Incomplete
    def __init__(self, payload: Incomplete | None = None, header_registry: Incomplete | None = None) -> None: ...
    @property
    def allowed_algs(self): ...
    @allowed_algs.setter
    def allowed_algs(self, algs) -> None: ...
    @property
    def is_valid(self): ...
    def verify(self, key, alg: Incomplete | None = None, detached_payload: Incomplete | None = None) -> None: ...
    def deserialize(self, raw_jws, key: Incomplete | None = None, alg: Incomplete | None = None) -> None: ...
    def add_signature(
        self, key, alg: Incomplete | None = None, protected: Incomplete | None = None, header: Incomplete | None = None
    ) -> None: ...
    def serialize(self, compact: bool = False) -> str: ...
    @property
    def payload(self): ...
    def detach_payload(self) -> None: ...
    @property
    def jose_header(self): ...
    @classmethod
    def from_jose_token(cls, token: str | bytes) -> Self: ...
    def __eq__(self, other: object) -> bool: ...
