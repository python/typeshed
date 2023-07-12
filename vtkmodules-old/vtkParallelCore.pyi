from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore

class vtkCommunicator(vtkmodules.vtkCommonCore.vtkObject):
    class Tags(int): ...
    class StandardOperations(int): ...
    BARRIER_TAG:'Tags'
    BITWISE_AND_OP:'StandardOperations'
    BITWISE_OR_OP:'StandardOperations'
    BITWISE_XOR_OP:'StandardOperations'
    BROADCAST_TAG:'Tags'
    GATHERV_TAG:'Tags'
    GATHER_TAG:'Tags'
    LOGICAL_AND_OP:'StandardOperations'
    LOGICAL_OR_OP:'StandardOperations'
    LOGICAL_XOR_OP:'StandardOperations'
    MAX_OP:'StandardOperations'
    MIN_OP:'StandardOperations'
    PRODUCT_OP:'StandardOperations'
    REDUCE_TAG:'Tags'
    SCATTERV_TAG:'Tags'
    SCATTER_TAG:'Tags'
    SUM_OP:'StandardOperations'
    @overload
    def AllGather(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], length:int) -> int: ...
    @overload
    def AllGather(self, sendBuffer:str, recvBuffer:str, length:int) -> int: ...
    @overload
    def AllGather(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], length:int) -> int: ...
    @overload
    def AllGather(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray') -> int: ...
    @overload
    def AllGather(self, sendBuffer:'vtkDataObject', recvBuffer:MutableSequence['vtkDataObject']) -> int: ...
    @overload
    def AllGatherV(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int]) -> int: ...
    @overload
    def AllGatherV(self, sendBuffer:str, recvBuffer:str, sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int]) -> int: ...
    @overload
    def AllGatherV(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int]) -> int: ...
    @overload
    def AllGatherV(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray', recvLengths:MutableSequence[int], offsets:MutableSequence[int]) -> int: ...
    @overload
    def AllGatherV(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray') -> int: ...
    def AllGatherVVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int], type:int) -> int: ...
    def AllGatherVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, length:int, type:int) -> int: ...
    @overload
    def AllReduce(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], length:int, operation:int) -> int: ...
    @overload
    def AllReduce(self, sendBuffer:str, recvBuffer:str, length:int, operation:int) -> int: ...
    @overload
    def AllReduce(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], length:int, operation:int) -> int: ...
    @overload
    def AllReduce(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray', operation:int) -> int: ...
    def AllReduceVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, length:int, type:int, operation:int) -> int: ...
    def Barrier(self) -> None: ...
    @overload
    def Broadcast(self, data:MutableSequence[int], length:int, srcProcessId:int) -> int: ...
    @overload
    def Broadcast(self, data:str, length:int, srcProcessId:int) -> int: ...
    @overload
    def Broadcast(self, data:MutableSequence[float], length:int, srcProcessId:int) -> int: ...
    @overload
    def Broadcast(self, data:'vtkDataObject', srcProcessId:int) -> int: ...
    @overload
    def Broadcast(self, data:'vtkDataArray', srcProcessId:int) -> int: ...
    @overload
    def Broadcast(self, stream:'vtkMultiProcessStream', srcProcessId:int) -> int: ...
    def BroadcastVoidArray(self, data:Pointer, length:int, type:int, srcProcessId:int) -> int: ...
    @overload
    def Gather(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], length:int, destProcessId:int) -> int: ...
    @overload
    def Gather(self, sendBuffer:str, recvBuffer:str, length:int, destProcessId:int) -> int: ...
    @overload
    def Gather(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], length:int, destProcessId:int) -> int: ...
    @overload
    def Gather(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray', destProcessId:int) -> int: ...
    @overload
    def Gather(self, sendBuffer:'vtkDataObject', recvBuffer:MutableSequence['vtkDataObject'], destProcessId:int) -> int: ...
    @overload
    def GatherV(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int], destProcessId:int) -> int: ...
    @overload
    def GatherV(self, sendBuffer:str, recvBuffer:str, sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int], destProcessId:int) -> int: ...
    @overload
    def GatherV(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int], destProcessId:int) -> int: ...
    @overload
    def GatherV(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray', recvLengths:MutableSequence[int], offsets:MutableSequence[int], destProcessId:int) -> int: ...
    def GatherVVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int], type:int, destProcessId:int) -> int: ...
    def GatherVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, length:int, type:int, destProcessId:int) -> int: ...
    def GetCount(self) -> int: ...
    @staticmethod
    def GetLeftChildProcessor(pid:int) -> int: ...
    def GetLocalProcessId(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfProcesses(self) -> int: ...
    @staticmethod
    def GetParentProcessor(pid:int) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    @staticmethod
    def MarshalDataObject(object:'vtkDataObject', buffer:'vtkCharArray') -> int: ...
    def NewInstance(self) -> 'vtkCommunicator': ...
    @overload
    def Receive(self, data:'vtkDataObject', remoteHandle:int, tag:int) -> int: ...
    @overload
    def Receive(self, data:'vtkDataArray', remoteHandle:int, tag:int) -> int: ...
    @overload
    def Receive(self, data:MutableSequence[int], maxlength:int, remoteHandle:int, tag:int) -> int: ...
    @overload
    def Receive(self, data:str, maxlength:int, remoteHandle:int, tag:int) -> int: ...
    @overload
    def Receive(self, data:MutableSequence[float], maxlength:int, remoteHandle:int, tag:int) -> int: ...
    @overload
    def Receive(self, stream:'vtkMultiProcessStream', remoteId:int, tag:int) -> int: ...
    def ReceiveDataObject(self, remoteHandle:int, tag:int) -> 'vtkDataObject': ...
    def ReceiveVoidArray(self, data:Pointer, maxlength:int, type:int, remoteHandle:int, tag:int) -> int: ...
    @overload
    def Reduce(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], length:int, operation:int, destProcessId:int) -> int: ...
    @overload
    def Reduce(self, sendBuffer:str, recvBuffer:str, length:int, operation:int, destProcessId:int) -> int: ...
    @overload
    def Reduce(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], length:int, operation:int, destProcessId:int) -> int: ...
    @overload
    def Reduce(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray', operation:int, destProcessId:int) -> int: ...
    def ReduceVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, length:int, type:int, operation:int, destProcessId:int) -> int: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkCommunicator': ...
    @overload
    def Scatter(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], length:int, srcProcessId:int) -> int: ...
    @overload
    def Scatter(self, sendBuffer:str, recvBuffer:str, length:int, srcProcessId:int) -> int: ...
    @overload
    def Scatter(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], length:int, srcProcessId:int) -> int: ...
    @overload
    def Scatter(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray', srcProcessId:int) -> int: ...
    @overload
    def ScatterV(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], sendLengths:MutableSequence[int], offsets:MutableSequence[int], recvLength:int, srcProcessId:int) -> int: ...
    @overload
    def ScatterV(self, sendBuffer:str, recvBuffer:str, sendLengths:MutableSequence[int], offsets:MutableSequence[int], recvLength:int, srcProcessId:int) -> int: ...
    @overload
    def ScatterV(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], sendLengths:MutableSequence[int], offsets:MutableSequence[int], recvLength:int, srcProcessId:int) -> int: ...
    def ScatterVVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, sendLengths:MutableSequence[int], offsets:MutableSequence[int], recvLength:int, type:int, srcProcessId:int) -> int: ...
    def ScatterVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, length:int, type:int, srcProcessId:int) -> int: ...
    @overload
    def Send(self, data:'vtkDataObject', remoteHandle:int, tag:int) -> int: ...
    @overload
    def Send(self, data:'vtkDataArray', remoteHandle:int, tag:int) -> int: ...
    @overload
    def Send(self, data:Sequence[int], length:int, remoteHandle:int, tag:int) -> int: ...
    @overload
    def Send(self, data:str, length:int, remoteHandle:int, tag:int) -> int: ...
    @overload
    def Send(self, data:Sequence[float], length:int, remoteHandle:int, tag:int) -> int: ...
    @overload
    def Send(self, stream:'vtkMultiProcessStream', remoteId:int, tag:int) -> int: ...
    def SendVoidArray(self, data:Pointer, length:int, type:int, remoteHandle:int, tag:int) -> int: ...
    def SetNumberOfProcesses(self, num:int) -> None: ...
    @staticmethod
    def SetUseCopy(useCopy:int) -> None: ...
    @overload
    @staticmethod
    def UnMarshalDataObject(buffer:'vtkCharArray', object:'vtkDataObject') -> int: ...
    @overload
    @staticmethod
    def UnMarshalDataObject(buffer:'vtkCharArray') -> 'vtkDataObject': ...

