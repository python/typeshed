from _typeshed import Incomplete
from typing import Callable

from tensorflow.keras import (
    activations as activations,
    constraints as constraints,
    initializers as initializers,
    layers as layers,
    losses as losses,
    metrics as metrics,
    models as models,
    optimizers as optimizers,
    regularizers as regularizers,
)
from tensorflow.keras.models import Model as Model
import tensorflow as tf
from tensorflow._aliases import _TensorCompatible

def __getattr__(name: str) -> Incomplete: ...

_Loss = (
   str
    | tf.keras.losses.Loss
    | Callable[[_TensorCompatible, _TensorCompatible], tf._Tensor]
)

_Metric = (
    str
    | tf.keras.metrics.Metric
    | Callable[[_TensorCompatible, _TensorCompatible], tf._Tensor]
    | None
)
