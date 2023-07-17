from collections.abc import MutableSequence, Sequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkImagingCore
import vtkmodules.vtkImagingGeneral


VTK_IMAGE_NON_MAXIMUM_SUPPRESSION_MAGNITUDE_INPUT: int
VTK_IMAGE_NON_MAXIMUM_SUPPRESSION_VECTOR_INPUT: int

class vtkImage2DIslandPixel_t:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __a: vtkImage2DIslandPixel_t) -> None: ...

class vtkImageConnectivityFilter(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    class ExtractionModeEnum(int): ...
    class LabelModeEnum(int): ...
    AllRegions: ExtractionModeEnum
    ConstantValue: LabelModeEnum
    LargestRegion: ExtractionModeEnum
    SeedScalar: LabelModeEnum
    SeededRegions: ExtractionModeEnum
    SizeRank: LabelModeEnum
    def GenerateRegionExtentsOff(self) -> None: ...
    def GenerateRegionExtentsOn(self) -> None: ...
    def GetActiveComponent(self) -> int: ...
    def GetExtractedRegionExtents(self) -> vtkmodules.vtkCommonCore.vtkIntArray: ...
    def GetExtractedRegionLabels(self) -> vtkmodules.vtkCommonCore.vtkIdTypeArray: ...
    def GetExtractedRegionSeedIds(self) -> vtkmodules.vtkCommonCore.vtkIdTypeArray: ...
    def GetExtractedRegionSizes(self) -> vtkmodules.vtkCommonCore.vtkIdTypeArray: ...
    def GetExtractionMode(self) -> int: ...
    def GetExtractionModeAsString(self) -> str: ...
    def GetGenerateRegionExtents(self) -> int: ...
    def GetLabelConstantValue(self) -> int: ...
    def GetLabelMode(self) -> int: ...
    def GetLabelModeAsString(self) -> str: ...
    def GetLabelScalarType(self) -> int: ...
    def GetLabelScalarTypeAsString(self) -> str: ...
    def GetNumberOfExtractedRegions(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetScalarRange(self) -> Tuple[float, float]: ...
    def GetSeedConnection(self) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    def GetSizeRange(self) -> Tuple[int, int]: ...
    def GetStencilConnection(self) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageConnectivityFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageConnectivityFilter: ...
    def SetActiveComponent(self, _arg: int) -> None: ...
    def SetExtractionMode(self, _arg: int) -> None: ...
    def SetExtractionModeToAllRegions(self) -> None: ...
    def SetExtractionModeToLargestRegion(self) -> None: ...
    def SetExtractionModeToSeededRegions(self) -> None: ...
    def SetGenerateRegionExtents(self, _arg: int) -> None: ...
    def SetLabelConstantValue(self, _arg: int) -> None: ...
    def SetLabelMode(self, _arg: int) -> None: ...
    def SetLabelModeToConstantValue(self) -> None: ...
    def SetLabelModeToSeedScalar(self) -> None: ...
    def SetLabelModeToSizeRank(self) -> None: ...
    def SetLabelScalarType(self, _arg: int) -> None: ...
    def SetLabelScalarTypeToInt(self) -> None: ...
    def SetLabelScalarTypeToShort(self) -> None: ...
    def SetLabelScalarTypeToUnsignedChar(self) -> None: ...
    def SetLabelScalarTypeToUnsignedShort(self) -> None: ...
    @overload
    def SetScalarRange(self, _arg1: float, _arg2: float) -> None: ...
    @overload
    def SetScalarRange(self, _arg: Sequence[float]) -> None: ...
    def SetSeedConnection(self, port: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetSeedData(self, data: vtkmodules.vtkCommonDataModel.vtkDataSet) -> None: ...
    @overload
    def SetSizeRange(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetSizeRange(self, _arg: Sequence[int]) -> None: ...
    def SetStencilConnection(self, port: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetStencilData(self, data: vtkmodules.vtkImagingCore.vtkImageStencilData) -> None: ...

class vtkImageConnector(vtkmodules.vtkCommonCore.vtkObject):
    def GetConnectedValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetUnconnectedValue(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MarkData(
        self, data: vtkmodules.vtkCommonDataModel.vtkImageData, dimensionality: int, ext: MutableSequence[int]
    ) -> None: ...
    def NewInstance(self) -> vtkImageConnector: ...
    def RemoveAllSeeds(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageConnector: ...
    def SetConnectedValue(self, _arg: int) -> None: ...
    def SetUnconnectedValue(self, _arg: int) -> None: ...

class vtkImageConnectorSeed:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __a: vtkImageConnectorSeed) -> None: ...

class vtkImageContinuousDilate3D(vtkmodules.vtkImagingGeneral.vtkImageSpatialAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageContinuousDilate3D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageContinuousDilate3D: ...
    def SetKernelSize(self, size0: int, size1: int, size2: int) -> None: ...

class vtkImageContinuousErode3D(vtkmodules.vtkImagingGeneral.vtkImageSpatialAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageContinuousErode3D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageContinuousErode3D: ...
    def SetKernelSize(self, size0: int, size1: int, size2: int) -> None: ...

class vtkImageDilateErode3D(vtkmodules.vtkImagingGeneral.vtkImageSpatialAlgorithm):
    def GetDilateValue(self) -> float: ...
    def GetErodeValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageDilateErode3D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageDilateErode3D: ...
    def SetDilateValue(self, _arg: float) -> None: ...
    def SetErodeValue(self, _arg: float) -> None: ...
    def SetKernelSize(self, size0: int, size1: int, size2: int) -> None: ...

class vtkImageIslandRemoval2D(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetAreaThreshold(self) -> int: ...
    def GetIslandValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetReplaceValue(self) -> float: ...
    def GetSquareNeighborhood(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageIslandRemoval2D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageIslandRemoval2D: ...
    def SetAreaThreshold(self, _arg: int) -> None: ...
    def SetIslandValue(self, _arg: float) -> None: ...
    def SetReplaceValue(self, _arg: float) -> None: ...
    def SetSquareNeighborhood(self, _arg: int) -> None: ...
    def SquareNeighborhoodOff(self) -> None: ...
    def SquareNeighborhoodOn(self) -> None: ...

class vtkImageNonMaximumSuppression(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
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
    def NewInstance(self) -> vtkImageNonMaximumSuppression: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageNonMaximumSuppression: ...
    def SetDimensionality(self, _arg: int) -> None: ...
    def SetHandleBoundaries(self, _arg: int) -> None: ...
    def SetMagnitudeInputData(self, input: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    def SetVectorInputData(self, input: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...

class vtkImageOpenClose3D(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def DebugOff(self) -> None: ...
    def DebugOn(self) -> None: ...
    def GetCloseValue(self) -> float: ...
    def GetFilter0(self) -> vtkImageDilateErode3D: ...
    def GetFilter1(self) -> vtkImageDilateErode3D: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOpenValue(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def Modified(self) -> None: ...
    def NewInstance(self) -> vtkImageOpenClose3D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageOpenClose3D: ...
    def SetCloseValue(self, value: float) -> None: ...
    def SetKernelSize(self, size0: int, size1: int, size2: int) -> None: ...
    def SetOpenValue(self, value: float) -> None: ...

class vtkImageSeedConnectivity(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    @overload
    def AddSeed(self, num: int, index: MutableSequence[int]) -> None: ...
    @overload
    def AddSeed(self, i0: int, i1: int, i2: int) -> None: ...
    @overload
    def AddSeed(self, i0: int, i1: int) -> None: ...
    def GetConnector(self) -> vtkImageConnector: ...
    def GetDimensionality(self) -> int: ...
    def GetInputConnectValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputConnectedValue(self) -> int: ...
    def GetOutputUnconnectedValue(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageSeedConnectivity: ...
    def RemoveAllSeeds(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageSeedConnectivity: ...
    def SetDimensionality(self, _arg: int) -> None: ...
    def SetInputConnectValue(self, _arg: int) -> None: ...
    def SetOutputConnectedValue(self, _arg: int) -> None: ...
    def SetOutputUnconnectedValue(self, _arg: int) -> None: ...

class vtkImageSkeleton2D(vtkmodules.vtkImagingCore.vtkImageIterateFilter):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPrune(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageSkeleton2D: ...
    def PruneOff(self) -> None: ...
    def PruneOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageSkeleton2D: ...
    def SetNumberOfIterations(self, num: int) -> None: ...
    def SetPrune(self, _arg: int) -> None: ...

class vtkImageThresholdConnectivity(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetActiveComponent(self) -> int: ...
    def GetInValue(self) -> float: ...
    def GetLowerThreshold(self) -> float: ...
    def GetMTime(self) -> int: ...
    def GetNeighborhoodFraction(self) -> float: ...
    def GetNeighborhoodFractionMaxValue(self) -> float: ...
    def GetNeighborhoodFractionMinValue(self) -> float: ...
    def GetNeighborhoodRadius(self) -> Tuple[float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfInVoxels(self) -> int: ...
    def GetOutValue(self) -> float: ...
    def GetReplaceIn(self) -> int: ...
    def GetReplaceOut(self) -> int: ...
    def GetSeedPoints(self) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    def GetSliceRangeX(self) -> Tuple[int, int]: ...
    def GetSliceRangeY(self) -> Tuple[int, int]: ...
    def GetSliceRangeZ(self) -> Tuple[int, int]: ...
    def GetStencil(self) -> vtkmodules.vtkImagingCore.vtkImageStencilData: ...
    def GetUpperThreshold(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageThresholdConnectivity: ...
    def ReplaceInOff(self) -> None: ...
    def ReplaceInOn(self) -> None: ...
    def ReplaceOutOff(self) -> None: ...
    def ReplaceOutOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageThresholdConnectivity: ...
    def SetActiveComponent(self, _arg: int) -> None: ...
    def SetInValue(self, val: float) -> None: ...
    def SetNeighborhoodFraction(self, _arg: float) -> None: ...
    @overload
    def SetNeighborhoodRadius(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetNeighborhoodRadius(self, _arg: Sequence[float]) -> None: ...
    def SetOutValue(self, val: float) -> None: ...
    def SetReplaceIn(self, _arg: int) -> None: ...
    def SetReplaceOut(self, _arg: int) -> None: ...
    def SetSeedPoints(self, points: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...
    @overload
    def SetSliceRangeX(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetSliceRangeX(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetSliceRangeY(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetSliceRangeY(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetSliceRangeZ(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetSliceRangeZ(self, _arg: Sequence[int]) -> None: ...
    def SetStencilData(self, stencil: vtkmodules.vtkImagingCore.vtkImageStencilData) -> None: ...
    def ThresholdBetween(self, lower: float, upper: float) -> None: ...
    def ThresholdByLower(self, thresh: float) -> None: ...
    def ThresholdByUpper(self, thresh: float) -> None: ...
