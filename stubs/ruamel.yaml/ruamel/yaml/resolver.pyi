from collections.abc import Iterable
from re import Pattern
from typing import Any, Final, overload
from typing_extensions import TypeAlias

from .compat import VersionType
from .dumper import _Dumper
from .error import YAMLError
from .loader import _Loader
from .main import YAML
from .nodes import CollectionNode, MappingNode, Node, ScalarNode, SequenceNode
from .parser import Parser
from .tag import Tag
from .tokens import _VersionTuple

__all__ = ["BaseResolver", "Resolver", "VersionedResolver"]

_TagStr: TypeAlias = str
_First: TypeAlias = str | None

implicit_resolvers: list[tuple[list[_VersionTuple], _TagStr, Pattern[str], list[_First]]]

class ResolverError(YAMLError): ...

class BaseResolver:
    DEFAULT_SCALAR_TAG: Final[Tag]
    DEFAULT_SEQUENCE_TAG: Final[Tag]
    DEFAULT_MAPPING_TAG: Final[Tag]
    yaml_implicit_resolvers: dict[_First, list[tuple[_TagStr, Pattern[str]]]]
    yaml_path_resolvers: dict[Any, _TagStr]
    loadumper: YAML | _Loader | _Dumper | None
    resolver_exact_paths: list[Any]
    resolver_prefix_paths: list[Any]
    def __init__(self, loadumper: YAML | _Loader | _Dumper | None = None) -> None: ...
    @property
    def parser(self) -> Parser | None: ...
    @classmethod
    def add_implicit_resolver_base(cls, tag: _TagStr, regexp: Pattern[str], first: list[_First] | None) -> None: ...
    @classmethod
    def add_implicit_resolver(cls, tag: _TagStr, regexp: Pattern[str], first: list[_First] | None) -> None: ...
    @classmethod
    def add_path_resolver(cls, tag: _TagStr, path: Iterable[Any], kind: type | None = None) -> None: ...
    def descend_resolver(self, current_node: CollectionNode | None, current_index: int | Node | None) -> None: ...
    def ascend_resolver(self) -> None: ...
    def check_resolver_prefix(self, depth: int, path, kind, current_node, current_index) -> bool: ...
    @overload
    def resolve(self, kind: type[ScalarNode], value: str, implicit: tuple[bool, bool]) -> Tag: ...
    @overload
    def resolve(self, kind: type[SequenceNode], value: list[Node] | None, implicit: bool) -> Tag: ...
    @overload
    def resolve(self, kind: type[MappingNode], value: list[tuple[Node, Node]] | None, implicit: bool) -> Tag: ...
    @property
    def processing_version(self) -> _VersionTuple | None: ...

class Resolver(BaseResolver): ...

class VersionedResolver(BaseResolver):
    def __init__(
        self,
        version: VersionType | None = None,
        loader: YAML | _Loader | _Dumper | None = None,
        loadumper: YAML | _Loader | _Dumper | None = None,
    ) -> None: ...
    def add_version_implicit_resolver(
        self, version: VersionType, tag: _TagStr, regexp: Pattern[str], first: list[_First] | None
    ) -> None: ...
    def get_loader_version(self, version: VersionType | None) -> _VersionTuple | None: ...
    @property
    def versioned_resolver(self) -> dict[_First, list[tuple[_TagStr, Pattern[str]]]]: ...
    @property
    def processing_version(self) -> _VersionTuple: ...
