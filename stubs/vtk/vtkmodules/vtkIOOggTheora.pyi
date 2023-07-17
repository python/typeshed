from typing import TypeVar

import vtkmodules.vtkCommonCore
import vtkmodules.vtkIOMovie


class vtkOggTheoraWriter(vtkmodules.vtkIOMovie.vtkGenericMovieWriter):
    def End(self) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetQuality(self) -> int: ...
    def GetQualityMaxValue(self) -> int: ...
    def GetQualityMinValue(self) -> int: ...
    def GetRate(self) -> int: ...
    def GetRateMaxValue(self) -> int: ...
    def GetRateMinValue(self) -> int: ...
    def GetSubsampling(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOggTheoraWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOggTheoraWriter: ...
    def SetQuality(self, _arg: int) -> None: ...
    def SetRate(self, _arg: int) -> None: ...
    def SetSubsampling(self, _arg: int) -> None: ...
    def Start(self) -> None: ...
    def SubsamplingOff(self) -> None: ...
    def SubsamplingOn(self) -> None: ...
    def Write(self) -> None: ...
