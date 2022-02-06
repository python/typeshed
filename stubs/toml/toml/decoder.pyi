import sys
from _typeshed import StrPath
from typing import IO, Callable, Generic, MutableMapping, Pattern, Protocol, Text, TypeVar

_T = TypeVar("_T")
_KT_contra = TypeVar("_KT_contra", contravariant=True)
_VT = TypeVar("_VT")

if sys.version_info >= (3, 3):
    FNFError = FileNotFoundError
else:
    FNFError = IOError

if sys.version_info >= (3, 6):
    _PathLike = StrPath
elif sys.version_info >= (3, 4):
    import pathlib

    _PathLike = StrPath | pathlib.PurePath
else:
    _PathLike = StrPath

class _SupportsGetSetItem(Protocol[_KT_contra, _VT]):
    def __getitem__(self, __k: _KT_contra) -> _VT: ...
    def __setitem__(self, __k: _KT_contra, __v: _VT) -> None: ...

TIME_RE: Pattern[str]

class TomlDecodeError(ValueError):
    msg: str
    doc: str
    pos: int
    lineno: int
    colno: int
    def __init__(self, msg: str, doc: str, pos: int) -> None: ...

class CommentValue(_SupportsGetSetItem[_KT_contra, _VT]):
    val: _SupportsGetSetItem[_KT_contra, _VT]
    comment: str
    def __init__(
        self,
        val: _SupportsGetSetItem[_KT_contra, _VT],
        comment: str,
        beginline: bool,
        _dict: type[MutableMapping[_KT_contra, _VT]],
    ) -> None: ...
    def __getitem__(self, key: _KT_contra) -> _VT: ...
    def __setitem__(self, key: _KT_contra, value: _VT) -> None: ...
    def dump(self, dump_value_func: Callable[[_SupportsGetSetItem[_KT_contra, _VT]], str]) -> str: ...

def load(
    f: _PathLike | list[Text] | IO[str], _dict: type[MutableMapping[str, _T]] = ..., decoder: TomlDecoder[_T] | None = ...
) -> MutableMapping[str, _T]: ...
def loads(
    s: Text, _dict: type[MutableMapping[str, _T]] = ..., decoder: TomlDecoder[_T] | None = ...
) -> MutableMapping[str, _T]: ...

class InlineTableDict: ...

class TomlDecoder(Generic[_T]):
    _dict: type[MutableMapping[str, _T]]
    def __init__(self, _dict: type[MutableMapping[str, _T]] | None = ...) -> None: ...
    def get_empty_table(self) -> MutableMapping[str, _T]: ...
    def get_empty_inline_table(self) -> InlineTableDict: ...  # incomplete python/typing#213
    def load_inline_object(
        self, line: str, currentlevel: MutableMapping[str, _T], multikey: bool = ..., multibackslash: bool = ...
    ) -> None: ...
    def load_line(
        self, line: str, currentlevel: MutableMapping[str, _T], multikey: bool | None, multibackslash: bool
    ) -> tuple[bool | None, str, bool] | None: ...
    def load_value(self, v: str, strictly_valid: bool = ...) -> tuple[bool, str]: ...
    def bounded_string(self, s: str) -> bool: ...
    def load_array(self, a: str) -> list[_T]: ...
    def preserve_comment(self, line_no: int, key: str, comment: str, beginline: bool) -> None: ...
    def embed_comments(self, idx: int, currentlevel: MutableMapping[str, _T]) -> None: ...

class TomlPreserveCommentDecoder(TomlDecoder[_T]):
    saved_comments: MutableMapping[int, tuple[str, str, bool]]
