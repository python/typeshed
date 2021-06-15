import datetime
import sys
from _typeshed import SupportsItems
from types import BuiltinFunctionType, FunctionType, ModuleType
from typing import Any, Callable, ClassVar, Iterable, Mapping, NoReturn, Tuple, Type, TypeVar, Union

from yaml.error import YAMLError as YAMLError
from yaml.nodes import MappingNode as MappingNode, Node as Node, ScalarNode as ScalarNode, SequenceNode as SequenceNode

_T = TypeVar("_T")
_R = TypeVar("_R", bound=BaseRepresenter)

MappingLike = Union[SupportsItems[Any, Any], Iterable[Tuple[Any, Any]]]

class RepresenterError(YAMLError): ...

class BaseRepresenter:
    yaml_representers: ClassVar[dict[Type[Any], Callable[[BaseRepresenter, Any], Node]]]
    yaml_multi_representers: ClassVar[dict[Type[Any], Callable[[BaseRepresenter, Any], Node]]]
    default_style: str | Any
    sort_keys: bool
    default_flow_style: bool
    represented_objects: dict[int, Node]
    object_keeper: list[Any]
    alias_key: int | Any
    def __init__(self, default_style: str | None = ..., default_flow_style: bool = ..., sort_keys: bool = ...) -> None: ...
    def represent(self, data) -> None: ...
    def represent_data(self, data) -> Node: ...
    if sys.version_info < (3, 0):
        def get_classobj_bases(self, cls): ...
    @classmethod
    def add_representer(cls: Type[_R], data_type: Type[_T], representer: Callable[[_R, _T], Node]) -> None: ...
    @classmethod
    def add_multi_representer(cls: Type[_R], data_type: Type[_T], representer: Callable[[_R, _T], Node]) -> None: ...
    def represent_scalar(self, tag: str, value, style: str | None = ...) -> ScalarNode: ...
    def represent_sequence(self, tag: str, sequence: Iterable[Any], flow_style: bool | None = ...) -> SequenceNode: ...
    def represent_mapping(self, tag: str, mapping: MappingLike, flow_style: bool | None = ...) -> MappingNode: ...
    def ignore_aliases(self, data) -> bool: ...

class SafeRepresenter(BaseRepresenter):
    inf_value: ClassVar[float]
    def ignore_aliases(self, data) -> bool: ...
    def represent_none(self, data) -> ScalarNode: ...
    def represent_str(self, data: str) -> ScalarNode: ...
    if sys.version_info < (3, 0):
        def represent_unicode(self, data): ...
        def represent_long(self, data): ...
    def represent_binary(self, data: bytes) -> ScalarNode: ...
    def represent_bool(self, data: bool) -> ScalarNode: ...
    def represent_int(self, data: int) -> ScalarNode: ...
    def represent_float(self, data: float) -> ScalarNode: ...
    def represent_list(self, data: Iterable[Any]) -> SequenceNode: ...
    def represent_dict(self, data: MappingLike) -> MappingNode: ...
    def represent_set(self, data: Iterable[Any]) -> MappingNode: ...
    def represent_date(self, data: datetime.date) -> ScalarNode: ...
    def represent_datetime(self, data: datetime.datetime) -> ScalarNode: ...
    def represent_yaml_object(self, tag: str, data, cls, flow_style: bool | None = ...) -> MappingNode: ...
    def represent_undefined(self, data) -> NoReturn: ...

class Representer(SafeRepresenter):
    if sys.version_info < (3, 0):
        def represent_unicode(self, data): ...
        def represent_long(self, data): ...
        def represent_instance(self, data): ...
    def represent_complex(self, data: complex) -> ScalarNode: ...
    def represent_tuple(self, data: Iterable[Any]) -> SequenceNode: ...
    def represent_name(self, data: BuiltinFunctionType | FunctionType) -> ScalarNode: ...
    def represent_module(self, data: ModuleType) -> ScalarNode: ...
    def represent_object(self, data) -> SequenceNode | MappingNode: ...
    def represent_ordered_dict(self, data: Mapping[Any, Any]) -> SequenceNode: ...
