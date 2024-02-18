from typing import Any, Generic, TypeVar, overload
from typing_extensions import ParamSpec

import tensorflow as tf
from tensorflow._aliases import ContainerGeneric
from tensorflow.python.framework.func_graph import FuncGraph

_P = ParamSpec("_P")
_R = TypeVar("_R", covariant=True)

class Callable(Generic[_P, _R]):
    def __call__(self, *args: _P.args, **kwargs: _P.kwargs) -> _R: ...

class GenericFunction(Callable[_P, _R]):
    @overload
    def get_concrete_function(self, *args: _P.args, **kwargs: _P.kwargs) -> ConcreteFunction[_P, _R]: ...
    @overload
    def get_concrete_function(  # type: ignore
        self, *args: ContainerGeneric[tf.TypeSpec[Any]], **kwargs: ContainerGeneric[tf.TypeSpec[Any]]
    ) -> ConcreteFunction[_P, _R]: ...

class ConcreteFunction(Callable[_P, _R]):
    @property
    def structured_input_signature(self) -> tuple[tuple[Any, ...], dict[str, tf.TypeSpec[Any]]]: ...
    @property
    def structured_outputs(self) -> dict[str, tf.Tensor | tf.SparseTensor | tf.RaggedTensor | tf.TypeSpec[Any]]: ...
    @property
    def graph(self) -> FuncGraph: ...
    @property
    def inputs(self) -> list[tf.Tensor]: ...
    @property
    def outputs(self) -> list[tf.Tensor]: ...
