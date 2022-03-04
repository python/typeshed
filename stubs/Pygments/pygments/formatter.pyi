from typing import Any, Generic, TypeVar, overload, type_check_only

_T = TypeVar("_T", str, bytes)

class Formatter:
    name: Any
    aliases: Any
    filenames: Any
    unicodeoutput: bool
    style: Any
    full: Any
    title: Any
    encoding: Any
    options: Any
    def get_style_defs(self, arg: str = ...): ...
    def format(self, tokensource, outfile): ...

@type_check_only
class _Formatter(Generic[_T], Formatter): ...

@type_check_only
class _BinaryFormatter(_Formatter[bytes]):
    def __init__(self, **options) -> None: ...

@type_check_only
class _TextFormatter(_Formatter[_T]):
    @overload
    def __init__(self: _Formatter[str], *, encoding: None = ..., outencoding: None = ..., **options) -> None: ...
    @overload
    def __init__(self: _Formatter[bytes], *, encoding: str, outencoding: None = ..., **options) -> None: ...
    @overload
    def __init__(self: _Formatter[bytes], *, encoding: None = ..., outencoding: str, **options) -> None: ...
