import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

class vtkTecplotTableReader(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    def GeneratePedigreeIdsOff(self) -> None: ...
    def GeneratePedigreeIdsOn(self) -> None: ...
    def GetColumnNamesOnLine(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetGeneratePedigreeIds(self) -> bool: ...
    def GetHeaderLines(self) -> int: ...
    def GetLastError(self) -> str: ...
    def GetMaxRecords(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputPedigreeIds(self) -> bool: ...
    def GetPedigreeIdArrayName(self) -> str: ...
    def GetSkipColumnNames(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTecplotTableReader: ...
    def OutputPedigreeIdsOff(self) -> None: ...
    def OutputPedigreeIdsOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTecplotTableReader: ...
    def SetColumnNamesOnLine(self, _arg: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetGeneratePedigreeIds(self, _arg: bool) -> None: ...
    def SetHeaderLines(self, _arg: int) -> None: ...
    def SetMaxRecords(self, _arg: int) -> None: ...
    def SetOutputPedigreeIds(self, _arg: bool) -> None: ...
    def SetPedigreeIdArrayName(self, _arg: str) -> None: ...
    def SetSkipColumnNames(self, _arg: int) -> None: ...
