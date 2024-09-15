from collections.abc import Generator, Iterable, Iterator, Mapping, Set as AbstractSet
from datetime import date, datetime
from types import ModuleType
from typing import Any, ClassVar, Final, NoReturn, Protocol, TypeVar, overload
from typing_extensions import Self

from . import util
from .comments import CommentedMap, CommentedOrderedMap, CommentedSeq, CommentedSet, TaggedScalar
from .compat import ordereddict
from .composer import Composer
from .error import MarkedYAMLError, MarkedYAMLFutureWarning, _Mark
from .loader import _Loader
from .main import YAML
from .nodes import MappingNode, Node, ScalarNode, SequenceNode
from .resolver import BaseResolver
from .scalarbool import ScalarBoolean
from .scalarfloat import ScalarFloat
from .scanner import ScannedComments, Scanner
from .tag import Tag
from .timestamp import TimeStamp

__all__ = ["BaseConstructor", "SafeConstructor", "Constructor", "ConstructorError", "RoundTripConstructor"]

_T = TypeVar("_T")
_Constructor = TypeVar("_Constructor", bound=BaseConstructor, contravariant=True)

class _ConstructorFunction(Protocol[_Constructor]):
    def __call__(self, loader: _Constructor, node: Node, /) -> Any: ...

class _MultiConstructorFunction(Protocol[_Constructor]):
    def __call__(self, loader: _Constructor, tag_suffix: str, node: Node, /) -> Any: ...

class ConstructorError(MarkedYAMLError): ...
class DuplicateKeyFutureWarning(MarkedYAMLFutureWarning): ...
class DuplicateKeyError(MarkedYAMLError): ...

class BaseConstructor:
    yaml_constructors: ClassVar[dict[str | None, _ConstructorFunction[Self]]]
    yaml_multi_constructors: ClassVar[dict[str | None, _MultiConstructorFunction[Self]]]
    loader: YAML | _Loader | None
    yaml_base_dict_type: type[dict[Any, Any]]
    yaml_base_list_type: type[list[Any]]
    constructed_objects: dict[Node, Any]
    recursive_objects: dict[Node, Any]
    state_generators: list[Generator[Any, Any, Any]]
    deep_construct: bool
    allow_duplicate_keys: bool | None
    def __init__(self, preserve_quotes: bool | None = None, loader: YAML | _Loader | None = None) -> None: ...
    @property
    def composer(self) -> Composer: ...
    @property
    def resolver(self) -> BaseResolver: ...
    @property
    def scanner(self) -> Scanner: ...
    def check_data(self) -> bool: ...
    def get_data(self) -> Any: ...
    def get_single_data(self) -> Any: ...
    def construct_document(self, node: Node) -> Any: ...
    def construct_object(self, node: Node, deep: bool = False) -> Any: ...
    def construct_non_recursive_object(self, node: Node, tag: str | None = None) -> Any: ...
    def construct_scalar(self, node: ScalarNode) -> str: ...
    def construct_sequence(self, node: SequenceNode, deep: bool = False) -> list[Any]: ...
    def construct_mapping(self, node: MappingNode, deep: bool = False) -> dict[Any, Any]: ...
    def check_mapping_key(self, node: MappingNode, key_node: Node, mapping: Mapping[Any, Any], key: Any, value: Any) -> bool: ...
    def check_set_key(self, node: MappingNode, key_node: ScalarNode, setting: AbstractSet[Any], key: Any) -> None: ...
    def construct_pairs(self, node: MappingNode, deep: bool = False) -> list[tuple[Any, Any]]: ...
    @classmethod
    def add_constructor(
        cls, tag: Tag | str | None, constructor: _ConstructorFunction[Self]
    ) -> _ConstructorFunction[Self] | None: ...
    @classmethod
    def add_multi_constructor(cls, tag_prefix: str | None, multi_constructor: _MultiConstructorFunction[Self]) -> None: ...
    @classmethod
    def add_default_constructor(cls, tag: str, method: str | None = None, tag_base: str = "tag:yaml.org,2002:") -> None: ...

class SafeConstructor(BaseConstructor):
    def construct_scalar(self, node: ScalarNode) -> str: ...
    def flatten_mapping(self, node: MappingNode) -> list[Any] | None: ...
    def construct_mapping(self, node: MappingNode, deep: bool = False) -> dict[Any, Any]: ...
    def construct_yaml_null(self, node: ScalarNode) -> None: ...
    bool_values: Final[dict[str, bool]]
    def construct_yaml_bool(self, node: ScalarNode) -> bool: ...
    def construct_yaml_int(self, node: ScalarNode) -> int: ...
    inf_value: Final[float]
    nan_value: Final[float]
    def construct_yaml_float(self, node: ScalarNode) -> float: ...
    def construct_yaml_binary(self, node: ScalarNode) -> bytes: ...
    timestamp_regexp: Final = util.timestamp_regexp
    def construct_yaml_timestamp(self, node: ScalarNode, values: dict[str, str | None] | None = None) -> date | datetime: ...
    def construct_yaml_omap(self, node: SequenceNode) -> Iterator[ordereddict[Any, Any]]: ...
    def construct_yaml_pairs(self, node: SequenceNode) -> Iterator[list[tuple[Any, Any]]]: ...
    def construct_yaml_set(self, node: MappingNode) -> Iterator[set[Any]]: ...
    def construct_yaml_str(self, node: ScalarNode) -> str: ...
    def construct_yaml_seq(self, node: SequenceNode) -> Iterator[list[Any]]: ...
    def construct_yaml_map(self, node: MappingNode) -> Iterator[dict[Any, Any]]: ...
    def construct_yaml_object(self, node: MappingNode, cls: type[_T]) -> Iterator[_T]: ...
    def construct_undefined(self, node: Node) -> NoReturn: ...

