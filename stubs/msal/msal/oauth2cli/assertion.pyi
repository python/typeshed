from _typeshed import Incomplete
from collections.abc import Callable
from logging import Logger
from typing import Any, Generic, TypeVar

_T = TypeVar("_T")

logger: Logger

class AssertionCreator:
    def create_normal_assertion(
        self, audience, issuer, subject, expires_at=None, expires_in: int = 600, issued_at=None, assertion_id=None, **kwargs
    ) -> bytes: ...
    def create_regenerative_assertion(
        self, audience, issuer, subject=None, expires_in: int = 600, **kwargs
    ) -> AutoRefresher[bytes]: ...

class AutoRefresher(Generic[_T]):
    def __init__(self, factory: Callable[[], _T], expires_in: float = 540) -> None: ...
    def __call__(self) -> _T: ...

class JwtAssertionCreator(AssertionCreator):
    key: Incomplete
    algorithm: str
    headers: dict[str, Any]
    def __init__(
        self,
        key,
        algorithm: str,
        sha1_thumbprint: str | None = None,
        headers: dict[str, Any] | None = None,
        *,
        sha256_thumbprint: str | None = None,
    ) -> None: ...
    def create_normal_assertion(
        self,
        audience,
        issuer,
        subject=None,
        expires_at=None,
        expires_in: int = 600,
        issued_at=None,
        assertion_id=None,
        not_before=None,
        additional_claims=None,
        **kwargs,
    ) -> bytes: ...
    sign_assertion = create_normal_assertion

Signer = AssertionCreator
JwtSigner = JwtAssertionCreator
