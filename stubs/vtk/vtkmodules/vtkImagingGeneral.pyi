from collections.abc import MutableSequence, Sequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkImagingCore


VTK_EDT_SAITO: int
VTK_EDT_SAITO_CACHED: int

class vtkImageSpatialAlgorithm(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetKernelMiddle(self) -> Tuple[int, int, int]: ...
    def GetKernelSize(self) -> Tuple[int, int, int]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageSpatialAlgorithm: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageSpatialAlgorithm: ...

class vtkImageAnisotropicDiffusion2D(vtkImageSpatialAlgorithm):
    def CornersOff(self) -> None: ...
    def CornersOn(self) -> None: ...
    def EdgesOff(self) -> None: ...
    def EdgesOn(self) -> None: ...
    def FacesOff(self) -> None: ...
    def FacesOn(self) -> None: ...
    def GetCorners(self) -> int: ...
    def GetDiffusionFactor(self) -> float: ...
    def GetDiffusionThreshold(self) -> float: ...
    def GetEdges(self) -> int: ...
    def GetFaces(self) -> int: ...
    def GetGradientMagnitudeThreshold(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfIterations(self) -> int: ...
    def GradientMagnitudeThresholdOff(self) -> None: ...
    def GradientMagnitudeThresholdOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageAnisotropicDiffusion2D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageAnisotropicDiffusion2D: ...
    def SetCorners(self, _arg: int) -> None: ...
    def SetDiffusionFactor(self, _arg: float) -> None: ...
    def SetDiffusionThreshold(self, _arg: float) -> None: ...
    def SetEdges(self, _arg: int) -> None: ...
    def SetFaces(self, _arg: int) -> None: ...
    def SetGradientMagnitudeThreshold(self, _arg: int) -> None: ...
    def SetNumberOfIterations(self, num: int) -> None: ...

class vtkImageAnisotropicDiffusion3D(vtkImageSpatialAlgorithm):
    def CornersOff(self) -> None: ...
    def CornersOn(self) -> None: ...
    def EdgesOff(self) -> None: ...
    def EdgesOn(self) -> None: ...
    def FacesOff(self) -> None: ...
    def FacesOn(self) -> None: ...
    def GetCorners(self) -> int: ...
    def GetDiffusionFactor(self) -> float: ...
    def GetDiffusionThreshold(self) -> float: ...
    def GetEdges(self) -> int: ...
    def GetFaces(self) -> int: ...
    def GetGradientMagnitudeThreshold(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfIterations(self) -> int: ...
    def GradientMagnitudeThresholdOff(self) -> None: ...
    def GradientMagnitudeThresholdOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageAnisotropicDiffusion3D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageAnisotropicDiffusion3D: ...
    def SetCorners(self, _arg: int) -> None: ...
    def SetDiffusionFactor(self, _arg: float) -> None: ...
    def SetDiffusionThreshold(self, _arg: float) -> None: ...
    def SetEdges(self, _arg: int) -> None: ...
    def SetFaces(self, _arg: int) -> None: ...
    def SetGradientMagnitudeThreshold(self, _arg: int) -> None: ...
    def SetNumberOfIterations(self, num: int) -> None: ...

class vtkImageCheckerboard(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetNumberOfDivisions(self) -> Tuple[int, int, int]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageCheckerboard: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageCheckerboard: ...
    def SetInput1Data(self, in_: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetInput2Data(self, in_: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    @overload
    def SetNumberOfDivisions(self, _arg1: int, _arg2: int, _arg3: int) -> None: ...
    @overload
    def SetNumberOfDivisions(self, _arg: Sequence[int]) -> None: ...

class vtkImageCityBlockDistance(vtkmodules.vtkImagingCore.vtkImageDecomposeFilter):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageCityBlockDistance: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageCityBlockDistance: ...

class vtkImageConvolve(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    @overload
    def GetKernel3x3(self) -> Tuple[float, float, float, float, float, float, float, float, float]: ...
    @overload
    def GetKernel3x3(self, kernel: MutableSequence[float]) -> None: ...
    @overload
    def GetKernel3x3x3(
        self,
    ) -> Tuple[
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
    ]: ...
    @overload
    def GetKernel3x3x3(self, kernel: MutableSequence[float]) -> None: ...
    @overload
    def GetKernel5x5(
        self,
    ) -> Tuple[
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
    ]: ...
    @overload
    def GetKernel5x5(self, kernel: MutableSequence[float]) -> None: ...
    def GetKernel5x5x5(
        self,
    ) -> Tuple[
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
    ]: ...
    @overload
    def GetKernel7x7(
        self,
    ) -> Tuple[
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
    ]: ...
    @overload
    def GetKernel7x7(self, kernel: MutableSequence[float]) -> None: ...
    def GetKernel7x7x7(self) -> Tuple[float, float]: ...
    def GetKernelSize(self) -> Tuple[int, int, int]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageConvolve: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageConvolve: ...
    def SetKernel3x3(self, kernel: Sequence[float]) -> None: ...
    def SetKernel3x3x3(self, kernel: Sequence[float]) -> None: ...
    def SetKernel5x5(self, kernel: Sequence[float]) -> None: ...
    def SetKernel5x5x5(self, kernel: Sequence[float]) -> None: ...
    def SetKernel7x7(self, kernel: Sequence[float]) -> None: ...

class vtkImageCorrelation(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetDimensionality(self) -> int: ...
    def GetDimensionalityMaxValue(self) -> int: ...
    def GetDimensionalityMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageCorrelation: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageCorrelation: ...
    def SetDimensionality(self, _arg: int) -> None: ...
    def SetInput1Data(self, in_: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetInput2Data(self, in_: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...

class vtkImageEuclideanDistance(vtkmodules.vtkImagingCore.vtkImageDecomposeFilter):
    def ConsiderAnisotropyOff(self) -> None: ...
    def ConsiderAnisotropyOn(self) -> None: ...
    def GetAlgorithm(self) -> int: ...
    def GetConsiderAnisotropy(self) -> int: ...
    def GetInitialize(self) -> int: ...
    def GetMaximumDistance(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def InitializeOff(self) -> None: ...
    def InitializeOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageEuclideanDistance: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageEuclideanDistance: ...
    def SetAlgorithm(self, _arg: int) -> None: ...
    def SetAlgorithmToSaito(self) -> None: ...
    def SetAlgorithmToSaitoCached(self) -> None: ...
    def SetConsiderAnisotropy(self, _arg: int) -> None: ...
    def SetInitialize(self, _arg: int) -> None: ...
    def SetMaximumDistance(self, _arg: float) -> None: ...

class vtkImageEuclideanToPolar(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetThetaMaximum(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageEuclideanToPolar: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageEuclideanToPolar: ...
    def SetThetaMaximum(self, _arg: float) -> None: ...

class vtkImageGaussianSmooth(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetDimensionality(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRadiusFactors(self) -> Tuple[float, float, float]: ...
    def GetStandardDeviations(self) -> Tuple[float, float, float]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageGaussianSmooth: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageGaussianSmooth: ...
    def SetDimensionality(self, _arg: int) -> None: ...
    def SetRadiusFactor(self, f: float) -> None: ...
    @overload
    def SetRadiusFactors(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetRadiusFactors(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetRadiusFactors(self, f: float, f2: float) -> None: ...
    @overload
    def SetStandardDeviation(self, std: float) -> None: ...
    @overload
    def SetStandardDeviation(self, a: float, b: float) -> None: ...
    @overload
    def SetStandardDeviation(self, a: float, b: float, c: float) -> None: ...
    @overload
    def SetStandardDeviations(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetStandardDeviations(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetStandardDeviations(self, a: float, b: float) -> None: ...

class vtkImageGradient(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetDimensionality(self) -> int: ...
    def GetDimensionalityMaxValue(self) -> int: ...
    def GetDimensionalityMinValue(self) -> int: ...
    def GetHandleBoundaries(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def HandleBoundariesOff(self) -> None: ...
    def HandleBoundariesOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageGradient: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageGradient: ...
    def SetDimensionality(self, _arg: int) -> None: ...
    def SetHandleBoundaries(self, _arg: int) -> None: ...

class vtkImageGradientMagnitude(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetDimensionality(self) -> int: ...
    def GetDimensionalityMaxValue(self) -> int: ...
    def GetDimensionalityMinValue(self) -> int: ...
    def GetHandleBoundaries(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def HandleBoundariesOff(self) -> None: ...
    def HandleBoundariesOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageGradientMagnitude: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageGradientMagnitude: ...
    def SetDimensionality(self, _arg: int) -> None: ...
    def SetHandleBoundaries(self, _arg: int) -> None: ...

class vtkImageHybridMedian2D(vtkImageSpatialAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageHybridMedian2D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageHybridMedian2D: ...

class vtkImageLaplacian(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetDimensionality(self) -> int: ...
    def GetDimensionalityMaxValue(self) -> int: ...
    def GetDimensionalityMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageLaplacian: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageLaplacian: ...
    def SetDimensionality(self, _arg: int) -> None: ...

class vtkImageMedian3D(vtkImageSpatialAlgorithm):
    def GetNumberOfElements(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageMedian3D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageMedian3D: ...
    def SetKernelSize(self, size0: int, size1: int, size2: int) -> None: ...

class vtkImageNormalize(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageNormalize: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageNormalize: ...

class vtkImageRange3D(vtkImageSpatialAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageRange3D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageRange3D: ...
    def SetKernelSize(self, size0: int, size1: int, size2: int) -> None: ...

class vtkImageSeparableConvolution(vtkmodules.vtkImagingCore.vtkImageDecomposeFilter):
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetXKernel(self) -> vtkmodules.vtkCommonCore.vtkFloatArray: ...
    def GetYKernel(self) -> vtkmodules.vtkCommonCore.vtkFloatArray: ...
    def GetZKernel(self) -> vtkmodules.vtkCommonCore.vtkFloatArray: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageSeparableConvolution: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageSeparableConvolution: ...
    def SetXKernel(self, __a: vtkmodules.vtkCommonCore.vtkFloatArray) -> None: ...
    def SetYKernel(self, __a: vtkmodules.vtkCommonCore.vtkFloatArray) -> None: ...
    def SetZKernel(self, __a: vtkmodules.vtkCommonCore.vtkFloatArray) -> None: ...

class vtkImageSlab(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetMultiSliceOutput(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOperation(self) -> int: ...
    def GetOperationAsString(self) -> str: ...
    def GetOperationMaxValue(self) -> int: ...
    def GetOperationMinValue(self) -> int: ...
    def GetOrientation(self) -> int: ...
    def GetOrientationMaxValue(self) -> int: ...
    def GetOrientationMinValue(self) -> int: ...
    def GetOutputScalarType(self) -> int: ...
    def GetSliceRange(self) -> Tuple[int, int]: ...
    def GetTrapezoidIntegration(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MultiSliceOutputOff(self) -> None: ...
    def MultiSliceOutputOn(self) -> None: ...
    def NewInstance(self) -> vtkImageSlab: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageSlab: ...
    def SetMultiSliceOutput(self, _arg: int) -> None: ...
    def SetOperation(self, _arg: int) -> None: ...
    def SetOperationToMax(self) -> None: ...
    def SetOperationToMean(self) -> None: ...
    def SetOperationToMin(self) -> None: ...
    def SetOperationToSum(self) -> None: ...
    def SetOrientation(self, _arg: int) -> None: ...
    def SetOrientationToX(self) -> None: ...
    def SetOrientationToY(self) -> None: ...
    def SetOrientationToZ(self) -> None: ...
    def SetOutputScalarTypeToDouble(self) -> None: ...
    def SetOutputScalarTypeToFloat(self) -> None: ...
    def SetOutputScalarTypeToInputScalarType(self) -> None: ...
    @overload
    def SetSliceRange(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetSliceRange(self, _arg: Sequence[int]) -> None: ...
    def SetTrapezoidIntegration(self, _arg: int) -> None: ...
    def TrapezoidIntegrationOff(self) -> None: ...
    def TrapezoidIntegrationOn(self) -> None: ...

class vtkImageSlabReslice(vtkmodules.vtkImagingCore.vtkImageReslice):
    def GetBlendMode(self) -> int: ...
    def GetNumBlendSamplePoints(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSlabResolution(self) -> float: ...
    def GetSlabThickness(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageSlabReslice: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageSlabReslice: ...
    def SetBlendMode(self, _arg: int) -> None: ...
    def SetBlendModeToMax(self) -> None: ...
    def SetBlendModeToMean(self) -> None: ...
    def SetBlendModeToMin(self) -> None: ...
    def SetSlabResolution(self, _arg: float) -> None: ...
    def SetSlabThickness(self, _arg: float) -> None: ...

class vtkImageSobel2D(vtkImageSpatialAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageSobel2D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageSobel2D: ...

class vtkImageSobel3D(vtkImageSpatialAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageSobel3D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageSobel3D: ...

class vtkImageVariance3D(vtkImageSpatialAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageVariance3D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageVariance3D: ...
    def SetKernelSize(self, size0: int, size1: int, size2: int) -> None: ...

class vtkSimpleImageFilterExample(vtkmodules.vtkCommonExecutionModel.vtkSimpleImageToImageFilter):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSimpleImageFilterExample: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSimpleImageFilterExample: ...
