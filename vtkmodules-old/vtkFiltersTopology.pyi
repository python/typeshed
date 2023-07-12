from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

class vtkFiberSurface(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    class BaseVertexType(int): ...
    class ClipVertexType(int): ...
    bv_edge_01:'BaseVertexType'
    bv_edge_02:'BaseVertexType'
    bv_edge_03:'BaseVertexType'
    bv_edge_12:'BaseVertexType'
    bv_edge_13:'BaseVertexType'
    bv_edge_23:'BaseVertexType'
    bv_not_used:'BaseVertexType'
    bv_vertex_0:'BaseVertexType'
    bv_vertex_1:'BaseVertexType'
    bv_vertex_2:'BaseVertexType'
    bv_vertex_3:'BaseVertexType'
    edge_0_parm_0:'ClipVertexType'
    edge_0_parm_1:'ClipVertexType'
    edge_1_parm_0:'ClipVertexType'
    edge_1_parm_1:'ClipVertexType'
    edge_2_parm_0:'ClipVertexType'
    edge_2_parm_1:'ClipVertexType'
    not_used:'ClipVertexType'
    vertex_0:'ClipVertexType'
    vertex_1:'ClipVertexType'
    vertex_2:'ClipVertexType'
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkFiberSurface': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkFiberSurface': ...
    def SetField1(self, fieldName:str) -> None: ...
    def SetField2(self, fieldName:str) -> None: ...

