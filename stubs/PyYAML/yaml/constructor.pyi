from collections.abc import Callable, Hashable
from datetime import date
from re import Pattern
from typing import Any, ClassVar, TypeVar
from typing_extensions import TypeAlias

from yaml.error import MarkedYAMLError
from yaml.loader import BaseLoader, FullLoader, Loader, SafeLoader, UnsafeLoader
from yaml.nodes import MappingNode, Node, ScalarNode, SequenceNode

_L = TypeVar("_L", bound=Loader | BaseLoader | FullLoader | SafeLoader | UnsafeLoader)
_N = TypeVar("_N", bound=Node)

_Scalar: TypeAlias = str | int | float | bool | None

class ConstructorError(MarkedYAMLError): ...

class BaseConstructor:
    yaml_constructors: Any
    yaml_multi_constructors: Any
    constructed_objects: Any
    recursive_objects: Any
    state_generators: Any
    deep_construct: Any
    def __init__(self) -> None: ...
    def check_data(self): ...
    def check_state_key(self, key: str) -> None: ...
    def get_data(self): ...
    def get_single_data(self) -> Any: ...
    def construct_document(self, node): ...
    def construct_object(self, node, deep=...): ...
    def construct_scalar(self, node: ScalarNode) -> _Scalar: ...
    def construct_sequence(self, node: SequenceNode, deep: bool = ...) -> list[Any]: ...
    def construct_mapping(self, node: MappingNode, deep: bool = ...) -> dict[Hashable, Any]: ...
    def construct_pairs(self, node, deep=...): ...
    @classmethod
    # Use typevars so we can have covariant behaviour in the parameter types
    def add_constructor(cls, tag: str, constructor: Callable[[_L, _N], Any]) -> None: ...
    @classmethod
    def add_multi_constructor(cls, tag_prefix, multi_constructor): ...

class SafeConstructor(BaseConstructor):
    def construct_scalar(self, node: ScalarNode) -> _Scalar: ...
    def flatten_mapping(self, node: MappingNode) -> None: ...
    def construct_mapping(self, node: MappingNode, deep: bool = ...) -> dict[Hashable, Any]: ...
    def construct_yaml_null(self, node: ScalarNode) -> None: ...
    bool_values: ClassVar[dict[str, bool]]
    def construct_yaml_bool(self, node: ScalarNode) -> bool: ...
    def construct_yaml_int(self, node: ScalarNode) -> int: ...
    inf_value: ClassVar[float]
    nan_value: ClassVar[float]
    def construct_yaml_float(self, node: ScalarNode) -> float: ...
    def construct_yaml_binary(self, node: ScalarNode) -> bytes: ...
    timestamp_regexp: ClassVar[Pattern[str]]
    def construct_yaml_timestamp(self, node: ScalarNode) -> date: ...
    def construct_yaml_omap(self, node): ...
    def construct_yaml_pairs(self, node): ...
    def construct_yaml_set(self, node): ...
    def construct_yaml_str(self, node): ...
    def construct_yaml_seq(self, node): ...
    def construct_yaml_map(self, node): ...
    def construct_yaml_object(self, node, cls): ...
    def construct_undefined(self, node): ...

class FullConstructor(SafeConstructor):
    def get_state_keys_blacklist(self) -> list[str]: ...
    def get_state_keys_blacklist_regexp(self) -> Pattern[str]: ...
    def construct_python_str(self, node): ...
    def construct_python_unicode(self, node): ...
    def construct_python_bytes(self, node): ...
    def construct_python_long(self, node): ...
    def construct_python_complex(self, node): ...
    def construct_python_tuple(self, node): ...
    def find_python_module(self, name, mark, unsafe=...): ...
    def find_python_name(self, name, mark, unsafe=...): ...
    def construct_python_name(self, suffix, node): ...
    def construct_python_module(self, suffix, node): ...
    def make_python_instance(self, suffix, node, args=..., kwds=..., newobj=..., unsafe=...): ...
    def set_python_instance_state(self, instance, state, unsafe: bool = ...) -> None: ...
    def construct_python_object(self, suffix, node): ...
    def construct_python_object_apply(self, suffix, node, newobj=...): ...
    def construct_python_object_new(self, suffix, node): ...

class UnsafeConstructor(FullConstructor):
    def find_python_module(self, name, mark): ...
    def find_python_name(self, name, mark): ...
    def make_python_instance(self, suffix, node, args=..., kwds=..., newobj=...): ...
    def set_python_instance_state(self, instance, state): ...

class Constructor(SafeConstructor):
    def construct_python_str(self, node): ...
    def construct_python_unicode(self, node): ...
    def construct_python_long(self, node): ...
    def construct_python_complex(self, node): ...
    def construct_python_tuple(self, node): ...
    def find_python_module(self, name, mark): ...
    def find_python_name(self, name, mark): ...
    def construct_python_name(self, suffix, node): ...
    def construct_python_module(self, suffix, node): ...
    def make_python_instance(self, suffix, node, args=..., kwds=..., newobj=...): ...
    def set_python_instance_state(self, instance, state): ...
    def construct_python_object(self, suffix, node): ...
    def construct_python_object_apply(self, suffix, node, newobj=...): ...
    def construct_python_object_new(self, suffix, node): ...
