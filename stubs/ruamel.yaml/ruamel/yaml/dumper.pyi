from _typeshed import Unused
from typing import TypeAlias

from .compat import StreamType, VersionType
from .emitter import Emitter, _LineBreak
from .representer import BaseRepresenter, Representer, RoundTripRepresenter, SafeRepresenter
from .resolver import BaseResolver, Resolver, VersionedResolver
from .serializer import Serializer
from .tag import _TagHandleToPrefix
from .tokens import _ScalarStyle

__all__ = ["BaseDumper", "SafeDumper", "Dumper", "RoundTripDumper"]

# https://github.com/python/typeshed/pull/8973
_Inf: TypeAlias = float

class BaseDumper(Emitter, Serializer, BaseRepresenter, BaseResolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: _ScalarStyle | None = None,
        default_flow_style: bool | None = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | _Inf | None = None,
        allow_unicode: bool | None = None,
        line_break: _LineBreak | None = None,
        encoding: str | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: VersionType | None = None,
        tags: _TagHandleToPrefix | None = None,
        block_seq_indent: int | None = None,
        top_level_colon_align: Unused = None,
        prefix_colon: Unused = None,
    ) -> None: ...

class SafeDumper(Emitter, Serializer, SafeRepresenter, Resolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: _ScalarStyle | None = None,
        default_flow_style: bool | None = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | _Inf | None = None,
        allow_unicode: bool | None = None,
        line_break: _LineBreak | None = None,
        encoding: str | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: VersionType | None = None,
        tags: _TagHandleToPrefix | None = None,
        block_seq_indent: int | None = None,
        top_level_colon_align: Unused = None,
        prefix_colon: Unused = None,
    ) -> None: ...

class Dumper(Emitter, Serializer, Representer, Resolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: _ScalarStyle | None = None,
        default_flow_style: bool | None = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | _Inf | None = None,
        allow_unicode: bool | None = None,
        line_break: _LineBreak | None = None,
        encoding: str | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: VersionType | None = None,
        tags: _TagHandleToPrefix | None = None,
        block_seq_indent: int | None = None,
        top_level_colon_align: Unused = None,
        prefix_colon: Unused = None,
    ) -> None: ...

class RoundTripDumper(Emitter, Serializer, RoundTripRepresenter, VersionedResolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: _ScalarStyle | None = None,
        default_flow_style: bool | None = None,
        canonical: bool | None = None,
        indent: int | None = None,
        width: int | _Inf | None = None,
        allow_unicode: bool | None = None,
        line_break: _LineBreak | None = None,
        encoding: str | None = None,
        explicit_start: bool | None = None,
        explicit_end: bool | None = None,
        version: VersionType | None = None,
        tags: _TagHandleToPrefix | None = None,
        block_seq_indent: int | None = None,
        top_level_colon_align: bool | None = None,
        prefix_colon: str | None = None,
    ) -> None: ...
