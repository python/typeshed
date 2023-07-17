from collections.abc import Sequence
from typing import Tuple, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkFiltersCore
import vtkmodules.vtkParallelCore

class vtkAdaptiveResampleToImage(vtkmodules.vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfImages(self) -> int: ...
    def GetNumberOfImagesMaxValue(self) -> int: ...
    def GetNumberOfImagesMinValue(self) -> int: ...
    def GetSamplingDimensions(self) -> Tuple[int, int, int]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkAdaptiveResampleToImage: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkAdaptiveResampleToImage: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def SetNumberOfImages(self, _arg: int) -> None: ...
    @overload
    def SetSamplingDimensions(self, _arg1: int, _arg2: int, _arg3: int) -> None: ...
    @overload
    def SetSamplingDimensions(self, _arg: Sequence[int]) -> None: ...

class vtkExtractSubsetWithSeed(vtkmodules.vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    LINE_I: int
    LINE_J: int
    LINE_K: int
    PLANE_IJ: int
    PLANE_JK: int
    PLANE_KI: int
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetDirection(self) -> int: ...
    def GetDirectionMaxValue(self) -> int: ...
    def GetDirectionMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSeed(self) -> Tuple[float, float, float]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkExtractSubsetWithSeed: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkExtractSubsetWithSeed: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def SetDirection(self, _arg: int) -> None: ...
    def SetDirectionToLineI(self) -> None: ...
    def SetDirectionToLineJ(self) -> None: ...
    def SetDirectionToLineK(self) -> None: ...
    def SetDirectionToPlaneIJ(self) -> None: ...
    def SetDirectionToPlaneJK(self) -> None: ...
    def SetDirectionToPlaneKI(self) -> None: ...
    @overload
    def SetSeed(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetSeed(self, _arg: Sequence[float]) -> None: ...

class vtkGenerateGlobalIds(vtkmodules.vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTolerance(self) -> float: ...
    def GetToleranceMaxValue(self) -> float: ...
    def GetToleranceMinValue(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGenerateGlobalIds: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGenerateGlobalIds: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def SetTolerance(self, _arg: float) -> None: ...

class vtkGhostCellsGenerator(vtkmodules.vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    def BuildIfRequiredOff(self) -> None: ...
    def BuildIfRequiredOn(self) -> None: ...
    def GetBuildIfRequired(self) -> bool: ...
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfGhostLayers(self) -> int: ...
    def GetNumberOfGhostLayersMaxValue(self) -> int: ...
    def GetNumberOfGhostLayersMinValue(self) -> int: ...
    def Initialize(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGhostCellsGenerator: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGhostCellsGenerator: ...
    def SetBuildIfRequired(self, _arg: bool) -> None: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def SetNumberOfGhostLayers(self, _arg: int) -> None: ...

class vtkOverlappingCellsDetector(vtkmodules.vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfOverlapsPerCellArrayName(self) -> str: ...
    def GetTolerance(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOverlappingCellsDetector: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOverlappingCellsDetector: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def SetNumberOfOverlapsPerCellArrayName(self, _arg: str) -> None: ...
    def SetTolerance(self, _arg: float) -> None: ...

class vtkPResampleToImage(vtkmodules.vtkFiltersCore.vtkResampleToImage):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPResampleToImage: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPResampleToImage: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...

class vtkPResampleWithDataSet(vtkmodules.vtkFiltersCore.vtkResampleWithDataSet):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetUseBalancedPartitionForPointsLookup(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPResampleWithDataSet: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPResampleWithDataSet: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def SetUseBalancedPartitionForPointsLookup(self, _arg: bool) -> None: ...
    def UseBalancedPartitionForPointsLookupOff(self) -> None: ...
    def UseBalancedPartitionForPointsLookupOn(self) -> None: ...

class vtkProbeLineFilter(vtkmodules.vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    class SamplingPatternEnum(int): ...
    SAMPLE_LINE_AT_CELL_BOUNDARIES: SamplingPatternEnum
    SAMPLE_LINE_AT_SEGMENT_CENTERS: SamplingPatternEnum
    SAMPLE_LINE_UNIFORMLY: SamplingPatternEnum
    def AggregateAsPolyDataOff(self) -> None: ...
    def AggregateAsPolyDataOn(self) -> None: ...
    def ComputeToleranceOff(self) -> None: ...
    def ComputeToleranceOn(self) -> None: ...
    def GetAggregateAsPolyData(self) -> bool: ...
    def GetComputeTolerance(self) -> bool: ...
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetLineResolution(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPassCellArrays(self) -> bool: ...
    def GetPassFieldArrays(self) -> bool: ...
    def GetPassPartialArrays(self) -> bool: ...
    def GetPassPointArrays(self) -> bool: ...
    def GetSamplingPattern(self) -> int: ...
    def GetSamplingPatternMaxValue(self) -> int: ...
    def GetSamplingPatternMinValue(self) -> int: ...
    def GetTolerance(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkProbeLineFilter: ...
    def PassCellArraysOff(self) -> None: ...
    def PassCellArraysOn(self) -> None: ...
    def PassFieldArraysOff(self) -> None: ...
    def PassFieldArraysOn(self) -> None: ...
    def PassPartialArraysOff(self) -> None: ...
    def PassPartialArraysOn(self) -> None: ...
    def PassPointArraysOff(self) -> None: ...
    def PassPointArraysOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkProbeLineFilter: ...
    def SetAggregateAsPolyData(self, _arg: bool) -> None: ...
    def SetComputeTolerance(self, _arg: bool) -> None: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def SetLineResolution(self, _arg: int) -> None: ...
    def SetPassCellArrays(self, _arg: bool) -> None: ...
    def SetPassFieldArrays(self, _arg: bool) -> None: ...
    def SetPassPartialArrays(self, _arg: bool) -> None: ...
    def SetPassPointArrays(self, _arg: bool) -> None: ...
    def SetSamplingPattern(self, _arg: int) -> None: ...
    def SetSourceConnection(self, input: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetTolerance(self, _arg: float) -> None: ...

class vtkRedistributeDataSetFilter(vtkmodules.vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    class BoundaryModes(int): ...
    ASSIGN_TO_ALL_INTERSECTING_REGIONS: BoundaryModes
    ASSIGN_TO_ONE_REGION: BoundaryModes
    SPLIT_BOUNDARY_CELLS: BoundaryModes

    @overload
    def AddExplicitCut(self, bbox: vtkmodules.vtkCommonDataModel.vtkBoundingBox) -> None: ...
    @overload
    def AddExplicitCut(self, bbox: Sequence[float]) -> None: ...
    def EnableDebuggingOff(self) -> None: ...
    def EnableDebuggingOn(self) -> None: ...
    def ExpandExplicitCutsOff(self) -> None: ...
    def ExpandExplicitCutsOn(self) -> None: ...
    def GenerateGlobalCellIdsOff(self) -> None: ...
    def GenerateGlobalCellIdsOn(self) -> None: ...
    def GetBoundaryMode(self) -> int: ...
    def GetBoundaryModeMaxValue(self) -> int: ...
    def GetBoundaryModeMinValue(self) -> int: ...
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetEnableDebugging(self) -> bool: ...
    def GetExpandExplicitCuts(self) -> bool: ...
    def GetExplicitCut(self, index: int) -> vtkmodules.vtkCommonDataModel.vtkBoundingBox: ...
    def GetGenerateGlobalCellIds(self) -> bool: ...
    def GetLoadBalanceAcrossAllBlocks(self) -> bool: ...
    def GetNumberOfExplicitCuts(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfPartitions(self) -> int: ...
    def GetNumberOfPartitionsMaxValue(self) -> int: ...
    def GetNumberOfPartitionsMinValue(self) -> int: ...
    def GetPreservePartitionsInOutput(self) -> bool: ...
    def GetUseExplicitCuts(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def LoadBalanceAcrossAllBlocksOff(self) -> None: ...
    def LoadBalanceAcrossAllBlocksOn(self) -> None: ...
    def NewInstance(self) -> vtkRedistributeDataSetFilter: ...
    def PreservePartitionsInOutputOff(self) -> None: ...
    def PreservePartitionsInOutputOn(self) -> None: ...
    def RemoveAllExplicitCuts(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkRedistributeDataSetFilter: ...
    def SetBoundaryMode(self, _arg: int) -> None: ...
    def SetBoundaryModeToAssignToAllIntersectingRegions(self) -> None: ...
    def SetBoundaryModeToAssignToOneRegion(self) -> None: ...
    def SetBoundaryModeToSplitBoundaryCells(self) -> None: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def SetEnableDebugging(self, _arg: bool) -> None: ...
    def SetExpandExplicitCuts(self, _arg: bool) -> None: ...
    def SetGenerateGlobalCellIds(self, _arg: bool) -> None: ...
    def SetLoadBalanceAcrossAllBlocks(self, _arg: bool) -> None: ...
    def SetNumberOfPartitions(self, _arg: int) -> None: ...
    def SetPreservePartitionsInOutput(self, _arg: bool) -> None: ...
    def SetUseExplicitCuts(self, _arg: bool) -> None: ...
    def UseExplicitCutsOff(self) -> None: ...
    def UseExplicitCutsOn(self) -> None: ...
