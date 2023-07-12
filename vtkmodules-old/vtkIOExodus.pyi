from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkIOCore
import vtkmodules.vtkIOXMLParser

class vtkCPExodusIIElementBlock(vtkmodules.vtkCommonDataModel.vtkUnstructuredGridBase):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkCPExodusIIElementBlock': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkCPExodusIIElementBlock': ...

class vtkCPExodusIIElementBlockImpl(vtkmodules.vtkCommonCore.vtkObject):
    def Allocate(self, numCells:int, extSize:int=1000) -> None: ...
    def GetCellPoints(self, cellId:int, ptIds:'vtkIdList') -> None: ...
    def GetCellType(self, cellId:int) -> int: ...
    def GetFaceStream(self, cellId:int, ptIds:'vtkIdList') -> None: ...
    def GetIdsOfCellsOfType(self, type:int, array:'vtkIdTypeArray') -> None: ...
    def GetMaxCellSize(self) -> int: ...
    def GetNumberOfCells(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetPointCells(self, ptId:int, cellIds:'vtkIdList') -> None: ...
    @overload
    def InsertNextCell(self, type:int, ptIds:'vtkIdList') -> int: ...
    @overload
    def InsertNextCell(self, type:int, npts:int, ptIds:Sequence[int]) -> int: ...
    @overload
    def InsertNextCell(self, type:int, npts:int, ptIds:Sequence[int], nfaces:int, faces:Sequence[int]) -> int: ...
    def IsA(self, type:str) -> int: ...
    def IsHomogeneous(self) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkCPExodusIIElementBlockImpl': ...
    def ReplaceCell(self, cellId:int, npts:int, pts:Sequence[int]) -> None: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkCPExodusIIElementBlockImpl': ...
    def SetExodusConnectivityArray(self, elements:MutableSequence[int], type:str, numElements:int, nodesPerElement:int) -> bool: ...

class vtkCPExodusIIInSituReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def GetCurrentTimeStep(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetTimeStepRange(self) -> Tuple[int, int]: ...
    def GetTimeStepValue(self, step:int) -> float: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkCPExodusIIInSituReader': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkCPExodusIIInSituReader': ...
    def SetCurrentTimeStep(self, _arg:int) -> None: ...
    def SetFileName(self, _arg:str) -> None: ...

class vtkExodusIICache(vtkmodules.vtkCommonCore.vtkObject):
    def Clear(self) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetSpaceLeft(self) -> float: ...
    def Insert(self, key:'vtkExodusIICacheKey', value:'vtkDataArray') -> None: ...
    @overload
    def Invalidate(self, key:'vtkExodusIICacheKey') -> int: ...
    @overload
    def Invalidate(self, key:'vtkExodusIICacheKey', pattern:'vtkExodusIICacheKey') -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkExodusIICache': ...
    def ReduceToSize(self, newSize:float) -> int: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkExodusIICache': ...
    def SetCacheCapacity(self, sizeInMiB:float) -> None: ...

class vtkExodusIICacheEntry(object):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arr:'vtkDataArray') -> None: ...
    @overload
    def __init__(self, other:'vtkExodusIICacheEntry') -> None: ...
    def GetValue(self) -> 'vtkDataArray': ...

class vtkExodusIICacheKey(object):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, time:int, objType:int, objId:int, arrId:int) -> None: ...
    @overload
    def __init__(self, src:'vtkExodusIICacheKey') -> None: ...
    def match(self, other:'vtkExodusIICacheKey', pattern:'vtkExodusIICacheKey') -> bool: ...

class vtkExodusIIReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    class ObjectType(int): ...
    ASSEMBLY:'ObjectType'
    EDGE_BLOCK:'ObjectType'
    EDGE_BLOCK_ATTRIB:'ObjectType'
    EDGE_BLOCK_CONN:'ObjectType'
    EDGE_ID:'ObjectType'
    EDGE_MAP:'ObjectType'
    EDGE_SET:'ObjectType'
    EDGE_SET_CONN:'ObjectType'
    ELEMENT_ID:'ObjectType'
    ELEM_BLOCK:'ObjectType'
    ELEM_BLOCK_ATTRIB:'ObjectType'
    ELEM_BLOCK_EDGE_CONN:'ObjectType'
    ELEM_BLOCK_ELEM_CONN:'ObjectType'
    ELEM_BLOCK_FACE_CONN:'ObjectType'
    ELEM_BLOCK_TEMPORAL:'ObjectType'
    ELEM_MAP:'ObjectType'
    ELEM_SET:'ObjectType'
    ELEM_SET_CONN:'ObjectType'
    ENTITY_COUNTS:'ObjectType'
    FACE_BLOCK:'ObjectType'
    FACE_BLOCK_ATTRIB:'ObjectType'
    FACE_BLOCK_CONN:'ObjectType'
    FACE_ID:'ObjectType'
    FACE_MAP:'ObjectType'
    FACE_SET:'ObjectType'
    FACE_SET_CONN:'ObjectType'
    GLOBAL:'ObjectType'
    GLOBAL_CONN:'ObjectType'
    GLOBAL_ELEMENT_ID:'ObjectType'
    GLOBAL_NODE_ID:'ObjectType'
    GLOBAL_TEMPORAL:'ObjectType'
    HIERARCHY:'ObjectType'
    ID_NOT_FOUND:int
    IMPLICIT_ELEMENT_ID:'ObjectType'
    IMPLICIT_NODE_ID:'ObjectType'
    INFO_RECORDS:'ObjectType'
    MATERIAL:'ObjectType'
    NODAL:'ObjectType'
    NODAL_COORDS:'ObjectType'
    NODAL_SQUEEZEMAP:'ObjectType'
    NODAL_TEMPORAL:'ObjectType'
    NODE_ID:'ObjectType'
    NODE_MAP:'ObjectType'
    NODE_SET:'ObjectType'
    NODE_SET_CONN:'ObjectType'
    OBJECT_ID:'ObjectType'
    PART:'ObjectType'
    QA_RECORDS:'ObjectType'
    SEARCH_TYPE_ELEMENT:int
    SEARCH_TYPE_ELEMENT_THEN_NODE:int
    SEARCH_TYPE_NODE:int
    SEARCH_TYPE_NODE_THEN_ELEMENT:int
    SIDE_SET:'ObjectType'
    SIDE_SET_CONN:'ObjectType'
    def AnimateModeShapesOff(self) -> None: ...
    def AnimateModeShapesOn(self) -> None: ...
    def ApplyDisplacementsOff(self) -> None: ...
    def ApplyDisplacementsOn(self) -> None: ...
    def CanReadFile(self, fname:str) -> int: ...
    def Dump(self) -> None: ...
    @staticmethod
    def GLOBAL_TEMPORAL_VARIABLE() -> 'vtkInformationIntegerKey': ...
    @staticmethod
    def GLOBAL_VARIABLE() -> 'vtkInformationIntegerKey': ...
    def GenerateFileIdArrayOff(self) -> None: ...
    def GenerateFileIdArrayOn(self) -> None: ...
    def GenerateGlobalElementIdArrayOff(self) -> None: ...
    def GenerateGlobalElementIdArrayOn(self) -> None: ...
    def GenerateGlobalNodeIdArrayOff(self) -> None: ...
    def GenerateGlobalNodeIdArrayOn(self) -> None: ...
    def GenerateImplicitElementIdArrayOff(self) -> None: ...
    def GenerateImplicitElementIdArrayOn(self) -> None: ...
    def GenerateImplicitNodeIdArrayOff(self) -> None: ...
    def GenerateImplicitNodeIdArrayOn(self) -> None: ...
    def GenerateObjectIdCellArrayOff(self) -> None: ...
    def GenerateObjectIdCellArrayOn(self) -> None: ...
    def GetAnimateModeShapes(self) -> int: ...
    def GetApplyDisplacements(self) -> int: ...
    def GetAssemblyArrayID(self, name:str) -> int: ...
    def GetAssemblyArrayName(self, arrayIdx:int) -> str: ...
    @overload
    def GetAssemblyArrayStatus(self, index:int) -> int: ...
    @overload
    def GetAssemblyArrayStatus(self, __a:str) -> int: ...
    def GetCacheSize(self) -> float: ...
    def GetDimensionality(self) -> int: ...
    def GetDisplacementMagnitude(self) -> float: ...
    def GetDisplayType(self) -> int: ...
    def GetEdgeBlockArrayName(self, index:int) -> str: ...
    def GetEdgeBlockArrayStatus(self, name:str) -> int: ...
    def GetEdgeMapArrayName(self, index:int) -> str: ...
    def GetEdgeMapArrayStatus(self, name:str) -> int: ...
    def GetEdgeResultArrayName(self, index:int) -> str: ...
    def GetEdgeResultArrayStatus(self, name:str) -> int: ...
    def GetEdgeSetArrayName(self, index:int) -> str: ...
    def GetEdgeSetArrayStatus(self, name:str) -> int: ...
    def GetEdgeSetResultArrayName(self, index:int) -> str: ...
    def GetEdgeSetResultArrayStatus(self, name:str) -> int: ...
    def GetElementBlockArrayName(self, index:int) -> str: ...
    def GetElementBlockArrayStatus(self, name:str) -> int: ...
    def GetElementMapArrayName(self, index:int) -> str: ...
    def GetElementMapArrayStatus(self, name:str) -> int: ...
    def GetElementResultArrayName(self, index:int) -> str: ...
    def GetElementResultArrayStatus(self, name:str) -> int: ...
    def GetElementSetArrayName(self, index:int) -> str: ...
    def GetElementSetArrayStatus(self, name:str) -> int: ...
    def GetElementSetResultArrayName(self, index:int) -> str: ...
    def GetElementSetResultArrayStatus(self, name:str) -> int: ...
    def GetFaceBlockArrayName(self, index:int) -> str: ...
    def GetFaceBlockArrayStatus(self, name:str) -> int: ...
    def GetFaceMapArrayName(self, index:int) -> str: ...
    def GetFaceMapArrayStatus(self, name:str) -> int: ...
    def GetFaceResultArrayName(self, index:int) -> str: ...
    def GetFaceResultArrayStatus(self, name:str) -> int: ...
    def GetFaceSetArrayName(self, index:int) -> str: ...
    def GetFaceSetArrayStatus(self, name:str) -> int: ...
    def GetFaceSetResultArrayName(self, index:int) -> str: ...
    def GetFaceSetResultArrayStatus(self, name:str) -> int: ...
    def GetFileId(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetGenerateFileIdArray(self) -> int: ...
    def GetGenerateGlobalElementIdArray(self) -> int: ...
    def GetGenerateGlobalNodeIdArray(self) -> int: ...
    def GetGenerateImplicitElementIdArray(self) -> int: ...
    def GetGenerateImplicitNodeIdArray(self) -> int: ...
    def GetGenerateObjectIdCellArray(self) -> int: ...
    @overload
    @staticmethod
    def GetGlobalEdgeID(data:'vtkDataSet', localID:int) -> int: ...
    @overload
    @staticmethod
    def GetGlobalEdgeID(data:'vtkDataSet', localID:int, searchType:int) -> int: ...
    @staticmethod
    def GetGlobalEdgeIdArrayName() -> str: ...
    @overload
    @staticmethod
    def GetGlobalElementID(data:'vtkDataSet', localID:int) -> int: ...
    @overload
    @staticmethod
    def GetGlobalElementID(data:'vtkDataSet', localID:int, searchType:int) -> int: ...
    @staticmethod
    def GetGlobalElementIdArrayName() -> str: ...
    @overload
    @staticmethod
    def GetGlobalFaceID(data:'vtkDataSet', localID:int) -> int: ...
    @overload
    @staticmethod
    def GetGlobalFaceID(data:'vtkDataSet', localID:int, searchType:int) -> int: ...
    @staticmethod
    def GetGlobalFaceIdArrayName() -> str: ...
    @overload
    @staticmethod
    def GetGlobalNodeID(data:'vtkDataSet', localID:int) -> int: ...
    @overload
    @staticmethod
    def GetGlobalNodeID(data:'vtkDataSet', localID:int, searchType:int) -> int: ...
    @staticmethod
    def GetGlobalNodeIdArrayName() -> str: ...
    def GetGlobalResultArrayName(self, index:int) -> str: ...
    def GetGlobalResultArrayStatus(self, name:str) -> int: ...
    def GetHasModeShapes(self) -> int: ...
    def GetHierarchyArrayName(self, arrayIdx:int) -> str: ...
    @overload
    def GetHierarchyArrayStatus(self, index:int) -> int: ...
    @overload
    def GetHierarchyArrayStatus(self, __a:str) -> int: ...
    def GetIgnoreFileTime(self) -> bool: ...
    @staticmethod
    def GetImplicitEdgeIdArrayName() -> str: ...
    @staticmethod
    def GetImplicitElementIdArrayName() -> str: ...
    @staticmethod
    def GetImplicitFaceIdArrayName() -> str: ...
    @staticmethod
    def GetImplicitNodeIdArrayName() -> str: ...
    def GetMTime(self) -> int: ...
    def GetMaterialArrayID(self, name:str) -> int: ...
    def GetMaterialArrayName(self, arrayIdx:int) -> str: ...
    @overload
    def GetMaterialArrayStatus(self, index:int) -> int: ...
    @overload
    def GetMaterialArrayStatus(self, __a:str) -> int: ...
    def GetMaxNameLength(self) -> int: ...
    def GetMetadataMTime(self) -> int: ...
    def GetModeShapeTime(self) -> float: ...
    def GetModeShapesRange(self) -> Tuple[int, int]: ...
    def GetNodeMapArrayName(self, index:int) -> str: ...
    def GetNodeMapArrayStatus(self, name:str) -> int: ...
    def GetNodeSetArrayName(self, index:int) -> str: ...
    def GetNodeSetArrayStatus(self, name:str) -> int: ...
    def GetNodeSetResultArrayName(self, index:int) -> str: ...
    def GetNodeSetResultArrayStatus(self, name:str) -> int: ...
    def GetNumberOfAssemblyArrays(self) -> int: ...
    def GetNumberOfEdgeBlockArrays(self) -> int: ...
    def GetNumberOfEdgeMapArrays(self) -> int: ...
    def GetNumberOfEdgeResultArrays(self) -> int: ...
    def GetNumberOfEdgeSetArrays(self) -> int: ...
    def GetNumberOfEdgeSetResultArrays(self) -> int: ...
    def GetNumberOfEdgesInFile(self) -> int: ...
    def GetNumberOfElementBlockArrays(self) -> int: ...
    def GetNumberOfElementMapArrays(self) -> int: ...
    def GetNumberOfElementResultArrays(self) -> int: ...
    def GetNumberOfElementSetArrays(self) -> int: ...
    def GetNumberOfElementSetResultArrays(self) -> int: ...
    def GetNumberOfElementsInFile(self) -> int: ...
    def GetNumberOfEntriesInObject(self, objectType:int, objectIndex:int) -> int: ...
    def GetNumberOfFaceBlockArrays(self) -> int: ...
    def GetNumberOfFaceMapArrays(self) -> int: ...
    def GetNumberOfFaceResultArrays(self) -> int: ...
    def GetNumberOfFaceSetArrays(self) -> int: ...
    def GetNumberOfFaceSetResultArrays(self) -> int: ...
    def GetNumberOfFacesInFile(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfGlobalResultArrays(self) -> int: ...
    def GetNumberOfHierarchyArrays(self) -> int: ...
    def GetNumberOfMaterialArrays(self) -> int: ...
    def GetNumberOfNodeMapArrays(self) -> int: ...
    def GetNumberOfNodeSetArrays(self) -> int: ...
    def GetNumberOfNodeSetResultArrays(self) -> int: ...
    def GetNumberOfNodes(self) -> int: ...
    def GetNumberOfNodesInFile(self) -> int: ...
    def GetNumberOfObjectArrayComponents(self, objectType:int, arrayIndex:int) -> int: ...
    def GetNumberOfObjectArrays(self, objectType:int) -> int: ...
    def GetNumberOfObjectAttributes(self, objectType:int, objectIndex:int) -> int: ...
    def GetNumberOfObjects(self, objectType:int) -> int: ...
    def GetNumberOfPartArrays(self) -> int: ...
    def GetNumberOfPointResultArrays(self) -> int: ...
    def GetNumberOfSideSetArrays(self) -> int: ...
    def GetNumberOfSideSetResultArrays(self) -> int: ...
    def GetNumberOfTimeSteps(self) -> int: ...
    def GetObjectArrayIndex(self, objectType:int, arrayName:str) -> int: ...
    def GetObjectArrayName(self, objectType:int, arrayIndex:int) -> str: ...
    @overload
    def GetObjectArrayStatus(self, objectType:int, arrayIndex:int) -> int: ...
    @overload
    def GetObjectArrayStatus(self, objectType:int, arrayName:str) -> int: ...
    def GetObjectAttributeIndex(self, objectType:int, objectIndex:int, attribName:str) -> int: ...
    def GetObjectAttributeName(self, objectType:int, objectIndex:int, attribIndex:int) -> str: ...
    @overload
    def GetObjectAttributeStatus(self, objectType:int, objectIndex:int, attribIndex:int) -> int: ...
    @overload
    def GetObjectAttributeStatus(self, objectType:int, objectIndex:int, attribName:str) -> int: ...
    def GetObjectId(self, objectType:int, objectIndex:int) -> int: ...
    @staticmethod
    def GetObjectIdArrayName() -> str: ...
    @overload
    def GetObjectIndex(self, objectType:int, objectName:str) -> int: ...
    @overload
    def GetObjectIndex(self, objectType:int, id:int) -> int: ...
    @overload
    def GetObjectName(self, objectType:int, objectIndex:int) -> str: ...
    @overload
    def GetObjectName(self) -> str: ...
    @overload
    def GetObjectStatus(self, objectType:int, objectIndex:int) -> int: ...
    @overload
    def GetObjectStatus(self, objectType:int, objectName:str) -> int: ...
    def GetObjectTypeFromName(self, name:str) -> int: ...
    def GetObjectTypeName(self, __a:int) -> str: ...
    def GetPartArrayID(self, name:str) -> int: ...
    def GetPartArrayName(self, arrayIdx:int) -> str: ...
    @overload
    def GetPartArrayStatus(self, index:int) -> int: ...
    @overload
    def GetPartArrayStatus(self, __a:str) -> int: ...
    def GetPartBlockInfo(self, arrayIdx:int) -> str: ...
    @staticmethod
    def GetPedigreeEdgeIdArrayName() -> str: ...
    @staticmethod
    def GetPedigreeElementIdArrayName() -> str: ...
    @staticmethod
    def GetPedigreeFaceIdArrayName() -> str: ...
    @staticmethod
    def GetPedigreeNodeIdArrayName() -> str: ...
    def GetPointResultArrayName(self, index:int) -> str: ...
    def GetPointResultArrayStatus(self, name:str) -> int: ...
    def GetSIL(self) -> 'vtkGraph': ...
    def GetSILUpdateStamp(self) -> int: ...
    def GetSideSetArrayName(self, index:int) -> str: ...
    def GetSideSetArrayStatus(self, name:str) -> int: ...
    def GetSideSetResultArrayName(self, index:int) -> str: ...
    def GetSideSetResultArrayStatus(self, name:str) -> int: ...
    @staticmethod
    def GetSideSetSourceElementIdArrayName() -> str: ...
    @staticmethod
    def GetSideSetSourceElementSideArrayName() -> str: ...
    def GetSqueezePoints(self) -> bool: ...
    def GetTimeSeriesData(self, ID:int, vName:str, vType:str, result:'vtkFloatArray') -> int: ...
    def GetTimeStep(self) -> int: ...
    def GetTimeStepRange(self) -> Tuple[int, int]: ...
    def GetTitle(self) -> str: ...
    def GetTotalNumberOfEdges(self) -> int: ...
    def GetTotalNumberOfElements(self) -> int: ...
    def GetTotalNumberOfFaces(self) -> int: ...
    def GetTotalNumberOfNodes(self) -> int: ...
    def GetUseLegacyBlockNames(self) -> bool: ...
    def GetVariableID(self, type:str, name:str) -> int: ...
    def GetXMLFileName(self) -> str: ...
    def HasModeShapesOff(self) -> None: ...
    def HasModeShapesOn(self) -> None: ...
    def IgnoreFileTimeOff(self) -> None: ...
    def IgnoreFileTimeOn(self) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def IsValidVariable(self, type:str, name:str) -> int: ...
    def NewInstance(self) -> 'vtkExodusIIReader': ...
    def Reset(self) -> None: ...
    def ResetCache(self) -> None: ...
    def ResetSettings(self) -> None: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkExodusIIReader': ...
    def SetAllArrayStatus(self, otype:int, status:int) -> None: ...
    def SetAnimateModeShapes(self, flag:int) -> None: ...
    def SetApplyDisplacements(self, d:int) -> None: ...
    @overload
    def SetAssemblyArrayStatus(self, index:int, flag:int) -> None: ...
    @overload
    def SetAssemblyArrayStatus(self, __a:str, flag:int) -> None: ...
    def SetCacheSize(self, CacheSize:float) -> None: ...
    def SetDisplacementMagnitude(self, s:float) -> None: ...
    def SetDisplayType(self, type:int) -> None: ...
    def SetEdgeBlockArrayStatus(self, name:str, flag:int) -> None: ...
    def SetEdgeMapArrayStatus(self, name:str, flag:int) -> None: ...
    def SetEdgeResultArrayStatus(self, name:str, flag:int) -> None: ...
    def SetEdgeSetArrayStatus(self, name:str, flag:int) -> None: ...
    def SetEdgeSetResultArrayStatus(self, name:str, flag:int) -> None: ...
    def SetElementBlockArrayStatus(self, name:str, flag:int) -> None: ...
    def SetElementMapArrayStatus(self, name:str, flag:int) -> None: ...
    def SetElementResultArrayStatus(self, name:str, flag:int) -> None: ...
    def SetElementSetArrayStatus(self, name:str, flag:int) -> None: ...
    def SetElementSetResultArrayStatus(self, name:str, flag:int) -> None: ...
    def SetFaceBlockArrayStatus(self, name:str, flag:int) -> None: ...
    def SetFaceMapArrayStatus(self, name:str, flag:int) -> None: ...
    def SetFaceResultArrayStatus(self, name:str, flag:int) -> None: ...
    def SetFaceSetArrayStatus(self, name:str, flag:int) -> None: ...
    def SetFaceSetResultArrayStatus(self, name:str, flag:int) -> None: ...
    def SetFileId(self, f:int) -> None: ...
    def SetFileName(self, fname:str) -> None: ...
    def SetGenerateFileIdArray(self, f:int) -> None: ...
    def SetGenerateGlobalElementIdArray(self, g:int) -> None: ...
    def SetGenerateGlobalNodeIdArray(self, g:int) -> None: ...
    def SetGenerateImplicitElementIdArray(self, g:int) -> None: ...
    def SetGenerateImplicitNodeIdArray(self, g:int) -> None: ...
    def SetGenerateObjectIdCellArray(self, g:int) -> None: ...
    def SetGlobalResultArrayStatus(self, name:str, flag:int) -> None: ...
    def SetHasModeShapes(self, ms:int) -> None: ...
    @overload
    def SetHierarchyArrayStatus(self, index:int, flag:int) -> None: ...
    @overload
    def SetHierarchyArrayStatus(self, __a:str, flag:int) -> None: ...
    def SetIgnoreFileTime(self, flag:bool) -> None: ...
    @overload
    def SetMaterialArrayStatus(self, index:int, flag:int) -> None: ...
    @overload
    def SetMaterialArrayStatus(self, __a:str, flag:int) -> None: ...
    def SetModeShape(self, val:int) -> None: ...
    def SetModeShapeTime(self, phase:float) -> None: ...
    def SetNodeMapArrayStatus(self, name:str, flag:int) -> None: ...
    def SetNodeSetArrayStatus(self, name:str, flag:int) -> None: ...
    def SetNodeSetResultArrayStatus(self, name:str, flag:int) -> None: ...
    @overload
    def SetObjectArrayStatus(self, objectType:int, arrayIndex:int, status:int) -> None: ...
    @overload
    def SetObjectArrayStatus(self, objectType:int, arrayName:str, status:int) -> None: ...
    @overload
    def SetObjectAttributeStatus(self, objectType:int, objectIndex:int, attribIndex:int, status:int) -> None: ...
    @overload
    def SetObjectAttributeStatus(self, objectType:int, objectIndex:int, attribName:str, status:int) -> None: ...
    @overload
    def SetObjectStatus(self, objectType:int, objectIndex:int, status:int) -> None: ...
    @overload
    def SetObjectStatus(self, objectType:int, objectName:str, status:int) -> None: ...
    @overload
    def SetPartArrayStatus(self, index:int, flag:int) -> None: ...
    @overload
    def SetPartArrayStatus(self, __a:str, flag:int) -> None: ...
    def SetPointResultArrayStatus(self, name:str, flag:int) -> None: ...
    def SetSideSetArrayStatus(self, name:str, flag:int) -> None: ...
    def SetSideSetResultArrayStatus(self, name:str, flag:int) -> None: ...
    def SetSqueezePoints(self, sp:bool) -> None: ...
    def SetTimeStep(self, _arg:int) -> None: ...
    def SetUseLegacyBlockNames(self, _arg:bool) -> None: ...
    def SetXMLFileName(self, fname:str) -> None: ...
    def UseLegacyBlockNamesOff(self) -> None: ...
    def UseLegacyBlockNamesOn(self) -> None: ...

class vtkExodusIIReaderParser(vtkmodules.vtkIOXMLParser.vtkXMLParser):
    def GetBlockName(self, id:int) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetSIL(self) -> 'vtkMutableDirectedGraph': ...
    def Go(self, filename:str) -> None: ...
    def HasInformationAboutBlock(self, id:int) -> bool: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkExodusIIReaderParser': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkExodusIIReaderParser': ...

class vtkExodusIIWriter(vtkmodules.vtkIOCore.vtkWriter):
    def GetBlockIdArrayName(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetGhostLevel(self) -> int: ...
    def GetIgnoreMetaDataWarning(self) -> bool: ...
    def GetModelMetadata(self) -> 'vtkModelMetadata': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetStoreDoubles(self) -> int: ...
    def GetWriteAllTimeSteps(self) -> int: ...
    def GetWriteOutBlockIdArray(self) -> int: ...
    def GetWriteOutGlobalElementIdArray(self) -> int: ...
    def GetWriteOutGlobalNodeIdArray(self) -> int: ...
    def IgnoreMetaDataWarningOff(self) -> None: ...
    def IgnoreMetaDataWarningOn(self) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkExodusIIWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkExodusIIWriter': ...
    def SetBlockIdArrayName(self, _arg:str) -> None: ...
    def SetFileName(self, _arg:str) -> None: ...
    def SetGhostLevel(self, _arg:int) -> None: ...
    def SetIgnoreMetaDataWarning(self, _arg:bool) -> None: ...
    def SetModelMetadata(self, __a:'vtkModelMetadata') -> None: ...
    def SetStoreDoubles(self, _arg:int) -> None: ...
    def SetWriteAllTimeSteps(self, _arg:int) -> None: ...
    def SetWriteOutBlockIdArray(self, _arg:int) -> None: ...
    def SetWriteOutGlobalElementIdArray(self, _arg:int) -> None: ...
    def SetWriteOutGlobalNodeIdArray(self, _arg:int) -> None: ...
    def WriteAllTimeStepsOff(self) -> None: ...
    def WriteAllTimeStepsOn(self) -> None: ...
    def WriteOutBlockIdArrayOff(self) -> None: ...
    def WriteOutBlockIdArrayOn(self) -> None: ...
    def WriteOutGlobalElementIdArrayOff(self) -> None: ...
    def WriteOutGlobalElementIdArrayOn(self) -> None: ...
    def WriteOutGlobalNodeIdArrayOff(self) -> None: ...
    def WriteOutGlobalNodeIdArrayOn(self) -> None: ...

class vtkModelMetadata(vtkmodules.vtkCommonCore.vtkObject):
    def AllVariablesDefinedInAllBlocksOff(self) -> None: ...
    def AllVariablesDefinedInAllBlocksOn(self) -> None: ...
    def FreeAllGlobalData(self) -> None: ...
    def FreeAllLocalData(self) -> None: ...
    def FreeBlockDependentData(self) -> None: ...
    def FreeOriginalElementVariableNames(self) -> None: ...
    def FreeOriginalNodeVariableNames(self) -> None: ...
    def FreeUsedElementVariableNames(self) -> None: ...
    def FreeUsedElementVariables(self) -> None: ...
    def FreeUsedNodeVariableNames(self) -> None: ...
    def FreeUsedNodeVariables(self) -> None: ...
    def GetAllVariablesDefinedInAllBlocks(self) -> int: ...
    def GetBlockAttributes(self) -> Pointer: ...
    def GetBlockAttributesIndex(self) -> Pointer: ...
    def GetBlockElementIdList(self) -> Pointer: ...
    def GetBlockElementIdListIndex(self) -> Pointer: ...
    def GetBlockIds(self) -> Pointer: ...
    def GetBlockNodesPerElement(self) -> Pointer: ...
    def GetBlockNumberOfAttributesPerElement(self) -> Pointer: ...
    def GetBlockNumberOfElements(self) -> Pointer: ...
    def GetBlockPropertyValue(self) -> Pointer: ...
    def GetDimension(self) -> int: ...
    def GetElementVariableNumberOfComponents(self) -> Pointer: ...
    def GetElementVariableTruthTable(self) -> Pointer: ...
    def GetGlobalVariableValue(self) -> Pointer: ...
    def GetMapToOriginalElementVariableNames(self) -> Pointer: ...
    def GetMapToOriginalNodeVariableNames(self) -> Pointer: ...
    def GetNodeSetDistributionFactorIndex(self) -> Pointer: ...
    def GetNodeSetDistributionFactors(self) -> Pointer: ...
    def GetNodeSetIds(self) -> Pointer: ...
    def GetNodeSetNames(self) -> 'vtkStringArray': ...
    def GetNodeSetNodeIdList(self) -> Pointer: ...
    def GetNodeSetNodeIdListIndex(self) -> Pointer: ...
    def GetNodeSetNumberOfDistributionFactors(self) -> Pointer: ...
    def GetNodeSetPropertyValue(self) -> Pointer: ...
    def GetNodeSetSize(self) -> Pointer: ...
    def GetNodeVariableNumberOfComponents(self) -> Pointer: ...
    def GetNumberOfBlockProperties(self) -> int: ...
    def GetNumberOfBlocks(self) -> int: ...
    def GetNumberOfElementVariables(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfGlobalVariables(self) -> int: ...
    def GetNumberOfInformationLines(self) -> int: ...
    def GetNumberOfNodeSetProperties(self) -> int: ...
    def GetNumberOfNodeSets(self) -> int: ...
    def GetNumberOfNodeVariables(self) -> int: ...
    def GetNumberOfSideSetProperties(self) -> int: ...
    def GetNumberOfSideSets(self) -> int: ...
    def GetNumberOfTimeSteps(self) -> int: ...
    def GetOriginalNumberOfElementVariables(self) -> int: ...
    def GetOriginalNumberOfNodeVariables(self) -> int: ...
    def GetSideSetDistributionFactorIndex(self) -> Pointer: ...
    def GetSideSetDistributionFactors(self) -> Pointer: ...
    def GetSideSetElementList(self) -> Pointer: ...
    def GetSideSetIds(self) -> Pointer: ...
    def GetSideSetListIndex(self) -> Pointer: ...
    def GetSideSetNames(self) -> 'vtkStringArray': ...
    def GetSideSetNumDFPerSide(self) -> Pointer: ...
    def GetSideSetNumberOfDistributionFactors(self) -> Pointer: ...
    def GetSideSetPropertyValue(self) -> Pointer: ...
    def GetSideSetSideList(self) -> Pointer: ...
    def GetSideSetSize(self) -> Pointer: ...
    def GetSizeBlockAttributeArray(self) -> int: ...
    def GetSumDistFactPerNodeSet(self) -> int: ...
    def GetSumDistFactPerSideSet(self) -> int: ...
    def GetSumElementsPerBlock(self) -> int: ...
    def GetSumNodesPerNodeSet(self) -> int: ...
    def GetSumSidesPerSideSet(self) -> int: ...
    def GetTimeStepIndex(self) -> int: ...
    def GetTimeStepValues(self) -> Pointer: ...
    def GetTitle(self) -> str: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkModelMetadata': ...
    def PrintGlobalInformation(self) -> None: ...
    def PrintLocalInformation(self) -> None: ...
    def Reset(self) -> None: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkModelMetadata': ...
    def SetAllVariablesDefinedInAllBlocks(self, _arg:int) -> None: ...
    def SetBlockAttributes(self, __a:MutableSequence[float]) -> None: ...
    def SetBlockElementIdList(self, __a:MutableSequence[int]) -> None: ...
    def SetBlockIds(self, __a:MutableSequence[int]) -> None: ...
    def SetBlockNodesPerElement(self, __a:MutableSequence[int]) -> None: ...
    def SetBlockNumberOfAttributesPerElement(self, natts:MutableSequence[int]) -> int: ...
    def SetBlockNumberOfElements(self, nelts:MutableSequence[int]) -> int: ...
    def SetBlockPropertyValue(self, __a:MutableSequence[int]) -> None: ...
    def SetElementVariableTruthTable(self, __a:MutableSequence[int]) -> None: ...
    def SetGlobalVariableValue(self, f:MutableSequence[float]) -> None: ...
    def SetNodeSetDistributionFactors(self, __a:MutableSequence[float]) -> None: ...
    def SetNodeSetIds(self, __a:MutableSequence[int]) -> None: ...
    def SetNodeSetNames(self, names:'vtkStringArray') -> None: ...
    def SetNodeSetNodeIdList(self, __a:MutableSequence[int]) -> None: ...
    def SetNodeSetNumberOfDistributionFactors(self, __a:MutableSequence[int]) -> None: ...
    def SetNodeSetPropertyValue(self, __a:MutableSequence[int]) -> None: ...
    def SetNodeSetSize(self, __a:MutableSequence[int]) -> None: ...
    def SetNumberOfBlocks(self, _arg:int) -> None: ...
    def SetNumberOfNodeSets(self, _arg:int) -> None: ...
    def SetNumberOfSideSets(self, _arg:int) -> None: ...
    def SetSideSetDistributionFactors(self, __a:MutableSequence[float]) -> None: ...
    def SetSideSetElementList(self, __a:MutableSequence[int]) -> None: ...
    def SetSideSetIds(self, __a:MutableSequence[int]) -> None: ...
    def SetSideSetNames(self, names:'vtkStringArray') -> None: ...
    def SetSideSetNumDFPerSide(self, numNodes:MutableSequence[int]) -> None: ...
    def SetSideSetNumberOfDistributionFactors(self, df:MutableSequence[int]) -> int: ...
    def SetSideSetPropertyValue(self, __a:MutableSequence[int]) -> None: ...
    def SetSideSetSideList(self, __a:MutableSequence[int]) -> None: ...
    def SetSideSetSize(self, sizes:MutableSequence[int]) -> int: ...
    def SetSumNodesPerNodeSet(self, _arg:int) -> None: ...
    def SetSumSidesPerSideSet(self, _arg:int) -> None: ...
    def SetTimeStepIndex(self, _arg:int) -> None: ...
    def SetTimeSteps(self, numberOfTimeSteps:int, timeStepValues:MutableSequence[float]) -> None: ...
    def SetTitle(self, _arg:str) -> None: ...

