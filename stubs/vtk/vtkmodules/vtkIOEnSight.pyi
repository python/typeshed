from typing import overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

class EnsightReaderCellIdMode(int): ...

IMPLICIT_STRUCTURED_MODE: EnsightReaderCellIdMode
NON_SPARSE_MODE: EnsightReaderCellIdMode
SINGLE_PROCESS_MODE: EnsightReaderCellIdMode
SPARSE_MODE: EnsightReaderCellIdMode

class vtkGenericEnSightReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    class FileTypes(int): ...
    ENSIGHT_6: FileTypes
    ENSIGHT_6_BINARY: FileTypes
    ENSIGHT_GOLD: FileTypes
    ENSIGHT_GOLD_BINARY: FileTypes
    ENSIGHT_MASTER_SERVER: FileTypes
    FILE_BIG_ENDIAN: int
    FILE_LITTLE_ENDIAN: int
    FILE_UNKNOWN_ENDIAN: int
    def CanReadFile(self, casefilename: str) -> int: ...
    def DetermineEnSightVersion(self, quiet: int = 0) -> int: ...
    def GetByteOrder(self) -> int: ...
    def GetByteOrderAsString(self) -> str: ...
    def GetCaseFileName(self) -> str: ...
    def GetCellArrayName(self, index: int) -> str: ...
    def GetCellArrayStatus(self, name: str) -> int: ...
    def GetCellDataArraySelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetComplexDescription(self, n: int) -> str: ...
    def GetComplexVariableType(self, n: int) -> int: ...
    @overload
    def GetDescription(self, n: int) -> str: ...
    @overload
    def GetDescription(self, n: int, type: int) -> str: ...
    def GetEnSightVersion(self) -> int: ...
    def GetFilePath(self) -> str: ...
    def GetGeometryFileName(self) -> str: ...
    def GetMaximumTimeValue(self) -> float: ...
    def GetMinimumTimeValue(self) -> float: ...
    def GetNumberOfCellArrays(self) -> int: ...
    def GetNumberOfComplexScalarsPerElement(self) -> int: ...
    def GetNumberOfComplexScalarsPerNode(self) -> int: ...
    def GetNumberOfComplexVariables(self) -> int: ...
    def GetNumberOfComplexVectorsPerElement(self) -> int: ...
    def GetNumberOfComplexVectorsPerNode(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfPointArrays(self) -> int: ...
    def GetNumberOfScalarsPerElement(self) -> int: ...
    def GetNumberOfScalarsPerMeasuredNode(self) -> int: ...
    def GetNumberOfScalarsPerNode(self) -> int: ...
    def GetNumberOfTensorsAsymPerElement(self) -> int: ...
    def GetNumberOfTensorsAsymPerNode(self) -> int: ...
    def GetNumberOfTensorsSymmPerElement(self) -> int: ...
    def GetNumberOfTensorsSymmPerNode(self) -> int: ...
    @overload
    def GetNumberOfVariables(self) -> int: ...
    @overload
    def GetNumberOfVariables(self, type: int) -> int: ...
    def GetNumberOfVectorsPerElement(self) -> int: ...
    def GetNumberOfVectorsPerMeasuredNode(self) -> int: ...
    def GetNumberOfVectorsPerNode(self) -> int: ...
    def GetParticleCoordinatesByIndex(self) -> int: ...
    def GetPointArrayName(self, index: int) -> str: ...
    def GetPointArrayStatus(self, name: str) -> int: ...
    def GetPointDataArraySelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetReadAllVariables(self) -> int: ...
    def GetReader(self) -> vtkGenericEnSightReader: ...
    def GetTimeSets(self) -> vtkmodules.vtkCommonCore.vtkDataArrayCollection: ...
    def GetTimeValue(self) -> float: ...
    def GetVariableType(self, n: int) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsEnSightFile(casefilename: str) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGenericEnSightReader: ...
    def ParticleCoordinatesByIndexOff(self) -> None: ...
    def ParticleCoordinatesByIndexOn(self) -> None: ...
    def ReadAllVariablesOff(self) -> None: ...
    def ReadAllVariablesOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGenericEnSightReader: ...
    def SetByteOrder(self, _arg: int) -> None: ...
    def SetByteOrderToBigEndian(self) -> None: ...
    def SetByteOrderToLittleEndian(self) -> None: ...
    def SetCaseFileName(self, fileName: str) -> None: ...
    def SetCellArrayStatus(self, name: str, status: int) -> None: ...
    def SetFilePath(self, _arg: str) -> None: ...
    def SetParticleCoordinatesByIndex(self, _arg: int) -> None: ...
    def SetPointArrayStatus(self, name: str, status: int) -> None: ...
    def SetReadAllVariables(self, _arg: int) -> None: ...
    def SetTimeValue(self, value: float) -> None: ...

class vtkEnSightReader(vtkGenericEnSightReader):
    class ElementTypesList(int): ...
    class SectionTypeList(int): ...
    class VariableTypesList(int): ...
    BAR2: ElementTypesList
    BAR3: ElementTypesList
    BLOCK: SectionTypeList
    COMPLEX_SCALAR_PER_ELEMENT: VariableTypesList
    COMPLEX_SCALAR_PER_NODE: VariableTypesList
    COMPLEX_VECTOR_PER_ELEMENT: VariableTypesList
    COMPLEX_VECTOR_PER_NODE: VariableTypesList
    COORDINATES: SectionTypeList
    ELEMENT: SectionTypeList
    HEXA20: ElementTypesList
    HEXA8: ElementTypesList
    NFACED: ElementTypesList
    NSIDED: ElementTypesList
    NUMBER_OF_ELEMENT_TYPES: ElementTypesList
    PENTA15: ElementTypesList
    PENTA6: ElementTypesList
    POINT: ElementTypesList
    PYRAMID13: ElementTypesList
    PYRAMID5: ElementTypesList
    QUAD4: ElementTypesList
    QUAD8: ElementTypesList
    SCALAR_PER_ELEMENT: VariableTypesList
    SCALAR_PER_MEASURED_NODE: VariableTypesList
    SCALAR_PER_NODE: VariableTypesList
    TENSOR_ASYM_PER_ELEMENT: VariableTypesList
    TENSOR_ASYM_PER_NODE: VariableTypesList
    TENSOR_SYMM_PER_ELEMENT: VariableTypesList
    TENSOR_SYMM_PER_NODE: VariableTypesList
    TETRA10: ElementTypesList
    TETRA4: ElementTypesList
    TRIA3: ElementTypesList
    TRIA6: ElementTypesList
    VECTOR_PER_ELEMENT: VariableTypesList
    VECTOR_PER_MEASURED_NODE: VariableTypesList
    VECTOR_PER_NODE: VariableTypesList
    def GetMatchFileName(self) -> str: ...
    def GetMeasuredFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkEnSightReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkEnSightReader: ...

class vtkEnSight6BinaryReader(vtkEnSightReader):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkEnSight6BinaryReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkEnSight6BinaryReader: ...

class vtkEnSight6Reader(vtkEnSightReader):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkEnSight6Reader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkEnSight6Reader: ...

class vtkEnSightGoldBinaryReader(vtkEnSightReader):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkEnSightGoldBinaryReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkEnSightGoldBinaryReader: ...

class vtkEnSightGoldReader(vtkEnSightReader):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkEnSightGoldReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkEnSightGoldReader: ...

class vtkEnSightMasterServerReader(vtkGenericEnSightReader):
    def CanReadFile(self, fname: str) -> int: ...
    def DetermineFileName(self, piece: int) -> int: ...
    def GetCurrentPiece(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPieceCaseFileName(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkEnSightMasterServerReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkEnSightMasterServerReader: ...
    def SetCurrentPiece(self, _arg: int) -> None: ...
