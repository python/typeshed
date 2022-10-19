from collections.abc import Sequence
from typing import overload
from typing_extensions import TypeAlias

from cv2 import Mat, _MatF
from cv2.cv2 import _Boolean, _NumericScalar, _RectFloat, _RotatedRect, _Scalar, _Size, _UMat, dnn_Net
from cv2.mat_wrapper import _NDArray, _NDArrayF

_Buffer: TypeAlias = Sequence[_NumericScalar] | bytes | None

DNN_BACKEND_CUDA: int
DNN_BACKEND_DEFAULT: int
DNN_BACKEND_HALIDE: int
DNN_BACKEND_INFERENCE_ENGINE: int
DNN_BACKEND_OPENCV: int
DNN_BACKEND_VKCOM: int
DNN_BACKEND_WEBNN: int
DNN_TARGET_CPU: int
DNN_TARGET_CUDA: int
DNN_TARGET_CUDA_FP16: int
DNN_TARGET_FPGA: int
DNN_TARGET_HDDL: int
DNN_TARGET_MYRIAD: int
DNN_TARGET_OPENCL: int
DNN_TARGET_OPENCL_FP16: int
DNN_TARGET_VULKAN: int
SOFT_NMSMETHOD_SOFTNMS_GAUSSIAN: int
SOFT_NMSMETHOD_SOFTNMS_LINEAR: int
SoftNMSMethod_SOFTNMS_GAUSSIAN: int
SoftNMSMethod_SOFTNMS_LINEAR: int

def NMSBoxes(
    bboxes: Sequence[_RectFloat | None] | None,
    scores: Sequence[float | None] | None,
    score_threshold: float | None,
    nms_threshold: float | None,
    eta: float | None = ...,
    top_k: int | None = ...,
) -> _NDArray: ...
def NMSBoxesRotated(
    bboxes: Sequence[_RotatedRect | None] | None,
    scores: Sequence[float | None] | None,
    score_threshold: float | None,
    nms_threshold: float | None,
    eta: float | None = ...,
    top_k: int | None = ...,
) -> _NDArray: ...
@overload
def Net_readFromModelOptimizer(xml: str, bin: str) -> dnn_Net: ...
@overload
def Net_readFromModelOptimizer(bufferModelConfig: _Buffer, bufferWeights: _Buffer) -> dnn_Net: ...
def blobFromImage(
    image: _UMat | None,
    scalefactor: float | None = ...,
    size: _Size | None = ...,
    mean: _Scalar = ...,
    swapRB: _Boolean = ...,
    crop: _Boolean = ...,
    ddepth: int | None = ...,
) -> Mat: ...
def blobFromImages(
    images: Sequence[_UMat | None],
    scalefactor: float | None = ...,
    size: _Size | None = ...,
    mean: _Scalar = ...,
    swapRB: _Boolean = ...,
    crop: _Boolean = ...,
    ddepth: int | None = ...,
) -> Mat: ...
def getAvailableTargets(be: int | None) -> _NDArray: ...
def imagesFromBlob(blob_: _MatF, images_: Sequence[_MatF | Mat] = ...) -> tuple[_MatF, ...]: ...
@overload
def readNet(model: str, config: str = ..., framework: str = ...) -> dnn_Net: ...
@overload
def readNet(framework: str, bufferModel: _Buffer, bufferConfig: _Buffer = ...) -> dnn_Net: ...
@overload
def readNetFromCaffe(prototxt: str, caffeModel: str = ...) -> dnn_Net: ...
@overload
def readNetFromCaffe(bufferProto: _Buffer, bufferModel: _Buffer = ...) -> dnn_Net: ...
@overload
def readNetFromDarknet(cfgFile: str, darknetModel: str = ...) -> dnn_Net: ...
@overload
def readNetFromDarknet(bufferCfg: _Buffer, bufferModel: _Buffer = ...) -> dnn_Net: ...
@overload
def readNetFromModelOptimizer(xml: str, bin: str) -> dnn_Net: ...
@overload
def readNetFromModelOptimizer(bufferModelConfig: _Buffer, bufferWeights: _Buffer) -> dnn_Net: ...
@overload
def readNetFromONNX(onnxFile: str) -> dnn_Net: ...
@overload
def readNetFromONNX(buffer: _Buffer) -> dnn_Net: ...
@overload
def readNetFromTensorflow(model: str, config: str = ...) -> dnn_Net: ...
@overload
def readNetFromTensorflow(bufferModel: _Buffer, bufferConfig: _Buffer = ...) -> dnn_Net: ...
def readNetFromTorch(model: str, isBinary: _Boolean = ..., evaluate: _Boolean = ...) -> dnn_Net: ...
def readTensorFromONNX(path: str) -> Mat: ...
def readTorchBlob(filename: str, isBinary: _Boolean = ...) -> Mat: ...
def shrinkCaffeModel(src: str, dst: str, layersTypes: Sequence[str] = ...) -> None: ...
def softNMSBoxes(
    bboxes: Sequence[_RectFloat | None] | None,
    scores: Sequence[float | None] | None,
    score_threshold: float | None,
    nms_threshold: float | None,
    eta: float | None = ...,
    top_k: int | None = ...,
    sigma: float | None = ...,
    method: int | None = ...,
) -> tuple[_NDArrayF, _NDArray]: ...
def writeTextGraph(model: str, output: str) -> None: ...
