from collections.abc import Sequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkIOCore


class vtkMPASReader(vtkmodules.vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    @staticmethod
    def CanReadFile(filename: str) -> int: ...
    def DisableAllCellArrays(self) -> None: ...
    def DisableAllPointArrays(self) -> None: ...
    def EnableAllCellArrays(self) -> None: ...
    def EnableAllPointArrays(self) -> None: ...
    def GetAllDimensions(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetCellArrayName(self, index: int) -> str: ...
    def GetCellArrayStatus(self, name: str) -> int: ...
    def GetCenterLonRange(self) -> Tuple[int, int]: ...
    def GetDimensionCurrentIndex(self, dim: str) -> int: ...
    def GetDimensionName(self, idx: int) -> str: ...
    def GetDimensionSize(self, dim: str) -> int: ...
    def GetFileName(self) -> str: ...
    def GetIsAtmosphere(self) -> bool: ...
    def GetIsZeroCentered(self) -> bool: ...
    def GetLayerThickness(self) -> int: ...
    def GetLayerThicknessRange(self) -> Tuple[int, int]: ...
    def GetMTime(self) -> int: ...
    def GetMaximumCells(self) -> int: ...
    def GetMaximumPoints(self) -> int: ...
    def GetNumberOfCellArrays(self) -> int: ...
    def GetNumberOfCellVars(self) -> int: ...
    def GetNumberOfDimensions(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfPointArrays(self) -> int: ...
    def GetNumberOfPointVars(self) -> int: ...
    @overload
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkUnstructuredGrid: ...
    @overload
    def GetOutput(self, idx: int) -> vtkmodules.vtkCommonDataModel.vtkUnstructuredGrid: ...
    def GetPointArrayName(self, index: int) -> str: ...
    def GetPointArrayStatus(self, name: str) -> int: ...
    def GetProjectLatLon(self) -> bool: ...
    def GetShowMultilayerView(self) -> bool: ...
    def GetUseDimensionedArrayNames(self) -> bool: ...
    def GetVerticalDimension(self) -> str: ...
    def GetVerticalLevel(self) -> int: ...
    def GetVerticalLevelRange(self) -> Tuple[int, int]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMPASReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMPASReader: ...
    def SetCellArrayStatus(self, name: str, status: int) -> None: ...
    def SetCenterLon(self, val: int) -> None: ...
    def SetDimensionCurrentIndex(self, dim: str, idx: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetIsAtmosphere(self, _arg: bool) -> None: ...
    def SetIsZeroCentered(self, _arg: bool) -> None: ...
    def SetLayerThickness(self, _arg: int) -> None: ...
    def SetPointArrayStatus(self, name: str, status: int) -> None: ...
    def SetProjectLatLon(self, _arg: bool) -> None: ...
    def SetShowMultilayerView(self, _arg: bool) -> None: ...
    def SetUseDimensionedArrayNames(self, _arg: bool) -> None: ...
    def SetVerticalDimension(self, _arg: str) -> None: ...
    def SetVerticalLevel(self, level: int) -> None: ...
    def UseDimensionedArrayNamesOff(self) -> None: ...
    def UseDimensionedArrayNamesOn(self) -> None: ...

class vtkNetCDFCAMReader(vtkmodules.vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    class VerticalDimension(int): ...
    VERTICAL_DIMENSION_COUNT: VerticalDimension
    VERTICAL_DIMENSION_INTERFACE_LAYERS: VerticalDimension
    VERTICAL_DIMENSION_MIDPOINT_LAYERS: VerticalDimension
    VERTICAL_DIMENSION_SINGLE_LAYER: VerticalDimension
    @staticmethod
    def CanReadFile(fileName: str) -> int: ...
    def DisableAllPointArrays(self) -> None: ...
    def EnableAllPointArrays(self) -> None: ...
    def GetConnectivityFileName(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetInterfaceLayerIndex(self) -> int: ...
    def GetInterfaceLayersRange(self) -> Tuple[int, int]: ...
    def GetMidpointLayerIndex(self) -> int: ...
    def GetMidpointLayersRange(self) -> Tuple[int, int]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfPointArrays(self) -> int: ...
    def GetPointArrayName(self, index: int) -> str: ...
    def GetPointArrayStatus(self, name: str) -> int: ...
    def GetSingleInterfaceLayer(self) -> int: ...
    def GetSingleMidpointLayer(self) -> int: ...
    def GetVerticalDimension(self) -> int: ...
    def GetVerticalDimensionMaxValue(self) -> int: ...
    def GetVerticalDimensionMinValue(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkNetCDFCAMReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkNetCDFCAMReader: ...
    def SetConnectivityFileName(self, fileName: str) -> None: ...
    def SetFileName(self, fileName: str) -> None: ...
    def SetInterfaceLayerIndex(self, _arg: int) -> None: ...
    def SetMidpointLayerIndex(self, _arg: int) -> None: ...
    def SetPointArrayStatus(self, name: str, status: int) -> None: ...
    def SetSingleInterfaceLayer(self, _arg: int) -> None: ...
    def SetSingleMidpointLayer(self, _arg: int) -> None: ...
    def SetVerticalDimension(self, _arg: int) -> None: ...
    def SingleInterfaceLayerOff(self) -> None: ...
    def SingleInterfaceLayerOn(self) -> None: ...
    def SingleMidpointLayerOff(self) -> None: ...
    def SingleMidpointLayerOn(self) -> None: ...

class vtkNetCDFReader(vtkmodules.vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    def ComputeArraySelection(self) -> bool: ...
    def GetAllDimensions(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetAllVariableArrayNames(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetCalendar(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfVariableArrays(self) -> int: ...
    def GetReplaceFillValueWithNan(self) -> int: ...
    def GetTimeUnits(self) -> str: ...
    def GetVariableArrayName(self, index: int) -> str: ...
    def GetVariableArrayStatus(self, name: str) -> int: ...
    def GetVariableDimensions(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkNetCDFReader: ...
    def QueryArrayUnits(self, ArrayName: str) -> str: ...
    def ReplaceFillValueWithNanOff(self) -> None: ...
    def ReplaceFillValueWithNanOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkNetCDFReader: ...
    def SetDimensions(self, dimensions: str) -> None: ...
    def SetFileName(self, filename: str) -> None: ...
    def SetReplaceFillValueWithNan(self, _arg: int) -> None: ...
    def SetVariableArrayStatus(self, name: str, status: int) -> None: ...
    def UpdateMetaData(self) -> int: ...

class vtkNetCDFCFReader(vtkNetCDFReader):
    @staticmethod
    def CanReadFile(filename: str) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputType(self) -> int: ...
    def GetSphericalCoordinates(self) -> int: ...
    def GetVerticalBias(self) -> float: ...
    def GetVerticalScale(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkNetCDFCFReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkNetCDFCFReader: ...
    def SetOutputType(self, type: int) -> None: ...
    def SetOutputTypeToAutomatic(self) -> None: ...
    def SetOutputTypeToImage(self) -> None: ...
    def SetOutputTypeToRectilinear(self) -> None: ...
    def SetOutputTypeToStructured(self) -> None: ...
    def SetOutputTypeToUnstructured(self) -> None: ...
    def SetSphericalCoordinates(self, _arg: int) -> None: ...
    def SetVerticalBias(self, _arg: float) -> None: ...
    def SetVerticalScale(self, _arg: float) -> None: ...
    def SphericalCoordinatesOff(self) -> None: ...
    def SphericalCoordinatesOn(self) -> None: ...

class vtkNetCDFCFWriter(vtkmodules.vtkIOCore.vtkWriter):
    @overload
    def AddGridMappingAttribute(self, name: str, value: str) -> None: ...
    @overload
    def AddGridMappingAttribute(self, name: str, value: float) -> None: ...
    def ClearGridMappingAttributes(self) -> None: ...
    def FillBlankedAttributesOff(self) -> None: ...
    def FillBlankedAttributesOn(self) -> None: ...
    def GetAttributeType(self) -> int: ...
    def GetCellArrayNamePostfix(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetFillBlankedAttributes(self) -> bool: ...
    def GetFillValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkNetCDFCFWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkNetCDFCFWriter: ...
    def SetAttributeType(self, _arg: int) -> None: ...
    def SetCellArrayNamePostfix(self, _arg: str) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetFillBlankedAttributes(self, _arg: bool) -> None: ...
    def SetFillValue(self, _arg: int) -> None: ...

class vtkNetCDFPOPReader(vtkmodules.vtkCommonExecutionModel.vtkRectilinearGridAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfVariableArrays(self) -> int: ...
    def GetStride(self) -> Tuple[int, int, int]: ...
    def GetVariableArrayName(self, index: int) -> str: ...
    def GetVariableArrayStatus(self, name: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkNetCDFPOPReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkNetCDFPOPReader: ...
    def SetFileName(self, _arg: str) -> None: ...
    @overload
    def SetStride(self, _arg1: int, _arg2: int, _arg3: int) -> None: ...
    @overload
    def SetStride(self, _arg: Sequence[int]) -> None: ...
    def SetVariableArrayStatus(self, name: str, status: int) -> None: ...

class vtkSLACParticleReader(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    @staticmethod
    def CanReadFile(filename: str) -> int: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSLACParticleReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSLACParticleReader: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkSLACReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    NUM_OUTPUTS: int
    SURFACE_OUTPUT: int
    VOLUME_OUTPUT: int
    def AddModeFileName(self, fname: str) -> None: ...
    @staticmethod
    def CanReadFile(filename: str) -> int: ...
    def GetFrequencyScales(self) -> vtkmodules.vtkCommonCore.vtkDoubleArray: ...
    def GetMeshFileName(self) -> str: ...
    def GetModeFileName(self, idx: int) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfModeFileNames(self) -> int: ...
    def GetNumberOfVariableArrays(self) -> int: ...
    def GetPhaseShifts(self) -> vtkmodules.vtkCommonCore.vtkDoubleArray: ...
    def GetReadExternalSurface(self) -> int: ...
    def GetReadInternalVolume(self) -> int: ...
    def GetReadMidpoints(self) -> int: ...
    def GetVariableArrayName(self, index: int) -> str: ...
    def GetVariableArrayStatus(self, name: str) -> int: ...
    @staticmethod
    def IS_EXTERNAL_SURFACE() -> vtkmodules.vtkCommonCore.vtkInformationIntegerKey: ...
    @staticmethod
    def IS_INTERNAL_VOLUME() -> vtkmodules.vtkCommonCore.vtkInformationIntegerKey: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSLACReader: ...
    @staticmethod
    def POINTS() -> vtkmodules.vtkCommonCore.vtkInformationObjectBaseKey: ...
    @staticmethod
    def POINT_DATA() -> vtkmodules.vtkCommonCore.vtkInformationObjectBaseKey: ...
    def ReadExternalSurfaceOff(self) -> None: ...
    def ReadExternalSurfaceOn(self) -> None: ...
    def ReadInternalVolumeOff(self) -> None: ...
    def ReadInternalVolumeOn(self) -> None: ...
    def ReadMidpointsOff(self) -> None: ...
    def ReadMidpointsOn(self) -> None: ...
    def RemoveAllModeFileNames(self) -> None: ...
    def ResetFrequencyScales(self) -> None: ...
    def ResetPhaseShifts(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSLACReader: ...
    def SetFrequencyScale(self, index: int, scale: float) -> None: ...
    def SetMeshFileName(self, _arg: str) -> None: ...
    def SetPhaseShift(self, index: int, shift: float) -> None: ...
    def SetReadExternalSurface(self, _arg: int) -> None: ...
    def SetReadInternalVolume(self, _arg: int) -> None: ...
    def SetReadMidpoints(self, _arg: int) -> None: ...
    def SetVariableArrayStatus(self, name: str, status: int) -> None: ...
