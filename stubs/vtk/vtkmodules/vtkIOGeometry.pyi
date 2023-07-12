from typing import Callable, MutableSequence, Sequence, Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkIOCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonMath

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

VTK_FILE_BYTE_ORDER_BIG_ENDIAN: int
VTK_FILE_BYTE_ORDER_LITTLE_ENDIAN: int

class vtkAVSucdReader(vtkmodules.vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    def BinaryFileOff(self) -> None: ...
    def BinaryFileOn(self) -> None: ...
    def DisableAllCellArrays(self) -> None: ...
    def DisableAllPointArrays(self) -> None: ...
    def EnableAllCellArrays(self) -> None: ...
    def EnableAllPointArrays(self) -> None: ...
    def GetBinaryFile(self) -> int: ...
    def GetByteOrder(self) -> int: ...
    def GetByteOrderAsString(self) -> str: ...
    def GetCellArrayName(self, index: int) -> str: ...
    def GetCellArrayStatus(self, name: str) -> int: ...
    def GetCellDataRange(self, cellComp: int, index: int, min: MutableSequence[float], max: MutableSequence[float]) -> None: ...
    def GetFileName(self) -> str: ...
    def GetNodeDataRange(self, nodeComp: int, index: int, min: MutableSequence[float], max: MutableSequence[float]) -> None: ...
    def GetNumberOfCellArrays(self) -> int: ...
    def GetNumberOfCellComponents(self) -> int: ...
    def GetNumberOfCellFields(self) -> int: ...
    def GetNumberOfCells(self) -> int: ...
    def GetNumberOfFields(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfNodeComponents(self) -> int: ...
    def GetNumberOfNodeFields(self) -> int: ...
    def GetNumberOfNodes(self) -> int: ...
    def GetNumberOfPointArrays(self) -> int: ...
    def GetPointArrayName(self, index: int) -> str: ...
    def GetPointArrayStatus(self, name: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkAVSucdReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkAVSucdReader: ...
    def SetBinaryFile(self, _arg: int) -> None: ...
    def SetByteOrder(self, _arg: int) -> None: ...
    def SetByteOrderToBigEndian(self) -> None: ...
    def SetByteOrderToLittleEndian(self) -> None: ...
    def SetCellArrayStatus(self, name: str, status: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetPointArrayStatus(self, name: str, status: int) -> None: ...

class vtkBYUReader(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    @staticmethod
    def CanReadFile(filename: str) -> int: ...
    def GetDisplacementFileName(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetGeometryFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPartNumber(self) -> int: ...
    def GetPartNumberMaxValue(self) -> int: ...
    def GetPartNumberMinValue(self) -> int: ...
    def GetReadDisplacement(self) -> int: ...
    def GetReadScalar(self) -> int: ...
    def GetReadTexture(self) -> int: ...
    def GetScalarFileName(self) -> str: ...
    def GetTextureFileName(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkBYUReader: ...
    def ReadDisplacementOff(self) -> None: ...
    def ReadDisplacementOn(self) -> None: ...
    def ReadScalarOff(self) -> None: ...
    def ReadScalarOn(self) -> None: ...
    def ReadTextureOff(self) -> None: ...
    def ReadTextureOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkBYUReader: ...
    def SetDisplacementFileName(self, _arg: str) -> None: ...
    def SetFileName(self, f: str) -> None: ...
    def SetGeometryFileName(self, _arg: str) -> None: ...
    def SetPartNumber(self, _arg: int) -> None: ...
    def SetReadDisplacement(self, _arg: int) -> None: ...
    def SetReadScalar(self, _arg: int) -> None: ...
    def SetReadTexture(self, _arg: int) -> None: ...
    def SetScalarFileName(self, _arg: str) -> None: ...
    def SetTextureFileName(self, _arg: str) -> None: ...

class vtkBYUWriter(vtkmodules.vtkIOCore.vtkWriter):
    def GetDisplacementFileName(self) -> str: ...
    def GetGeometryFileName(self) -> str: ...
    @overload
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    @overload
    def GetInput(self, port: int) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetScalarFileName(self) -> str: ...
    def GetTextureFileName(self) -> str: ...
    def GetWriteDisplacement(self) -> int: ...
    def GetWriteScalar(self) -> int: ...
    def GetWriteTexture(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkBYUWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkBYUWriter: ...
    def SetDisplacementFileName(self, _arg: str) -> None: ...
    def SetGeometryFileName(self, _arg: str) -> None: ...
    def SetScalarFileName(self, _arg: str) -> None: ...
    def SetTextureFileName(self, _arg: str) -> None: ...
    def SetWriteDisplacement(self, _arg: int) -> None: ...
    def SetWriteScalar(self, _arg: int) -> None: ...
    def SetWriteTexture(self, _arg: int) -> None: ...
    def WriteDisplacementOff(self) -> None: ...
    def WriteDisplacementOn(self) -> None: ...
    def WriteScalarOff(self) -> None: ...
    def WriteScalarOn(self) -> None: ...
    def WriteTextureOff(self) -> None: ...
    def WriteTextureOn(self) -> None: ...

class vtkChacoReader(vtkmodules.vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    def GenerateEdgeWeightArraysOff(self) -> None: ...
    def GenerateEdgeWeightArraysOn(self) -> None: ...
    def GenerateGlobalElementIdArrayOff(self) -> None: ...
    def GenerateGlobalElementIdArrayOn(self) -> None: ...
    def GenerateGlobalNodeIdArrayOff(self) -> None: ...
    def GenerateGlobalNodeIdArrayOn(self) -> None: ...
    def GenerateVertexWeightArraysOff(self) -> None: ...
    def GenerateVertexWeightArraysOn(self) -> None: ...
    def GetBaseName(self) -> str: ...
    def GetDimensionality(self) -> int: ...
    def GetEdgeWeightArrayName(self, weight: int) -> str: ...
    def GetGenerateEdgeWeightArrays(self) -> int: ...
    def GetGenerateGlobalElementIdArray(self) -> int: ...
    def GetGenerateGlobalNodeIdArray(self) -> int: ...
    def GetGenerateVertexWeightArrays(self) -> int: ...
    @staticmethod
    def GetGlobalElementIdArrayName() -> str: ...
    @staticmethod
    def GetGlobalNodeIdArrayName() -> str: ...
    def GetNumberOfCellWeightArrays(self) -> int: ...
    def GetNumberOfEdgeWeights(self) -> int: ...
    def GetNumberOfEdges(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfPointWeightArrays(self) -> int: ...
    def GetNumberOfVertexWeights(self) -> int: ...
    def GetNumberOfVertices(self) -> int: ...
    def GetVertexWeightArrayName(self, weight: int) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkChacoReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkChacoReader: ...
    def SetBaseName(self, _arg: str) -> None: ...
    def SetGenerateEdgeWeightArrays(self, _arg: int) -> None: ...
    def SetGenerateGlobalElementIdArray(self, _arg: int) -> None: ...
    def SetGenerateGlobalNodeIdArray(self, _arg: int) -> None: ...
    def SetGenerateVertexWeightArrays(self, _arg: int) -> None: ...

class vtkFLUENTReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def DisableAllCellArrays(self) -> None: ...
    def EnableAllCellArrays(self) -> None: ...
    def GetCellArrayName(self, index: int) -> str: ...
    def GetCellArrayStatus(self, name: str) -> int: ...
    def GetDataByteOrder(self) -> int: ...
    def GetDataByteOrderAsString(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfCellArrays(self) -> int: ...
    def GetNumberOfCells(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkFLUENTReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkFLUENTReader: ...
    def SetCellArrayStatus(self, name: str, status: int) -> None: ...
    def SetDataByteOrder(self, __a: int) -> None: ...
    def SetDataByteOrderToBigEndian(self) -> None: ...
    def SetDataByteOrderToLittleEndian(self) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkFacetWriter(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkFacetWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkFacetWriter: ...
    def SetFileName(self, _arg: str) -> None: ...
    def Write(self) -> None: ...

class vtkGAMBITReader(vtkmodules.vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfCellFields(self) -> int: ...
    def GetNumberOfCells(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfNodeFields(self) -> int: ...
    def GetNumberOfNodes(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGAMBITReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGAMBITReader: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkGLTFDocumentLoader(vtkmodules.vtkCommonCore.vtkObject):
    class AccessorType(int):
        INVALID: AccessorType
        MAT2: AccessorType
        MAT3: AccessorType
        MAT4: AccessorType
        SCALAR: AccessorType
        VEC2: AccessorType
        VEC3: AccessorType
        VEC4: AccessorType

    class ComponentType(int):
        BYTE: ComponentType
        FLOAT: ComponentType
        SHORT: ComponentType
        UNSIGNED_BYTE: ComponentType
        UNSIGNED_INT: ComponentType
        UNSIGNED_SHORT: ComponentType

    class Target(int):
        ARRAY_BUFFER: Target
        ELEMENT_ARRAY_BUFFER: Target
    def ApplyAnimation(self, t: float, animationId: int, forceStep: bool = False) -> bool: ...
    @overload
    def BuildGlobalTransforms(self, nodeIndex: int, parentTransform: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...
    @overload
    def BuildGlobalTransforms(self) -> None: ...
    def BuildModelVTKGeometry(self) -> bool: ...
    @staticmethod
    def GetNumberOfComponentsForType(type: vtkGLTFDocumentLoader.AccessorType) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSupportedExtensions(self) -> Tuple[str, str]: ...
    def GetUsedExtensions(self) -> Tuple[str, str]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def LoadModelMetaDataFromFile(self, FileName: str) -> bool: ...
    def NewInstance(self) -> vtkGLTFDocumentLoader: ...
    def ResetAnimation(self, animationId: int) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGLTFDocumentLoader: ...

class vtkGLTFReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def ApplyDeformationsToGeometryOff(self) -> None: ...
    def ApplyDeformationsToGeometryOn(self) -> None: ...
    def DisableAnimation(self, animationIndex: int) -> None: ...
    def EnableAnimation(self, animationIndex: int) -> None: ...
    def GetAllSceneNames(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetAnimationDuration(self, animationIndex: int) -> float: ...
    def GetAnimationName(self, animationIndex: int) -> str: ...
    def GetAnimationSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetApplyDeformationsToGeometry(self) -> bool: ...
    def GetCurrentScene(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetFrameRate(self) -> int: ...
    def GetNumberOfAnimations(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfScenes(self) -> int: ...
    def GetNumberOfTextures(self) -> int: ...
    def GetSceneName(self, sceneIndex: int) -> str: ...
    def IsA(self, type: str) -> int: ...
    def IsAnimationEnabled(self, animationIndex: int) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGLTFReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGLTFReader: ...
    def SetApplyDeformationsToGeometry(self, flag: bool) -> None: ...
    def SetCurrentScene(self, _arg: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetFrameRate(self, _arg: int) -> None: ...
    def SetScene(self, scene: str) -> None: ...

class vtkGLTFWriter(vtkmodules.vtkIOCore.vtkWriter):
    def GetFileName(self) -> str: ...
    def GetInlineData(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSaveActivePointColor(self) -> bool: ...
    def GetSaveBatchId(self) -> bool: ...
    def GetSaveNormal(self) -> bool: ...
    def GetSaveTextures(self) -> bool: ...
    def GetTextureBaseDirectory(self) -> str: ...
    def InlineDataOff(self) -> None: ...
    def InlineDataOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGLTFWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGLTFWriter: ...
    def SaveActivePointColorOff(self) -> None: ...
    def SaveActivePointColorOn(self) -> None: ...
    def SaveBatchIdOff(self) -> None: ...
    def SaveBatchIdOn(self) -> None: ...
    def SaveNormalOff(self) -> None: ...
    def SaveNormalOn(self) -> None: ...
    def SaveTexturesOff(self) -> None: ...
    def SaveTexturesOn(self) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetInlineData(self, _arg: bool) -> None: ...
    def SetSaveActivePointColor(self, _arg: bool) -> None: ...
    def SetSaveBatchId(self, _arg: bool) -> None: ...
    def SetSaveNormal(self, _arg: bool) -> None: ...
    def SetSaveTextures(self, _arg: bool) -> None: ...
    def SetTextureBaseDirectory(self, _arg: str) -> None: ...
    def WriteToString(self) -> str: ...

class vtkHoudiniPolyDataWriter(vtkmodules.vtkIOCore.vtkWriter):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHoudiniPolyDataWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHoudiniPolyDataWriter: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkIVWriter(vtkmodules.vtkIOCore.vtkWriter):
    def GetFileName(self) -> str: ...
    @overload
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    @overload
    def GetInput(self, port: int) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkIVWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkIVWriter: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkMCubesReader(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def CreateDefaultLocator(self) -> None: ...
    def FlipNormalsOff(self) -> None: ...
    def FlipNormalsOn(self) -> None: ...
    def GetDataByteOrder(self) -> int: ...
    def GetDataByteOrderAsString(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetFlipNormals(self) -> int: ...
    def GetHeaderSize(self) -> int: ...
    def GetHeaderSizeMaxValue(self) -> int: ...
    def GetHeaderSizeMinValue(self) -> int: ...
    def GetLimitsFileName(self) -> str: ...
    def GetLocator(self) -> vtkmodules.vtkCommonDataModel.vtkIncrementalPointLocator: ...
    def GetMTime(self) -> int: ...
    def GetNormals(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSwapBytes(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMCubesReader: ...
    def NormalsOff(self) -> None: ...
    def NormalsOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMCubesReader: ...
    def SetDataByteOrder(self, __a: int) -> None: ...
    def SetDataByteOrderToBigEndian(self) -> None: ...
    def SetDataByteOrderToLittleEndian(self) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetFlipNormals(self, _arg: int) -> None: ...
    def SetHeaderSize(self, _arg: int) -> None: ...
    def SetLimitsFileName(self, _arg: str) -> None: ...
    def SetLocator(self, locator: vtkmodules.vtkCommonDataModel.vtkIncrementalPointLocator) -> None: ...
    def SetNormals(self, _arg: int) -> None: ...
    def SetSwapBytes(self, _arg: int) -> None: ...
    def SwapBytesOff(self) -> None: ...
    def SwapBytesOn(self) -> None: ...

class vtkMCubesWriter(vtkmodules.vtkIOCore.vtkWriter):
    def GetFileName(self) -> str: ...
    @overload
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    @overload
    def GetInput(self, port: int) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    def GetLimitsFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMCubesWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMCubesWriter: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetLimitsFileName(self, _arg: str) -> None: ...

class vtkMFIXReader(vtkmodules.vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    def DisableAllCellArrays(self) -> None: ...
    def EnableAllCellArrays(self) -> None: ...
    def GetCellArrayName(self, index: int) -> str: ...
    def GetCellArrayStatus(self, name: str) -> int: ...
    def GetCellDataRange(self, cellComp: int, min: MutableSequence[float], max: MutableSequence[float]) -> None: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfCellArrays(self) -> int: ...
    def GetNumberOfCellFields(self) -> int: ...
    def GetNumberOfCells(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfPoints(self) -> int: ...
    def GetNumberOfTimeSteps(self) -> int: ...
    def GetTimeStep(self) -> int: ...
    def GetTimeStepRange(self) -> Tuple[int, int]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMFIXReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMFIXReader: ...
    def SetCellArrayStatus(self, name: str, status: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetTimeStep(self, _arg: int) -> None: ...
    @overload
    def SetTimeStepRange(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetTimeStepRange(self, _arg: Sequence[int]) -> None: ...

class vtkOBJReader(vtkmodules.vtkIOCore.vtkAbstractPolyDataReader):
    def GetComment(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOBJReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOBJReader: ...

class vtkOBJWriter(vtkmodules.vtkIOCore.vtkWriter):
    def GetFileName(self) -> str: ...
    def GetInput(self, port: int) -> vtkmodules.vtkCommonDataModel.vtkDataSet: ...
    def GetInputGeometry(self) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    def GetInputTexture(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTextureFileName(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOBJWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOBJWriter: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetTextureFileName(self, _arg: str) -> None: ...

class vtkOpenFOAMReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def AddDimensionsToArrayNamesOff(self) -> None: ...
    def AddDimensionsToArrayNamesOn(self) -> None: ...
    def CacheMeshOff(self) -> None: ...
    def CacheMeshOn(self) -> None: ...
    def CanReadFile(self, __a: str) -> int: ...
    def CopyDataToCellZonesOff(self) -> None: ...
    def CopyDataToCellZonesOn(self) -> None: ...
    def CreateCellToPointOff(self) -> None: ...
    def CreateCellToPointOn(self) -> None: ...
    def DecomposePolyhedraOff(self) -> None: ...
    def DecomposePolyhedraOn(self) -> None: ...
    def DisableAllCellArrays(self) -> None: ...
    def DisableAllLagrangianArrays(self) -> None: ...
    def DisableAllPatchArrays(self) -> None: ...
    def DisableAllPointArrays(self) -> None: ...
    def EnableAllCellArrays(self) -> None: ...
    def EnableAllLagrangianArrays(self) -> None: ...
    def EnableAllPatchArrays(self) -> None: ...
    def EnableAllPointArrays(self) -> None: ...
    def GetAddDimensionsToArrayNames(self) -> int: ...
    def GetCacheMesh(self) -> int: ...
    def GetCellArrayName(self, index: int) -> str: ...
    def GetCellArrayStatus(self, name: str) -> int: ...
    def GetCopyDataToCellZones(self) -> bool: ...
    def GetCreateCellToPoint(self) -> int: ...
    def GetDecomposePolyhedra(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetLagrangianArrayName(self, index: int) -> str: ...
    def GetLagrangianArrayStatus(self, name: str) -> int: ...
    def GetListTimeStepsByControlDict(self) -> int: ...
    def GetNumberOfCellArrays(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfLagrangianArrays(self) -> int: ...
    def GetNumberOfPatchArrays(self) -> int: ...
    def GetNumberOfPointArrays(self) -> int: ...
    def GetPatchArrayName(self, index: int) -> str: ...
    def GetPatchArrayStatus(self, name: str) -> int: ...
    def GetPointArrayName(self, index: int) -> str: ...
    def GetPointArrayStatus(self, name: str) -> int: ...
    def GetPositionsIsIn13Format(self) -> int: ...
    def GetReadZones(self) -> int: ...
    def GetSkipZeroTime(self) -> bool: ...
    def GetTimeNames(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetTimeValue(self) -> float: ...
    def GetTimeValues(self) -> vtkmodules.vtkCommonCore.vtkDoubleArray: ...
    def GetUse64BitFloats(self) -> bool: ...
    def GetUse64BitLabels(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def ListTimeStepsByControlDictOff(self) -> None: ...
    def ListTimeStepsByControlDictOn(self) -> None: ...
    def MakeInformationVector(
        self,
        __a: vtkmodules.vtkCommonCore.vtkInformationVector,
        procDirName: str,
        timeNames: vtkmodules.vtkCommonCore.vtkStringArray = ...,
        timeValues: vtkmodules.vtkCommonCore.vtkDoubleArray = ...,
    ) -> int: ...
    def MakeMetaDataAtTimeStep(self, __a: bool) -> int: ...
    def NewInstance(self) -> vtkOpenFOAMReader: ...
    def PositionsIsIn13FormatOff(self) -> None: ...
    def PositionsIsIn13FormatOn(self) -> None: ...
    def ReadZonesOff(self) -> None: ...
    def ReadZonesOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOpenFOAMReader: ...
    def SetAddDimensionsToArrayNames(self, _arg: int) -> None: ...
    def SetCacheMesh(self, _arg: int) -> None: ...
    def SetCellArrayStatus(self, name: str, status: int) -> None: ...
    def SetCopyDataToCellZones(self, _arg: bool) -> None: ...
    def SetCreateCellToPoint(self, _arg: int) -> None: ...
    def SetDecomposePolyhedra(self, _arg: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetLagrangianArrayStatus(self, name: str, status: int) -> None: ...
    def SetListTimeStepsByControlDict(self, _arg: int) -> None: ...
    def SetParent(self, parent: vtkOpenFOAMReader) -> None: ...
    def SetPatchArrayStatus(self, name: str, status: int) -> None: ...
    def SetPointArrayStatus(self, name: str, status: int) -> None: ...
    def SetPositionsIsIn13Format(self, _arg: int) -> None: ...
    def SetReadZones(self, _arg: int) -> None: ...
    def SetRefresh(self) -> None: ...
    def SetSkipZeroTime(self, _arg: bool) -> None: ...
    def SetTimeValue(self, __a: float) -> bool: ...
    def SetUse64BitFloats(self, val: bool) -> None: ...
    def SetUse64BitLabels(self, val: bool) -> None: ...
    def SkipZeroTimeOff(self) -> None: ...
    def SkipZeroTimeOn(self) -> None: ...
    def Use64BitFloatsOff(self) -> None: ...
    def Use64BitFloatsOn(self) -> None: ...
    def Use64BitLabelsOff(self) -> None: ...
    def Use64BitLabelsOn(self) -> None: ...

class vtkPTSReader(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def CreateCellsOff(self) -> None: ...
    def CreateCellsOn(self) -> None: ...
    def GetCreateCells(self) -> bool: ...
    def GetFileName(self) -> str: ...
    def GetIncludeColorAndLuminance(self) -> bool: ...
    def GetLimitReadToBounds(self) -> bool: ...
    def GetLimitToMaxNumberOfPoints(self) -> bool: ...
    def GetMaxNumberOfPoints(self) -> int: ...
    def GetMaxNumberOfPointsMaxValue(self) -> int: ...
    def GetMaxNumberOfPointsMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputDataTypeIsDouble(self) -> bool: ...
    def GetReadBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    def IncludeColorAndLuminanceOff(self) -> None: ...
    def IncludeColorAndLuminanceOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def LimitReadToBoundsOff(self) -> None: ...
    def LimitReadToBoundsOn(self) -> None: ...
    def LimitToMaxNumberOfPointsOff(self) -> None: ...
    def LimitToMaxNumberOfPointsOn(self) -> None: ...
    def NewInstance(self) -> vtkPTSReader: ...
    def OutputDataTypeIsDoubleOff(self) -> None: ...
    def OutputDataTypeIsDoubleOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPTSReader: ...
    def SetCreateCells(self, _arg: bool) -> None: ...
    def SetFileName(self, filename: str) -> None: ...
    def SetIncludeColorAndLuminance(self, _arg: bool) -> None: ...
    def SetLimitReadToBounds(self, _arg: bool) -> None: ...
    def SetLimitToMaxNumberOfPoints(self, _arg: bool) -> None: ...
    def SetMaxNumberOfPoints(self, _arg: int) -> None: ...
    def SetOutputDataTypeIsDouble(self, _arg: bool) -> None: ...
    @overload
    def SetReadBounds(self, _arg1: float, _arg2: float, _arg3: float, _arg4: float, _arg5: float, _arg6: float) -> None: ...
    @overload
    def SetReadBounds(self, _arg: Sequence[float]) -> None: ...

class vtkParticleReader(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def GetDataByteOrder(self) -> int: ...
    def GetDataByteOrderAsString(self) -> str: ...
    def GetDataType(self) -> int: ...
    def GetDataTypeMaxValue(self) -> int: ...
    def GetDataTypeMinValue(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetFileType(self) -> int: ...
    def GetFileTypeMaxValue(self) -> int: ...
    def GetFileTypeMinValue(self) -> int: ...
    def GetHasScalar(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSwapBytes(self) -> int: ...
    def HasScalarOff(self) -> None: ...
    def HasScalarOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParticleReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParticleReader: ...
    def SetDataByteOrder(self, __a: int) -> None: ...
    def SetDataByteOrderToBigEndian(self) -> None: ...
    def SetDataByteOrderToLittleEndian(self) -> None: ...
    def SetDataType(self, _arg: int) -> None: ...
    def SetDataTypeToDouble(self) -> None: ...
    def SetDataTypeToFloat(self) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetFileType(self, _arg: int) -> None: ...
    def SetFileTypeToBinary(self) -> None: ...
    def SetFileTypeToText(self) -> None: ...
    def SetFileTypeToUnknown(self) -> None: ...
    def SetHasScalar(self, _arg: int) -> None: ...
    def SetSwapBytes(self, _arg: int) -> None: ...
    def SwapBytesOff(self) -> None: ...
    def SwapBytesOn(self) -> None: ...

class vtkProStarReader(vtkmodules.vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    class cellType(int): ...
    class shapeType(int): ...
    starcdBaffleType: cellType
    starcdFluidType: cellType
    starcdHex: shapeType
    starcdLine: shapeType
    starcdLineType: cellType
    starcdPoint: shapeType
    starcdPointType: cellType
    starcdPoly: shapeType
    starcdPrism: shapeType
    starcdPyr: shapeType
    starcdShell: shapeType
    starcdShellType: cellType
    starcdSolidType: cellType
    starcdTet: shapeType
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetScaleFactor(self) -> float: ...
    def GetScaleFactorMaxValue(self) -> float: ...
    def GetScaleFactorMinValue(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkProStarReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkProStarReader: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetScaleFactor(self, _arg: float) -> None: ...

class vtkSTLReader(vtkmodules.vtkIOCore.vtkAbstractPolyDataReader):
    def GetBinaryHeader(self) -> vtkmodules.vtkCommonCore.vtkUnsignedCharArray: ...
    def GetHeader(self) -> str: ...
    def GetLocator(self) -> vtkmodules.vtkCommonDataModel.vtkIncrementalPointLocator: ...
    def GetMTime(self) -> int: ...
    def GetMerging(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetScalarTags(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MergingOff(self) -> None: ...
    def MergingOn(self) -> None: ...
    def NewInstance(self) -> vtkSTLReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSTLReader: ...
    def ScalarTagsOff(self) -> None: ...
    def ScalarTagsOn(self) -> None: ...
    def SetLocator(self, locator: vtkmodules.vtkCommonDataModel.vtkIncrementalPointLocator) -> None: ...
    def SetMerging(self, _arg: int) -> None: ...
    def SetScalarTags(self, _arg: int) -> None: ...

class vtkSTLWriter(vtkmodules.vtkIOCore.vtkWriter):
    def GetBinaryHeader(self) -> vtkmodules.vtkCommonCore.vtkUnsignedCharArray: ...
    def GetFileName(self) -> str: ...
    def GetFileType(self) -> int: ...
    def GetFileTypeMaxValue(self) -> int: ...
    def GetFileTypeMinValue(self) -> int: ...
    def GetHeader(self) -> str: ...
    @overload
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    @overload
    def GetInput(self, port: int) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSTLWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSTLWriter: ...
    def SetBinaryHeader(self, binaryHeader: vtkmodules.vtkCommonCore.vtkUnsignedCharArray) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetFileType(self, _arg: int) -> None: ...
    def SetFileTypeToASCII(self) -> None: ...
    def SetFileTypeToBinary(self) -> None: ...
    def SetHeader(self, _arg: str) -> None: ...

class vtkTecplotReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def GetBlockName(self, blockIdx: int) -> str: ...
    def GetDataArrayName(self, arrayIdx: int) -> str: ...
    def GetDataArrayStatus(self, arayName: str) -> int: ...
    def GetDataAttributeName(self, attrIndx: int) -> str: ...
    def GetDataTitle(self) -> str: ...
    def GetNumberOfBlocks(self) -> int: ...
    def GetNumberOfDataArrays(self) -> int: ...
    def GetNumberOfDataAttributes(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfVariables(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @overload
    def IsDataAttributeCellBased(self, attrName: str) -> int: ...
    @overload
    def IsDataAttributeCellBased(self, attrIndx: int) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTecplotReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTecplotReader: ...
    def SetDataArrayStatus(self, arayName: str, bChecked: int) -> None: ...
    def SetFileName(self, fileName: str) -> None: ...

class vtkWindBladeReader(vtkmodules.vtkCommonExecutionModel.vtkStructuredGridAlgorithm):
    def DisableAllPointArrays(self) -> None: ...
    def EnableAllPointArrays(self) -> None: ...
    def GetBladeOutput(self) -> vtkmodules.vtkCommonDataModel.vtkUnstructuredGrid: ...
    def GetFieldOutput(self) -> vtkmodules.vtkCommonDataModel.vtkStructuredGrid: ...
    def GetFilename(self) -> str: ...
    def GetGroundOutput(self) -> vtkmodules.vtkCommonDataModel.vtkStructuredGrid: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfPointArrays(self) -> int: ...
    def GetPointArrayName(self, index: int) -> str: ...
    def GetPointArrayStatus(self, name: str) -> int: ...
    def GetSubExtent(self) -> Tuple[int, int, int, int, int, int]: ...
    def GetWholeExtent(self) -> Tuple[int, int, int, int, int, int]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWindBladeReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWindBladeReader: ...
    def SetFilename(self, _arg: str) -> None: ...
    def SetPointArrayStatus(self, name: str, status: int) -> None: ...
    @overload
    def SetSubExtent(self, _arg1: int, _arg2: int, _arg3: int, _arg4: int, _arg5: int, _arg6: int) -> None: ...
    @overload
    def SetSubExtent(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetWholeExtent(self, _arg1: int, _arg2: int, _arg3: int, _arg4: int, _arg5: int, _arg6: int) -> None: ...
    @overload
    def SetWholeExtent(self, _arg: Sequence[int]) -> None: ...
