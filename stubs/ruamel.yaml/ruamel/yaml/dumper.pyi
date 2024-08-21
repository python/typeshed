from typing import Any

from ruamel.yaml.compat import StreamType
from ruamel.yaml.emitter import Emitter
from ruamel.yaml.representer import BaseRepresenter, Representer, RoundTripRepresenter, SafeRepresenter
from ruamel.yaml.resolver import BaseResolver, Resolver, VersionedResolver
from ruamel.yaml.serializer import Serializer

__all__ = ["BaseDumper", "SafeDumper", "Dumper", "RoundTripDumper"]

class BaseDumper(Emitter, Serializer, BaseRepresenter, BaseResolver):
    def __init__(
        self,
        stream: StreamType,
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

class SafeDumper(Emitter, Serializer, SafeRepresenter, Resolver):
    def __init__(
        self,
        stream: StreamType,
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

class Dumper(Emitter, Serializer, Representer, Resolver):
    def __init__(
        self,
        stream: StreamType,
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

class RoundTripDumper(Emitter, Serializer, RoundTripRepresenter, VersionedResolver):
    def __init__(
        self,
        stream: StreamType,
        default_style: Any = None,
        default_flow_style: bool | None = None,
        canonical: int | None = None,
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
