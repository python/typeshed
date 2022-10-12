from _typeshed import Incomplete
from typing import Any
from typing_extensions import TypeAlias

from cv2.cv2 import gapi_ie_PyParams

# These are temporary placeholder return types, as were in the docstrings signatures from microsoft/python-type-stubs
_pyr: TypeAlias = Incomplete  # noqa: Y042
_weight: TypeAlias = Incomplete  # noqa: Y042
_src: TypeAlias = Incomplete  # noqa: Y042
_rmats: TypeAlias = Incomplete  # noqa: Y042

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

def BestOf2NearestMatcher_create(*args, **kwargs) -> Any: ...
def Blender_createDefault(*args, **kwargs) -> Any: ...
def ExposureCompensator_createDefault(*args, **kwargs) -> Any: ...
def SeamFinder_createDefault(*args, **kwargs) -> Any: ...
def Timelapser_createDefault(*args, **kwargs) -> Any: ...
def calibrateRotatingCamera(*args, **kwargs) -> Any: ...
def computeImageFeatures(*args, **kwargs) -> Any: ...
def computeImageFeatures2(*args, **kwargs) -> Any: ...
def createLaplacePyr(img, num_levels, pyr) -> _pyr: ...
def createLaplacePyrGpu(img, num_levels, pyr) -> _pyr: ...
def createWeightMap(mask, sharpness, weight) -> _weight: ...
def focalsFromHomography(H, f0, f1, f0_ok, f1_ok) -> None: ...
def leaveBiggestComponent(*args, **kwargs) -> Any: ...
def matchesGraphAsString(*args, **kwargs) -> Any: ...
def normalizeUsingWeightMap(weight, src) -> _src: ...
def overlapRoi(*args, **kwargs) -> Any: ...
def restoreImageFromLaplacePyr(pyr) -> _pyr: ...
def restoreImageFromLaplacePyrGpu(pyr) -> _pyr: ...
def resultRoi(*args, **kwargs) -> Any: ...
def resultRoiIntersection(*args, **kwargs) -> Any: ...
def resultTl(*args, **kwargs) -> Any: ...
def selectRandomSubset(count, size, subset) -> None: ...
def stitchingLogLevel(*args, **kwargs) -> Any: ...
def strip(params: gapi_ie_PyParams): ...
def waveCorrect(rmats, kind) -> _rmats: ...
