from typing import Any
from typing_extensions import Self

from tensorflow import Tensor, _TensorCompatible
from tensorflow.dtypes import DType

class Metric:
    def __init__(self, name: str, dtype: DType) -> None: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> Self: ...

def binary_crossentropy(
    y_true: _TensorCompatible, y_pred: _TensorCompatible, from_logits: bool = False, label_smoothing: float = 0.0, axis: int = -1
) -> Tensor: ...
def categorical_crossentropy(
    y_true: _TensorCompatible, y_pred: _TensorCompatible, from_logits: bool = False, label_smoothing: float = 0.0, axis: int = -1
) -> Tensor: ...
