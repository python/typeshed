from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

class vtkCMLMoleculeReader(vtkmodules.vtkCommonExecutionModel.vtkMoleculeAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetOutput(self) -> 'vtkMolecule': ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkCMLMoleculeReader': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkCMLMoleculeReader': ...
    def SetFileName(self, _arg:str) -> None: ...
    def SetOutput(self, __a:'vtkMolecule') -> None: ...

class vtkMoleculeReaderBase(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def GetBScale(self) -> float: ...
    def GetFileName(self) -> str: ...
    def GetHBScale(self) -> float: ...
    def GetNumberOfAtoms(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfModels(self) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkMoleculeReaderBase': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkMoleculeReaderBase': ...
    def SetBScale(self, _arg:float) -> None: ...
    def SetFileName(self, _arg:str) -> None: ...
    def SetHBScale(self, _arg:float) -> None: ...

class vtkGaussianCubeReader(vtkMoleculeReaderBase):
    def GetGridOutput(self) -> 'vtkImageData': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetTransform(self) -> 'vtkTransform': ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkGaussianCubeReader': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkGaussianCubeReader': ...

class vtkGaussianCubeReader2(vtkmodules.vtkCommonExecutionModel.vtkMoleculeAlgorithm):
    def GetFileName(self) -> str: ...
    def GetGridOutput(self) -> 'vtkImageData': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetOutput(self) -> 'vtkMolecule': ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkGaussianCubeReader2': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkGaussianCubeReader2': ...
    def SetFileName(self, _arg:str) -> None: ...
    def SetOutput(self, __a:'vtkMolecule') -> None: ...

class vtkPDBReader(vtkMoleculeReaderBase):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkPDBReader': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPDBReader': ...

class vtkVASPAnimationReader(vtkmodules.vtkCommonExecutionModel.vtkMoleculeAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkVASPAnimationReader': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkVASPAnimationReader': ...
    def SetFileName(self, _arg:str) -> None: ...

class vtkVASPTessellationReader(vtkmodules.vtkCommonExecutionModel.vtkMoleculeAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkVASPTessellationReader': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkVASPTessellationReader': ...
    def SetFileName(self, _arg:str) -> None: ...

class vtkXYZMolReader(vtkMoleculeReaderBase):
    def CanReadFile(self, name:str) -> int: ...
    def GetMaxTimeStep(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetTimeStep(self) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXYZMolReader': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXYZMolReader': ...
    def SetTimeStep(self, _arg:int) -> None: ...

class vtkXYZMolReader2(vtkmodules.vtkCommonExecutionModel.vtkMoleculeAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetOutput(self) -> 'vtkMolecule': ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXYZMolReader2': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXYZMolReader2': ...
    def SetFileName(self, arg:str) -> None: ...
    def SetOutput(self, __a:'vtkMolecule') -> None: ...