class vtkDummyCommunicator(vtkCommunicator):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkDummyCommunicator': ...
    def ReceiveVoidArray(self, __a:Pointer, __b:int, __c:int, __d:int, __e:int) -> int: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkDummyCommunicator': ...
    def SendVoidArray(self, __a:Pointer, __b:int, __c:int, __d:int, __e:int) -> int: ...

class vtkMultiProcessController(vtkmodules.vtkCommonCore.vtkObject):
    class Consts(int): ...
    class Tags(int): ...
    class Errors(int): ...
    ANY_SOURCE:'Consts'
    BREAK_RMI_TAG:'Tags'
    INVALID_SOURCE:'Consts'
    RMI_ARG_ERROR:'Errors'
    RMI_ARG_TAG:'Tags'
    RMI_NO_ERROR:'Errors'
    RMI_TAG:'Tags'
    RMI_TAG_ERROR:'Errors'
    XML_WRITER_DATA_INFO:'Tags'
    @overload
    def AllGather(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], length:int) -> int: ...
    @overload
    def AllGather(self, sendBuffer:str, recvBuffer:str, length:int) -> int: ...
    @overload
    def AllGather(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], length:int) -> int: ...
    @overload
    def AllGather(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray') -> int: ...
    @overload
    def AllGather(self, sendBuffer:'vtkDataObject', recvBuffer:MutableSequence['vtkDataObject']) -> int: ...
    @overload
    def AllGatherV(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int]) -> int: ...
    @overload
    def AllGatherV(self, sendBuffer:str, recvBuffer:str, sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int]) -> int: ...
    @overload
    def AllGatherV(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int]) -> int: ...
    @overload
    def AllGatherV(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray', recvLengths:MutableSequence[int], offsets:MutableSequence[int]) -> int: ...
    @overload
    def AllGatherV(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray') -> int: ...
    @overload
    def AllReduce(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], length:int, operation:int) -> int: ...
    @overload
    def AllReduce(self, sendBuffer:str, recvBuffer:str, length:int, operation:int) -> int: ...
    @overload
    def AllReduce(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], length:int, operation:int) -> int: ...
    @overload
    def AllReduce(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray', operation:int) -> int: ...
    @overload
    def AllReduce(self, sendBuffer:'vtkBoundingBox', recvBuffer:'vtkBoundingBox') -> int: ...
    @overload
    def AllReduce(self, sendBuffer:'vtkDataArraySelection', recvBuffer:'vtkDataArraySelection') -> int: ...
    def Barrier(self) -> None: ...
    @overload
    def Broadcast(self, data:MutableSequence[int], length:int, srcProcessId:int) -> int: ...
    @overload
    def Broadcast(self, data:str, length:int, srcProcessId:int) -> int: ...
    @overload
    def Broadcast(self, data:MutableSequence[float], length:int, srcProcessId:int) -> int: ...
    @overload
    def Broadcast(self, data:'vtkDataObject', srcProcessId:int) -> int: ...
    @overload
    def Broadcast(self, data:'vtkDataArray', srcProcessId:int) -> int: ...
    @overload
    def Broadcast(self, stream:'vtkMultiProcessStream', srcProcessId:int) -> int: ...
    def BroadcastProcessRMIs(self, reportErrors:int, dont_loop:int=0) -> int: ...
    def BroadcastTriggerRMIOff(self) -> None: ...
    def BroadcastTriggerRMIOn(self) -> None: ...
    def BroadcastTriggerRMIOnAllChildren(self, arg:Pointer, argLength:int, tag:int) -> None: ...
    def CreateOutputWindow(self) -> None: ...
    def CreateSubController(self, group:'vtkProcessGroup') -> 'vtkMultiProcessController': ...
    @overload
    def Finalize(self) -> None: ...
    @overload
    def Finalize(self, finalizedExternally:int) -> None: ...
    @overload
    def Gather(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], length:int, destProcessId:int) -> int: ...
    @overload
    def Gather(self, sendBuffer:str, recvBuffer:str, length:int, destProcessId:int) -> int: ...
    @overload
    def Gather(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], length:int, destProcessId:int) -> int: ...
    @overload
    def Gather(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray', destProcessId:int) -> int: ...
    @overload
    def Gather(self, sendBuffer:'vtkDataObject', recvBuffer:MutableSequence['vtkDataObject'], destProcessId:int) -> int: ...
    @overload
    def GatherV(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int], destProcessId:int) -> int: ...
    @overload
    def GatherV(self, sendBuffer:str, recvBuffer:str, sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int], destProcessId:int) -> int: ...
    @overload
    def GatherV(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int], destProcessId:int) -> int: ...
    @overload
    def GatherV(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray', recvLengths:MutableSequence[int], offsets:MutableSequence[int], destProcessId:int) -> int: ...
    def GetBreakFlag(self) -> int: ...
    @staticmethod
    def GetBreakRMITag() -> int: ...
    def GetBroadcastTriggerRMI(self) -> bool: ...
    def GetCommunicator(self) -> 'vtkCommunicator': ...
    def GetCount(self) -> int: ...
    @staticmethod
    def GetGlobalController() -> 'vtkMultiProcessController': ...
    def GetLocalProcessId(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfProcesses(self) -> int: ...
    @staticmethod
    def GetRMIArgTag() -> int: ...
    @staticmethod
    def GetRMITag() -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def MultipleMethodExecute(self) -> None: ...
    def NewInstance(self) -> 'vtkMultiProcessController': ...
    def PartitionController(self, localColor:int, localKey:int) -> 'vtkMultiProcessController': ...
    @overload
    def ProcessRMIs(self, reportErrors:int, dont_loop:int=0) -> int: ...
    @overload
    def ProcessRMIs(self) -> int: ...
    @overload
    def Receive(self, data:MutableSequence[int], maxlength:int, remoteProcessId:int, tag:int) -> int: ...
    @overload
    def Receive(self, data:str, maxlength:int, remoteProcessId:int, tag:int) -> int: ...
    @overload
    def Receive(self, data:MutableSequence[float], maxlength:int, remoteProcessId:int, tag:int) -> int: ...
    @overload
    def Receive(self, data:MutableSequence[int], maxLength:int, remoteProcessId:int, tag:int) -> int: ...
    @overload
    def Receive(self, data:'vtkDataObject', remoteId:int, tag:int) -> int: ...
    @overload
    def Receive(self, data:'vtkDataArray', remoteId:int, tag:int) -> int: ...
    @overload
    def Receive(self, stream:'vtkMultiProcessStream', remoteId:int, tag:int) -> int: ...
    def ReceiveDataObject(self, remoteId:int, tag:int) -> 'vtkDataObject': ...
    @overload
    def Reduce(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], length:int, operation:int, destProcessId:int) -> int: ...
    @overload
    def Reduce(self, sendBuffer:str, recvBuffer:str, length:int, operation:int, destProcessId:int) -> int: ...
    @overload
    def Reduce(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], length:int, operation:int, destProcessId:int) -> int: ...
    @overload
    def Reduce(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray', operation:int, destProcessId:int) -> int: ...
    @overload
    def Reduce(self, sendBuffer:'vtkBoundingBox', recvBuffer:'vtkBoundingBox', destProcessId:int) -> int: ...
    @overload
    def Reduce(self, sendBuffer:'vtkDataArraySelection', recvBuffer:'vtkDataArraySelection', destProcessId:int) -> int: ...
    def RemoveAllRMICallbacks(self, tag:int) -> None: ...
    def RemoveFirstRMI(self, tag:int) -> int: ...
    def RemoveRMI(self, id:int) -> int: ...
    def RemoveRMICallback(self, id:int) -> bool: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkMultiProcessController': ...
    @overload
    def Scatter(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], length:int, srcProcessId:int) -> int: ...
    @overload
    def Scatter(self, sendBuffer:str, recvBuffer:str, length:int, srcProcessId:int) -> int: ...
    @overload
    def Scatter(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], length:int, srcProcessId:int) -> int: ...
    @overload
    def Scatter(self, sendBuffer:'vtkDataArray', recvBuffer:'vtkDataArray', srcProcessId:int) -> int: ...
    @overload
    def ScatterV(self, sendBuffer:Sequence[int], recvBuffer:MutableSequence[int], sendLengths:MutableSequence[int], offsets:MutableSequence[int], recvLength:int, srcProcessId:int) -> int: ...
    @overload
    def ScatterV(self, sendBuffer:str, recvBuffer:str, sendLengths:MutableSequence[int], offsets:MutableSequence[int], recvLength:int, srcProcessId:int) -> int: ...
    @overload
    def ScatterV(self, sendBuffer:Sequence[float], recvBuffer:MutableSequence[float], sendLengths:MutableSequence[int], offsets:MutableSequence[int], recvLength:int, srcProcessId:int) -> int: ...
    @overload
    def Send(self, data:Sequence[int], length:int, remoteProcessId:int, tag:int) -> int: ...
    @overload
    def Send(self, data:str, length:int, remoteProcessId:int, tag:int) -> int: ...
    @overload
    def Send(self, data:Sequence[float], length:int, remoteProcessId:int, tag:int) -> int: ...
    @overload
    def Send(self, data:'vtkDataObject', remoteId:int, tag:int) -> int: ...
    @overload
    def Send(self, data:'vtkDataArray', remoteId:int, tag:int) -> int: ...
    @overload
    def Send(self, stream:'vtkMultiProcessStream', remoteId:int, tag:int) -> int: ...
    def SetBreakFlag(self, _arg:int) -> None: ...
    def SetBroadcastTriggerRMI(self, _arg:bool) -> None: ...
    @staticmethod
    def SetGlobalController(controller:'vtkMultiProcessController') -> None: ...
    def SetNumberOfProcesses(self, num:int) -> None: ...
    def SetSingleProcessObject(self, p:'vtkProcess') -> None: ...
    def SingleMethodExecute(self) -> None: ...
    def TriggerBreakRMIs(self) -> None: ...
    @overload
    def TriggerRMI(self, remoteProcessId:int, arg:Pointer, argLength:int, tag:int) -> None: ...
    @overload
    def TriggerRMI(self, remoteProcessId:int, arg:str, tag:int) -> None: ...
    @overload
    def TriggerRMI(self, remoteProcessId:int, tag:int) -> None: ...
    @overload
    def TriggerRMIOnAllChildren(self, arg:Pointer, argLength:int, tag:int) -> None: ...
    @overload
    def TriggerRMIOnAllChildren(self, arg:str, tag:int) -> None: ...
    @overload
    def TriggerRMIOnAllChildren(self, tag:int) -> None: ...

