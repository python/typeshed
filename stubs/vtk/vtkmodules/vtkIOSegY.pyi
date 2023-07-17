from typing import TypeVar

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkSegYReader(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    class VTKSegYCoordinateModes(int): ...
    class VTKSegYVerticalCRS(int): ...
    VTK_SEGY_CDP: VTKSegYCoordinateModes
    VTK_SEGY_CUSTOM: VTKSegYCoordinateModes
    VTK_SEGY_SOURCE: VTKSegYCoordinateModes
    VTK_SEGY_VERTICAL_DEPTHS: VTKSegYVerticalCRS
    VTK_SEGY_VERTICAL_HEIGHTS: VTKSegYVerticalCRS
    def Force2DOff(self) -> None: ...
    def Force2DOn(self) -> None: ...
    def GetFileName(self) -> str: ...
    def GetForce2D(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetStructuredGrid(self) -> int: ...
    def GetVerticalCRS(self) -> int: ...
    def GetXCoordByte(self) -> int: ...
    def GetXYCoordMode(self) -> int: ...
    def GetXYCoordModeMaxValue(self) -> int: ...
    def GetXYCoordModeMinValue(self) -> int: ...
    def GetYCoordByte(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSegYReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSegYReader: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetForce2D(self, _arg: bool) -> None: ...
    def SetStructuredGrid(self, _arg: int) -> None: ...
    def SetVerticalCRS(self, _arg: int) -> None: ...
    def SetXCoordByte(self, _arg: int) -> None: ...
    def SetXYCoordMode(self, _arg: int) -> None: ...
    def SetXYCoordModeToCDP(self) -> None: ...
    def SetXYCoordModeToCustom(self) -> None: ...
    def SetXYCoordModeToSource(self) -> None: ...
    def SetYCoordByte(self, _arg: int) -> None: ...
    def StructuredGridOff(self) -> None: ...
    def StructuredGridOn(self) -> None: ...
