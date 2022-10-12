from typing_extensions import TypeAlias

from cv2 import data as data, gapi as gapi, mat_wrapper as mat_wrapper, misc as misc, utils as utils, version as version
from cv2.cv2 import *
from cv2.mat_wrapper import Mat as WrappedMat, _NDArray

__all__: list[str] = []

def bootstrap() -> None: ...

Mat: TypeAlias = WrappedMat | _NDArray
# TODO: Make Mat generic with int or float
_MatF: TypeAlias = WrappedMat | _NDArray
