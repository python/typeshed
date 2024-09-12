from _typeshed import Unused

from _ruamel_yaml import CEmitter, CParser

from .compat import StreamTextType, StreamType
from .constructor import BaseConstructor, Constructor, SafeConstructor
from .emitter import _LineBreak
from .representer import BaseRepresenter, Representer, SafeRepresenter
from .resolver import BaseResolver, Resolver
from .tag import _TagHandleToPrefix
from .tokens import _ScalarStyle, _VersionTuple

__all__ = ["CBaseLoader", "CSafeLoader", "CLoader", "CBaseDumper", "CSafeDumper", "CDumper"]

class CBaseLoader(CParser, BaseConstructor, BaseResolver):
    def __init__(self, stream: StreamTextType, version: Unused = None, preserve_quotes: Unused = None) -> None: ...

class CSafeLoader(CParser, SafeConstructor, Resolver):
    def __init__(self, stream: StreamTextType, version: Unused = None, preserve_quotes: Unused = None) -> None: ...

class CLoader(CParser, Constructor, Resolver):
    def __init__(self, stream: StreamTextType, version: Unused = None, preserve_quotes: Unused = None) -> None: ...

class CBaseDumper(CEmitter, BaseRepresenter, BaseResolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: _ScalarStyle | None = None,
        default_flow_style: bool | None = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: _LineBreak | None = None,
        encoding: str | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: _VersionTuple | None = None,
        tags: _TagHandleToPrefix | None = None,
        block_seq_indent: Unused = None,
        top_level_colon_align: Unused = None,
        prefix_colon: Unused = None,
    ) -> None: ...

class CSafeDumper(CEmitter, SafeRepresenter, Resolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: _ScalarStyle | None = None,
        default_flow_style: bool | None = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: _LineBreak | None = None,
        encoding: str | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: _VersionTuple | None = None,
        tags: _TagHandleToPrefix | None = None,
        block_seq_indent: Unused = None,
        top_level_colon_align: Unused = None,
        prefix_colon: Unused = None,
    ) -> None: ...

class CDumper(CEmitter, Representer, Resolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: _ScalarStyle | None = None,
        default_flow_style: bool | None = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: _LineBreak | None = None,
        encoding: str | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: _VersionTuple | None = None,
        tags: _TagHandleToPrefix | None = None,
        block_seq_indent: Unused = None,
        top_level_colon_align: Unused = None,
        prefix_colon: Unused = None,
    ) -> None: ...
