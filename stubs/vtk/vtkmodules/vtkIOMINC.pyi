from collections.abc import Callable, MutableSequence
from typing import Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkIOCore
import vtkmodules.vtkIOImage
import vtkmodules.vtkCommonMath
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkRenderingCore
import vtkmodules.vtkCommonTransforms

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkMINCImageAttributes(vtkmodules.vtkCommonCore.vtkObject):
    @overload
    def AddDimension(self, dimension: str) -> None: ...
    @overload
    def AddDimension(self, dimension: str, length: int) -> None: ...
    def FindImageRange(self, range: MutableSequence[float]) -> None: ...
    def FindValidRange(self, range: MutableSequence[float]) -> None: ...
    def GetAttributeNames(self, variable: str) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetAttributeValueAsArray(self, variable: str, attribute: str) -> vtkmodules.vtkCommonCore.vtkDataArray: ...
    def GetAttributeValueAsDouble(self, variable: str, attribute: str) -> float: ...
    def GetAttributeValueAsInt(self, variable: str, attribute: str) -> int: ...
    def GetAttributeValueAsString(self, variable: str, attribute: str) -> str: ...
    def GetDataType(self) -> int: ...
    def GetDimensionLengths(self) -> vtkmodules.vtkCommonCore.vtkIdTypeArray: ...
    def GetDimensionNames(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetImageMax(self) -> vtkmodules.vtkCommonCore.vtkDoubleArray: ...
    def GetImageMin(self) -> vtkmodules.vtkCommonCore.vtkDoubleArray: ...
    def GetName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfImageMinMaxDimensions(self) -> int: ...
    def GetValidateAttributes(self) -> int: ...
    def GetVariableNames(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def HasAttribute(self, variable: str, attribute: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMINCImageAttributes: ...
    def PrintFileHeader(self) -> None: ...
    def Reset(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMINCImageAttributes: ...
    def SetAttributeValueAsArray(self, variable: str, attribute: str, array: vtkmodules.vtkCommonCore.vtkDataArray) -> None: ...
    def SetAttributeValueAsDouble(self, variable: str, attribute: str, value: float) -> None: ...
    def SetAttributeValueAsInt(self, variable: str, attribute: str, value: int) -> None: ...
    def SetAttributeValueAsString(self, variable: str, attribute: str, value: str) -> None: ...
    def SetDataType(self, _arg: int) -> None: ...
    def SetImageMax(self, imageMax: vtkmodules.vtkCommonCore.vtkDoubleArray) -> None: ...
    def SetImageMin(self, imageMin: vtkmodules.vtkCommonCore.vtkDoubleArray) -> None: ...
    def SetName(self, _arg: str) -> None: ...
    def SetNumberOfImageMinMaxDimensions(self, _arg: int) -> None: ...
    def SetValidateAttributes(self, _arg: int) -> None: ...
    def ShallowCopy(self, source: vtkMINCImageAttributes) -> None: ...
    def ValidateAttribute(self, varname: str, attname: str, array: vtkmodules.vtkCommonCore.vtkDataArray) -> int: ...
    def ValidateAttributesOff(self) -> None: ...
    def ValidateAttributesOn(self) -> None: ...

class vtkMINCImageReader(vtkmodules.vtkIOImage.vtkImageReader2):
    def CanReadFile(self, name: str) -> int: ...
    @overload
    def GetDataRange(self) -> Tuple[float, float]: ...
    @overload
    def GetDataRange(self, range: MutableSequence[float]) -> None: ...
    def GetDescriptiveName(self) -> str: ...
    def GetDirectionCosines(self) -> vtkmodules.vtkCommonMath.vtkMatrix4x4: ...
    def GetFileExtensions(self) -> str: ...
    def GetImageAttributes(self) -> vtkMINCImageAttributes: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfTimeSteps(self) -> int: ...
    def GetRescaleIntercept(self) -> float: ...
    def GetRescaleRealValues(self) -> int: ...
    def GetRescaleSlope(self) -> float: ...
    def GetTimeStep(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMINCImageReader: ...
    def RescaleRealValuesOff(self) -> None: ...
    def RescaleRealValuesOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMINCImageReader: ...
    def SetFileName(self, name: str) -> None: ...
    def SetRescaleRealValues(self, _arg: int) -> None: ...
    def SetTimeStep(self, _arg: int) -> None: ...

class vtkMINCImageWriter(vtkmodules.vtkIOImage.vtkImageWriter):
    def GetDescriptiveName(self) -> str: ...
    def GetDirectionCosines(self) -> vtkmodules.vtkCommonMath.vtkMatrix4x4: ...
    def GetFileExtensions(self) -> str: ...
    def GetHistoryAddition(self) -> str: ...
    def GetImageAttributes(self) -> vtkMINCImageAttributes: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRescaleIntercept(self) -> float: ...
    def GetRescaleSlope(self) -> float: ...
    def GetStrictValidation(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMINCImageWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMINCImageWriter: ...
    def SetDirectionCosines(self, matrix: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...
    def SetFileName(self, name: str) -> None: ...
    def SetHistoryAddition(self, _arg: str) -> None: ...
    def SetImageAttributes(self, attributes: vtkMINCImageAttributes) -> None: ...
    def SetRescaleIntercept(self, _arg: float) -> None: ...
    def SetRescaleSlope(self, _arg: float) -> None: ...
    def SetStrictValidation(self, _arg: int) -> None: ...
    def StrictValidationOff(self) -> None: ...
    def StrictValidationOn(self) -> None: ...
    def Write(self) -> None: ...

class vtkMNIObjectReader(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def CanReadFile(self, name: str) -> int: ...
    def GetDescriptiveName(self) -> str: ...
    def GetFileExtensions(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetProperty(self) -> vtkmodules.vtkRenderingCore.vtkProperty: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMNIObjectReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMNIObjectReader: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkMNIObjectWriter(vtkmodules.vtkIOCore.vtkWriter):
    def GetDescriptiveName(self) -> str: ...
    def GetFileExtensions(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetFileType(self) -> int: ...
    def GetFileTypeMaxValue(self) -> int: ...
    def GetFileTypeMinValue(self) -> int: ...
    @overload
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    @overload
    def GetInput(self, port: int) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    def GetLookupTable(self) -> vtkmodules.vtkCommonCore.vtkLookupTable: ...
    def GetMapper(self) -> vtkmodules.vtkRenderingCore.vtkMapper: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetProperty(self) -> vtkmodules.vtkRenderingCore.vtkProperty: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMNIObjectWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMNIObjectWriter: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetFileType(self, _arg: int) -> None: ...
    def SetFileTypeToASCII(self) -> None: ...
    def SetFileTypeToBinary(self) -> None: ...
    def SetLookupTable(self, table: vtkmodules.vtkCommonCore.vtkLookupTable) -> None: ...
    def SetMapper(self, mapper: vtkmodules.vtkRenderingCore.vtkMapper) -> None: ...
    def SetProperty(self, property: vtkmodules.vtkRenderingCore.vtkProperty) -> None: ...

class vtkMNITagPointReader(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def CanReadFile(self, name: str) -> int: ...
    def GetComments(self) -> str: ...
    def GetDescriptiveName(self) -> str: ...
    def GetFileExtensions(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetLabelText(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfVolumes(self) -> int: ...
    def GetPatientIds(self) -> vtkmodules.vtkCommonCore.vtkIntArray: ...
    @overload
    def GetPoints(self, port: int) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    @overload
    def GetPoints(self) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    def GetStructureIds(self) -> vtkmodules.vtkCommonCore.vtkIntArray: ...
    def GetWeights(self) -> vtkmodules.vtkCommonCore.vtkDoubleArray: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMNITagPointReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMNITagPointReader: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkMNITagPointWriter(vtkmodules.vtkIOCore.vtkWriter):
    def GetComments(self) -> str: ...
    def GetDescriptiveName(self) -> str: ...
    def GetFileExtensions(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetLabelText(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPatientIds(self) -> vtkmodules.vtkCommonCore.vtkIntArray: ...
    @overload
    def GetPoints(self, port: int) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    @overload
    def GetPoints(self) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    def GetStructureIds(self) -> vtkmodules.vtkCommonCore.vtkIntArray: ...
    def GetWeights(self) -> vtkmodules.vtkCommonCore.vtkDoubleArray: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMNITagPointWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMNITagPointWriter: ...
    def SetComments(self, _arg: str) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetLabelText(self, a: vtkmodules.vtkCommonCore.vtkStringArray) -> None: ...
    def SetPatientIds(self, a: vtkmodules.vtkCommonCore.vtkIntArray) -> None: ...
    @overload
    def SetPoints(self, port: int, points: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...
    @overload
    def SetPoints(self, points: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...
    def SetStructureIds(self, a: vtkmodules.vtkCommonCore.vtkIntArray) -> None: ...
    def SetWeights(self, a: vtkmodules.vtkCommonCore.vtkDoubleArray) -> None: ...
    def Write(self) -> int: ...

class vtkMNITransformReader(vtkmodules.vtkCommonExecutionModel.vtkAlgorithm):
    def CanReadFile(self, name: str) -> int: ...
    def GetComments(self) -> str: ...
    def GetDescriptiveName(self) -> str: ...
    def GetFileExtensions(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetNthTransform(self, i: int) -> vtkmodules.vtkCommonTransforms.vtkAbstractTransform: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfTransforms(self) -> int: ...
    def GetTransform(self) -> vtkmodules.vtkCommonTransforms.vtkAbstractTransform: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMNITransformReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMNITransformReader: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkMNITransformWriter(vtkmodules.vtkCommonExecutionModel.vtkAlgorithm):
    def AddTransform(self, transform: vtkmodules.vtkCommonTransforms.vtkAbstractTransform) -> None: ...
    def GetComments(self) -> str: ...
    def GetDescriptiveName(self) -> str: ...
    def GetFileExtensions(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfTransforms(self) -> int: ...
    def GetTransform(self) -> vtkmodules.vtkCommonTransforms.vtkAbstractTransform: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMNITransformWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMNITransformWriter: ...
    def SetComments(self, _arg: str) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetTransform(self, transform: vtkmodules.vtkCommonTransforms.vtkAbstractTransform) -> None: ...
    def Write(self) -> None: ...