class vtkDummyController(vtkMultiProcessController):
    def CreateOutputWindow(self) -> None: ...
    @overload
    def Finalize(self) -> None: ...
    @overload
    def Finalize(self, __a:int) -> None: ...
    def GetLocalProcessId(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetRMICommunicator(self) -> 'vtkCommunicator': ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def MultipleMethodExecute(self) -> None: ...
    def NewInstance(self) -> 'vtkDummyController': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkDummyController': ...
    def SetCommunicator(self, __a:'vtkCommunicator') -> None: ...
    def SetRMICommunicator(self, __a:'vtkCommunicator') -> None: ...
    def SingleMethodExecute(self) -> None: ...

class vtkFieldDataSerializer(vtkmodules.vtkCommonCore.vtkObject):
    @staticmethod
    def DeSerializeToSubExtent(subext:MutableSequence[int], gridExtent:MutableSequence[int], fieldData:'vtkFieldData', bytestream:'vtkMultiProcessStream') -> None: ...
    @staticmethod
    def Deserialize(bytestream:'vtkMultiProcessStream', fieldData:'vtkFieldData') -> None: ...
    @staticmethod
    def DeserializeMetaData(bytestream:'vtkMultiProcessStream', names:'vtkStringArray', datatypes:'vtkIntArray', dimensions:'vtkIntArray') -> None: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkFieldDataSerializer': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkFieldDataSerializer': ...
    @staticmethod
    def Serialize(fieldData:'vtkFieldData', bytestream:'vtkMultiProcessStream') -> None: ...
    @staticmethod
    def SerializeMetaData(fieldData:'vtkFieldData', bytestream:'vtkMultiProcessStream') -> None: ...
    @staticmethod
    def SerializeSubExtent(subext:MutableSequence[int], gridExtent:MutableSequence[int], fieldData:'vtkFieldData', bytestream:'vtkMultiProcessStream') -> None: ...
    @staticmethod
    def SerializeTuples(tupleIds:'vtkIdList', fieldData:'vtkFieldData', bytestream:'vtkMultiProcessStream') -> None: ...

class vtkMultiProcessStream(object):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __a:'vtkMultiProcessStream') -> None: ...
    def Empty(self) -> bool: ...
    @overload
    def GetRawData(self, data:MutableSequence[int]) -> None: ...
    @overload
    def GetRawData(self, data:MutableSequence[int], size:int) -> None: ...
    @overload
    def GetRawData(self) -> Tuple[int, int]: ...
    @overload
    def Pop(self, array:MutableSequence[float], size:int) -> None: ...
    @overload
    def Pop(self, array:MutableSequence[int], size:int) -> None: ...
    @overload
    def Push(self, array:MutableSequence[float], size:int) -> None: ...
    @overload
    def Push(self, array:MutableSequence[int], size:int) -> None: ...
    @overload
    def Push(self, array:str, size:int) -> None: ...
    def RawSize(self) -> int: ...
    def Reset(self) -> None: ...
    @overload
    def SetRawData(self, data:Sequence[int]) -> None: ...
    @overload
    def SetRawData(self, __a:Sequence[int], size:int) -> None: ...
    def Size(self) -> int: ...

