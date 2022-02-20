from typing import overload

from tensorflow import RaggedTensor, SparseTensor, Tensor
from tensorflow._aliases import _TensorCompatible

@overload
def abs(x: _TensorCompatible, name: str | None = ...) -> Tensor: ...
@overload
def abs(x: SparseTensor, name: str | None = ...) -> SparseTensor: ...
@overload
def abs(x: RaggedTensor, name: str | None = ...) -> RaggedTensor: ...
