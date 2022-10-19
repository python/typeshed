from collections.abc import Sequence
from typing import overload

from cv2 import Mat, UMat
from cv2.cv2 import _Size, _TermCriteria, _UMat

CALIB_CHECK_COND: int
CALIB_FIX_FOCAL_LENGTH: int
CALIB_FIX_INTRINSIC: int
CALIB_FIX_K1: int
CALIB_FIX_K2: int
CALIB_FIX_K3: int
CALIB_FIX_K4: int
CALIB_FIX_PRINCIPAL_POINT: int
CALIB_FIX_SKEW: int
CALIB_RECOMPUTE_EXTRINSIC: int
CALIB_USE_INTRINSIC_GUESS: int
CALIB_ZERO_DISPARITY: int

@overload
def calibrate(
    objectPoints: Sequence[Mat],
    imagePoints: Sequence[Mat],
    image_size: _Size,
    K: Mat,
    D: Mat,
    rvecs: Sequence[Mat] = ...,
    tvecs: Sequence[Mat] = ...,
    flags: int | None = ...,
    criteria: _TermCriteria | None = ...,
) -> tuple[float, Mat, Mat, tuple[Mat, ...], tuple[Mat, ...]]: ...
@overload
def calibrate(
    objectPoints: Sequence[_UMat],
    imagePoints: Sequence[_UMat],
    image_size: _Size,
    K: _UMat,
    D: _UMat,
    rvecs: Sequence[_UMat] = ...,
    tvecs: Sequence[_UMat] = ...,
    flags: int | None = ...,
    criteria: _TermCriteria | None = ...,
) -> tuple[float, UMat, UMat, tuple[UMat, ...], tuple[UMat, ...]]: ...
@overload
def distortPoints(undistorted: Mat, K: Mat, D: Mat, distorted: Mat | None = ..., alpha: float | None = ...) -> Mat: ...
@overload
def distortPoints(undistorted: _UMat, K: _UMat, D: _UMat, distorted: _UMat | None = ..., alpha: float | None = ...) -> UMat: ...
@overload
def estimateNewCameraMatrixForUndistortRectify(
    K: Mat,
    D: Mat,
    image_size: _Size | None,
    R: Mat | None,
    P: Mat | None = ...,
    balance: float | None = ...,
    new_size: _Size | None = ...,
    fov_scale: float | None = ...,
) -> Mat: ...
@overload
def estimateNewCameraMatrixForUndistortRectify(
    K: _UMat,
    D: _UMat,
    image_size: _Size | None,
    R: _UMat | None,
    P: _UMat | None = ...,
    balance: float | None = ...,
    new_size: _Size | None = ...,
    fov_scale: float | None = ...,
) -> UMat: ...
@overload
def initUndistortRectifyMap(
    K: Mat,
    D: Mat,
    R: Mat | None,
    P: Mat | None,
    size: _Size | None,
    m1type: int | None,
    map1: Mat | None = ...,
    map2: Mat | None = ...,
) -> tuple[Mat, Mat]: ...
@overload
def initUndistortRectifyMap(
    K: _UMat,
    D: _UMat,
    R: _UMat | None,
    P: _UMat | None,
    size: _Size | None,
    m1type: int | None,
    map1: _UMat | None = ...,
    map2: _UMat | None = ...,
) -> tuple[UMat, UMat]: ...
@overload
def projectPoints(
    objectPoints: Sequence[Mat],
    rvec: Mat,
    tvec: Mat,
    K: Mat,
    D: Mat,
    imagePoints: Sequence[Mat] | None = ...,
    alpha: float | None = ...,
    jacobian: Mat | None = ...,
) -> tuple[Mat, Mat]: ...
@overload
def projectPoints(
    objectPoints: Sequence[_UMat],
    rvec: _UMat,
    tvec: _UMat,
    K: _UMat,
    D: _UMat,
    imagePoints: Sequence[_UMat] | None = ...,
    alpha: float | None = ...,
    jacobian: _UMat | None = ...,
) -> tuple[UMat, UMat]: ...
@overload
def stereoCalibrate(
    objectPoints: Sequence[Mat],
    imagePoints1: Sequence[Mat],
    imagePoints2: Sequence[Mat],
    K1: Mat,
    D1: Mat,
    K2: Mat,
    D2: Mat,
    imageSize: _Size | None,
    R: Mat | None = ...,
    T: Mat | None = ...,
    flags: int | None = ...,
    criteria: _TermCriteria = ...,
) -> tuple[float, Mat, Mat, Mat, Mat, Mat, Mat]: ...
@overload
def stereoCalibrate(
    objectPoints: Sequence[_UMat],
    imagePoints1: Sequence[_UMat],
    imagePoints2: Sequence[_UMat],
    K1: _UMat,
    D1: _UMat,
    K2: _UMat,
    D2: _UMat,
    imageSize: _Size | None,
    R: _UMat | None = ...,
    T: _UMat | None = ...,
    flags: int | None = ...,
    criteria: _TermCriteria = ...,
) -> tuple[float, UMat, UMat, UMat, UMat, UMat, UMat]: ...
@overload
def stereoRectify(
    K1: Mat,
    D1: Mat,
    K2: Mat,
    D2: Mat,
    imageSize: _Size | None,
    R: Mat,
    tvec: Mat,
    flags: int | None,
    R1: Mat | None = ...,
    R2: Mat | None = ...,
    P1: Mat | None = ...,
    P2: Mat | None = ...,
    Q: Mat | None = ...,
    newImageSize: _Size | None = ...,
    balance: float | None = ...,
    fov_scale: float | None = ...,
) -> tuple[Mat, Mat, Mat, Mat, Mat]: ...
@overload
def stereoRectify(
    K1: _UMat,
    D1: _UMat,
    K2: _UMat,
    D2: _UMat,
    imageSize: _Size | None,
    R: _UMat,
    tvec: _UMat,
    flags: int | None,
    R1: _UMat | None = ...,
    R2: _UMat | None = ...,
    P1: _UMat | None = ...,
    P2: _UMat | None = ...,
    Q: _UMat | None = ...,
    newImageSize: _Size | None = ...,
    balance: float | None = ...,
    fov_scale: float | None = ...,
) -> tuple[Mat, Mat, Mat, Mat, Mat]: ...
@overload
def undistortImage(
    distorted: Mat, K: Mat, D: Mat, undistorted: Mat | None = ..., Knew: Mat = ..., new_size: _Size | None = ...
) -> Mat: ...
@overload
def undistortImage(
    distorted: _UMat, K: _UMat, D: _UMat, undistorted: _UMat | None = ..., Knew: _UMat = ..., new_size: _Size | None = ...
) -> UMat: ...
@overload
def undistortPoints(
    distorted: Mat, K: Mat, D: Mat, undistorted: Mat | None = ..., R: Mat | None = ..., P: Mat | None = ...
) -> Mat: ...
@overload
def undistortPoints(
    distorted: _UMat, K: _UMat, D: _UMat, undistorted: _UMat | None = ..., R: _UMat | None = ..., P: _UMat | None = ...
) -> UMat: ...
