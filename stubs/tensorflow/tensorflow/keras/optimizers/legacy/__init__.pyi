from _typeshed import Incomplete
from collections.abc import Callable, Iterable
from typing import Any
from typing_extensions import Self, TypeAlias

import tensorflow as tf
from tensorflow._aliases import Gradients
from tensorflow._internal import Trackable
from tensorflow.keras.optimizers import schedules as schedules

_Initializer: TypeAlias = str | Callable[[], tf.Tensor] | dict[str, Any]
_Shape: TypeAlias = tf.TensorShape | Iterable[int | None]
_Dtype: TypeAlias = tf.DType | str | None
_LearningRate: TypeAlias = float | tf.Tensor | schedules.LearningRateSchedule | Callable[[], float | tf.Tensor]
_GradientAggregator: TypeAlias = Callable[[list[tuple[Gradients, tf.Variable]]], list[tuple[Gradients, tf.Variable]]] | None
_GradientTransformer: TypeAlias = (
    Iterable[Callable[[list[tuple[Gradients, tf.Variable]]], list[tuple[Gradients, tf.Variable]]]] | None
)

class Optimizer(Trackable):
    _name: str
    _iterations: tf.Variable | None
    _weights: list[tf.Variable]
    gradient_aggregator: _GradientAggregator
    gradient_transformers: _GradientTransformer
    learning_rate: _LearningRate
    def __init__(
        self,
        name: str | None = None,
        gradient_aggregator: _GradientAggregator = None,
        gradient_transformers: _GradientTransformer = None,
        clipvalue: float | None = None,
        clipnorm: float | None = None,
        global_clipnorm: float | None = None,
    ) -> None: ...
    def _create_all_weights(self, var_list: Iterable[tf.Variable]) -> None: ...
    @property
    def iterations(self) -> tf.Variable: ...
    @iterations.setter
    def iterations(self, variable: tf.Variable) -> None: ...
    def add_slot(
        self, var: tf.Variable, slot_name: str, initializer: _Initializer = "zeros", shape: tf.TensorShape | None = None
    ) -> tf.Variable: ...
    def add_weight(
        self,
        name: str,
        shape: _Shape,
        dtype: _Dtype = None,
        trainable: None | bool = None,
        synchronization: tf.VariableSynchronization = ...,
        aggregation: tf.VariableAggregation = ...,
    ) -> tf.Variable: ...
    def apply_gradients(
        self,
        grads_and_vars: Iterable[tuple[Gradients, tf.Variable]],
        name: str | None = None,
        experimental_aggregate_gradients: bool = True,
    ) -> tf.Operation | None: ...
    @classmethod
    def from_config(cls, config: dict[str, Any], custom_objects: dict[str, type] | None = None) -> Self: ...
    def get_config(self) -> dict[str, Any]: ...
    def get_slot(self, var: tf.Variable, slot_name: str) -> tf.Variable: ...
    def get_slot_names(self) -> list[str]: ...
    def get_gradients(self, loss: tf.Tensor, params: list[tf.Variable]) -> list[tf.Tensor]: ...
    def minimize(
        self,
        loss: tf.Tensor | Callable[[], tf.Tensor],
        var_list: list[tf.Variable] | tuple[tf.Variable, ...] | Callable[[], list[tf.Variable] | tuple[tf.Variable, ...]],
        grad_loss: tf.Tensor | None = None,
        name: str | None = None,
        tape: tf.GradientTape | None = None,
    ) -> tf.Operation: ...
    def variables(self) -> list[tf.Variable]: ...
    @property
    def weights(self) -> list[tf.Variable]: ...

class Adam(Optimizer):
    def __init__(
        self,
        learning_rate: _LearningRate = 0.001,
        beta_1: float = 0.9,
        beta_2: float = 0.999,
        epsilon: float = 1e-07,
        amsgrad: bool = False,
        name: str | None = "Adam",
    ) -> None: ...

class Adagrad(Optimizer):
    _initial_accumulator_value: float

class SGD(Optimizer):
    def __init__(
        self,
        learning_rate: _LearningRate = 0.01,
        momentum: float = 0.0,
        nesterov: bool = False,
        name: str | None = None,
        clipvalue: float | None = None,
        clipnorm: float | None = None,
        global_clipnorm: float | None = None,
        gradient_aggregator: _GradientAggregator = None,
        gradient_transformers: _GradientTransformer = None,
    ) -> None: ...

def __getattr__(name: str) -> Incomplete: ...
