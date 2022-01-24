from _typeshed import SupportsKeysAndGetItem
from collections.abc import Callable, Generator, Iterable
from typing import Any, ClassVar

from ._utils import URIDict

# This class does not exist runtime. Compatible classes are created at
# runtime by create().
class _Validator:
    VALIDATORS: ClassVar[dict[Any, Any]]
    META_SCHEMA: ClassVar[dict[Any, Any]]
    TYPE_CHECKER: Any
    @staticmethod
    def ID_OF(): ...
    schema: Any
    resolver: Any
    format_checker: Any
    evolve: Any
    @classmethod
    def check_schema(cls, schema) -> None: ...
    def iter_errors(self, instance, _schema: Any | None = ...) -> Generator[Any, None, None]: ...
    def descend(self, instance, schema, path: Any | None = ..., schema_path: Any | None = ...) -> Generator[Any, None, None]: ...
    def validate(self, *args, **kwargs) -> None: ...
    def is_type(self, instance, type): ...
    def is_valid(self, instance, _schema: Any | None = ...) -> bool: ...

def validates(version: str) -> Callable[..., Any]: ...
def create(
    meta_schema, validators=..., version: Any | None = ..., type_checker=..., id_of=..., applicable_validators=...
) -> type[_Validator]: ...
def extend(validator, validators=..., version: Any | None = ..., type_checker: Any | None = ...): ...

Draft3Validator: type[_Validator]
Draft4Validator: type[_Validator]
Draft6Validator: type[_Validator]
Draft7Validator: type[_Validator]
Draft201909Validator: type[_Validator]
Draft202012Validator: type[_Validator]

_Handler = Callable[[str], Any]

class RefResolver:
    referrer: str
    cache_remote: Any
    handlers: dict[str, _Handler]
    store: URIDict
    def __init__(
        self,
        base_uri: str,
        referrer: str,
        store: SupportsKeysAndGetItem[str, str] | Iterable[tuple[str, str]] = ...,
        cache_remote: bool = ...,
        handlers: SupportsKeysAndGetItem[str, _Handler] | Iterable[tuple[str, _Handler]] = ...,
        urljoin_cache: Any | None = ...,
        remote_cache: Any | None = ...,
    ) -> None: ...
    @classmethod
    def from_schema(cls, schema, id_of=..., *args, **kwargs): ...
    def push_scope(self, scope) -> None: ...
    def pop_scope(self) -> None: ...
    @property
    def resolution_scope(self): ...
    @property
    def base_uri(self): ...
    def in_scope(self, scope) -> None: ...
    def resolving(self, ref) -> None: ...
    def resolve(self, ref): ...
    def resolve_from_url(self, url): ...
    def resolve_fragment(self, document, fragment): ...
    def resolve_remote(self, uri): ...

def validate(instance: object, schema: object, cls: type[_Validator] | None = ..., *args: Any, **kwargs: Any) -> None: ...
def validator_for(schema, default=...): ...
