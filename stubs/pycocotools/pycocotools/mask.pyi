from _typeshed import Incomplete
from typing import overload
from typing_extensions import TypeAlias

from .coco_types import _EncodedRLE

# import numpy as np
# import numpy.typing as npt


_NPUInt32: TypeAlias = Incomplete  # np.uint32
_NDArrayUInt8: TypeAlias = Incomplete  # npt.NDArray[np.uint8]
_NDArrayUInt32: TypeAlias = Incomplete  # npt.NDArray[np.uint32]
_NDArrayFloat64: TypeAlias = Incomplete  # npt.NDArray[np.float64]

def iou(
    dt: _NDArrayUInt32 | list[float] | list[_EncodedRLE],
    gt: _NDArrayUInt32 | list[float] | list[_EncodedRLE],
    pyiscrowd: list[int] | _NDArrayUInt8,
) -> list | _NDArrayFloat64: ...
def merge(rleObjs: list[_EncodedRLE], intersect: int = ...): ...
@overload
def frPyObjects(pyobj: _NDArrayUInt32 | list[list[int]] | list[_EncodedRLE], h: int, w: int) -> list[_EncodedRLE]: ...
def frPyObjects(pyobj: _NDArrayUInt32 | list[list[int]] | list[_EncodedRLE], h: int, w: int) -> list[_EncodedRLE]: ...
@overload
def frPyObjects(pyobj: list[int] | _EncodedRLE, h: int, w: int) -> _EncodedRLE: ...
def encode(bimask: _NDArrayUInt8) -> _EncodedRLE: ...
def decode(rleObjs: _EncodedRLE) -> _NDArrayUInt8: ...
def area(rleObjs: _EncodedRLE) -> _NPUInt32: ...
def toBbox(rleObjs: _EncodedRLE) -> _NDArrayFloat64: ...
