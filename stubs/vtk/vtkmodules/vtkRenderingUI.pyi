from typing import Callable, MutableSequence, TypeVar, Union

import vtkmodules.vtkCommonCore
import vtkmodules.vtkRenderingCore

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkGenericRenderWindowInteractor(vtkmodules.vtkRenderingCore.vtkRenderWindowInteractor):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTimerEventResetsTimer(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGenericRenderWindowInteractor: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGenericRenderWindowInteractor: ...
    def SetTimerEventResetsTimer(self, _arg: int) -> None: ...
    def TimerEvent(self) -> None: ...
    def TimerEventResetsTimerOff(self) -> None: ...
    def TimerEventResetsTimerOn(self) -> None: ...

class vtkXRenderWindowInteractor(vtkmodules.vtkRenderingCore.vtkRenderWindowInteractor):
    def Disable(self) -> None: ...
    def Enable(self) -> None: ...
    def GetMousePosition(self, x: MutableSequence[int], y: MutableSequence[int]) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def Initialize(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkXRenderWindowInteractor: ...
    def ProcessEvents(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkXRenderWindowInteractor: ...
    def TerminateApp(self) -> None: ...
    def UpdateSize(self, __a: int, __b: int) -> None: ...
