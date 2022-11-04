from typing import Literal, TypeAlias

import numpy as np
import numpy.typing as npt

from .coco import COCO
from .coco_types import _EvaluationResult

_TIOU: TypeAlias = Literal["segm", "bbox", "keypoints"]

class COCOeval:
    cocoGt: COCO
    cocoDt: COCO
    evalImgs: list[_EvaluationResult]
    eval: _EvaluationResult
    params: Params
    stats: npt.NDArray[np.float64]
    ious: dict[tuple[int, int], list[float]]
    def __init__(self, cocoGt: COCO | None = ..., cocoDt: COCO | None = ..., iouType: _TIOU = ...) -> None: ...
    def evaluate(self) -> None: ...
    def computeIoU(self, imgId: int, catId: int) -> list[float]: ...
    def computeOks(self, imgId: int, catId: int) -> npt.NDArray[np.float64]: ...
    def evaluateImg(self, imgId: int, catId: int, aRng: list[int], maxDet: int) -> _EvaluationResult: ...
    def accumulate(self, p: Params | None = ...) -> None: ...
    def summarize(self) -> None: ...

class Params:
    imgIds: list[int]
    catIds: list[int]
    iouThrs: npt.NDArray[np.float64]
    recThrs: npt.NDArray[np.float64]
    maxDets: list[int]
    areaRng: list[int]
    areaRngLbl: list[str]
    useCats: int
    kpt_oks_sigmas: npt.NDArray[np.float64]
    iouType: _TIOU
    useSegm: int | None
    def __init__(self, iouType: _TIOU = ...) -> None: ...
    def setDetParams(self) -> None: ...
    def setKpParams(self) -> None: ...
