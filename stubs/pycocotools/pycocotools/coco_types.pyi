from typing import Generic, TypeAlias, TypedDict, TypeVar

import numpy as np
import numpy.typing as npt

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
    dtMatches: npt.NDArray[np.float64]
    gtMatches: npt.NDArray[np.float64]
    dtScores: list[float]
    gtIgnore: npt.NDArray[np.float64]
    dtIgnore: npt.NDArray[np.float64]


class Dataset(TypedDict):
    images: list[Image]
    annotations: list[Annotation]
    categories: list[Category]
