from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias, TypedDict

from .coco import COCO

# TODO: Use numpy types when #5768 is resolved.
# import numpy as np
# import numpy.typing as npt

_NDArray: TypeAlias = Incomplete
_TIOU: TypeAlias = Literal["segm", "bbox", "keypoints"]

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

class COCOeval:
    cocoGt: COCO
    cocoDt: COCO
    evalImgs: list[_EvaluationResult]
    eval: _EvaluationResult
    params: Params
    stats: _NDArray
    # stats: npt.NDArray[np.float64]
    ious: dict[tuple[int, int], list[float]]
    def __init__(self, cocoGt: COCO | None = ..., cocoDt: COCO | None = ..., iouType: _TIOU = ...) -> None: ...
    def evaluate(self) -> None: ...
    def computeIoU(self, imgId: int, catId: int) -> list[float]: ...
    def computeOks(self, imgId: int, catId: int) -> _NDArray: ...
    # def computeOks(self, imgId: int, catId: int) -> npt.NDArray[np.float64]: ...
    def evaluateImg(self, imgId: int, catId: int, aRng: list[int], maxDet: int) -> _EvaluationResult: ...
    def accumulate(self, p: Params | None = ...) -> None: ...
    def summarize(self) -> None: ...

class Params:
    imgIds: list[int]
    catIds: list[int]
    iouThrs: _NDArray
    # iouThrs: npt.NDArray[np.float64]
    recThrs: _NDArray
    # recThrs: npt.NDArray[np.float64]
    maxDets: list[int]
    areaRng: list[int]
    areaRngLbl: list[str]
    useCats: int
    kpt_oks_sigmas: _NDArray
    # kpt_oks_sigmas: npt.NDArray[np.float64]
    iouType: _TIOU
    useSegm: int | None
    def __init__(self, iouType: _TIOU = ...) -> None: ...
    def setDetParams(self) -> None: ...
    def setKpParams(self) -> None: ...
