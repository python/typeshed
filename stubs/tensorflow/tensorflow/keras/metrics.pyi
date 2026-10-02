from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from collections.abc import Callable, Iterable, Sequence
from typing import Any, Literal, TypeAlias
from typing_extensions import Self

import tensorflow as tf
from tensorflow import Operation, Tensor
from tensorflow._aliases import DTypeLike, KerasSerializable, TensorCompatible
from tensorflow.keras.initializers import _Initializer

_Output: TypeAlias = Tensor | dict[str, Tensor]

class Metric(tf.keras.layers.Layer[tf.Tensor, tf.Tensor], metaclass=ABCMeta):
    def __init__(self, dtype: DTypeLike | None = None, name: str | None = None) -> None: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> Self: ...
    def reset_state(self) -> None: ...
    @abstractmethod
    def update_state(
        self, y_true: TensorCompatible, y_pred: TensorCompatible, sample_weight: TensorCompatible | None = None
    ) -> Operation | None: ...
    @abstractmethod
    def result(self) -> _Output: ...
    # Metric's compatibility wrapper differs from Layer.add_weight.
    def add_weight(  # type: ignore[override]
        self,
        shape: Iterable[int | None] = (),
        initializer: _Initializer | None = None,
        dtype: DTypeLike | None = None,
        name: str | None = None,
    ): ...  # Keras 3 returns a backend Variable, which is not yet modeled here.

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
        dtype: DTypeLike | None = None,
        thresholds: Sequence[float] | None = None,
        multi_label: bool = False,
        num_labels: int | None = None,
        label_weights: TensorCompatible | None = None,
        from_logits: bool = False,
    ) -> None: ...
    def update_state(
        self, y_true: TensorCompatible, y_pred: TensorCompatible, sample_weight: TensorCompatible | None = None
    ) -> Operation: ...
    def result(self) -> tf.Tensor: ...

class Precision(Metric):
    def __init__(
        self,
        thresholds: float | Sequence[float] | None = None,
        top_k: int | None = None,
        class_id: int | None = None,
        name: str | None = None,
        dtype: DTypeLike | None = None,
    ) -> None: ...
    def update_state(
        self, y_true: TensorCompatible, y_pred: TensorCompatible, sample_weight: TensorCompatible | None = None
    ) -> Operation: ...
    def result(self) -> tf.Tensor: ...

class Recall(Metric):
    def __init__(
        self,
        thresholds: float | Sequence[float] | None = None,
        top_k: int | None = None,
        class_id: int | None = None,
        name: str | None = None,
        dtype: DTypeLike | None = None,
    ) -> None: ...
    def update_state(
        self, y_true: TensorCompatible, y_pred: TensorCompatible, sample_weight: TensorCompatible | None = None
    ) -> Operation: ...
    def result(self) -> tf.Tensor: ...

class MeanMetricWrapper(Metric):
    def __init__(
        self, fn: Callable[[tf.Tensor, tf.Tensor], tf.Tensor], name: str | None = None, dtype: DTypeLike | None = None
    ) -> None: ...
    def update_state(
        self, y_true: TensorCompatible, y_pred: TensorCompatible, sample_weight: TensorCompatible | None = None
    ) -> Operation: ...
    def result(self) -> tf.Tensor: ...

class BinaryAccuracy(MeanMetricWrapper):
    def __init__(self, name: str | None = "binary_accuracy", dtype: DTypeLike | None = None, threshold: float = 0.5) -> None: ...

class Accuracy(MeanMetricWrapper):
    def __init__(self, name: str | None = "accuracy", dtype: DTypeLike | None = None) -> None: ...

class CategoricalAccuracy(MeanMetricWrapper):
    def __init__(self, name: str | None = "categorical_accuracy", dtype: DTypeLike | None = None) -> None: ...

class TopKCategoricalAccuracy(MeanMetricWrapper):
    def __init__(self, k: int = 5, name: str | None = "top_k_categorical_accuracy", dtype: DTypeLike | None = None) -> None: ...

class SparseTopKCategoricalAccuracy(MeanMetricWrapper):
    def __init__(
        self,
        k: int = 5,
        name: str | None = "sparse_top_k_categorical_accuracy",
        dtype: DTypeLike | None = None,
        from_sorted_ids: bool = False,
    ) -> None: ...

class MeanSquaredError(MeanMetricWrapper):
    def __init__(self, name: str | None = "mean_squared_error", dtype: DTypeLike | None = None) -> None: ...

class Mean(Metric):
    total: Incomplete
    count: Incomplete
    def __init__(self, name: str | None = "mean", dtype: DTypeLike | None = None) -> None: ...
    def update_state(self, values: TensorCompatible, sample_weight: TensorCompatible | None = None) -> None: ...  # type: ignore[override]
    def result(self) -> Tensor: ...

def serialize(metric: KerasSerializable) -> dict[str, Any]: ...
def binary_crossentropy(
    y_true: TensorCompatible, y_pred: TensorCompatible, from_logits: bool = False, label_smoothing: float = 0.0, axis: int = -1
) -> Tensor: ...
def categorical_crossentropy(
    y_true: TensorCompatible, y_pred: TensorCompatible, from_logits: bool = False, label_smoothing: float = 0.0, axis: int = -1
) -> Tensor: ...
def __getattr__(name: str): ...  # incomplete module
