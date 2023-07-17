from typing import TypeVar

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel


class vtkTRUCHASReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    @staticmethod
    def CanReadFile(filename: str) -> int: ...
    def GetBlockArrayName(self, index: int) -> str: ...
    def GetBlockArrayStatus(self, gridname: str) -> int: ...
    def GetCellArrayName(self, index: int) -> str: ...
    def GetCellArrayStatus(self, name: str) -> int: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfBlockArrays(self) -> int: ...
    def GetNumberOfCellArrays(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfPointArrays(self) -> int: ...
    def GetPointArrayName(self, index: int) -> str: ...
    def GetPointArrayStatus(self, name: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTRUCHASReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTRUCHASReader: ...
    def SetBlockArrayStatus(self, gridname: str, status: int) -> None: ...
    def SetCellArrayStatus(self, name: str, status: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetPointArrayStatus(self, name: str, status: int) -> None: ...
