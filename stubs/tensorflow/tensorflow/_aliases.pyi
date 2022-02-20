# Collection of commonly need type aliases. These are all private
# and do not exist at runtime.

from typing import Iterable, Mapping, Optional, Sequence, TypeVar, Union

import numpy as np
import tensorflow as tf

# These aliases mostly ignore rank/shape/dtype information as that
# will complicate the types heavily and can be a follow up problem.
_FloatDataSequence = Union[Sequence[float], Sequence["_FloatDataSequence"]]
_StrDataSequence = Union[Sequence[str], Sequence["_StrDataSequence"]]
_ScalarTensorConvertible = Union[str, float, np.number, np.ndarray]
_ScalarTensorCompatible = Union[tf.Tensor, _ScalarTensorConvertible]
_TensorConvertible = Union[_ScalarTensorConvertible, _FloatDataSequence, _StrDataSequence]
_TensorCompatible = Union[tf.Tensor, _TensorConvertible]

# Sparse tensors need to be treated carefully. Most functions do
# not document if they handle sparse tensors. Most functions do
# not support them. Ragged tensors usually work and are documented
# here, https://www.tensorflow.org/api_docs/python/tf/ragged
_SparseTensorCompatible = Union[_TensorCompatible, tf.SparseTensor]
_RaggedTensorCompatible = Union[_TensorCompatible, tf.RaggedTensor]
_AnyTensorCompatible = Union[_TensorCompatible, tf.Tensor, tf.Variable]

_SparseTensorLike = Union[tf.Tensor, tf.SparseTensor]
_RaggedTensorLike = Union[tf.Tensor, tf.RaggedTensor]
_AnyTensorLike = Union[tf.Tensor, tf.SparseTensor, tf.RaggedTensor]

_T1 = TypeVar("_T1", covariant=True)
_ContainerGeneric = Union[Mapping[str, "_ContainerGeneric[_T1]"], Sequence["_ContainerGeneric[_T1]"], _T1]
_ContainerTensors = _ContainerGeneric[tf.Tensor]
_ContainerTensorCompatible = _ContainerGeneric[_TensorCompatible]

_ShapeLike = Union[tf.TensorShape, Iterable[Optional[int]], int, tf.Tensor]
_DTypeLike = Union[tf.DType, str, np.dtype]
