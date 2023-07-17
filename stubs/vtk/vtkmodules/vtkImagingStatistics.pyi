from collections.abc import Callable, MutableSequence, Sequence
from typing import Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkImagingCore


class vtkImageAccumulate(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    @overload
    def GetComponentExtent(self, extent: MutableSequence[int]) -> None: ...
    @overload
    def GetComponentExtent(self) -> Tuple[int, int, int, int, int, int]: ...
    def GetComponentOrigin(self) -> Tuple[float, float, float]: ...
    def GetComponentSpacing(self) -> Tuple[float, float, float]: ...
    def GetIgnoreZero(self) -> int: ...
    def GetIgnoreZeroMaxValue(self) -> int: ...
    def GetIgnoreZeroMinValue(self) -> int: ...
    def GetMax(self) -> Tuple[float, float, float]: ...
    def GetMean(self) -> Tuple[float, float, float]: ...
    def GetMin(self) -> Tuple[float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetReverseStencil(self) -> int: ...
    def GetReverseStencilMaxValue(self) -> int: ...
    def GetReverseStencilMinValue(self) -> int: ...
    def GetStandardDeviation(self) -> Tuple[float, float, float]: ...
    def GetStencil(self) -> vtkmodules.vtkImagingCore.vtkImageStencilData: ...
    def GetVoxelCount(self) -> int: ...
    def IgnoreZeroOff(self) -> None: ...
    def IgnoreZeroOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageAccumulate: ...
    def ReverseStencilOff(self) -> None: ...
    def ReverseStencilOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageAccumulate: ...
    @overload
    def SetComponentExtent(self, extent: MutableSequence[int]) -> None: ...
    @overload
    def SetComponentExtent(self, minX: int, maxX: int, minY: int, maxY: int, minZ: int, maxZ: int) -> None: ...
    @overload
    def SetComponentOrigin(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetComponentOrigin(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetComponentSpacing(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetComponentSpacing(self, _arg: Sequence[float]) -> None: ...
    def SetIgnoreZero(self, _arg: int) -> None: ...
    def SetReverseStencil(self, _arg: int) -> None: ...
    def SetStencilData(self, stencil: vtkmodules.vtkImagingCore.vtkImageStencilData) -> None: ...

class vtkImageHistogram(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    Linear: int
    Log: int
    Sqrt: int
    def AutomaticBinningOff(self) -> None: ...
    def AutomaticBinningOn(self) -> None: ...
    def GenerateHistogramImageOff(self) -> None: ...
    def GenerateHistogramImageOn(self) -> None: ...
    def GetActiveComponent(self) -> int: ...
    def GetAutomaticBinning(self) -> int: ...
    def GetBinOrigin(self) -> float: ...
    def GetBinSpacing(self) -> float: ...
    def GetGenerateHistogramImage(self) -> int: ...
    def GetHistogram(self) -> vtkmodules.vtkCommonCore.vtkIdTypeArray: ...
    def GetHistogramImageScale(self) -> int: ...
    def GetHistogramImageScaleAsString(self) -> str: ...
    def GetHistogramImageScaleMaxValue(self) -> int: ...
    def GetHistogramImageScaleMinValue(self) -> int: ...
    def GetHistogramImageSize(self) -> Tuple[int, int]: ...
    def GetMaximumNumberOfBins(self) -> int: ...
    def GetNumberOfBins(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetStencil(self) -> vtkmodules.vtkImagingCore.vtkImageStencilData: ...
    def GetTotal(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageHistogram: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageHistogram: ...
    def SetActiveComponent(self, _arg: int) -> None: ...
    def SetAutomaticBinning(self, _arg: int) -> None: ...
    def SetBinOrigin(self, _arg: float) -> None: ...
    def SetBinSpacing(self, _arg: float) -> None: ...
    def SetGenerateHistogramImage(self, _arg: int) -> None: ...
    def SetHistogramImageScale(self, _arg: int) -> None: ...
    def SetHistogramImageScaleToLinear(self) -> None: ...
    def SetHistogramImageScaleToLog(self) -> None: ...
    def SetHistogramImageScaleToSqrt(self) -> None: ...
    @overload
    def SetHistogramImageSize(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetHistogramImageSize(self, _arg: Sequence[int]) -> None: ...
    def SetMaximumNumberOfBins(self, _arg: int) -> None: ...
    def SetNumberOfBins(self, _arg: int) -> None: ...
    def SetStencilConnection(self, algOutput: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetStencilData(self, stencil: vtkmodules.vtkImagingCore.vtkImageStencilData) -> None: ...

class vtkImageHistogramStatistics(vtkImageHistogram):
    def GetAutoRange(self) -> Tuple[float, float]: ...
    def GetAutoRangeExpansionFactors(self) -> Tuple[float, float]: ...
    def GetAutoRangePercentiles(self) -> Tuple[float, float]: ...
    def GetMaximum(self) -> float: ...
    def GetMean(self) -> float: ...
    def GetMedian(self) -> float: ...
    def GetMinimum(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetStandardDeviation(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageHistogramStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageHistogramStatistics: ...
    @overload
    def SetAutoRangeExpansionFactors(self, _arg1: float, _arg2: float) -> None: ...
    @overload
    def SetAutoRangeExpansionFactors(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetAutoRangePercentiles(self, _arg1: float, _arg2: float) -> None: ...
    @overload
    def SetAutoRangePercentiles(self, _arg: Sequence[float]) -> None: ...
