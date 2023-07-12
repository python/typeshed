import vtkmodules.vtkRenderingContext2D
import vtkmodules.vtkCommonCore
from typing import Callable, TypeVar, Union

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")


class vtkPythonItem(vtkmodules.vtkRenderingContext2D.vtkContextItem):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPythonItem: ...

    def Paint(
        self, painter: vtkmodules.vtkRenderingContext2D.vtkContext2D) -> bool: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPythonItem: ...

    def SetPythonObject(self, obj: "PyObject") -> None: ...
