from _typeshed import StrOrBytesPath, StrPath, SupportsKeysAndGetItem
from collections.abc import Container, Iterable, Iterator, Mapping, MutableMapping, Sequence
from typing import TypeVar, overload
from typing_extensions import Literal, TypeAlias
from uuid import UUID

_T = TypeVar("_T")

_Token: TypeAlias = (
    tuple[Literal["EMPTY"], str, None]
    | tuple[Literal["COMMENT"], str, None]
    | tuple[Literal["SECTION"], str, tuple[str, ...]]
    | tuple[Literal["KV"], str, tuple[str, str, str]]
)

def get_app_dir(app_name: str, roaming: bool = ..., force_posix: bool = ...) -> str: ...

class Dialect:
    ns_sep: str
    kv_sep: str
    quotes: Sequence[str]
    true: Sequence[str]
    false: Sequence[str]
    comments: Container[str]
    allow_escaping: bool
    linesep: str | None
    def __init__(
        self,
        ns_sep: str = ...,
        kv_sep: str = ...,
        quotes: Sequence[str] = ...,
        true: Sequence[str] = ...,
        false: Sequence[str] = ...,
        comments: Container[str] = ...,
        allow_escaping: bool = ...,
        linesep: str | None = ...,
    ) -> None: ...
    def get_actual_linesep(self) -> str: ...
    def get_strippable_lineseps(self) -> str: ...
    def kv_serialize(self, key, val: str | None) -> str | None: ...
    def escape(self, value: str, quote: str | None = ...) -> str: ...
    def unescape(self, value: str) -> str: ...
    def to_string(self, value: bool | float | str) -> str: ...
    def dict_from_iterable(self, iterable: Iterable[str]) -> MutableMapping[str, str]: ...
    def tokenize(self, iterable: Iterable[str]) -> Iterator[_Token]: ...
    def update_tokens(
        self, old_tokens: Iterable[_Token], changes: SupportsKeysAndGetItem[str, str] | Iterable[tuple[str, str]]
    ) -> list[_Token]: ...

default_dialect: Dialect

class IniData(MutableMapping[str, str]):
    def __init__(self, mapping: Mapping[str, str] | None = ..., dialect: Dialect | None = ...) -> None: ...
    @property
    def is_dirty(self) -> bool: ...
    def get_updated_lines(self, line_iter: Iterable[_Token] | None = ...) -> list[_Token]: ...
    def discard(self) -> None: ...
    def rollover(self) -> None: ...
    def to_dict(self) -> dict[str, str]: ...
    def __len__(self) -> int: ...
    @overload
    def get(self, name: str) -> str | None: ...
    @overload
    def get(self, name: str, default: _T) -> str | _T: ...
    @overload
    def get_ascii(self, name: str) -> str | None: ...
    @overload
    def get_ascii(self, name: str, default: _T) -> str | _T: ...
    @overload
    def get_bool(self, name: str) -> bool: ...
    @overload
    def get_bool(self, name: str, default: _T) -> bool | _T: ...
    @overload
    def get_int(self, name: str) -> int | None: ...
    @overload
    def get_int(self, name: str, default: _T = ...) -> int | _T: ...
    @overload
    def get_float(self, name: str) -> float | None: ...
    @overload
    def get_float(self, name: str, default: _T) -> float | _T: ...
    @overload
    def get_uuid(self, name: str) -> UUID | None: ...
    @overload
    def get_uuid(self, name: str, default: _T) -> UUID | _T: ...
    def itersections(self) -> Iterator[str]: ...
    def sections(self) -> Iterator[str]: ...
    def iteritems(self) -> Iterator[tuple[str, str]]: ...
    def iterkeys(self) -> Iterator[str]: ...
    def itervalues(self) -> Iterator[str]: ...
    # NB: keys, items, values currently return a generator, which is
    # incompatible with the views returned by Mappings
    def items(self) -> Iterator[tuple[str, str]]: ...  # type: ignore[override]
    def keys(self) -> Iterator[str]: ...  # type: ignore[override]
    def __iter__(self) -> Iterator[str]: ...
    def values(self) -> Iterator[str]: ...  # type: ignore[override]
    def section_as_dict(self, section: str) -> dict[str, str]: ...
    def __getitem__(self, name: str) -> str: ...
    def __setitem__(self, name: str, value: str) -> None: ...
    def __delitem__(self, name: str) -> None: ...

class IniFile(IniData):
    def __init__(self, filename: StrOrBytesPath | int, encoding: str | None = ..., dialect: Dialect | None = ...) -> None: ...
    def save(self, create_folder: bool = ...) -> None: ...

class AppIniFile(IniFile):
    def __init__(
        self,
        app_name: str,
        filename: StrPath,
        roaming: bool = ...,
        force_posix: bool = ...,
        encoding: str | None = ...,
        dialect: Dialect | None = ...,
    ) -> None: ...
