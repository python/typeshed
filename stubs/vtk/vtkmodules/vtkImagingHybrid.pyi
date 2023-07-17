from collections.abc import MutableSequence, Sequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkImagingCore
import vtkmodules.vtkIOImage


VTK_ACCUMULATION_MODE_MAX: int
VTK_ACCUMULATION_MODE_MIN: int
VTK_ACCUMULATION_MODE_SUM: int
VTK_WIPE_HORIZONTAL: int
VTK_WIPE_LOWER_LEFT: int
VTK_WIPE_LOWER_RIGHT: int
VTK_WIPE_QUAD: int
VTK_WIPE_UPPER_LEFT: int
VTK_WIPE_UPPER_RIGHT: int
VTK_WIPE_VERTICAL: int

class vtkBooleanTexture(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetInIn(self) -> Tuple[int, int]: ...
    def GetInOn(self) -> Tuple[int, int]: ...
    def GetInOut(self) -> Tuple[int, int]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOnIn(self) -> Tuple[int, int]: ...
    def GetOnOn(self) -> Tuple[int, int]: ...
    def GetOnOut(self) -> Tuple[int, int]: ...
    def GetOutIn(self) -> Tuple[int, int]: ...
    def GetOutOn(self) -> Tuple[int, int]: ...
    def GetOutOut(self) -> Tuple[int, int]: ...
    def GetThickness(self) -> int: ...
    def GetXSize(self) -> int: ...
    def GetYSize(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkBooleanTexture: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkBooleanTexture: ...
    @overload
    def SetInIn(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetInIn(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetInOn(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetInOn(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetInOut(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetInOut(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetOnIn(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetOnIn(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetOnOn(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetOnOn(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetOnOut(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetOnOut(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetOutIn(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetOutIn(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetOutOn(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetOutOn(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetOutOut(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetOutOut(self, _arg: Sequence[int]) -> None: ...
    def SetThickness(self, _arg: int) -> None: ...
    def SetXSize(self, _arg: int) -> None: ...
    def SetYSize(self, _arg: int) -> None: ...

class vtkCheckerboardSplatter(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def CappingOff(self) -> None: ...
    def CappingOn(self) -> None: ...
    def ComputeModelBounds(
        self,
        input: vtkmodules.vtkCommonDataModel.vtkDataSet,
        output: vtkmodules.vtkCommonDataModel.vtkImageData,
        outInfo: vtkmodules.vtkCommonCore.vtkInformation,
    ) -> None: ...
    def GetAccumulationMode(self) -> int: ...
    def GetAccumulationModeAsString(self) -> str: ...
    def GetAccumulationModeMaxValue(self) -> int: ...
    def GetAccumulationModeMinValue(self) -> int: ...
    def GetCapValue(self) -> float: ...
    def GetCapping(self) -> int: ...
    def GetEccentricity(self) -> float: ...
    def GetEccentricityMaxValue(self) -> float: ...
    def GetEccentricityMinValue(self) -> float: ...
    def GetExponentFactor(self) -> float: ...
    def GetFootprint(self) -> int: ...
    def GetFootprintMaxValue(self) -> int: ...
    def GetFootprintMinValue(self) -> int: ...
    def GetMaximumDimension(self) -> int: ...
    def GetMaximumDimensionMaxValue(self) -> int: ...
    def GetMaximumDimensionMinValue(self) -> int: ...
    def GetModelBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    def GetNormalWarping(self) -> int: ...
    def GetNullValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputScalarType(self) -> int: ...
    def GetParallelSplatCrossover(self) -> int: ...
    def GetParallelSplatCrossoverMaxValue(self) -> int: ...
    def GetParallelSplatCrossoverMinValue(self) -> int: ...
    def GetRadius(self) -> float: ...
    def GetRadiusMaxValue(self) -> float: ...
    def GetRadiusMinValue(self) -> float: ...
    def GetSampleDimensions(self) -> Tuple[int, int, int]: ...
    def GetScalarWarping(self) -> int: ...
    def GetScaleFactor(self) -> float: ...
    def GetScaleFactorMaxValue(self) -> float: ...
    def GetScaleFactorMinValue(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCheckerboardSplatter: ...
    def NormalWarpingOff(self) -> None: ...
    def NormalWarpingOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCheckerboardSplatter: ...
    def ScalarWarpingOff(self) -> None: ...
    def ScalarWarpingOn(self) -> None: ...
    def SetAccumulationMode(self, _arg: int) -> None: ...
    def SetAccumulationModeToMax(self) -> None: ...
    def SetAccumulationModeToMin(self) -> None: ...
    def SetAccumulationModeToSum(self) -> None: ...
    def SetCapValue(self, _arg: float) -> None: ...
    def SetCapping(self, _arg: int) -> None: ...
    def SetEccentricity(self, _arg: float) -> None: ...
    def SetExponentFactor(self, _arg: float) -> None: ...
    def SetFootprint(self, _arg: int) -> None: ...
    def SetMaximumDimension(self, _arg: int) -> None: ...
    @overload
    def SetModelBounds(self, _arg1: float, _arg2: float, _arg3: float, _arg4: float, _arg5: float, _arg6: float) -> None: ...
    @overload
    def SetModelBounds(self, _arg: Sequence[float]) -> None: ...
    def SetNormalWarping(self, _arg: int) -> None: ...
    def SetNullValue(self, _arg: float) -> None: ...
    def SetOutputScalarType(self, _arg: int) -> None: ...
    def SetOutputScalarTypeToDouble(self) -> None: ...
    def SetOutputScalarTypeToFloat(self) -> None: ...
    def SetParallelSplatCrossover(self, _arg: int) -> None: ...
    def SetRadius(self, _arg: float) -> None: ...
    @overload
    def SetSampleDimensions(self, i: int, j: int, k: int) -> None: ...
    @overload
    def SetSampleDimensions(self, dim: MutableSequence[int]) -> None: ...
    def SetScalarWarping(self, _arg: int) -> None: ...
    def SetScaleFactor(self, _arg: float) -> None: ...

class vtkFastSplatter(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    ClampLimit: int
    FreezeScaleLimit: int
    NoneLimit: int
    ScaleLimit: int
    def GetLimitMode(self) -> int: ...
    def GetMaxValue(self) -> float: ...
    def GetMinValue(self) -> float: ...
    def GetModelBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfPointsSplatted(self) -> int: ...
    def GetOutputDimensions(self) -> Tuple[int, int, int]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkFastSplatter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkFastSplatter: ...
    def SetLimitMode(self, _arg: int) -> None: ...
    def SetLimitModeToClamp(self) -> None: ...
    def SetLimitModeToFreezeScale(self) -> None: ...
    def SetLimitModeToNone(self) -> None: ...
    def SetLimitModeToScale(self) -> None: ...
    def SetMaxValue(self, _arg: float) -> None: ...
    def SetMinValue(self, _arg: float) -> None: ...
    @overload
    def SetModelBounds(self, _arg1: float, _arg2: float, _arg3: float, _arg4: float, _arg5: float, _arg6: float) -> None: ...
    @overload
    def SetModelBounds(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetOutputDimensions(self, _arg1: int, _arg2: int, _arg3: int) -> None: ...
    @overload
    def SetOutputDimensions(self, _arg: Sequence[int]) -> None: ...
    def SetSplatConnection(self, __a: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...

class vtkGaussianSplatter(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def CappingOff(self) -> None: ...
    def CappingOn(self) -> None: ...
    @overload
    def ComputeModelBounds(
        self,
        input: vtkmodules.vtkCommonDataModel.vtkDataSet,
        output: vtkmodules.vtkCommonDataModel.vtkImageData,
        outInfo: vtkmodules.vtkCommonCore.vtkInformation,
    ) -> None: ...
    @overload
    def ComputeModelBounds(
        self,
        input: vtkmodules.vtkCommonDataModel.vtkCompositeDataSet,
        output: vtkmodules.vtkCommonDataModel.vtkImageData,
        outInfo: vtkmodules.vtkCommonCore.vtkInformation,
    ) -> None: ...
    def GetAccumulationMode(self) -> int: ...
    def GetAccumulationModeAsString(self) -> str: ...
    def GetAccumulationModeMaxValue(self) -> int: ...
    def GetAccumulationModeMinValue(self) -> int: ...
    def GetCapValue(self) -> float: ...
    def GetCapping(self) -> int: ...
    def GetEccentricity(self) -> float: ...
    def GetEccentricityMaxValue(self) -> float: ...
    def GetEccentricityMinValue(self) -> float: ...
    def GetExponentFactor(self) -> float: ...
    def GetModelBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    def GetNormalWarping(self) -> int: ...
    def GetNullValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRadius(self) -> float: ...
    def GetRadiusMaxValue(self) -> float: ...
    def GetRadiusMinValue(self) -> float: ...
    def GetSampleDimensions(self) -> Tuple[int, int, int]: ...
    def GetScalarWarping(self) -> int: ...
    def GetScaleFactor(self) -> float: ...
    def GetScaleFactorMaxValue(self) -> float: ...
    def GetScaleFactorMinValue(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGaussianSplatter: ...
    def NormalWarpingOff(self) -> None: ...
    def NormalWarpingOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGaussianSplatter: ...
    def SamplePoint(self, x: MutableSequence[float]) -> float: ...
    def ScalarWarpingOff(self) -> None: ...
    def ScalarWarpingOn(self) -> None: ...
    def SetAccumulationMode(self, _arg: int) -> None: ...
    def SetAccumulationModeToMax(self) -> None: ...
    def SetAccumulationModeToMin(self) -> None: ...
    def SetAccumulationModeToSum(self) -> None: ...
    def SetCapValue(self, _arg: float) -> None: ...
    def SetCapping(self, _arg: int) -> None: ...
    def SetEccentricity(self, _arg: float) -> None: ...
    def SetExponentFactor(self, _arg: float) -> None: ...
    @overload
    def SetModelBounds(self, _arg1: float, _arg2: float, _arg3: float, _arg4: float, _arg5: float, _arg6: float) -> None: ...
    @overload
    def SetModelBounds(self, _arg: Sequence[float]) -> None: ...
    def SetNormalWarping(self, _arg: int) -> None: ...
    def SetNullValue(self, _arg: float) -> None: ...
    def SetRadius(self, _arg: float) -> None: ...
    @overload
    def SetSampleDimensions(self, i: int, j: int, k: int) -> None: ...
    @overload
    def SetSampleDimensions(self, dim: MutableSequence[int]) -> None: ...
    def SetScalar(self, idx: int, dist2: float, sPtr: MutableSequence[float]) -> None: ...
    def SetScalarWarping(self, _arg: int) -> None: ...
    def SetScaleFactor(self, _arg: float) -> None: ...

class vtkImageCursor3D(vtkmodules.vtkCommonExecutionModel.vtkImageInPlaceFilter):
    def GetCursorPosition(self) -> Tuple[float, float, float]: ...
    def GetCursorRadius(self) -> int: ...
    def GetCursorValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageCursor3D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageCursor3D: ...
    @overload
    def SetCursorPosition(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetCursorPosition(self, _arg: Sequence[float]) -> None: ...
    def SetCursorRadius(self, _arg: int) -> None: ...
    def SetCursorValue(self, _arg: float) -> None: ...

class vtkImageRectilinearWipe(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetAxis(self) -> Tuple[int, int]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPosition(self) -> Tuple[int, int]: ...
    def GetWipe(self) -> int: ...
    def GetWipeMaxValue(self) -> int: ...
    def GetWipeMinValue(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageRectilinearWipe: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageRectilinearWipe: ...
    @overload
    def SetAxis(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetAxis(self, _arg: Sequence[int]) -> None: ...
    def SetInput1Data(self, in_: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetInput2Data(self, in_: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    @overload
    def SetPosition(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetPosition(self, _arg: Sequence[int]) -> None: ...
    def SetWipe(self, _arg: int) -> None: ...
    def SetWipeToHorizontal(self) -> None: ...
    def SetWipeToLowerLeft(self) -> None: ...
    def SetWipeToLowerRight(self) -> None: ...
    def SetWipeToQuad(self) -> None: ...
    def SetWipeToUpperLeft(self) -> None: ...
    def SetWipeToUpperRight(self) -> None: ...
    def SetWipeToVertical(self) -> None: ...

class vtkImageToPoints(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputPointsPrecision(self) -> int: ...
    def GetStencilConnection(self) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageToPoints: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageToPoints: ...
    def SetOutputPointsPrecision(self, _arg: int) -> None: ...
    def SetStencilConnection(self, port: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetStencilData(self, stencil: vtkmodules.vtkImagingCore.vtkImageStencilData) -> None: ...

class vtkPointLoad(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def ComputeEffectiveStressOff(self) -> None: ...
    def ComputeEffectiveStressOn(self) -> None: ...
    def GetComputeEffectiveStress(self) -> int: ...
    def GetLoadValue(self) -> float: ...
    def GetModelBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPoissonsRatio(self) -> float: ...
    def GetSampleDimensions(self) -> Tuple[int, int, int]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPointLoad: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPointLoad: ...
    def SetComputeEffectiveStress(self, __a: int) -> None: ...
    def SetLoadValue(self, _arg: float) -> None: ...
    @overload
    def SetModelBounds(self, _arg1: float, _arg2: float, _arg3: float, _arg4: float, _arg5: float, _arg6: float) -> None: ...
    @overload
    def SetModelBounds(self, _arg: Sequence[float]) -> None: ...
    def SetPoissonsRatio(self, _arg: float) -> None: ...
    @overload
    def SetSampleDimensions(self, dim: MutableSequence[int]) -> None: ...
    @overload
    def SetSampleDimensions(self, i: int, j: int, k: int) -> None: ...

class vtkSampleFunction(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def CappingOff(self) -> None: ...
    def CappingOn(self) -> None: ...
    def ComputeNormalsOff(self) -> None: ...
    def ComputeNormalsOn(self) -> None: ...
    def GetCapValue(self) -> float: ...
    def GetCapping(self) -> int: ...
    def GetComputeNormals(self) -> int: ...
    def GetImplicitFunction(self) -> vtkmodules.vtkCommonDataModel.vtkImplicitFunction: ...
    def GetMTime(self) -> int: ...
    def GetModelBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    def GetNormalArrayName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputScalarType(self) -> int: ...
    def GetSampleDimensions(self) -> Tuple[int, int, int]: ...
    def GetScalarArrayName(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSampleFunction: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSampleFunction: ...
    def SetCapValue(self, _arg: float) -> None: ...
    def SetCapping(self, _arg: int) -> None: ...
    def SetComputeNormals(self, _arg: int) -> None: ...
    def SetImplicitFunction(self, __a: vtkmodules.vtkCommonDataModel.vtkImplicitFunction) -> None: ...
    @overload
    def SetModelBounds(self, bounds: Sequence[float]) -> None: ...
    @overload
    def SetModelBounds(self, xMin: float, xMax: float, yMin: float, yMax: float, zMin: float, zMax: float) -> None: ...
    def SetNormalArrayName(self, _arg: str) -> None: ...
    def SetOutputScalarType(self, _arg: int) -> None: ...
    def SetOutputScalarTypeToChar(self) -> None: ...
    def SetOutputScalarTypeToDouble(self) -> None: ...
    def SetOutputScalarTypeToFloat(self) -> None: ...
    def SetOutputScalarTypeToInt(self) -> None: ...
    def SetOutputScalarTypeToLong(self) -> None: ...
    def SetOutputScalarTypeToShort(self) -> None: ...
    def SetOutputScalarTypeToUnsignedChar(self) -> None: ...
    def SetOutputScalarTypeToUnsignedInt(self) -> None: ...
    def SetOutputScalarTypeToUnsignedLong(self) -> None: ...
    def SetOutputScalarTypeToUnsignedShort(self) -> None: ...
    @overload
    def SetSampleDimensions(self, i: int, j: int, k: int) -> None: ...
    @overload
    def SetSampleDimensions(self, dim: MutableSequence[int]) -> None: ...
    def SetScalarArrayName(self, _arg: str) -> None: ...

class vtkShepardMethod(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def ComputeModelBounds(self, origin: MutableSequence[float], spacing: MutableSequence[float]) -> float: ...
    def GetMaximumDistance(self) -> float: ...
    def GetMaximumDistanceMaxValue(self) -> float: ...
    def GetMaximumDistanceMinValue(self) -> float: ...
    def GetModelBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    def GetNullValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPowerParameter(self) -> float: ...
    def GetPowerParameterMaxValue(self) -> float: ...
    def GetPowerParameterMinValue(self) -> float: ...
    def GetSampleDimensions(self) -> Tuple[int, int, int]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkShepardMethod: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkShepardMethod: ...
    def SetMaximumDistance(self, _arg: float) -> None: ...
    @overload
    def SetModelBounds(self, _arg1: float, _arg2: float, _arg3: float, _arg4: float, _arg5: float, _arg6: float) -> None: ...
    @overload
    def SetModelBounds(self, _arg: Sequence[float]) -> None: ...
    def SetNullValue(self, _arg: float) -> None: ...
    def SetPowerParameter(self, _arg: float) -> None: ...
    @overload
    def SetSampleDimensions(self, i: int, j: int, k: int) -> None: ...
    @overload
    def SetSampleDimensions(self, dim: MutableSequence[int]) -> None: ...

class vtkSliceCubes(vtkmodules.vtkCommonCore.vtkObject):
    def GetFileName(self) -> str: ...
    def GetLimitsFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetReader(self) -> vtkmodules.vtkIOImage.vtkVolumeReader: ...
    def GetValue(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSliceCubes: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSliceCubes: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetLimitsFileName(self, _arg: str) -> None: ...
    def SetReader(self, __a: vtkmodules.vtkIOImage.vtkVolumeReader) -> None: ...
    def SetValue(self, _arg: float) -> None: ...
    def Update(self) -> None: ...
    def Write(self) -> None: ...

class vtkSurfaceReconstructionFilter(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetNeighborhoodSize(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSampleSpacing(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSurfaceReconstructionFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSurfaceReconstructionFilter: ...
    def SetNeighborhoodSize(self, _arg: int) -> None: ...
    def SetSampleSpacing(self, _arg: float) -> None: ...

class vtkTriangularTexture(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetScaleFactor(self) -> float: ...
    def GetTexturePattern(self) -> int: ...
    def GetTexturePatternMaxValue(self) -> int: ...
    def GetTexturePatternMinValue(self) -> int: ...
    def GetXSize(self) -> int: ...
    def GetYSize(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTriangularTexture: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTriangularTexture: ...
    def SetScaleFactor(self, _arg: float) -> None: ...
    def SetTexturePattern(self, _arg: int) -> None: ...
    def SetXSize(self, _arg: int) -> None: ...
    def SetYSize(self, _arg: int) -> None: ...

class vtkVoxelModeller(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def ComputeModelBounds(self, origin: MutableSequence[float], spacing: MutableSequence[float]) -> float: ...
    def GetBackgroundValue(self) -> float: ...
    def GetForegroundValue(self) -> float: ...
    def GetMaximumDistance(self) -> float: ...
    def GetMaximumDistanceMaxValue(self) -> float: ...
    def GetMaximumDistanceMinValue(self) -> float: ...
    def GetModelBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSampleDimensions(self) -> Tuple[int, int, int]: ...
    def GetScalarType(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkVoxelModeller: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkVoxelModeller: ...
    def SetBackgroundValue(self, _arg: float) -> None: ...
    def SetForegroundValue(self, _arg: float) -> None: ...
    def SetMaximumDistance(self, _arg: float) -> None: ...
    @overload
    def SetModelBounds(self, bounds: Sequence[float]) -> None: ...
    @overload
    def SetModelBounds(self, xmin: float, xmax: float, ymin: float, ymax: float, zmin: float, zmax: float) -> None: ...
    @overload
    def SetSampleDimensions(self, i: int, j: int, k: int) -> None: ...
    @overload
    def SetSampleDimensions(self, dim: MutableSequence[int]) -> None: ...
    def SetScalarType(self, _arg: int) -> None: ...
    def SetScalarTypeToBit(self) -> None: ...
    def SetScalarTypeToChar(self) -> None: ...
    def SetScalarTypeToDouble(self) -> None: ...
    def SetScalarTypeToFloat(self) -> None: ...
    def SetScalarTypeToInt(self) -> None: ...
    def SetScalarTypeToLong(self) -> None: ...
    def SetScalarTypeToShort(self) -> None: ...
    def SetScalarTypeToUnsignedChar(self) -> None: ...
    def SetScalarTypeToUnsignedInt(self) -> None: ...
    def SetScalarTypeToUnsignedLong(self) -> None: ...
    def SetScalarTypeToUnsignedShort(self) -> None: ...
