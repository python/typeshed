from typing import TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkRenderingCore

Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

VTK_SKIP_RETURN_CODE: int

class vtkTesting(vtkmodules.vtkCommonCore.vtkObject):
    class ReturnValue(int): ...
    DO_INTERACTOR: ReturnValue
    FAILED: ReturnValue
    NOT_RUN: ReturnValue
    PASSED: ReturnValue
    def AddArgument(self, argv: str) -> None: ...
    def CleanArguments(self) -> None: ...
    @overload
    def CompareAverageOfL2Norm(
        self, dsA: vtkmodules.vtkCommonDataModel.vtkDataSet, dsB: vtkmodules.vtkCommonDataModel.vtkDataSet, tol: float
    ) -> int: ...
    @overload
    def CompareAverageOfL2Norm(
        self, daA: vtkmodules.vtkCommonCore.vtkDataArray, daB: vtkmodules.vtkCommonCore.vtkDataArray, tol: float
    ) -> int: ...
    def FrontBufferOff(self) -> None: ...
    def FrontBufferOn(self) -> None: ...
    def GetArgument(self, arg: str) -> str: ...
    def GetBorderOffset(self) -> int: ...
    def GetDataRoot(self) -> str: ...
    def GetFrontBuffer(self) -> int: ...
    def GetImageDifference(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRenderWindow(self) -> vtkmodules.vtkRenderingCore.vtkRenderWindow: ...
    def GetTempDirectory(self) -> str: ...
    def GetValidImageFileName(self) -> str: ...
    def GetVerbose(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    def IsFlagSpecified(self, flag: str) -> int: ...
    def IsInteractiveModeSpecified(self) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def IsValidImageSpecified(self) -> int: ...
    def NewInstance(self) -> vtkTesting: ...
    @overload
    def RegressionTest(self, thresh: float) -> int: ...
    @overload
    def RegressionTest(self, pngFileName: str, thresh: float) -> int: ...
    @overload
    def RegressionTest(self, imageSource: vtkmodules.vtkCommonExecutionModel.vtkAlgorithm, thresh: float) -> int: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTesting: ...
    def SetBorderOffset(self, _arg: int) -> None: ...
    def SetDataRoot(self, _arg: str) -> None: ...
    def SetFrontBuffer(self, frontBuffer: int) -> None: ...
    def SetRenderWindow(self, rw: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> None: ...
    def SetTempDirectory(self, _arg: str) -> None: ...
    def SetValidImageFileName(self, _arg: str) -> None: ...
    def SetVerbose(self, _arg: int) -> None: ...

class vtkTestingInteractor(vtkmodules.vtkRenderingCore.vtkRenderWindowInteractor):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTestingInteractor: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTestingInteractor: ...
    def Start(self) -> None: ...

class vtkTestingObjectFactory(vtkmodules.vtkCommonCore.vtkObjectFactory):
    def GetDescription(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetVTKSourceVersion(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTestingObjectFactory: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTestingObjectFactory: ...
