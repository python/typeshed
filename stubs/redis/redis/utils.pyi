from contextlib import AbstractContextManager
from contextlib.abc import Iterable, Mapping
from typing import Any, TypeVar, overload
from typing_extensions import Literal

from .client import Pipeline, Redis, _StrType

_T = TypeVar("_T")

HIREDIS_AVAILABLE: bool
CRYPTOGRAPHY_AVAILABLE: bool

@overload
def from_url(url: str, *, db: int = ..., decode_responses: Literal[True], **kwargs: Any) -> Redis[str]: ...
@overload
def from_url(url: str, *, db: int = ..., decode_responses: Literal[False] = ..., **kwargs: Any) -> Redis[bytes]: ...
def pipeline(redis_obj: Redis[_StrType]) -> AbstractContextManager[Pipeline[_StrType]]: ...
def str_if_bytes(value: str | bytes) -> str: ...
def safe_str(value: object) -> str: ...
def dict_merge(*dicts: Mapping[str, object]) -> dict[str, object]:
def list_keys_to_dict(key_list, callback): ...  # unused, alias for `dict.fromkeys`
def merge_result(command: object, res: Mapping[object, Iterable[_T]]) -> list[_T]: ...