class vtkPDirectory(vtkmodules.vtkCommonCore.vtkObject):
    def Clear(self) -> None: ...
    @staticmethod
    def DeleteDirectory(dir:str) -> int: ...
    def FileIsDirectory(self, name:str) -> int: ...
    @staticmethod
    def GetCurrentWorkingDirectory(buf:str, len:int) -> str: ...
    def GetFile(self, index:int) -> str: ...
    def GetFiles(self) -> 'vtkStringArray': ...
    def GetNumberOfFiles(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetPath(self) -> str: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def Load(self, __a:str) -> bool: ...
    @staticmethod
    def MakeDirectory(dir:str) -> int: ...
    def NewInstance(self) -> 'vtkPDirectory': ...
    def Open(self, dir:str) -> int: ...
    @staticmethod
    def Rename(oldname:str, newname:str) -> int: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPDirectory': ...

class vtkPSystemTools(vtkmodules.vtkCommonCore.vtkObject):
    @staticmethod
    def BroadcastString(__a:str, proc:int) -> None: ...
    @overload
    @staticmethod
    def CollapseFullPath(in_relative:str) -> str: ...
    @overload
    @staticmethod
    def CollapseFullPath(in_relative:str, in_base:str) -> str: ...
    @overload
    @staticmethod
    def FileExists(filename:str, isFile:bool) -> bool: ...
    @overload
    @staticmethod
    def FileExists(filename:str) -> bool: ...
    @staticmethod
    def FileIsDirectory(name:str) -> bool: ...
    @staticmethod
    def FindProgramPath(argv0:str, pathOut:str, errorMsg:str, exeName:str=..., buildDir:str=..., installPrefix:str=...) -> bool: ...
    @staticmethod
    def GetCurrentWorkingDirectory(collapse:bool=True) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    @staticmethod
    def GetProgramPath(__a:str) -> str: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkPSystemTools': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPSystemTools': ...

class vtkProcess(vtkmodules.vtkCommonCore.vtkObject):
    def Execute(self) -> None: ...
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetReturnValue(self) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkProcess': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkProcess': ...
    def SetController(self, aController:'vtkMultiProcessController') -> None: ...

class vtkProcessGroup(vtkmodules.vtkCommonCore.vtkObject):
    def AddProcessId(self, processId:int) -> int: ...
    def Copy(self, group:'vtkProcessGroup') -> None: ...
    def FindProcessId(self, processId:int) -> int: ...
    def GetCommunicator(self) -> 'vtkCommunicator': ...
    def GetLocalProcessId(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfProcessIds(self) -> int: ...
    def GetProcessId(self, pos:int) -> int: ...
    @overload
    def Initialize(self, controller:'vtkMultiProcessController') -> None: ...
    @overload
    def Initialize(self, communicator:'vtkCommunicator') -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkProcessGroup': ...
    def RemoveAllProcessIds(self) -> None: ...
    def RemoveProcessId(self, processId:int) -> int: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkProcessGroup': ...
    def SetCommunicator(self, communicator:'vtkCommunicator') -> None: ...

class vtkSocketCommunicator(vtkCommunicator):
    def AllGatherVVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int], type:int) -> int: ...
    def AllGatherVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, length:int, type:int) -> int: ...
    def AllReduceVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, length:int, type:int, operation:int) -> int: ...
    def Barrier(self) -> None: ...
    def BroadcastVoidArray(self, data:Pointer, length:int, type:int, srcProcessId:int) -> int: ...
    def BufferCurrentMessage(self) -> None: ...
    def ClientSideHandshake(self) -> int: ...
    def CloseConnection(self) -> None: ...
    def ConnectTo(self, hostName:str, port:int) -> int: ...
    def GatherVVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, sendLength:int, recvLengths:MutableSequence[int], offsets:MutableSequence[int], type:int, destProcessId:int) -> int: ...
    def GatherVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, length:int, type:int, destProcessId:int) -> int: ...
    def GetIsConnected(self) -> int: ...
    def GetIsServer(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetPerformHandshake(self) -> int: ...
    def GetPerformHandshakeMaxValue(self) -> int: ...
    def GetPerformHandshakeMinValue(self) -> int: ...
    def GetReportErrors(self) -> int: ...
    def GetSocket(self) -> 'vtkClientSocket': ...
    def GetSwapBytesInReceivedData(self) -> int: ...
    @staticmethod
    def GetVersion() -> int: ...
    def Handshake(self) -> int: ...
    def HasBufferredMessages(self) -> bool: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    @overload
    def LogToFile(self, name:str) -> int: ...
    @overload
    def LogToFile(self, name:str, append:int) -> int: ...
    def NewInstance(self) -> 'vtkSocketCommunicator': ...
    def PerformHandshakeOff(self) -> None: ...
    def PerformHandshakeOn(self) -> None: ...
    def ReceiveVoidArray(self, data:Pointer, length:int, type:int, remoteHandle:int, tag:int) -> int: ...
    def ReduceVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, length:int, type:int, operation:int, destProcessId:int) -> int: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkSocketCommunicator': ...
    def ScatterVVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, sendLengths:MutableSequence[int], offsets:MutableSequence[int], recvLength:int, type:int, srcProcessId:int) -> int: ...
    def ScatterVoidArray(self, sendBuffer:Pointer, recvBuffer:Pointer, length:int, type:int, srcProcessId:int) -> int: ...
    def SendVoidArray(self, data:Pointer, length:int, type:int, remoteHandle:int, tag:int) -> int: ...
    def ServerSideHandshake(self) -> int: ...
    def SetNumberOfProcesses(self, num:int) -> None: ...
    def SetPerformHandshake(self, _arg:int) -> None: ...
    def SetReportErrors(self, _arg:int) -> None: ...
    def SetSocket(self, __a:'vtkClientSocket') -> None: ...
    @overload
    def WaitForConnection(self, port:int) -> int: ...
    @overload
    def WaitForConnection(self, socket:'vtkServerSocket', msec:int=0) -> int: ...

