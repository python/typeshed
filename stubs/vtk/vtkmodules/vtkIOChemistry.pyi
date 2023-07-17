from collections.abc import Callable
from typing import TypeVar, Union

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkCommonTransforms

Template = TypeVar("Template")

class vtkCMLMoleculeReader(vtkmodules.vtkCommonExecutionModel.vtkMoleculeAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkMolecule: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCMLMoleculeReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCMLMoleculeReader: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetOutput(self, __a: vtkmodules.vtkCommonDataModel.vtkMolecule) -> None: ...

class vtkMoleculeReaderBase(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def GetBScale(self) -> float: ...
    def GetFileName(self) -> str: ...
    def GetHBScale(self) -> float: ...
    def GetNumberOfAtoms(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfModels(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMoleculeReaderBase: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMoleculeReaderBase: ...
    def SetBScale(self, _arg: float) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetHBScale(self, _arg: float) -> None: ...

class vtkGaussianCubeReader(vtkMoleculeReaderBase):
    def GetGridOutput(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTransform(self) -> vtkmodules.vtkCommonTransforms.vtkTransform: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGaussianCubeReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGaussianCubeReader: ...

class vtkGaussianCubeReader2(vtkmodules.vtkCommonExecutionModel.vtkMoleculeAlgorithm):
    def GetFileName(self) -> str: ...
    def GetGridOutput(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkMolecule: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGaussianCubeReader2: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGaussianCubeReader2: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetOutput(self, __a: vtkmodules.vtkCommonDataModel.vtkMolecule) -> None: ...

class vtkPDBReader(vtkMoleculeReaderBase):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPDBReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPDBReader: ...

class vtkVASPAnimationReader(vtkmodules.vtkCommonExecutionModel.vtkMoleculeAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkVASPAnimationReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkVASPAnimationReader: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkVASPTessellationReader(vtkmodules.vtkCommonExecutionModel.vtkMoleculeAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkVASPTessellationReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkVASPTessellationReader: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkXYZMolReader(vtkMoleculeReaderBase):
    def CanReadFile(self, name: str) -> int: ...
    def GetMaxTimeStep(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTimeStep(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkXYZMolReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkXYZMolReader: ...
    def SetTimeStep(self, _arg: int) -> None: ...

class vtkXYZMolReader2(vtkmodules.vtkCommonExecutionModel.vtkMoleculeAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkMolecule: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkXYZMolReader2: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkXYZMolReader2: ...
    def SetFileName(self, arg: str) -> None: ...
    def SetOutput(self, __a: vtkmodules.vtkCommonDataModel.vtkMolecule) -> None: ...
