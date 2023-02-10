from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Sequence
from typing import Any, Generic, TypeVar, overload
from typing_extensions import Self, TypeAlias

import tensorflow as tf
from tensorflow import DTypeLike, Tensor, Variable, _TensorCompatible
from tensorflow._aliases import _AnyArray, _ContainerGeneric
from tensorflow.keras.activations import _Activation
from tensorflow.keras.constraints import _Constraint
from tensorflow.keras.initializers import _Initializer
from tensorflow.keras.regularizers import _Regularizer

_InputT = TypeVar("_InputT", contravariant=True)
_OutputT = TypeVar("_OutputT", covariant=True)

class InputSpec:
    dtype: str | None
    shape: tuple[int | None, ...]
    ndim: int | None
    max_ndim: int | None
    min_ndim: int | None
    axes: dict[int, int | None] | None
    def __init__(
        self,
        dtype: tf._DTypeLike | None = None,
        shape: Iterable[int | None] | None = None,
        ndim: int | None = None,
        max_ndim: int | None = None,
        min_ndim: int | None = None,
        axes: dict[int, int | None] | None = None,
        allow_last_axis_squeeze: bool = False,
        name: str | None = None,
    ): ...
    def get_config(self) -> dict[str, Any]: ...
    @classmethod
    def from_config(cls, config: dict[str, Any]) -> type[Self]: ...

_InputSpecs: TypeAlias = _ContainerGeneric[InputSpec]

# Most layers have input and output type of just Tensor and when we support default type variables,
# maybe worth trying.
class Layer(Generic[_InputT, _OutputT], tf.Module):
    input_spec: _InputSpecs

    @property
    def trainable(self) -> bool: ...
    @trainable.setter
    def trainable(self, value: bool) -> None: ...
    def __init__(
        self, trainable: bool = True, name: str | None = None, dtype: DTypeLike | None = None, dynamic: bool = False
    ) -> None: ...

    # *args/**kwargs are allowed, but have obscure footguns and tensorflow documentation discourages their usage.
    # First argument will automatically be cast to layer's compute dtype, but any other tensor arguments will not be.
    # Also various tensorflow tools/apis can misbehave if they encounter a layer with *args/**kwargs.
    def __call__(self, inputs: _InputT, /, *, training: bool = False, mask: _TensorCompatible | None = None) -> _OutputT: ...
    def call(self, inputs: _InputT, /) -> _OutputT: ...

    # input_shape's real type depends on _InputT, but we can't express that without HKT.
    # For example _InputT tf.Tensor -> tf.TensorShape, _InputT dict[str, tf.Tensor] -> dict[str, tf.TensorShape].
    def build(self, input_shape: Any) -> None: ...
    @overload
    def compute_output_shape(self: Layer[tf.Tensor, tf.Tensor], input_shape: tf.TensorShape) -> tf.TensorShape: ...
    @overload
    def compute_output_shape(self, input_shape: Any) -> Any: ...
    def add_weight(
        self,
        name: str | None = None,
        shape: Iterable[int | None] | None = None,
        dtype: tf._DTypeLike | None = None,
        initializer: _Initializer | None = None,
        regularizer: _Regularizer = None,
        constraint: _Constraint = None,
        trainable: bool | None = None,
    ) -> tf.Variable: ...
    def add_loss(self, losses: tf.Tensor | Sequence[tf.Tensor] | Callable[[], tf.Tensor]) -> None: ...
    def count_params(self) -> int: ...
    @property
    def trainable_variables(self) -> list[Variable]: ...
    @property
    def non_trainable_variables(self) -> list[Variable]: ...
    @property
    def trainable_weights(self) -> list[Variable]: ...
    @property
    def non_trainable_weights(self) -> list[Variable]: ...
    @property
    def losses(self) -> list[Tensor]: ...
    def get_weights(self) -> list[_AnyArray]: ...
    def set_weights(self, weights: Sequence[_AnyArray]) -> None: ...
    def get_config(self) -> dict[str, Any]: ...
    @classmethod
    def from_config(cls: type[Self], config: dict[str, Any]) -> Self: ...
    def __getattr__(name: str) -> Incomplete: ...

class Dense(Layer[tf.Tensor, tf.Tensor]):
    input_spec: InputSpec
    def __init__(
        self,
        units: int,
        activation: _Activation = None,
        use_bias: bool = True,
        kernel_initializer: _Initializer = "glorot_uniform",
        bias_initializer: _Initializer = "zeros",
        kernel_regularizer: _Regularizer = None,
        bias_regularizer: _Regularizer = None,
        activity_regularizer: _Regularizer = None,
        kernel_constraint: _Constraint = None,
        bias_constraint: _Constraint = None,
        name: str | None = None,
    ) -> None: ...

class BatchNormalization(Layer[tf.Tensor, tf.Tensor]):
    def __init__(
        self,
        axis: int = -1,
        momentum: float = 0.99,
        epsilon: float = 0.001,
        center: bool = True,
        scale: bool = True,
        beta_initializer: _Initializer = "zeros",
        gamma_initializer: _Initializer = "ones",
        moving_mean_initializer: _Initializer = "zeros",
        moving_variance_initializer: _Initializer = "ones",
        beta_regularizer: _Regularizer = None,
        gamma_regularizer: _Regularizer = None,
        beta_constraint: _Constraint = None,
        gamma_constraint: _Constraint = None,
        name: str | None = None,
    ): ...

class ReLU(Layer[tf.Tensor, tf.Tensor]):
    def __init__(
        self,
        max_value: float | None = None,
        negative_slope: float | None = 0.0,
        threshold: float | None = 0.0,
        name: str | None = None,
    ) -> None: ...

class Dropout(Layer[tf.Tensor, tf.Tensor]):
    def __init__(
        self,
        rate: float,
        noise_shape: _TensorCompatible | Sequence[int | None] | None = None,
        seed: int | None = None,
        name: str | None = None,
    ) -> None: ...

class Embedding(Layer[tf.Tensor, tf.Tensor]):
    def __init__(
        self,
        input_dim: int,
        output_dim: int,
        embeddings_initializer: _Initializer = "uniform",
        embeddings_regularizer: _Regularizer = None,
        embeddings_constraint: _Constraint = None,
        mask_zero: bool = False,
        input_length: int | None = None,
        name: str | None = None,
    ): ...

def __getattr__(name: str) -> Incomplete: ...
