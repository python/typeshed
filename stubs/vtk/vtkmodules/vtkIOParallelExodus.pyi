from collections.abc import MutableSequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkIOExodus
import vtkmodules.vtkParallelCore

Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkPExodusIIReader(vtkmodules.vtkIOExodus.vtkExodusIIReader):
    def Broadcast(self, ctrl: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetFilePattern(self) -> str: ...
    def GetFilePrefix(self) -> str: ...
    def GetFileRange(self) -> Tuple[int, int]: ...
    def GetNumberOfFileNames(self) -> int: ...
    def GetNumberOfFiles(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTotalNumberOfElements(self) -> int: ...
    def GetTotalNumberOfNodes(self) -> int: ...
    def GetVariableCacheSize(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPExodusIIReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPExodusIIReader: ...
    def SetController(self, c: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def SetFileName(self, name: str) -> None: ...
    def SetFilePattern(self, _arg: str) -> None: ...
    def SetFilePrefix(self, _arg: str) -> None: ...
    @overload
    def SetFileRange(self, __a: int, __b: int) -> None: ...
    @overload
    def SetFileRange(self, r: MutableSequence[int]) -> None: ...
    def SetVariableCacheSize(self, _arg: float) -> None: ...

class vtkPExodusIIWriter(vtkmodules.vtkIOExodus.vtkExodusIIWriter):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPExodusIIWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPExodusIIWriter: ...
