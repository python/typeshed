from _typeshed import Incomplete
from typing import Generic, TypeAlias, TypeVar
from typing_extensions import TypedDict

# import numpy as np
# import numpy.typing as npt

_NDArray: TypeAlias = Incomplete

class _Image(TypedDict):
    id: int
    width: int
    height: int
    file_name: str

_TPolygonSegmentation: TypeAlias = list[list[float]]

class _RLE(TypedDict):
    size: list[int]
    counts: list[int]

class _EncodedRLE(TypedDict):
    size: list[int]
    counts: str | bytes

class _Annotation(TypedDict):
    id: int
    image_id: int
    category_id: int
    segmentation: _TPolygonSegmentation | _RLE | _EncodedRLE
    area: float
    bbox: list[float]
    iscrowd: int  # Either 1 or 0

_TSeg = TypeVar("_TSeg", _TPolygonSegmentation, _RLE, _EncodedRLE)

class _AnnotationG(TypedDict, Generic[_TSeg]):
    id: int
    image_id: int
    category_id: int
    segmentation: _TSeg
    area: float
    bbox: list[float]
    iscrowd: int  # Either 1 or 0

class _Category(TypedDict):
    id: int
    name: str
    supercategory: str

class _EvaluationResult(TypedDict):
    image_id: int
    category_id: int
    aRng: list[int]
    maxDet: int
    dtIds: list[int]
    gtIds: list[int]
    dtMatches: _NDArray
    # dtMatches: npt.NDArray[np.float64]
    gtMatches: _NDArray
    # gtMatches: npt.NDArray[np.float64]
    dtScores: list[float]
    gtIgnore: _NDArray
    # gtIgnore: npt.NDArray[np.float64]
    dtIgnore: _NDArray
    # dtIgnore: npt.NDArray[np.float64]

class _Dataset(TypedDict):
    images: list[_Image]
    annotations: list[_Annotation]
    categories: list[_Category]