class Constructor(SafeConstructor):
    def construct_python_str(self, node: ScalarNode) -> str: ...
    def construct_python_unicode(self, node: ScalarNode) -> str: ...
    def construct_python_bytes(self, node: ScalarNode) -> bytes: ...
    def construct_python_long(self, node: ScalarNode) -> int: ...
    def construct_python_complex(self, node: ScalarNode) -> complex: ...
    def construct_python_tuple(self, node: SequenceNode) -> tuple[Any, ...]: ...
    def find_python_module(self, name: str, mark: _Mark) -> ModuleType: ...
    def find_python_name(self, name: str, mark: _Mark) -> Any: ...
    def construct_python_name(self, suffix: str, node: ScalarNode) -> Any: ...
    def construct_python_module(self, suffix: str, node: ScalarNode) -> ModuleType: ...
    def make_python_instance(
        self,
        suffix: str,
        node: Node,
        args: Iterable[Any] | None = None,
        kwds: Mapping[str, Any] | None = None,
        newobj: bool = False,
    ) -> Any: ...
    def set_python_instance_state(self, instance, state) -> None: ...
    def construct_python_object(self, suffix: str, node: MappingNode) -> Iterator[Any]: ...
    def construct_python_object_apply(self, suffix: str, node: SequenceNode | MappingNode, newobj: bool = False) -> Any: ...
    def construct_python_object_new(self, suffix: str, node: SequenceNode | MappingNode) -> Any: ...
    @classmethod
    def add_default_constructor(
        cls, tag: str, method: str | None = None, tag_base: str = "tag:yaml.org,2002:python/"
    ) -> None: ...

class RoundTripConstructor(SafeConstructor):
    def comment(self, idx: int) -> ScannedComments: ...  # RTSC
    def comments(self, list_of_comments: list[list[int] | None], idx: int | None = None) -> Iterator[ScannedComments]: ...  # RTSC
    def construct_scalar(self, node: ScalarNode) -> str: ...
    def construct_yaml_int(self, node: ScalarNode) -> int: ...
    def construct_yaml_float(self, node: ScalarNode) -> float | ScalarFloat: ...
    def construct_yaml_str(self, node: ScalarNode) -> str | TaggedScalar: ...  # type: ignore[override]
    def construct_rt_sequence(self, node: SequenceNode, seqtyp: CommentedSeq[_T], deep: bool = False) -> list[_T]: ...
    def flatten_mapping(self, node: MappingNode) -> list[tuple[int, CommentedMap[Any, Any]]]: ...
    def construct_mapping(self, node: MappingNode, maptyp: CommentedMap[Any, Any], deep: bool = False) -> None: ...  # type: ignore[override]
    def construct_setting(self, node: MappingNode, typ: CommentedSet[Any], deep: bool = False) -> None: ...
    def construct_yaml_seq(self, node: SequenceNode) -> Iterator[CommentedSeq[Any]]: ...
    def construct_yaml_map(self, node: MappingNode) -> Iterator[CommentedMap[Any, Any]]: ...
    def set_collection_style(
        self, data: CommentedSeq[Any] | CommentedMap[Any, Any], node: SequenceNode | MappingNode
    ) -> None: ...
    def construct_yaml_object(self, node: MappingNode, cls: type[_T]) -> Iterator[_T]: ...
    def construct_yaml_omap(self, node: SequenceNode) -> Iterator[CommentedOrderedMap[Any, Any]]: ...
    def construct_yaml_set(self, node: MappingNode) -> Iterator[CommentedSet[Any]]: ...  # type: ignore[override]
    @overload
    def construct_unknown(self, node: ScalarNode) -> Iterator[TaggedScalar]: ...
    @overload
    def construct_unknown(self, node: SequenceNode) -> Iterator[CommentedSeq[Any]]: ...
    @overload
    def construct_unknown(self, node: MappingNode) -> Iterator[CommentedMap[Any, Any]]: ...
    def construct_yaml_timestamp(
        self, node: ScalarNode, values: dict[str, str | None] | None = None
    ) -> date | datetime | TimeStamp: ...
    def construct_yaml_sbool(self, node: ScalarNode) -> bool | ScalarBoolean: ...
