from collections.abc import MutableSequence, Sequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkFiltersStatistics

_Pointer = TypeVar("_Pointer")

class vtkComputeHistogram2DOutliers(vtkmodules.vtkCommonExecutionModel.vtkSelectionAlgorithm):
    class InputPorts(int): ...
    class OutputPorts(int): ...
    INPUT_HISTOGRAMS_IMAGE_DATA: InputPorts
    INPUT_HISTOGRAMS_MULTIBLOCK: InputPorts
    INPUT_TABLE_DATA: InputPorts
    OUTPUT_SELECTED_ROWS: OutputPorts
    OUTPUT_SELECTED_TABLE_DATA: OutputPorts
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputTable(self) -> vtkmodules.vtkCommonDataModel.vtkTable: ...
    def GetPreferredNumberOfOutliers(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkComputeHistogram2DOutliers: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkComputeHistogram2DOutliers: ...
    def SetInputHistogramImageDataConnection(self, cxn: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetInputHistogramMultiBlockConnection(self, cxn: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetInputTableConnection(self, cxn: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetPreferredNumberOfOutliers(self, _arg: int) -> None: ...

class vtkExtractHistogram2D(vtkmodules.vtkFiltersStatistics.vtkStatisticsAlgorithm):
    class OutputIndices(int): ...
    HISTOGRAM_IMAGE: OutputIndices

    def Aggregate(
        self, __a: vtkmodules.vtkCommonDataModel.vtkDataObjectCollection, __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet
    ) -> None: ...
    @overload
    def GetBinRange(self, binX: int, binY: int, range: MutableSequence[float]) -> int: ...
    @overload
    def GetBinRange(self, bin: int, range: MutableSequence[float]) -> int: ...
    def GetBinWidth(self, bw: MutableSequence[float]) -> None: ...
    def GetComponentsToProcess(self) -> tuple[int, int]: ...
    def GetCustomHistogramExtents(self) -> tuple[float, float, float, float]: ...
    def GetHistogramExtents(self) -> _Pointer: ...
    def GetMaximumBinCount(self) -> float: ...
    def GetNumberOfBins(self) -> tuple[int, int]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputHistogramImage(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetRowMask(self) -> vtkmodules.vtkCommonCore.vtkDataArray: ...
    def GetScalarType(self) -> int: ...
    def GetSwapColumns(self) -> int: ...
    def GetUseCustomHistogramExtents(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkExtractHistogram2D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkExtractHistogram2D: ...
    @overload
    def SetComponentsToProcess(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetComponentsToProcess(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetCustomHistogramExtents(self, _arg1: float, _arg2: float, _arg3: float, _arg4: float) -> None: ...
    @overload
    def SetCustomHistogramExtents(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetNumberOfBins(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetNumberOfBins(self, _arg: Sequence[int]) -> None: ...
    def SetRowMask(self, __a: vtkmodules.vtkCommonCore.vtkDataArray) -> None: ...
    def SetScalarType(self, _arg: int) -> None: ...
    def SetScalarTypeToDouble(self) -> None: ...
    def SetScalarTypeToFloat(self) -> None: ...
    def SetScalarTypeToUnsignedChar(self) -> None: ...
    def SetScalarTypeToUnsignedInt(self) -> None: ...
    def SetScalarTypeToUnsignedLong(self) -> None: ...
    def SetScalarTypeToUnsignedShort(self) -> None: ...
    def SetSwapColumns(self, _arg: int) -> None: ...
    def SetUseCustomHistogramExtents(self, _arg: int) -> None: ...
    def SwapColumnsOff(self) -> None: ...
    def SwapColumnsOn(self) -> None: ...
    def UseCustomHistogramExtentsOff(self) -> None: ...
    def UseCustomHistogramExtentsOn(self) -> None: ...

class vtkPairwiseExtractHistogram2D(vtkmodules.vtkFiltersStatistics.vtkStatisticsAlgorithm):
    class OutputIndices(int): ...
    HISTOGRAM_IMAGE: OutputIndices

    def Aggregate(
        self, __a: vtkmodules.vtkCommonDataModel.vtkDataObjectCollection, __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet
    ) -> None: ...
    @overload
    def GetBinRange(self, idx: int, binX: int, binY: int, range: MutableSequence[float]) -> int: ...
    @overload
    def GetBinRange(self, idx: int, bin: int, range: MutableSequence[float]) -> int: ...
    def GetBinWidth(self, idx: int, bw: MutableSequence[float]) -> None: ...
    def GetHistogramExtents(self, idx: int) -> _Pointer: ...
    def GetHistogramFilter(self, idx: int) -> vtkExtractHistogram2D: ...
    @overload
    def GetMaximumBinCount(self, idx: int) -> float: ...
    @overload
    def GetMaximumBinCount(self) -> float: ...
    def GetNumberOfBins(self) -> tuple[int, int]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputHistogramImage(self, idx: int) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetScalarType(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPairwiseExtractHistogram2D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPairwiseExtractHistogram2D: ...
    @overload
    def SetCustomColumnRange(self, col: int, range: MutableSequence[float]) -> None: ...
    @overload
    def SetCustomColumnRange(self, col: int, rmin: float, rmax: float) -> None: ...
    def SetCustomColumnRangeByIndex(self, __a: float, __b: float) -> None: ...
    def SetCustomColumnRangeIndex(self, _arg: int) -> None: ...
    @overload
    def SetNumberOfBins(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetNumberOfBins(self, _arg: Sequence[int]) -> None: ...
    def SetScalarType(self, _arg: int) -> None: ...
    def SetScalarTypeToUnsignedChar(self) -> None: ...
    def SetScalarTypeToUnsignedInt(self) -> None: ...
    def SetScalarTypeToUnsignedLong(self) -> None: ...
    def SetScalarTypeToUnsignedShort(self) -> None: ...
