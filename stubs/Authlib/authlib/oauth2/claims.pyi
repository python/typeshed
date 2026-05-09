from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, TypedDict

class ClaimsOption(TypedDict, total=False):
    essential: bool
    allow_blank: bool | None
    value: str | int | bool
    values: list[str | int | bool] | list[str] | list[int] | list[bool]
    validate: Callable[[BaseClaims, Any], bool]

class BaseClaims(dict[str, Incomplete]):
    registry_cls: Incomplete
    REGISTERED_CLAIMS: list[str]
    header: dict[str, Any]
    options: dict[str, ClaimsOption]
    params: dict[str, Any]
    def __init__(
        self,
        claims: dict[str, Any],
        header: dict[str, Any],
        options: dict[str, ClaimsOption] | None = None,
        params: dict[str, Any] | None = None,
    ) -> None: ...
    def get_registered_claims(self) -> dict[str, Incomplete]: ...
    def validate(self, now: int | Callable[[], int] | None = None, leeway: int = 0) -> None: ...

class JWTClaims(BaseClaims):
    registry_cls: Incomplete
    REGISTERED_CLAIMS: list[str]
    def validate(self, now: int | Callable[[], int] | None = None, leeway: int = 0) -> None: ...
