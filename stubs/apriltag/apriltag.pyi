import ctypes
from _typeshed import Incomplete
from typing import NamedTuple
import numpy # type: ignore
from typing import List, Dict, Any, Tuple

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
    homography: numpy.ndarray
    center: numpy.ndarray
    corners: numpy.ndarray

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
    def __init__(self, families: str = ..., border: int = ..., nthreads: int = ..., quad_decimate: float = ..., quad_blur: float = ..., refine_edges: bool = ..., refine_decode: bool = ..., refine_pose: bool = ..., debug: bool = ..., quad_contours: bool = ...) -> None: ...

def add_arguments(parser) -> None: ...

class Detector:
    options: DetectorOptions
    libc: ctypes.CDLL
    tag_detector: _ApriltagDetector
    families: List[str]
    def __init__(self, options: DetectorOptions | None = ..., searchpath: List[str]=...) -> None: ...
    def __del__(self) -> None: ...
    def detect(self, img: numpy.ndarray, return_image: bool = ...) -> numpy.ndarray: ...
    def add_tag_family(self, name) -> None: ...
    def detection_pose(self, detection, camera_params, tag_size: int = ..., z_sign: int = ...) -> Tuple[numpy.ndarray, float, float]: ...

def main() -> None: ...
