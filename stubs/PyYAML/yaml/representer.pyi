import datetime
from _typeshed import Incomplete, ReadableBuffer, SupportsItems
from collections.abc import Callable, Iterable, Mapping
from types import BuiltinFunctionType, FunctionType, ModuleType
from typing import Any, ClassVar, NoReturn, TypeVar
from typing_extensions import Self

from yaml.error import YAMLError as YAMLError
from yaml.nodes import MappingNode as MappingNode, Node as Node, ScalarNode as ScalarNode, SequenceNode as SequenceNode

_T = TypeVar("_T")
_R = TypeVar("_R", bound=BaseRepresenter)

class RepresenterError(YAMLError): ...

class BaseRepresenter:
    yaml_representers: ClassVar[dict[type[Any], Callable[[BaseRepresenter, Any], Node]]]
    yaml_multi_representers: ClassVar[dict[type[Any], Callable[[BaseRepresenter, Any], Node]]]
    default_style: str | Incomplete
    sort_keys: bool
    default_flow_style: bool
    represented_objects: dict[int, Node]
    object_keeper: list[Any]
    alias_key: int | Incomplete
    def __init__(self, default_style: str | None = None, default_flow_style: bool = False, sort_keys: bool = True) -> None: ...
    def represent(self, data) -> None: ...
    def represent_data(self, data) -> Node: ...
    @classmethod
    def add_representer(cls, data_type: type[_T], representer: Callable[[Self, _T], Node]) -> None: ...
    @classmethod
    def add_multi_representer(cls, data_type: type[_T], representer: Callable[[Self, _T], Node]) -> None: ...
    def represent_scalar(self, tag: str, value, style: str | None = None) -> ScalarNode: ...
    def represent_sequence(self, tag: str, sequence: Iterable[Any], flow_style: bool | None = None) -> SequenceNode: ...
    def represent_mapping(
        self, tag: str, mapping: SupportsItems[Any, Any] | Iterable[tuple[Any, Any]], flow_style: bool | None = None
    ) -> MappingNode: ...
    def ignore_aliases(self, data) -> bool: ...

class SafeRepresenter(BaseRepresenter):
    inf_value: ClassVar[float]
    def ignore_aliases(self, data) -> bool: ...
    def represent_none(self, data) -> ScalarNode: ...
    def represent_str(self, data: str) -> ScalarNode: ...
    def represent_binary(self, data: ReadableBuffer) -> ScalarNode: ...
    def represent_bool(self, data: bool) -> ScalarNode: ...
    def represent_int(self, data: int) -> ScalarNode: ...
    def represent_float(self, data: float) -> ScalarNode: ...
    def represent_list(self, data: Iterable[Any]) -> SequenceNode: ...
    def represent_dict(self, data: SupportsItems[Any, Any] | Iterable[tuple[Any, Any]]) -> MappingNode: ...
    def represent_set(self, data: Iterable[Any]) -> MappingNode: ...
    def represent_date(self, data: datetime.date) -> ScalarNode: ...
    def represent_datetime(self, data: datetime.datetime) -> ScalarNode: ...
    def represent_yaml_object(self, tag: str, data, cls, flow_style: bool | None = None) -> MappingNode: ...
    def represent_undefined(self, data) -> NoReturn: ...

class Representer(SafeRepresenter):
    def represent_complex(self, data: complex) -> ScalarNode: ...
    def represent_tuple(self, data: Iterable[Any]) -> SequenceNode: ...
    def represent_name(self, data: BuiltinFunctionType | FunctionType) -> ScalarNode: ...
    def represent_module(self, data: ModuleType) -> ScalarNode: ...
    def represent_object(self, data) -> SequenceNode | MappingNode: ...
    def represent_ordered_dict(self, data: Mapping[Any, Any]) -> SequenceNode: ...

__all__ = ["BaseRepresenter", "SafeRepresenter", "Representer", "RepresenterError"]
