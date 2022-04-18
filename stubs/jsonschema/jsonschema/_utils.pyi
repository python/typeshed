from _typeshed import SupportsKeysAndGetItem
from collections.abc import Generator, Iterable, Iterator, Mapping, MutableMapping, Sized
from typing import Any

class URIDict(MutableMapping[str, str]):
    def normalize(self, uri: str) -> str: ...
    store: dict[str, str]
    def __init__(self, __m: SupportsKeysAndGetItem[str, str] | Iterable[tuple[str, str]], **kwargs: str) -> None: ...
    def __getitem__(self, uri: str) -> str: ...
    def __setitem__(self, uri: str, value: str) -> None: ...
    def __delitem__(self, uri: str) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...

class Unset: ...

def load_schema(name): ...
def format_as_index(container: str, indices) -> str: ...
def find_additional_properties(instance: Iterable[Any], schema: Mapping[Any, Any]) -> Generator[Any, None, None]: ...
def extras_msg(extras: Iterable[Any] | Sized) -> str: ...
def ensure_list(thing) -> list[Any]: ...
def equal(one, two) -> bool: ...
def unbool(element, true=..., false=...): ...
def uniq(container) -> bool: ...
def find_evaluated_item_indexes_by_schema(validator, instance, schema) -> list[Any]: ...
def find_evaluated_property_keys_by_schema(validator, instance, schema) -> list[Any]: ...
