from typing import overload

import numpy as np
import numpy.typing as npt

from .coco_types import _EncodedRLE

def iou(
    dt: npt.NDArray[np.uint32] | list[float] | list[_EncodedRLE],
    gt: npt.NDArray[np.uint32] | list[float] | list[_EncodedRLE],
    pyiscrowd: list[int] | npt.NDArray[np.uint8],
) -> list | npt.NDArray[np.float64]: ...
def merge(rleObjs: list[_EncodedRLE], intersect: int = ...): ...
@overload
def frPyObjects(pyobj: npt.NDArray[np.uint32] | list[list[int]] | list[_EncodedRLE], h: int, w: int) -> list[_EncodedRLE]: ...
@overload
def frPyObjects(pyobj: list[int] | _EncodedRLE, h: int, w: int) -> _EncodedRLE: ...
def encode(bimask: npt.NDArray[np.uint8]) -> _EncodedRLE: ...
def decode(rleObjs: _EncodedRLE) -> npt.NDArray[np.uint8]: ...
def area(rleObjs: _EncodedRLE) -> np.uint32: ...
def toBbox(rleObjs: _EncodedRLE) -> npt.NDArray[np.float64]: ...
