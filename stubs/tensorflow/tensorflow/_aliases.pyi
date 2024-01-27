# Commonly used type aliases.
# Everything in this module is private for stubs. There is no runtime
# equivalent.

from collections.abc import Mapping, Sequence
from typing import Any, Iterable, Mapping, Protocol, Sequence, TypeVar
from typing_extensions import TypeAlias

import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import InputSpec

_T1 = TypeVar("_T1")
_T = TypeVar("_T")
_ContainerGeneric: TypeAlias = Mapping[str, _ContainerGeneric[_T1]] | Sequence[_ContainerGeneric[_T1]] | _T1

_TensorLike: TypeAlias = tf.Tensor | tf.RaggedTensor | tf.SparseTensor
_SparseTensorLike = tf.Tensor | tf.SparseTensor
_RaggedTensorLike = tf.Tensor | tf.RaggedTensor
_RaggedTensorLikeT = TypeVar("_RaggedTensorLikeT", tf.Tensor, tf.RaggedTensor)
_Gradients: TypeAlias = tf.Tensor | tf.IndexedSlices

class _KerasSerializable1(Protocol):
    def get_config(self) -> dict[str, Any]: ...

class _KerasSerializable2(Protocol):
    __name__: str

_KerasSerializable: TypeAlias = _KerasSerializable1 | _KerasSerializable2

_FloatDataSequence = Sequence[float] | Sequence[_FloatDataSequence]
_StrDataSequence = Sequence[str] | Sequence[_StrDataSequence]
_ScalarTensorCompatible = tf.Tensor | str | float | np.ndarray[Any, Any] | np.number[Any]

_TensorCompatible = _ScalarTensorCompatible | Sequence[_TensorCompatible]
_TensorCompatibleT = TypeVar("_TensorCompatibleT", bound=_TensorCompatible)
# Sparse tensors are very annoying. Some operations work on them, but many do not. You
# will need to manually verify if an operation supports them. SparseTensorCompatible is intended to be a
# broader type than TensorCompatible and not all operations will support broader version. If unsure,
# use TensorCompatible instead.
_SparseTensorCompatible = _TensorCompatible | tf.SparseTensor

_ShapeLike = tf.TensorShape | Iterable[_ScalarTensorCompatible | None] | int | tf.Tensor
_DTypeLike = tf.DType | str | np.dtype[Any] | int
_GradientsT = tf.Tensor | tf.IndexedSlices

_ContainerTensors = _ContainerGeneric[tf.Tensor]
_ContainerTensorsLike = _ContainerGeneric[_TensorLike]
_ContainerTensorCompatible = _ContainerGeneric[_TensorCompatible]
_ContainerGradients = _ContainerGeneric[_GradientsT]
_ContainerTensorShape = _ContainerGeneric[tf.TensorShape]
_ContainerInputSpec = _ContainerGeneric[InputSpec]

_AnyArray = np.ndarray[Any, Any]
_FloatArray = np.ndarray[Any, np.dtype[np.float_ | np.float16 | np.float32 | np.float64]]
_IntArray = np.ndarray[Any, np.dtype[np.int_ | np.uint8 | np.int32 | np.int64]]
