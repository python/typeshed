from typing import Callable, MutableSequence, TypeVar, Union

import vtkmodules.vtkDomainsChemistry
import vtkmodules.vtkCommonCore
import vtkmodules.vtkRenderingOpenGL2
import vtkmodules.vtkRenderingCore

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")


class vtkOpenGLMoleculeMapper(vtkmodules.vtkDomainsChemistry.vtkMoleculeMapper):
    def GetFastAtomMapper(
        self) -> vtkmodules.vtkRenderingOpenGL2.vtkOpenGLSphereMapper: ...

    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOpenGLMoleculeMapper: ...

    def ProcessSelectorPixelBuffers(
        self,
        sel: vtkmodules.vtkRenderingCore.vtkHardwareSelector,
        pixeloffsets: MutableSequence[int],
        prop: vtkmodules.vtkRenderingCore.vtkProp,
    ) -> None: ...

    def ReleaseGraphicsResources(
        self, __a: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...

    def Render(self, __a: vtkmodules.vtkRenderingCore.vtkRenderer,
               __b: vtkmodules.vtkRenderingCore.vtkActor) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOpenGLMoleculeMapper: ...

    def SetMapScalars(self, map: bool) -> None: ...
