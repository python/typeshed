import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

class vtkPythonAlgorithm(vtkmodules.vtkCommonExecutionModel.vtkAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPythonAlgorithm: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPythonAlgorithm: ...
    def SetNumberOfInputPorts(self, n: int) -> None: ...
    def SetNumberOfOutputPorts(self, n: int) -> None: ...
    def SetPythonObject(self, obj: PyObject) -> None: ...
