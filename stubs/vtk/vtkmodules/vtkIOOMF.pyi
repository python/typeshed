from typing import Callable, TypeVar, Union

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkOMFReader(vtkmodules.vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    def GetColumnMajorOrdering(self) -> bool: ...
    def GetDataElementArrayName(self, index: int) -> str: ...
    def GetDataElementArraySelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetDataElementArrayStatus(self, name: str) -> bool: ...
    def GetFileName(self) -> str: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfDataElementArrays(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetWriteOutTextures(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOMFReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOMFReader: ...
    def SetColumnMajorOrdering(self, _arg: bool) -> None: ...
    def SetDataElementArrayStatus(self, name: str, status: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetWriteOutTextures(self, _arg: bool) -> None: ...
