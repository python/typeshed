from collections.abc import Callable
from typing import TypeVar, Union

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkFiltersImaging
import vtkmodules.vtkFiltersParallel
import vtkmodules.vtkImagingCore
import vtkmodules.vtkParallelCore

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkExtractPiece(vtkmodules.vtkCommonExecutionModel.vtkCompositeDataSetAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkExtractPiece: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkExtractPiece: ...

class vtkMemoryLimitImageDataStreamer(vtkmodules.vtkImagingCore.vtkImageDataStreamer):
    def GetMemoryLimit(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMemoryLimitImageDataStreamer: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMemoryLimitImageDataStreamer: ...
    def SetMemoryLimit(self, _arg: int) -> None: ...

class vtkPComputeHistogram2DOutliers(vtkmodules.vtkFiltersImaging.vtkComputeHistogram2DOutliers):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPComputeHistogram2DOutliers: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPComputeHistogram2DOutliers: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...

class vtkPExtractHistogram2D(vtkmodules.vtkFiltersImaging.vtkExtractHistogram2D):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPExtractHistogram2D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPExtractHistogram2D: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...

class vtkPPairwiseExtractHistogram2D(vtkmodules.vtkFiltersImaging.vtkPairwiseExtractHistogram2D):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPPairwiseExtractHistogram2D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPPairwiseExtractHistogram2D: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...

class vtkTransmitImageDataPiece(vtkmodules.vtkFiltersParallel.vtkTransmitStructuredDataPiece):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTransmitImageDataPiece: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTransmitImageDataPiece: ...
