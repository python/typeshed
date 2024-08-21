from _typeshed import Incomplete

from _ruamel_yaml import CEmitter, CParser

from .compat import StreamTextType, VersionType
from .constructor import BaseConstructor, Constructor, SafeConstructor
from .representer import BaseRepresenter, Representer, SafeRepresenter
from .resolver import BaseResolver, Resolver

__all__ = ["CBaseLoader", "CSafeLoader", "CLoader", "CBaseDumper", "CSafeDumper", "CDumper"]

class CBaseLoader(CParser, BaseConstructor, BaseResolver):
    def __init__(
        self, stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None
    ) -> None: ...

class CSafeLoader(CParser, SafeConstructor, Resolver):
    def __init__(
        self, stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None
    ) -> None: ...

class CLoader(CParser, Constructor, Resolver):
    def __init__(
        self, stream: StreamTextType, version: VersionType | None = None, preserve_quotes: bool | None = None
    ) -> None: ...

class CBaseDumper(CEmitter, BaseRepresenter, BaseResolver):
    def __init__(
        self,
        stream,
        default_style: Incomplete | None = None,
        default_flow_style: Incomplete | None = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: Incomplete | None = None,
        encoding: Incomplete | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: Incomplete | None = None,
        tags: Incomplete | None = None,
        block_seq_indent: Incomplete | None = None,
        top_level_colon_align: Incomplete | None = None,
        prefix_colon: Incomplete | None = None,
    ) -> None: ...

class CSafeDumper(CEmitter, SafeRepresenter, Resolver):
    def __init__(
        self,
        stream,
        default_style: Incomplete | None = None,
        default_flow_style: Incomplete | None = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: Incomplete | None = None,
        encoding: Incomplete | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: Incomplete | None = None,
        tags: Incomplete | None = None,
        block_seq_indent: Incomplete | None = None,
        top_level_colon_align: Incomplete | None = None,
        prefix_colon: Incomplete | None = None,
    ) -> None: ...

class CDumper(CEmitter, Representer, Resolver):
    def __init__(
        self,
        stream,
        default_style: Incomplete | None = None,
        default_flow_style: Incomplete | None = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: Incomplete | None = None,
        encoding: Incomplete | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: Incomplete | None = None,
        tags: Incomplete | None = None,
        block_seq_indent: Incomplete | None = None,
        top_level_colon_align: Incomplete | None = None,
        prefix_colon: Incomplete | None = None,
    ) -> None: ...
