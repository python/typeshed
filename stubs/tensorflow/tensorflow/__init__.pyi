from _typeshed import Incomplete, Unused
from abc import ABCMeta
from builtins import bool as _bool
from collections.abc import Callable, Iterable, Iterator, Sequence
from contextlib import contextmanager
from enum import Enum
from types import TracebackType
from typing import Any, NoReturn, TypeVar, overload
from typing_extensions import ParamSpec, Self, TypeAlias

import numpy
from tensorflow import initializers as initializers, keras as keras, math as math

# Explicit import of DType is covered by the wildcard, but
# is necessary to avoid a crash in pytype.
from tensorflow.dtypes import *
from tensorflow.dtypes import DType as DType

# Most tf.math functions are exported as tf, but sadly not all are.
from tensorflow.math import (
    abs as abs,
    add as add,
    add_n as add_n,
    argmax as argmax,
    argmin as argmin,
    cos as cos,
    cosh as cosh,
    divide as divide,
    equal as equal,
    greater as greater,
    greater_equal as greater_equal,
    less as less,
    less_equal as less_equal,
    logical_and as logical_and,
    logical_not as logical_not,
    logical_or as logical_or,
    maximum as maximum,
    minimum as minimum,
    multiply as multiply,
    not_equal as not_equal,
    pow as pow,
    reduce_max as reduce_max,
    reduce_mean as reduce_mean,
    reduce_min as reduce_min,
    reduce_prod as reduce_prod,
    reduce_sum as reduce_sum,
    sigmoid as sigmoid,
    sign as sign,
    sin as sin,
    sinh as sinh,
    sqrt as sqrt,
    square as square,
    subtract as subtract,
    tanh as tanh,
)
from tensorflow.sparse import SparseTensor

# Tensors ideally should be a generic type, but properly typing data type/shape
# will be a lot of work. Until we have good non-generic tensorflow stubs,
# we will skip making Tensor generic. Also good type hints for shapes will
# run quickly into many places where type system is not strong enough today.
# So shape typing is probably not worth doing anytime soon.
_Slice: TypeAlias = int | slice | None

_FloatDataSequence: TypeAlias = Sequence[float] | Sequence[_FloatDataSequence]
_StrDataSequence: TypeAlias = Sequence[str] | Sequence[_StrDataSequence]
_ScalarTensorCompatible: TypeAlias = Tensor | str | float | numpy.ndarray[Any, Any] | numpy.number[Any]
_TensorCompatible: TypeAlias = _ScalarTensorCompatible | Sequence[_TensorCompatible]
_ShapeLike: TypeAlias = TensorShape | Iterable[_ScalarTensorCompatible | None] | int | Tensor
_DTypeLike: TypeAlias = DType | str | numpy.dtype[Any]

