from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from collections.abc import Callable, Iterable, Sequence
from typing import Any, Literal
from typing_extensions import Self, TypeAlias

import tensorflow as tf
from tensorflow import Operation, Tensor, _DTypeLike, _ShapeLike, _TensorCompatible
from tensorflow._aliases import KerasSerializable
from tensorflow.keras.initializers import _Initializer

_Output: TypeAlias = Tensor | dict[str, Tensor]

class Metric(tf.keras.layers.Layer[tf.Tensor, tf.Tensor], metaclass=ABCMeta):
    trainable_weights: list[Incomplete]
    non_trainable_weights: Incomplete
    _trackable_saved_model_saver: Incomplete

    def __init__(self, name: str | None = None, dtype: _DTypeLike | None = None) -> None: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> Self: ...
    def __call__(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def __str__(self) -> str: ...
    def __deepcopy__(self, memo: Incomplete | None = None) -> Incomplete: ...
    def merge_state(self, metrics: Iterable[Self]) -> list[Operation]: ...
    def reset_state(self) -> None: ...
    @abstractmethod
    def update_state(
        self, y_true: _TensorCompatible, y_pred: _TensorCompatible, sample_weight: _TensorCompatible | None = None
    ) -> Operation | None: ...
    @abstractmethod
    def result(self) -> _Output: ...
    @classmethod
    def from_config(cls, config: dict[str, Any]) -> Self: ...
    def get_config(self) -> dict[str, Any]: ...
    def add_weight(
        self,
        name: str,
        shape: _ShapeLike = (),
        aggregation: tf.VariableAggregation = tf.VariableAggregation.SUM,
        synchronization: tf.VariableSynchronization = tf.VariableSynchronization.ON_READ,
        initializer: _Initializer = None,
        dtype: _DTypeLike | None = None,
    ) -> Incomplete: ...

class AUC(Metric):
    _from_logits: bool
    _num_labels: int
    num_labels: int | None
    def __init__(
        self,
        num_thresholds: int = 200,
        curve: Literal["ROC", "PR"] = "ROC",
        summation_method: Literal["interpolation", "minoring", "majoring"] = "interpolation",
        name: str | None = None,
        dtype: _DTypeLike | None = None,
        thresholds: Sequence[float] | None = None,
        multi_label: bool = False,
        num_labels: int | None = None,
        label_weights: _TensorCompatible | None = None,
        from_logits: bool = False,
    ) -> None: ...
    def update_state(
        self, y_true: _TensorCompatible, y_pred: _TensorCompatible, sample_weight: _TensorCompatible | None = None
    ) -> Operation: ...
    def result(self) -> tf.Tensor: ...

class Precision(Metric):
    def __init__(
        self,
        thresholds: float | Sequence[float] | None = None,
        top_k: int | None = None,
        class_id: int | None = None,
        name: str | None = None,
        dtype: _DTypeLike | None = None,
    ) -> None: ...
    def update_state(
        self, y_true: _TensorCompatible, y_pred: _TensorCompatible, sample_weight: _TensorCompatible | None = None
    ) -> Operation: ...
    def result(self) -> tf.Tensor: ...

class Recall(Metric):
    def __init__(
        self,
        thresholds: float | Sequence[float] | None = None,
        top_k: int | None = None,
        class_id: int | None = None,
        name: str | None = None,
        dtype: _DTypeLike | None = None,
    ) -> None: ...
    def update_state(
        self, y_true: _TensorCompatible, y_pred: _TensorCompatible, sample_weight: _TensorCompatible | None = None
    ) -> Operation: ...
    def result(self) -> tf.Tensor: ...

class MeanMetricWrapper(Metric):
    def __init__(
        self, fn: Callable[[tf.Tensor, tf.Tensor], tf.Tensor], name: str | None = None, dtype: _DTypeLike | None = None
    ) -> None: ...
    def update_state(
        self, y_true: _TensorCompatible, y_pred: _TensorCompatible, sample_weight: _TensorCompatible | None = None
    ) -> Operation: ...
    def result(self) -> tf.Tensor: ...

class BinaryAccuracy(MeanMetricWrapper):
    def __init__(self, name: str | None = "binary_accuracy", dtype: _DTypeLike | None = None, threshold: float = 0.5) -> None: ...

class Accuracy(MeanMetricWrapper):
    def __init__(self, name: str | None = "accuracy", dtype: _DTypeLike | None = None) -> None: ...

class CategoricalAccuracy(MeanMetricWrapper):
    def __init__(self, name: str | None = "categorical_accuracy", dtype: _DTypeLike | None = None) -> None: ...

class TopKCategoricalAccuracy(MeanMetricWrapper):
    def __init__(self, k: int = 5, name: str | None = None, dtype: _DTypeLike | None = None) -> None: ...

class SparseTopKCategoricalAccuracy(MeanMetricWrapper):
    def __init__(self, k: int = 5, name: str | None = None, dtype: _DTypeLike | None = None) -> None: ...

def serialize(metric: KerasSerializable) -> dict[str, Any]: ...
def binary_crossentropy(
    y_true: _TensorCompatible, y_pred: _TensorCompatible, from_logits: bool = False, label_smoothing: float = 0.0, axis: int = -1
) -> Tensor: ...
def categorical_crossentropy(
    y_true: _TensorCompatible, y_pred: _TensorCompatible, from_logits: bool = False, label_smoothing: float = 0.0, axis: int = -1
) -> Tensor: ...
def __getattr__(name: str) -> Incomplete: ...
