from typing_extensions import TypeAlias

from cv2 import (
    Error as Error,
    data as data,
    gapi as gapi,
    mat_wrapper as mat_wrapper,
    misc as misc,
    utils as utils,
    version as version,
)
from cv2.cv2 import *
from cv2.mat_wrapper import Mat as _WrappedMat, _NDArray

__all__: list[str] = []

def bootstrap() -> None: ...

Mat: TypeAlias = _WrappedMat | _NDArray
# TODO: Make Mat generic with int or float
_MatF: TypeAlias = _WrappedMat | _NDArray  # noqa: Y047
