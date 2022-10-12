from collections.abc import Sequence
from typing import overload

from cv2 import Mat, _MatF
from cv2.cv2 import (
    Feature2D,
    UMat,
    _Boolean,
    _NumericScalar,
    _Point,
    _Rect,
    _Size,
    _TUMat,
    _TUMatF,
    _UMat,
    _UMatF,
    detail_BestOf2NearestMatcher,
    detail_Blender,
    detail_ExposureCompensator,
    detail_ImageFeatures,
    detail_MatchesInfo,
    detail_SeamFinder,
    detail_Timelapser,
    gapi_GNetParam,
    gapi_ie_PyParams,
)

ARG_KIND_GARRAY: int
ARG_KIND_GFRAME: int
ARG_KIND_GMAT: int
ARG_KIND_GMATP: int
ARG_KIND_GOBJREF: int
ARG_KIND_GOPAQUE: int
ARG_KIND_GSCALAR: int
ARG_KIND_OPAQUE: int
ARG_KIND_OPAQUE_VAL: int
ArgKind_GARRAY: int
ArgKind_GFRAME: int
ArgKind_GMAT: int
ArgKind_GMATP: int
ArgKind_GOBJREF: int
ArgKind_GOPAQUE: int
ArgKind_GSCALAR: int
ArgKind_OPAQUE: int
ArgKind_OPAQUE_VAL: int
BLENDER_FEATHER: int
BLENDER_MULTI_BAND: int
BLENDER_NO: int
Blender_FEATHER: int
Blender_MULTI_BAND: int
Blender_NO: int
DP_SEAM_FINDER_COLOR: int
DP_SEAM_FINDER_COLOR_GRAD: int
DpSeamFinder_COLOR: int
DpSeamFinder_COLOR_GRAD: int
EXPOSURE_COMPENSATOR_CHANNELS: int
EXPOSURE_COMPENSATOR_CHANNELS_BLOCKS: int
EXPOSURE_COMPENSATOR_GAIN: int
EXPOSURE_COMPENSATOR_GAIN_BLOCKS: int
EXPOSURE_COMPENSATOR_NO: int
ExposureCompensator_CHANNELS: int
ExposureCompensator_CHANNELS_BLOCKS: int
ExposureCompensator_GAIN: int
ExposureCompensator_GAIN_BLOCKS: int
ExposureCompensator_NO: int
GRAPH_CUT_SEAM_FINDER_BASE_COST_COLOR: int
GRAPH_CUT_SEAM_FINDER_BASE_COST_COLOR_GRAD: int
GraphCutSeamFinderBase_COST_COLOR: int
GraphCutSeamFinderBase_COST_COLOR_GRAD: int
OPAQUE_KIND_CV_BOOL: int
OPAQUE_KIND_CV_DOUBLE: int
OPAQUE_KIND_CV_DRAW_PRIM: int
OPAQUE_KIND_CV_FLOAT: int
OPAQUE_KIND_CV_INT: int
OPAQUE_KIND_CV_INT64: int
OPAQUE_KIND_CV_MAT: int
OPAQUE_KIND_CV_POINT: int
OPAQUE_KIND_CV_POINT2F: int
OPAQUE_KIND_CV_RECT: int
OPAQUE_KIND_CV_SCALAR: int
OPAQUE_KIND_CV_SIZE: int
OPAQUE_KIND_CV_STRING: int
OPAQUE_KIND_CV_UINT64: int
OPAQUE_KIND_CV_UNKNOWN: int
OpaqueKind_CV_BOOL: int
OpaqueKind_CV_DOUBLE: int
OpaqueKind_CV_DRAW_PRIM: int
OpaqueKind_CV_FLOAT: int
OpaqueKind_CV_INT: int
OpaqueKind_CV_INT64: int
OpaqueKind_CV_MAT: int
OpaqueKind_CV_POINT: int
OpaqueKind_CV_POINT2F: int
OpaqueKind_CV_RECT: int
OpaqueKind_CV_SCALAR: int
OpaqueKind_CV_SIZE: int
OpaqueKind_CV_STRING: int
OpaqueKind_CV_UINT64: int
OpaqueKind_CV_UNKNOWN: int
SEAM_FINDER_DP_SEAM: int
SEAM_FINDER_NO: int
SEAM_FINDER_VORONOI_SEAM: int
SeamFinder_DP_SEAM: int
SeamFinder_NO: int
SeamFinder_VORONOI_SEAM: int
TEST_CUSTOM: int
TEST_EQ: int
TEST_GE: int
TEST_GT: int
TEST_LE: int
TEST_LT: int
TEST_NE: int
TIMELAPSER_AS_IS: int
TIMELAPSER_CROP: int
TRACKER_SAMPLER_CSC_MODE_DETECT: int
TRACKER_SAMPLER_CSC_MODE_INIT_NEG: int
TRACKER_SAMPLER_CSC_MODE_INIT_POS: int
TRACKER_SAMPLER_CSC_MODE_TRACK_NEG: int
TRACKER_SAMPLER_CSC_MODE_TRACK_POS: int
Timelapser_AS_IS: int
Timelapser_CROP: int
TrackerSamplerCSC_MODE_DETECT: int
TrackerSamplerCSC_MODE_INIT_NEG: int
TrackerSamplerCSC_MODE_INIT_POS: int
TrackerSamplerCSC_MODE_TRACK_NEG: int
TrackerSamplerCSC_MODE_TRACK_POS: int
WAVE_CORRECT_AUTO: int
WAVE_CORRECT_HORIZ: int
WAVE_CORRECT_VERT: int