class vtkSocketController(vtkMultiProcessController):
    class Consts(int): ...
    ENDIAN_TAG:'Consts'
    HASH_TAG:'Consts'
    IDTYPESIZE_TAG:'Consts'
    VERSION_TAG:'Consts'
    def CloseConnection(self) -> None: ...
    def ConnectTo(self, hostName:str, port:int) -> int: ...
    def CreateCompliantController(self) -> 'vtkMultiProcessController': ...
    def CreateOutputWindow(self) -> None: ...
    @overload
    def Finalize(self) -> None: ...
    @overload
    def Finalize(self, __a:int) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetSwapBytesInReceivedData(self) -> int: ...
    def Initialize(self) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def MultipleMethodExecute(self) -> None: ...
    def NewInstance(self) -> 'vtkSocketController': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkSocketController': ...
    def SetCommunicator(self, comm:'vtkSocketCommunicator') -> None: ...
    def SingleMethodExecute(self) -> None: ...
    def WaitForConnection(self, port:int) -> int: ...

class vtkSubCommunicator(vtkCommunicator):
    def GetGroup(self) -> 'vtkProcessGroup': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkSubCommunicator': ...
    def ReceiveVoidArray(self, data:Pointer, length:int, type:int, remoteHandle:int, tag:int) -> int: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkSubCommunicator': ...
    def SendVoidArray(self, data:Pointer, length:int, type:int, remoteHandle:int, tag:int) -> int: ...
    def SetGroup(self, group:'vtkProcessGroup') -> None: ...

