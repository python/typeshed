from typing import Any

from _ruamel_yaml import CEmitter, CParser
from ruamel.yaml.compat import StreamTextType, VersionType
from ruamel.yaml.constructor import BaseConstructor, Constructor, SafeConstructor
from ruamel.yaml.representer import BaseRepresenter, Representer, SafeRepresenter
from ruamel.yaml.resolver import BaseResolver, Resolver

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
        stream: Any,
        default_style: Any = None,
        default_flow_style: Any = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: Any = None,
        encoding: Any = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: Any = None,
        tags: Any = None,
        block_seq_indent: Any = None,
        top_level_colon_align: Any = None,
        prefix_colon: Any = None,
    ) -> None: ...

class CSafeDumper(CEmitter, SafeRepresenter, Resolver):
    def __init__(
        self,
        stream: Any,
        default_style: Any = None,
        default_flow_style: Any = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: Any = None,
        encoding: Any = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: Any = None,
        tags: Any = None,
        block_seq_indent: Any = None,
        top_level_colon_align: Any = None,
        prefix_colon: Any = None,
    ) -> None: ...

class CDumper(CEmitter, Representer, Resolver):
    def __init__(
        self,
        stream: Any,
        default_style: Any = None,
        default_flow_style: Any = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | None = None,
        allow_unicode: bool | None = None,
        line_break: Any = None,
        encoding: Any = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: Any = None,
        tags: Any = None,
        block_seq_indent: Any = None,
        top_level_colon_align: Any = None,
        prefix_colon: Any = None,
    ) -> None: ...