def BestOf2NearestMatcher_create(
    try_use_gpu: _Boolean = ..., match_conf: float = ..., num_matches_thresh1: int = ..., num_matches_thresh2: int = ...
) -> detail_BestOf2NearestMatcher: ...

# OpenCV 4.6
# def BestOf2NearestMatcher_create(
#     try_use_gpu: _Boolean = ...,
#     match_conf: float = ...,
#     num_matches_thresh1: int = ...,
#     num_matches_thresh2: int = ...,
#     matches_confindece_thresh: float = ...,
# ) -> detail_BestOf2NearestMatcher: ...
def Blender_createDefault(type: int, try_gpu: _Boolean = ...) -> detail_Blender: ...
def ExposureCompensator_createDefault(type: int) -> detail_ExposureCompensator: ...
def SeamFinder_createDefault(type: int) -> detail_SeamFinder: ...
def Timelapser_createDefault(type: int) -> detail_Timelapser: ...
def calibrateRotatingCamera(Hs: Sequence[_MatF], K: _NumericScalar = ...) -> tuple[bool, _MatF]: ...
def computeImageFeatures(
    featuresFinder: Feature2D, images: Sequence[_UMat], masks: Sequence[_UMat] = ...
) -> detail_ImageFeatures: ...
def computeImageFeatures2(featuresFinder: Feature2D, image: _UMat, mask: _UMat = ...) -> detail_ImageFeatures: ...
def createLaplacePyr(img: _UMat, num_levels: int, pyr: Sequence[_UMat]) -> tuple[UMat, ...]: ...
def createLaplacePyrGpu(img: _UMat, num_levels: int, pyr: Sequence[_UMat]) -> tuple[UMat, ...]: ...
def createWeightMap(mask: _TUMat, sharpness: float, weight: _TUMat) -> _TUMat: ...
def focalsFromHomography(H: Mat, f0: float, f1: float, f0_ok: bool, f1_ok: bool) -> None: ...
def leaveBiggestComponent(
    features: Sequence[detail_ImageFeatures], pairwise_matches: Sequence[detail_MatchesInfo], conf_threshold: float
) -> tuple[int, ...]: ...
def matchesGraphAsString(pathes: Sequence[str], pairwise_matches: Sequence[detail_MatchesInfo], conf_threshold: float) -> str: ...
def normalizeUsingWeightMap(weight: _UMatF, src: _TUMatF) -> _TUMatF: ...
def overlapRoi(tl1: _Point, tl2: _Point, sz1: _Size, sz2: _Size, roi: _Rect) -> bool: ...
def restoreImageFromLaplacePyr(pyr: Sequence[_UMat]) -> tuple[UMat, ...]: ...
def restoreImageFromLaplacePyrGpu(pyr: Sequence[_UMat]) -> tuple[UMat, ...]: ...
@overload
def resultRoi(corners: Sequence[_Point], images: Sequence[_UMat]) -> tuple[int, int, int, int]: ...
@overload
def resultRoi(corners: Sequence[_Point], sizes: Sequence[_Point]) -> tuple[int, int, int, int]: ...
def resultRoiIntersection(corners: Sequence[_Point], sizes: Sequence[_Point]) -> tuple[int, int, int, int]: ...
def resultTl(corners: Sequence[_Point]) -> tuple[int, int]: ...
def selectRandomSubset(count: int, size: int, subset: Sequence[int]) -> None: ...
def stitchingLogLevel() -> int: ...
def strip(params: gapi_ie_PyParams) -> gapi_GNetParam: ...
def waveCorrect(rmats: Sequence[_MatF], kind: int) -> tuple[_MatF, ...]: ...
