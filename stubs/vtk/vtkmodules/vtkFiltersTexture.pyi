from typing import Callable, MutableSequence, Sequence, Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkImplicitTextureCoords(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def FlipTextureOff(self) -> None: ...
    def FlipTextureOn(self) -> None: ...
    def GetFlipTexture(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRFunction(self) -> vtkmodules.vtkCommonDataModel.vtkImplicitFunction: ...
    def GetSFunction(self) -> vtkmodules.vtkCommonDataModel.vtkImplicitFunction: ...
    def GetTFunction(self) -> vtkmodules.vtkCommonDataModel.vtkImplicitFunction: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImplicitTextureCoords: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImplicitTextureCoords: ...
    def SetFlipTexture(self, _arg: int) -> None: ...
    def SetRFunction(self, __a: vtkmodules.vtkCommonDataModel.vtkImplicitFunction) -> None: ...
    def SetSFunction(self, __a: vtkmodules.vtkCommonDataModel.vtkImplicitFunction) -> None: ...
    def SetTFunction(self, __a: vtkmodules.vtkCommonDataModel.vtkImplicitFunction) -> None: ...

class vtkScalarsToTextureFilter(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTextureDimensions(self) -> Tuple[int, int]: ...
    def GetTransferFunction(self) -> vtkmodules.vtkCommonCore.vtkScalarsToColors: ...
    def GetUseTransferFunction(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkScalarsToTextureFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkScalarsToTextureFilter: ...
    @overload
    def SetTextureDimensions(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetTextureDimensions(self, _arg: Sequence[int]) -> None: ...
    def SetTransferFunction(self, stc: vtkmodules.vtkCommonCore.vtkScalarsToColors) -> None: ...
    def SetUseTransferFunction(self, _arg: bool) -> None: ...
    def UseTransferFunctionOff(self) -> None: ...
    def UseTransferFunctionOn(self) -> None: ...

class vtkTextureMapToCylinder(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def AutomaticCylinderGenerationOff(self) -> None: ...
    def AutomaticCylinderGenerationOn(self) -> None: ...
    def GetAutomaticCylinderGeneration(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPoint1(self) -> Tuple[float, float, float]: ...
    def GetPoint2(self) -> Tuple[float, float, float]: ...
    def GetPreventSeam(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTextureMapToCylinder: ...
    def PreventSeamOff(self) -> None: ...
    def PreventSeamOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTextureMapToCylinder: ...
    def SetAutomaticCylinderGeneration(self, _arg: int) -> None: ...
    @overload
    def SetPoint1(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetPoint1(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetPoint2(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetPoint2(self, _arg: Sequence[float]) -> None: ...
    def SetPreventSeam(self, _arg: int) -> None: ...

class vtkTextureMapToPlane(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def AutomaticPlaneGenerationOff(self) -> None: ...
    def AutomaticPlaneGenerationOn(self) -> None: ...
    def GetAutomaticPlaneGeneration(self) -> int: ...
    def GetNormal(self) -> Tuple[float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOrigin(self) -> Tuple[float, float, float]: ...
    def GetPoint1(self) -> Tuple[float, float, float]: ...
    def GetPoint2(self) -> Tuple[float, float, float]: ...
    def GetSRange(self) -> Tuple[float, float]: ...
    def GetTRange(self) -> Tuple[float, float]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTextureMapToPlane: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTextureMapToPlane: ...
    def SetAutomaticPlaneGeneration(self, _arg: int) -> None: ...
    @overload
    def SetNormal(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetNormal(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetOrigin(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetOrigin(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetPoint1(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetPoint1(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetPoint2(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetPoint2(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetSRange(self, _arg1: float, _arg2: float) -> None: ...
    @overload
    def SetSRange(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetTRange(self, _arg1: float, _arg2: float) -> None: ...
    @overload
    def SetTRange(self, _arg: Sequence[float]) -> None: ...

class vtkTextureMapToSphere(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def AutomaticSphereGenerationOff(self) -> None: ...
    def AutomaticSphereGenerationOn(self) -> None: ...
    def ComputeCenter(self, input: vtkmodules.vtkCommonDataModel.vtkDataSet) -> None: ...
    def GetAutomaticSphereGeneration(self) -> int: ...
    def GetCenter(self) -> Tuple[float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPreventSeam(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTextureMapToSphere: ...
    def PreventSeamOff(self) -> None: ...
    def PreventSeamOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTextureMapToSphere: ...
    def SetAutomaticSphereGeneration(self, _arg: int) -> None: ...
    @overload
    def SetCenter(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetCenter(self, _arg: Sequence[float]) -> None: ...
    def SetPreventSeam(self, _arg: int) -> None: ...

class vtkThresholdTextureCoords(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def GetInTextureCoord(self) -> Tuple[float, float, float]: ...
    def GetLowerThreshold(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutTextureCoord(self) -> Tuple[float, float, float]: ...
    def GetTextureDimension(self) -> int: ...
    def GetTextureDimensionMaxValue(self) -> int: ...
    def GetTextureDimensionMinValue(self) -> int: ...
    def GetUpperThreshold(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkThresholdTextureCoords: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkThresholdTextureCoords: ...
    @overload
    def SetInTextureCoord(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetInTextureCoord(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetOutTextureCoord(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetOutTextureCoord(self, _arg: Sequence[float]) -> None: ...
    def SetTextureDimension(self, _arg: int) -> None: ...
    def ThresholdBetween(self, lower: float, upper: float) -> None: ...
    def ThresholdByLower(self, lower: float) -> None: ...
    def ThresholdByUpper(self, upper: float) -> None: ...

class vtkTransformTextureCoords(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    @overload
    def AddPosition(self, deltaR: float, deltaS: float, deltaT: float) -> None: ...
    @overload
    def AddPosition(self, deltaPosition: MutableSequence[float]) -> None: ...
    def FlipROff(self) -> None: ...
    def FlipROn(self) -> None: ...
    def FlipSOff(self) -> None: ...
    def FlipSOn(self) -> None: ...
    def FlipTOff(self) -> None: ...
    def FlipTOn(self) -> None: ...
    def GetFlipR(self) -> int: ...
    def GetFlipS(self) -> int: ...
    def GetFlipT(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOrigin(self) -> Tuple[float, float, float]: ...
    def GetPosition(self) -> Tuple[float, float, float]: ...
    def GetScale(self) -> Tuple[float, float, float]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTransformTextureCoords: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTransformTextureCoords: ...
    def SetFlipR(self, _arg: int) -> None: ...
    def SetFlipS(self, _arg: int) -> None: ...
    def SetFlipT(self, _arg: int) -> None: ...
    @overload
    def SetOrigin(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetOrigin(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetPosition(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetPosition(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetScale(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetScale(self, _arg: Sequence[float]) -> None: ...

class vtkTriangularTCoords(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTriangularTCoords: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTriangularTCoords: ...
