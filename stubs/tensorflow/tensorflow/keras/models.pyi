from collections.abc import Callable
from pathlib import Path

import tensorflow
import tensorflow as tf
from tensorflow import _ShapeLike, _TensorCompatible
from tensorflow.keras.layers import Layer, _InputT, _OutputT

class Model(Layer[_InputT, _OutputT], tf.Module):
    def __init__(self, *args, **kwargs) -> None: ...
    def build(self, input_shape: _ShapeLike) -> None: ...
    def summary(
        self,
        line_length: None | int = None,
        positions: None | list[float] = None,
        print_fn: None | Callable[[str], None] = None,
        expand_nested: bool = False,
        show_trainable: bool = False,
        layer_range: None | list[str] | tuple[str, str] = None,
    ): ...
    def load_weights(
        self,
        filepath: str | Path,
        skip_mismatch: bool = False,
        by_name: bool = False,
        options: None | tensorflow.train.CheckpointOptions = None,
    ): ...
    def __call__(self, inputs: _InputT, *, training: bool = False, mask: _TensorCompatible | None = None) -> _OutputT: ...
    def call(self, __inputs: _InputT) -> _OutputT: ...
