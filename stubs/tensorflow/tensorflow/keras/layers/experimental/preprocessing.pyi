import abc
from typing import overload

import tensorflow as tf
from tensorflow._aliases import AnyArray, TensorLike
from tensorflow.keras.layers import Layer

class PreprocessingLayer(Layer[TensorLike, TensorLike], metaclass=abc.ABCMeta):
    @overload
    def __call__(self, inputs: tf.Tensor) -> tf.Tensor: ...
    @overload
    def __call__(self, inputs: tf.SparseTensor) -> tf.SparseTensor: ...
    @overload
    def __call__(self, inputs: tf.RaggedTensor) -> tf.RaggedTensor: ...  # type: ignore
    def adapt(
        self, data: tf.data.Dataset[TensorLike] | AnyArray, batch_size: int | None = None, steps: int | None = None
    ) -> None: ...
    def compile(self, run_eagerly: bool | None = None, steps_per_execution: int | None = None) -> None: ...
