from collections.abc import Callable, Sequence
from typing import Callable, TypeVar, Union, overload

import vtkmodules.vtkCommonCore

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkViewNode(vtkmodules.vtkCommonCore.vtkObject):
    class operation_type(int): ...
    build: operation_type
    invalidate: operation_type
    noop: operation_type
    render: operation_type
    synchronize: operation_type
    def Build(self, __a: bool) -> None: ...
    def GetFirstAncestorOfType(self, type: str) -> vtkViewNode: ...
    def GetFirstChildOfType(self, type: str) -> vtkViewNode: ...
    def GetMyFactory(self) -> vtkViewNodeFactory: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetParent(self) -> vtkViewNode: ...
    def GetRenderable(self) -> vtkmodules.vtkCommonCore.vtkObject: ...
    def GetViewNodeFor(self, __a: vtkmodules.vtkCommonCore.vtkObject) -> vtkViewNode: ...
    def Invalidate(self, __a: bool) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkViewNode: ...
    def Render(self, __a: bool) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkViewNode: ...
    def SetMyFactory(self, __a: vtkViewNodeFactory) -> None: ...
    def SetParent(self, __a: vtkViewNode) -> None: ...
    def SetRenderable(self, __a: vtkmodules.vtkCommonCore.vtkObject) -> None: ...
    def Synchronize(self, __a: bool) -> None: ...
    def Traverse(self, operation: int) -> None: ...
    def TraverseAllPasses(self) -> None: ...

class vtkActorNode(vtkViewNode):
    def Build(self, prepass: bool) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkActorNode: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkActorNode: ...

class vtkCameraNode(vtkViewNode):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCameraNode: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCameraNode: ...

class vtkLightNode(vtkViewNode):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLightNode: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLightNode: ...

class vtkMapperNode(vtkViewNode):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMapperNode: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMapperNode: ...

class vtkPolyDataMapperNode(vtkMapperNode):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPolyDataMapperNode: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPolyDataMapperNode: ...

class vtkRendererNode(vtkViewNode):
    def Build(self, prepass: bool) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetScale(self) -> Tuple[int, int]: ...
    def GetSize(self) -> Tuple[int, int]: ...
    def GetViewport(self) -> Tuple[float, float, float, float]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkRendererNode: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkRendererNode: ...
    @overload
    def SetScale(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetScale(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetSize(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetSize(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetViewport(self, _arg1: float, _arg2: float, _arg3: float, _arg4: float) -> None: ...
    @overload
    def SetViewport(self, _arg: Sequence[float]) -> None: ...

class vtkViewNodeFactory(vtkmodules.vtkCommonCore.vtkObject):
    def CreateNode(self, __a: vtkmodules.vtkCommonCore.vtkObject) -> vtkViewNode: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkViewNodeFactory: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkViewNodeFactory: ...

class vtkVolumeMapperNode(vtkMapperNode):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkVolumeMapperNode: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkVolumeMapperNode: ...

class vtkVolumeNode(vtkViewNode):
    def Build(self, prepass: bool) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkVolumeNode: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkVolumeNode: ...

class vtkWindowNode(vtkViewNode):
    def Build(self, prepass: bool) -> None: ...
    def GetColorBuffer(self) -> vtkmodules.vtkCommonCore.vtkUnsignedCharArray: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSize(self) -> Pointer: ...
    def GetZBuffer(self) -> vtkmodules.vtkCommonCore.vtkFloatArray: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWindowNode: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWindowNode: ...
    def Synchronize(self, prepass: bool) -> None: ...
