from typing import Callable, MutableSequence, Sequence, Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkCommonTransforms
import vtkmodules.vtkFiltersCore
import vtkmodules.vtkFiltersGeneral
import vtkmodules.vtkImagingCore

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkmAverageToCells(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmAverageToCells: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmAverageToCells: ...

class vtkmAverageToPoints(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmAverageToPoints: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmAverageToPoints: ...

class vtkmCleanGrid(vtkmodules.vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    def CompactPointsOff(self) -> None: ...
    def CompactPointsOn(self) -> None: ...
    def GetCompactPoints(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmCleanGrid: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmCleanGrid: ...
    def SetCompactPoints(self, _arg: bool) -> None: ...

class vtkmClip(vtkmodules.vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    def ForceVTKmOff(self) -> None: ...
    def ForceVTKmOn(self) -> None: ...
    def GetClipFunction(self) -> vtkmodules.vtkCommonDataModel.vtkImplicitFunction: ...
    def GetClipValue(self) -> float: ...
    def GetComputeScalars(self) -> bool: ...
    def GetForceVTKm(self) -> int: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmClip: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmClip: ...
    def SetClipFunction(self, __a: vtkmodules.vtkCommonDataModel.vtkImplicitFunction) -> None: ...
    def SetClipValue(self, __a: float) -> None: ...
    def SetComputeScalars(self, __a: bool) -> None: ...
    def SetForceVTKm(self, _arg: int) -> None: ...

class vtkmContour(vtkmodules.vtkFiltersCore.vtkContourFilter):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmContour: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmContour: ...

class vtkmCoordinateSystemTransform(vtkmodules.vtkCommonExecutionModel.vtkPointSetAlgorithm):
    def FillInputPortInformation(self, port: int, info: vtkmodules.vtkCommonCore.vtkInformation) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmCoordinateSystemTransform: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmCoordinateSystemTransform: ...
    def SetCartesianToCylindrical(self) -> None: ...
    def SetCartesianToSpherical(self) -> None: ...
    def SetCylindricalToCartesian(self) -> None: ...
    def SetSphericalToCartesian(self) -> None: ...

class vtkmExternalFaces(vtkmodules.vtkCommonExecutionModel.vtkAlgorithm):
    def CompactPointsOff(self) -> None: ...
    def CompactPointsOn(self) -> None: ...
    def GetCompactPoints(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkUnstructuredGrid: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmExternalFaces: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmExternalFaces: ...
    def SetCompactPoints(self, _arg: bool) -> None: ...
    def SetInputData(self, ds: vtkmodules.vtkCommonDataModel.vtkUnstructuredGrid) -> None: ...

class vtkmExtractVOI(vtkmodules.vtkImagingCore.vtkExtractVOI):
    def ForceVTKmOff(self) -> None: ...
    def ForceVTKmOn(self) -> None: ...
    def GetForceVTKm(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmExtractVOI: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmExtractVOI: ...
    def SetForceVTKm(self, _arg: int) -> None: ...

class vtkmFilterOverrides:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __a: vtkmFilterOverrides) -> None: ...
    @staticmethod
    def EnabledOff() -> None: ...
    @staticmethod
    def EnabledOn() -> None: ...
    @staticmethod
    def GetEnabled() -> bool: ...
    @staticmethod
    def SetEnabled(value: bool) -> None: ...

class vtkmGradient(vtkmodules.vtkFiltersGeneral.vtkGradientFilter):
    def ForceVTKmOff(self) -> None: ...
    def ForceVTKmOn(self) -> None: ...
    def GetForceVTKm(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmGradient: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmGradient: ...
    def SetForceVTKm(self, _arg: int) -> None: ...

class vtkmHistogram(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    def CenterBinsAroundMinAndMaxOff(self) -> None: ...
    def CenterBinsAroundMinAndMaxOn(self) -> None: ...
    def GetBinDelta(self) -> float: ...
    def GetCenterBinsAroundMinAndMax(self) -> bool: ...
    def GetComputedRange(self) -> Tuple[float, float]: ...
    def GetCustomBinRange(self) -> Tuple[float, float]: ...
    def GetNumberOfBins(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetUseCustomBinRanges(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmHistogram: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmHistogram: ...
    def SetCenterBinsAroundMinAndMax(self, _arg: bool) -> None: ...
    @overload
    def SetCustomBinRange(self, _arg1: float, _arg2: float) -> None: ...
    @overload
    def SetCustomBinRange(self, _arg: Sequence[float]) -> None: ...
    def SetNumberOfBins(self, _arg: int) -> None: ...
    def SetUseCustomBinRanges(self, _arg: bool) -> None: ...
    def UseCustomBinRangesOff(self) -> None: ...
    def UseCustomBinRangesOn(self) -> None: ...

class vtkmImageConnectivity(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmImageConnectivity: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmImageConnectivity: ...

class vtkmLevelOfDetail(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    @overload
    def GetNumberOfDivisions(self) -> Pointer: ...
    @overload
    def GetNumberOfDivisions(self, div: MutableSequence[int]) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfXDivisions(self) -> int: ...
    def GetNumberOfYDivisions(self) -> int: ...
    def GetNumberOfZDivisions(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmLevelOfDetail: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmLevelOfDetail: ...
    @overload
    def SetNumberOfDivisions(self, div: MutableSequence[int]) -> None: ...
    @overload
    def SetNumberOfDivisions(self, div0: int, div1: int, div2: int) -> None: ...
    def SetNumberOfXDivisions(self, num: int) -> None: ...
    def SetNumberOfYDivisions(self, num: int) -> None: ...
    def SetNumberOfZDivisions(self, num: int) -> None: ...

class vtkmNDHistogram(vtkmodules.vtkCommonExecutionModel.vtkArrayDataAlgorithm):
    def AddFieldAndBin(self, fieldName: str, numberOfBins: int) -> None: ...
    def GetBinDelta(self, fieldIndex: int) -> float: ...
    def GetFieldIndexFromFieldName(self, fieldName: str) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmNDHistogram: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmNDHistogram: ...

class vtkmPointElevation(vtkmodules.vtkFiltersCore.vtkElevationFilter):
    def ForceVTKmOff(self) -> None: ...
    def ForceVTKmOn(self) -> None: ...
    def GetForceVTKm(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmPointElevation: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmPointElevation: ...
    def SetForceVTKm(self, _arg: int) -> None: ...

class vtkmPointTransform(vtkmodules.vtkCommonExecutionModel.vtkPointSetAlgorithm):
    def FillInputPortInformation(self, port: int, info: vtkmodules.vtkCommonCore.vtkInformation) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTransform(self) -> vtkmodules.vtkCommonTransforms.vtkHomogeneousTransform: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmPointTransform: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmPointTransform: ...
    def SetTransform(self, tf: vtkmodules.vtkCommonTransforms.vtkHomogeneousTransform) -> None: ...

class vtkmPolyDataNormals(vtkmodules.vtkFiltersCore.vtkPolyDataNormals):
    def ForceVTKmOff(self) -> None: ...
    def ForceVTKmOn(self) -> None: ...
    def GetForceVTKm(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmPolyDataNormals: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmPolyDataNormals: ...
    def SetForceVTKm(self, _arg: int) -> None: ...

class vtkmProbe(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPassCellArrays(self) -> int: ...
    def GetPassFieldArrays(self) -> int: ...
    def GetPassPointArrays(self) -> int: ...
    def GetSource(self) -> vtkmodules.vtkCommonDataModel.vtkDataObject: ...
    def GetValidCellMaskArrayName(self) -> str: ...
    def GetValidPointMaskArrayName(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmProbe: ...
    def PassCellArraysOff(self) -> None: ...
    def PassCellArraysOn(self) -> None: ...
    def PassFieldArraysOff(self) -> None: ...
    def PassFieldArraysOn(self) -> None: ...
    def PassPointArraysOff(self) -> None: ...
    def PassPointArraysOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmProbe: ...
    def SetPassCellArrays(self, _arg: int) -> None: ...
    def SetPassFieldArrays(self, _arg: int) -> None: ...
    def SetPassPointArrays(self, _arg: int) -> None: ...
    def SetSourceConnection(self, algOutput: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetSourceData(self, source: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetValidCellMaskArrayName(self, _arg: str) -> None: ...
    def SetValidPointMaskArrayName(self, _arg: str) -> None: ...

class vtkmThreshold(vtkmodules.vtkFiltersCore.vtkThreshold):
    def ForceVTKmOff(self) -> None: ...
    def ForceVTKmOn(self) -> None: ...
    def GetForceVTKm(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmThreshold: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmThreshold: ...
    def SetForceVTKm(self, _arg: int) -> None: ...

class vtkmTriangleMeshPointNormals(vtkmodules.vtkFiltersCore.vtkTriangleMeshPointNormals):
    def ForceVTKmOff(self) -> None: ...
    def ForceVTKmOn(self) -> None: ...
    def GetForceVTKm(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmTriangleMeshPointNormals: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmTriangleMeshPointNormals: ...
    def SetForceVTKm(self, _arg: int) -> None: ...

class vtkmWarpScalar(vtkmodules.vtkFiltersGeneral.vtkWarpScalar):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmWarpScalar: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmWarpScalar: ...

class vtkmWarpVector(vtkmodules.vtkFiltersGeneral.vtkWarpVector):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkmWarpVector: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkmWarpVector: ...
