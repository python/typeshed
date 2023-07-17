from collections.abc import Callable
from typing import TypeVar, Union

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

Template = TypeVar("Template")

class vtkCONVERGECFDReader(vtkmodules.vtkCommonExecutionModel.vtkPartitionedDataSetCollectionAlgorithm):
    def CanReadFile(self, fname: str) -> int: ...
    def GetCellDataArraySelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetParcelDataArraySelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCONVERGECFDReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCONVERGECFDReader: ...
    def SetFileName(self, _arg: str) -> None: ...
