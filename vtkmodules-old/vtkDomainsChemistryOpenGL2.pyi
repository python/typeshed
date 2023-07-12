from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkDomainsChemistry

class vtkOpenGLMoleculeMapper(vtkmodules.vtkDomainsChemistry.vtkMoleculeMapper):
    def GetFastAtomMapper(self) -> 'vtkOpenGLSphereMapper': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkOpenGLMoleculeMapper': ...
    def ProcessSelectorPixelBuffers(self, sel:'vtkHardwareSelector', pixeloffsets:MutableSequence[int], prop:'vtkProp') -> None: ...
    def ReleaseGraphicsResources(self, __a:'vtkWindow') -> None: ...
    def Render(self, __a:'vtkRenderer', __b:'vtkActor') -> None: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkOpenGLMoleculeMapper': ...
    def SetMapScalars(self, map:bool) -> None: ...

