from collections.abc import Sequence
from typing import overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkIOCore

class vtkCesium3DTilesWriter(vtkmodules.vtkIOCore.vtkWriter):
    class InputType(int): ...
    Buildings: InputType
    Mesh: InputType
    Points: InputType
    def ContentGLTFOff(self) -> None: ...
    def ContentGLTFOn(self) -> None: ...
    def GetCRS(self) -> str: ...
    def GetContentGLTF(self) -> bool: ...
    def GetDirectoryName(self) -> str: ...
    def GetInputType(self) -> int: ...
    def GetMergeTilePolyData(self) -> bool: ...
    def GetNumberOfFeaturesPerTile(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOffset(self) -> tuple[float, float, float]: ...
    def GetSaveTextures(self) -> bool: ...
    def GetSaveTiles(self) -> bool: ...
    def GetTextureBaseDirectory(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MergeTilePolyDataOff(self) -> None: ...
    def MergeTilePolyDataOn(self) -> None: ...
    def NewInstance(self) -> vtkCesium3DTilesWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCesium3DTilesWriter: ...
    def SaveTexturesOff(self) -> None: ...
    def SaveTexturesOn(self) -> None: ...
    def SaveTilesOff(self) -> None: ...
    def SaveTilesOn(self) -> None: ...
    def SetCRS(self, _arg: str) -> None: ...
    def SetContentGLTF(self, _arg: bool) -> None: ...
    def SetDirectoryName(self, _arg: str) -> None: ...
    def SetInputType(self, _arg: int) -> None: ...
    def SetMergeTilePolyData(self, _arg: bool) -> None: ...
    def SetNumberOfFeaturesPerTile(self, _arg: int) -> None: ...
    @overload
    def SetOffset(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetOffset(self, _arg: Sequence[float]) -> None: ...
    def SetSaveTextures(self, _arg: bool) -> None: ...
    def SetSaveTiles(self, _arg: bool) -> None: ...
    def SetTextureBaseDirectory(self, _arg: str) -> None: ...

class vtkCesiumPointCloudWriter(vtkmodules.vtkIOCore.vtkWriter):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPointIds(self) -> vtkmodules.vtkCommonCore.vtkIdList: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCesiumPointCloudWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCesiumPointCloudWriter: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetPointIds(self, _arg: vtkmodules.vtkCommonCore.vtkIdList) -> None: ...
