import argparse
import ctypes
from typing import Any, Dict, List, NamedTuple, Tuple
from typing_extensions import TypeAlias

# TODO: Use numpy types when #5768 is resolved.
# import numpy as np
# import numpy.typing as npt

_NDArray: TypeAlias = Any  # FIXME: no typings for numpy arrays

class _ImageU8(ctypes.Structure): ...
class _Matd(ctypes.Structure): ...
class _ZArray(ctypes.Structure): ...
class _ApriltagFamily(ctypes.Structure): ...
class _ApriltagDetection(ctypes.Structure): ...
class _ApriltagDetector(ctypes.Structure): ...

class DetectionBase(NamedTuple):
    tag_family: str
    tag_id: int
    hamming: int
    goodness: float
    decision_margin: float
    homography: _NDArray
    center: _NDArray
    corners: _NDArray

class Detection(DetectionBase):
    def tostring(self, values: Dict[str, Any] | None = ..., indent: int = ...) -> str: ...

class DetectorOptions:
    families: str
    border: int
    nthreads: int
    quad_decimate: float
    quad_sigma: float
    refine_edges: bool
    refine_decode: bool
    refine_pose: bool
    debug: bool
    quad_contours: bool
    def __init__(
        self,
        families: str = ...,
        border: int = ...,
        nthreads: int = ...,
        quad_decimate: float = ...,
        quad_blur: float = ...,
        refine_edges: bool = ...,
        refine_decode: bool = ...,
        refine_pose: bool = ...,
        debug: bool = ...,
        quad_contours: bool = ...,
    ) -> None: ...

def add_arguments(parser: argparse.ArgumentParser) -> None: ...

class Detector:
    options: DetectorOptions
    libc: ctypes.CDLL
    tag_detector: _ApriltagDetector
    families: List[str]
    def __init__(self, options: DetectorOptions | None = ..., searchpath: List[str] = ...) -> None: ...
    def __del__(self) -> None: ...
    def detect(self, img: _NDArray, return_image: bool = ...) -> _NDArray: ...
    def add_tag_family(self, name: str) -> None: ...
    def detection_pose(
        self, detection: Detection, camera_params: Tuple[float], tag_size: int = ..., z_sign: int = ...
    ) -> Tuple[_NDArray, float, float]: ...

def main() -> None: ...
