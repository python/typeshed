from typing import TypeVar

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkGenericMovieWriter(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    class MovieWriterErrorIds(int): ...
    CanNotCompress: MovieWriterErrorIds
    CanNotFormat: MovieWriterErrorIds
    ChangedResolutionError: MovieWriterErrorIds
    InitError: MovieWriterErrorIds
    NoInputError: MovieWriterErrorIds
    UserError: MovieWriterErrorIds
    def End(self) -> None: ...
    def GetError(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    @staticmethod
    def GetStringFromErrorCode(error: int) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGenericMovieWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGenericMovieWriter: ...
    def SetFileName(self, _arg: str) -> None: ...
    def Start(self) -> None: ...
    def Write(self) -> None: ...