class Tensor:
    def __init__(self, op: Operation, value_index: int, dtype: DType) -> None: ...
    def consumers(self) -> list[Incomplete]: ...
    @property
    def shape(self) -> TensorShape: ...
    def get_shape(self) -> TensorShape: ...
    @property
    def dtype(self) -> DType: ...
    @property
    def graph(self) -> Graph: ...
    @property
    def name(self) -> str: ...
    @property
    def op(self) -> Operation: ...
    def numpy(self) -> numpy.ndarray[Any, Any]: ...
    def __int__(self) -> int: ...
    def __abs__(self, name: str | None = None) -> Tensor: ...
    def __add__(self, other: _TensorCompatible) -> Tensor: ...
    def __radd__(self, other: _TensorCompatible) -> Tensor: ...
    def __sub__(self, other: _TensorCompatible) -> Tensor: ...
    def __rsub__(self, other: _TensorCompatible) -> Tensor: ...
    def __mul__(self, other: _TensorCompatible) -> Tensor: ...
    def __rmul__(self, other: _TensorCompatible) -> Tensor: ...
    def __pow__(self, other: _TensorCompatible) -> Tensor: ...
    def __matmul__(self, other: _TensorCompatible) -> Tensor: ...
    def __rmatmul__(self, other: _TensorCompatible) -> Tensor: ...
    def __floordiv__(self, other: _TensorCompatible) -> Tensor: ...
    def __rfloordiv__(self, other: _TensorCompatible) -> Tensor: ...
    def __truediv__(self, other: _TensorCompatible) -> Tensor: ...
    def __rtruediv__(self, other: _TensorCompatible) -> Tensor: ...
    def __neg__(self, name: str | None = None) -> Tensor: ...
    def __and__(self, other: _TensorCompatible) -> Tensor: ...
    def __rand__(self, other: _TensorCompatible) -> Tensor: ...
    def __or__(self, other: _TensorCompatible) -> Tensor: ...
    def __ror__(self, other: _TensorCompatible) -> Tensor: ...
    def __eq__(self, other: _TensorCompatible) -> Tensor: ...  # type: ignore[override]
    def __ne__(self, other: _TensorCompatible) -> Tensor: ...  # type: ignore[override]
    def __ge__(self, other: _TensorCompatible, name: str | None = None) -> Tensor: ...
    def __gt__(self, other: _TensorCompatible, name: str | None = None) -> Tensor: ...
    def __le__(self, other: _TensorCompatible, name: str | None = None) -> Tensor: ...
    def __lt__(self, other: _TensorCompatible, name: str | None = None) -> Tensor: ...
    def __bool__(self) -> NoReturn: ...
    def __getitem__(self, slice_spec: _Slice | tuple[_Slice, ...]) -> Tensor: ...
    def __len__(self) -> int: ...
    # This only works for rank 0 tensors.
    def __index__(self) -> int: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class VariableSynchronization(Enum):
    AUTO = 0
    NONE = 1
    ON_WRITE = 2
    ON_READ = 3

class VariableAggregation(Enum):
    AUTO = 0
    NONE = 1
    ON_WRITE = 2
    ON_READ = 3

class _VariableMetaclass(type): ...

