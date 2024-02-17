import abc
from typing import overload

import tensorflow as tf
from tensorflow._aliases import AnyArray, DataSequence, Float, Integer, TensorCompatible, TensorLike
from tensorflow.keras.layers import Layer

class PreprocessingLayer(Layer[TensorLike, TensorLike], metaclass=abc.ABCMeta):
    @property
    def is_adapted(self) -> bool: ...
    @overload  # type: ignore
    def __call__(self, inputs: tf.Tensor, *, training: bool = False, mask: TensorCompatible | None = None) -> tf.Tensor: ...
    @overload
    def __call__(
        self, inputs: tf.SparseTensor, *, training: bool = False, mask: TensorCompatible | None = None
    ) -> tf.SparseTensor: ...
    @overload
    def __call__(
        self, inputs: tf.RaggedTensor, *, training: bool = False, mask: TensorCompatible | None = None
    ) -> tf.RaggedTensor: ...
    def adapt(
        self,
        data: tf.data.Dataset[TensorLike] | AnyArray | DataSequence,
        batch_size: Integer | None = None,
        steps: Float | None = None,
    ) -> None: ...
    def compile(self, run_eagerly: bool | None = None, steps_per_execution: Integer | None = None) -> None: ...
