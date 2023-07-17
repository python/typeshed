from collections.abc import MutableSequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkRenderingCore


class vtkHyperTreeGridMapper(vtkmodules.vtkRenderingCore.vtkMapper):
    def FillInputPortInformation(self, port: int, info: vtkmodules.vtkCommonCore.vtkInformation) -> int: ...
    @overload
    def GetBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    @overload
    def GetBounds(self, bounds: MutableSequence[float]) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetUseAdaptiveDecimation(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHyperTreeGridMapper: ...
    def Render(self, ren: vtkmodules.vtkRenderingCore.vtkRenderer, act: vtkmodules.vtkRenderingCore.vtkActor) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHyperTreeGridMapper: ...
    @overload
    def SetInputConnection(self, port: int, input: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    @overload
    def SetInputConnection(self, input: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    @overload
    def SetInputDataObject(self, port: int, input: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    @overload
    def SetInputDataObject(self, input: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetUseAdaptiveDecimation(self, _arg: bool) -> None: ...
    def UseAdaptiveDecimationOff(self) -> None: ...
    def UseAdaptiveDecimationOn(self) -> None: ...
