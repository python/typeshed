import abc
import dataclasses
from _typeshed import Incomplete
from typing import Sequence

from tensorflow import Tensor, TensorShape
from tensorflow.dtypes import DType
from tensorflow.python.trackable.base import Trackable

@dataclasses.dataclass(frozen=True)
class ShardableTensor:
    _tensor_save_spec: Incomplete  # saveable_object.SaveSpec
    tensor: Tensor
    dtype: DType
    device: Incomplete  # device_lib.DeviceSpec
    name: str
    shape: TensorShape
    slice_spec: Incomplete  # variables.Variable.SaveSliceInfo
    checkpoint_key: str
    trackable: Trackable
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...

class ShardingCallback(abc.ABC):
    def description(self) -> str: ...
    @abc.abstractmethod
    def __call__(self, shardable_tensors: Sequence[ShardableTensor]) -> Sequence[Incomplete]: ...  # Sequence[TensorSliceDict]
    def __hash__(self) -> int: ...

def __getattr__(name: str) -> Incomplete: ...
