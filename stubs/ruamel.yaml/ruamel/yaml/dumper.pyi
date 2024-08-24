from _typeshed import Incomplete
from typing_extensions import TypeAlias

from .compat import StreamType
from .emitter import Emitter
from .representer import BaseRepresenter, Representer, RoundTripRepresenter, SafeRepresenter
from .resolver import BaseResolver, Resolver, VersionedResolver
from .serializer import Serializer

__all__ = ["BaseDumper", "SafeDumper", "Dumper", "RoundTripDumper"]

# https://github.com/python/typeshed/pull/8973
_Inf: TypeAlias = float

class BaseDumper(Emitter, Serializer, BaseRepresenter, BaseResolver):
    def __init__(
        self,
        stream: StreamType,
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

class SafeDumper(Emitter, Serializer, SafeRepresenter, Resolver):
    def __init__(
        self,
        stream: StreamType,
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

class Dumper(Emitter, Serializer, Representer, Resolver):
    def __init__(
        self,
        stream: StreamType,
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

class RoundTripDumper(Emitter, Serializer, RoundTripRepresenter, VersionedResolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: Incomplete | None = None,
        default_flow_style: bool | None = None,
        canonical: int | None = None,
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