class vtkSubGroup(vtkmodules.vtkCommonCore.vtkObject):
    MAXOP:int
    MINOP:int
    SUMOP:int
    def Barrier(self) -> int: ...
    @overload
    def Broadcast(self, data:MutableSequence[float], length:int, root:int) -> int: ...
    @overload
    def Broadcast(self, data:MutableSequence[int], length:int, root:int) -> int: ...
    @overload
    def Broadcast(self, data:str, length:int, root:int) -> int: ...
    @overload
    def Gather(self, data:MutableSequence[int], to:MutableSequence[int], length:int, root:int) -> int: ...
    @overload
    def Gather(self, data:str, to:str, length:int, root:int) -> int: ...
    @overload
    def Gather(self, data:MutableSequence[float], to:MutableSequence[float], length:int, root:int) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def Initialize(self, p0:int, p1:int, me:int, tag:int, c:'vtkCommunicator') -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkSubGroup': ...
    def PrintSubGroup(self) -> None: ...
    @overload
    def ReduceMax(self, data:MutableSequence[float], to:MutableSequence[float], length:int, root:int) -> int: ...
    @overload
    def ReduceMax(self, data:MutableSequence[int], to:MutableSequence[int], length:int, root:int) -> int: ...
    @overload
    def ReduceMin(self, data:MutableSequence[float], to:MutableSequence[float], length:int, root:int) -> int: ...
    @overload
    def ReduceMin(self, data:MutableSequence[int], to:MutableSequence[int], length:int, root:int) -> int: ...
    def ReduceSum(self, data:MutableSequence[int], to:MutableSequence[int], length:int, root:int) -> int: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkSubGroup': ...
    def getLocalRank(self, processID:int) -> int: ...
    def setGatherPattern(self, root:int, length:int) -> None: ...