# Variable class in intent/documentation is a Tensor. In implementation there's
# TODO comment to make it Tensor. It is not actually Tensor type wise, but even
# dynamically patches on most methods of tf.Tensor
# https://github.com/tensorflow/tensorflow/blob/9524a636cae9ae3f0554203c1ba7ee29c85fcf12/tensorflow/python/ops/variables.py#L1086.
class Variable(Tensor, metaclass=_VariableMetaclass):
    def __init__(
        self,
        initial_value: Tensor | Callable[[], Tensor] | None = None,
        trainable: _bool | None = None,
        validate_shape: _bool = True,
        # Valid non-None values are deprecated.
        caching_device: None = None,
        name: str | None = None,
        # Real type is VariableDef protobuf type. Can be added after adding script
        # to generate tensorflow protobuf stubs with mypy-protobuf.
        variable_def: Incomplete | None = None,
        dtype: _DTypeLike | None = None,
        import_scope: str | None = None,
        constraint: Callable[[Tensor], Tensor] | None = None,
        synchronization: VariableSynchronization = ...,
        aggregation: VariableAggregation = ...,
        shape: _ShapeLike | None = None,
        experimental_enable_variable_lifting: _bool = True,
    ) -> None: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class RaggedTensor(metaclass=ABCMeta):
    def bounding_shape(
        self, axis: _TensorCompatible | None = None, name: str | None = None, out_type: _DTypeLike | None = None
    ) -> Tensor: ...
    @classmethod
    def from_sparse(cls, st_input: SparseTensor, name: str | None = None, row_splits_dtype: _DTypeLike = ...) -> RaggedTensor: ...
    def to_sparse(self, name: str | None = None) -> SparseTensor: ...
    def to_tensor(
        self, default_value: float | str | None = None, name: str | None = None, shape: _ShapeLike | None = None
    ) -> Tensor: ...
    def __add__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __radd__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __sub__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __mul__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __rmul__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __floordiv__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __truediv__(self, other: RaggedTensor | float, name: str | None = None) -> RaggedTensor: ...
    def __getitem__(self, slice_spec: _Slice | tuple[_Slice, ...]) -> RaggedTensor: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class Operation:
    def __init__(
        self,
        node_def: Incomplete,
        g: Graph,
        # isinstance is used so can not be Sequence/Iterable.
        inputs: list[Tensor] | None = None,
        output_types: Unused = None,
        control_inputs: Iterable[Tensor | Operation] | None = None,
        input_types: Iterable[DType] | None = None,
        original_op: Operation | None = None,
        op_def: Incomplete = None,
    ) -> None: ...
    @property
    def inputs(self) -> list[Tensor]: ...
    @property
    def outputs(self) -> list[Tensor]: ...
    @property
    def device(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def type(self) -> str: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class TensorShape(metaclass=ABCMeta):
    def __init__(self, dims: _ShapeLike) -> None: ...
    @property
    def rank(self) -> int: ...
    def as_list(self) -> list[int | None]: ...
    def assert_has_rank(self, rank: int) -> None: ...
    def assert_is_compatible_with(self, other: Iterable[int | None]) -> None: ...
    def __bool__(self) -> _bool: ...
    @overload
    def __getitem__(self, key: int) -> int | None: ...
    @overload
    def __getitem__(self, key: slice) -> TensorShape: ...
    def __iter__(self) -> Iterator[int | None]: ...
    def __len__(self) -> int: ...
    def __add__(self, other: Iterable[int | None]) -> TensorShape: ...
    def __radd__(self, other: Iterable[int | None]) -> TensorShape: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class Graph:
    def add_to_collection(self, name: str, value: object) -> None: ...
    def add_to_collections(self, names: Iterable[str] | str, value: object) -> None: ...
    @contextmanager
    def as_default(self) -> Iterator[Self]: ...
    def finalize(self) -> None: ...
    def get_tensor_by_name(self, name: str) -> Tensor: ...
    def get_operation_by_name(self, name: str) -> Operation: ...
    def get_operations(self) -> list[Operation]: ...
    def get_name_scope(self) -> str: ...
    def __getattr__(self, name: str) -> Incomplete: ...

class IndexedSlices(metaclass=ABCMeta):
    def __init__(self, values: Tensor, indices: Tensor, dense_shape: None | Tensor = None) -> None: ...
    @property
    def values(self) -> Tensor: ...
    @property
    def indices(self) -> Tensor: ...
    @property
    def dense_shape(self) -> None | Tensor: ...
    @property
    def shape(self) -> TensorShape: ...
    @property
    def dtype(self) -> DType: ...
    @property
    def name(self) -> str: ...
    @property
    def op(self) -> Operation: ...
    @property
    def graph(self) -> Graph: ...
    @property
    def device(self) -> str: ...
    def __neg__(self) -> IndexedSlices: ...
    def consumers(self) -> list[Operation]: ...

class name_scope:
    def __init__(self, name: str) -> None: ...
    def __enter__(self) -> str: ...
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...

_P = ParamSpec("_P")
_R = TypeVar("_R")

class Module:
    def __init__(self, name: str | None = None) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def name_scope(self) -> name_scope: ...
    # Documentation only specifies these as returning Sequence. Actual
    # implementation does tuple.
    @property
    def variables(self) -> Sequence[Variable]: ...
    @property
    def trainable_variables(self) -> Sequence[Variable]: ...
    @property
    def non_trainable_variables(self) -> Sequence[Variable]: ...
    @property
    def submodules(self) -> Sequence[Module]: ...
    @classmethod
    def with_name_scope(cls, method: Callable[_P, _R]) -> Callable[_P, _R]: ...

def __getattr__(name: str) -> Incomplete: ...
