# Commonly used type aliases.
# Everything in this module is private for stubs. There is no runtime equivalent.

from collections.abc import Iterable, Mapping, Sequence
from typing import Any, Protocol, TypeVar
from typing_extensions import TypeAlias

import numpy as np
import numpy.typing as npt
import tensorflow as tf
from tensorflow.keras.layers import InputSpec

_T = TypeVar("_T")
_ContainerGeneric: TypeAlias = Mapping[str, _ContainerGeneric[_T]] | Sequence[_ContainerGeneric[_T]] | _T

_TensorLike: TypeAlias = tf.Tensor | tf.RaggedTensor | tf.SparseTensor
# _SparseTensorLike: TypeAlias = tf.Tensor | tf.SparseTensor
# _RaggedTensorLike: TypeAlias = tf.Tensor | tf.RaggedTensor
# _RaggedTensorLikeT = TypeVar("_RaggedTensorLikeT", tf.Tensor, tf.RaggedTensor)
_Gradients: TypeAlias = tf.Tensor | tf.IndexedSlices

class _KerasSerializable1(Protocol):
    def get_config(self) -> dict[str, Any]: ...

class _KerasSerializable2(Protocol):
    __name__: str

_KerasSerializable: TypeAlias = _KerasSerializable1 | _KerasSerializable2

_Slice: TypeAlias = int | slice | None
_FloatDataSequence: TypeAlias = Sequence[float] | Sequence[_FloatDataSequence]
_StrDataSequence: TypeAlias = Sequence[str] | Sequence[_StrDataSequence]
_ScalarTensorCompatible: TypeAlias = tf.Tensor | str | float | np.ndarray[Any, Any] | np.number[Any]

_TensorCompatible: TypeAlias = _ScalarTensorCompatible | Sequence[_TensorCompatible]
_TensorCompatibleT = TypeVar("_TensorCompatibleT", bound=_TensorCompatible)
# Sparse tensors are very annoying. Some operations work on them, but many do not.
# You will need to manually verify if an operation supports them. SparseTensorCompatible is intended to be a
# broader type than TensorCompatible and not all operations will support broader version. If unsure,
# use TensorCompatible instead.
_SparseTensorCompatible: TypeAlias = _TensorCompatible | tf.SparseTensor

_ShapeLike: TypeAlias = tf.TensorShape | Iterable[_ScalarTensorCompatible | None] | int | tf.Tensor
_DTypeLike: TypeAlias = tf.DType | str | np.dtype[Any] | int

_ContainerTensors: TypeAlias = _ContainerGeneric[tf.Tensor]
_ContainerTensorsLike: TypeAlias = _ContainerGeneric[_TensorLike]
_ContainerTensorCompatible: TypeAlias = _ContainerGeneric[_TensorCompatible]
_ContainerGradients: TypeAlias = _ContainerGeneric[_Gradients]
_ContainerTensorShape: TypeAlias = _ContainerGeneric[tf.TensorShape]
_ContainerInputSpec: TypeAlias = _ContainerGeneric[InputSpec]

_AnyArray: TypeAlias = npt.NDArray[Any]
_FloatArray: TypeAlias = npt.NDArray[np.float_ | np.float16 | np.float32 | np.float64]
_IntArray: TypeAlias = npt.NDArray[np.int_ | np.uint8 | np.int32 | np.int64]
