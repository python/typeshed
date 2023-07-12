from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkFiltersImaging
import vtkmodules.vtkFiltersParallel
import vtkmodules.vtkImagingCore

class vtkExtractPiece(vtkmodules.vtkCommonExecutionModel.vtkCompositeDataSetAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkExtractPiece': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkExtractPiece': ...

class vtkMemoryLimitImageDataStreamer(vtkmodules.vtkImagingCore.vtkImageDataStreamer):
    def GetMemoryLimit(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkMemoryLimitImageDataStreamer': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkMemoryLimitImageDataStreamer': ...
    def SetMemoryLimit(self, _arg:int) -> None: ...

class vtkPComputeHistogram2DOutliers(vtkmodules.vtkFiltersImaging.vtkComputeHistogram2DOutliers):
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkPComputeHistogram2DOutliers': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPComputeHistogram2DOutliers': ...
    def SetController(self, __a:'vtkMultiProcessController') -> None: ...

class vtkPExtractHistogram2D(vtkmodules.vtkFiltersImaging.vtkExtractHistogram2D):
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkPExtractHistogram2D': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPExtractHistogram2D': ...
    def SetController(self, __a:'vtkMultiProcessController') -> None: ...

class vtkPPairwiseExtractHistogram2D(vtkmodules.vtkFiltersImaging.vtkPairwiseExtractHistogram2D):
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkPPairwiseExtractHistogram2D': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPPairwiseExtractHistogram2D': ...
    def SetController(self, __a:'vtkMultiProcessController') -> None: ...

class vtkTransmitImageDataPiece(vtkmodules.vtkFiltersParallel.vtkTransmitStructuredDataPiece):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkTransmitImageDataPiece': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkTransmitImageDataPiece': ...

