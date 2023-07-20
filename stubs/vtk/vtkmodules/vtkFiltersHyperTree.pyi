from collections.abc import MutableSequence, Sequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkFiltersCore

_Pointer = TypeVar("_Pointer")

class vtkHyperTreeGridAxisClip(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    class ClipType(int): ...
    BOX: ClipType
    PLANE: ClipType
    QUADRIC: ClipType
    def GetBounds(self) -> tuple[float, float, float, float, float, float]: ...
    def GetClipType(self) -> int: ...
    def GetClipTypeMaxValue(self) -> int: ...
    def GetClipTypeMinValue(self) -> int: ...
    def GetInsideOut(self) -> bool: ...
    def GetMTime(self) -> int: ...
    def GetMaximumBounds(self, __a: MutableSequence[float]) -> None: ...
    def GetMinimumBounds(self, __a: MutableSequence[float]) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPlaneNormalAxis(self) -> int: ...
    def GetPlaneNormalAxisMaxValue(self) -> int: ...
    def GetPlaneNormalAxisMinValue(self) -> int: ...
    def GetPlanePosition(self) -> float: ...
    def GetQuadric(self) -> vtkmodules.vtkCommonDataModel.vtkQuadric: ...
    @overload
    def GetQuadricCoefficients(self, __a: MutableSequence[float]) -> None: ...
    @overload
    def GetQuadricCoefficients(self) -> _Pointer: ...
    def InsideOutOff(self) -> None: ...
    def InsideOutOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridAxisClip: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridAxisClip: ...
    @overload
    def SetBounds(self, _arg1: float, _arg2: float, _arg3: float, _arg4: float, _arg5: float, _arg6: float) -> None: ...
    @overload
    def SetBounds(self, _arg: Sequence[float]) -> None: ...
    def SetClipType(self, _arg: int) -> None: ...
    def SetClipTypeToBox(self) -> None: ...
    def SetClipTypeToPlane(self) -> None: ...
    def SetClipTypeToQuadric(self) -> None: ...
    def SetInsideOut(self, _arg: bool) -> None: ...
    def SetPlaneNormalAxis(self, _arg: int) -> None: ...
    def SetPlanePosition(self, _arg: float) -> None: ...
    def SetQuadric(self, __a: vtkmodules.vtkCommonDataModel.vtkQuadric) -> None: ...
    @overload
    def SetQuadricCoefficients(
        self, a: float, b: float, c: float, d: float, e: float, f: float, g: float, h: float, i: float, j: float
    ) -> None: ...
    @overload
    def SetQuadricCoefficients(self, __a: MutableSequence[float]) -> None: ...

class vtkHyperTreeGridAxisCut(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPlaneNormalAxis(self) -> int: ...
    def GetPlaneNormalAxisMaxValue(self) -> int: ...
    def GetPlaneNormalAxisMinValue(self) -> int: ...
    def GetPlanePosition(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridAxisCut: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridAxisCut: ...
    def SetPlaneNormalAxis(self, _arg: int) -> None: ...
    def SetPlanePosition(self, _arg: float) -> None: ...

class vtkHyperTreeGridAxisReflection(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    class AxisReflectionPlane(int): ...
    USE_X: AxisReflectionPlane
    USE_X_MAX: AxisReflectionPlane
    USE_X_MIN: AxisReflectionPlane
    USE_Y: AxisReflectionPlane
    USE_Y_MAX: AxisReflectionPlane
    USE_Y_MIN: AxisReflectionPlane
    USE_Z: AxisReflectionPlane
    USE_Z_MAX: AxisReflectionPlane
    USE_Z_MIN: AxisReflectionPlane
    def GetCenter(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPlane(self) -> int: ...
    def GetPlaneMaxValue(self) -> int: ...
    def GetPlaneMinValue(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridAxisReflection: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridAxisReflection: ...
    def SetCenter(self, _arg: float) -> None: ...
    def SetPlane(self, _arg: int) -> None: ...
    def SetPlaneToX(self) -> None: ...
    def SetPlaneToXMax(self) -> None: ...
    def SetPlaneToXMin(self) -> None: ...
    def SetPlaneToY(self) -> None: ...
    def SetPlaneToYMax(self) -> None: ...
    def SetPlaneToYMin(self) -> None: ...
    def SetPlaneToZ(self) -> None: ...
    def SetPlaneToZMax(self) -> None: ...
    def SetPlaneToZMin(self) -> None: ...

class vtkHyperTreeGridCellCenters(vtkmodules.vtkFiltersCore.vtkCellCenters):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridCellCenters: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridCellCenters: ...

class vtkHyperTreeGridContour(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    def CreateDefaultLocator(self) -> None: ...
    @overload
    def GenerateValues(self, __a: int, __b: MutableSequence[float]) -> None: ...
    @overload
    def GenerateValues(self, __a: int, __b: float, __c: float) -> None: ...
    def GetLocator(self) -> vtkmodules.vtkCommonDataModel.vtkIncrementalPointLocator: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfContours(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetValue(self, __a: int) -> float: ...
    @overload
    def GetValues(self) -> _Pointer: ...
    @overload
    def GetValues(self, __a: MutableSequence[float]) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridContour: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridContour: ...
    def SetLocator(self, __a: vtkmodules.vtkCommonDataModel.vtkIncrementalPointLocator) -> None: ...
    def SetNumberOfContours(self, __a: int) -> None: ...
    def SetValue(self, __a: int, __b: float) -> None: ...

class vtkHyperTreeGridDepthLimiter(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    def GetDepth(self) -> int: ...
    def GetJustCreateNewMask(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridDepthLimiter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridDepthLimiter: ...
    def SetDepth(self, _arg: int) -> None: ...
    def SetJustCreateNewMask(self, _arg: bool) -> None: ...

class vtkHyperTreeGridEvaluateCoarse(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    OPERATOR_AVERAGE: int
    OPERATOR_DON_T_CHANGE: int
    OPERATOR_DON_T_CHANGE_FAST: int
    OPERATOR_ELDER_CHILD: int
    OPERATOR_MAX: int
    OPERATOR_MIN: int
    OPERATOR_SPLATTING_AVERAGE: int
    OPERATOR_SUM: int
    OPERATOR_UNMASKED_AVERAGE: int
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOperator(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridEvaluateCoarse: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridEvaluateCoarse: ...
    def SetDefault(self, _arg: float) -> None: ...
    def SetOperator(self, _arg: int) -> None: ...

class vtkHyperTreeGridGeometry(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    def GetMerging(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridGeometry: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridGeometry: ...
    def SetMerging(self, _arg: bool) -> None: ...

class vtkHyperTreeGridGradient(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetResultArrayName(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridGradient: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridGradient: ...
    def SetResultArrayName(self, _arg: str) -> None: ...

class vtkHyperTreeGridPlaneCutter(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    def DualOff(self) -> None: ...
    def DualOn(self) -> None: ...
    def GetAxisAlignment(self) -> int: ...
    def GetDual(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPlane(self) -> tuple[float, float, float, float]: ...
    def IsA(self, type: str) -> int: ...
    def IsPlaneOrthogonalToXAxis(self) -> bool: ...
    def IsPlaneOrthogonalToYAxis(self) -> bool: ...
    def IsPlaneOrthogonalToZAxis(self) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridPlaneCutter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridPlaneCutter: ...
    def SetDual(self, _arg: int) -> None: ...
    def SetPlane(self, a: float, b: float, c: float, d: float) -> None: ...

class vtkHyperTreeGridThreshold(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    def GetJustCreateNewMask(self) -> bool: ...
    def GetLowerThreshold(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetUpperThreshold(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridThreshold: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridThreshold: ...
    def SetJustCreateNewMask(self, _arg: bool) -> None: ...
    def SetLowerThreshold(self, _arg: float) -> None: ...
    def SetUpperThreshold(self, _arg: float) -> None: ...
    def ThresholdBetween(self, __a: float, __b: float) -> None: ...

class vtkHyperTreeGridToDualGrid(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridToDualGrid: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridToDualGrid: ...

class vtkHyperTreeGridToUnstructuredGrid(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    def AddOriginalIdsOff(self) -> None: ...
    def AddOriginalIdsOn(self) -> None: ...
    def GetAddOriginalIds(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridToUnstructuredGrid: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridToUnstructuredGrid: ...
    def SetAddOriginalIds(self, _arg: bool) -> None: ...

class vtkImageDataToHyperTreeGrid(vtkmodules.vtkCommonExecutionModel.vtkHyperTreeGridAlgorithm):
    def GetDepthMax(self) -> int: ...
    def GetNbColors(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageDataToHyperTreeGrid: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageDataToHyperTreeGrid: ...
    def SetDepthMax(self, _arg: int) -> None: ...
    def SetNbColors(self, _arg: int) -> None: ...
