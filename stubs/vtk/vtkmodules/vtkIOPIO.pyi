from collections.abc import Callable
from typing import TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel

Template = TypeVar("Template")

MAX_CHILD: int
MAX_DIM: int
NZero0: int
NZero1: int
NZero2: int
Ncylin: int
Nd0: int
Nd1: int
Nd2: int
Nmesh0: int
Nmesh1: int
Nmesh2: int
Nnumdim: int
Nsphere: int
Ntime: int

class vtkPIOReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def DisableAllCellArrays(self) -> None: ...
    def EnableAllCellArrays(self) -> None: ...
    def GetActiveTimeDataArrayName(self) -> str: ...
    def GetCellArrayName(self, index: int) -> str: ...
    def GetCellArrayStatus(self, name: str) -> int: ...
    def GetCellDataArraySelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetCurrentTimeStep(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetFloat64(self) -> bool: ...
    def GetHyperTreeGrid(self) -> bool: ...
    def GetNumberOfCellArrays(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfTimeDataArrays(self) -> int: ...
    @overload
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet: ...
    @overload
    def GetOutput(self, index: int) -> vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet: ...
    def GetTimeDataArray(self, idx: int) -> str: ...
    def GetTimeDataStringArray(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetTracers(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPIOReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPIOReader: ...
    def SetActiveTimeDataArrayName(self, _arg: str) -> None: ...
    def SetCellArrayStatus(self, name: str, status: int) -> None: ...
    def SetCurrentTimeStep(self, _arg: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetFloat64(self, _arg: bool) -> None: ...
    def SetHyperTreeGrid(self, _arg: bool) -> None: ...
    def SetTracers(self, _arg: bool) -> None: ...
