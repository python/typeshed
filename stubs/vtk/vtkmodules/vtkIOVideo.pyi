from collections.abc import MutableSequence, Sequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkVideoSource(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def AutoAdvanceOff(self) -> None: ...
    def AutoAdvanceOn(self) -> None: ...
    def FastForward(self) -> None: ...
    def GetAutoAdvance(self) -> int: ...
    def GetClipRegion(self) -> Tuple[int, int, int, int, int, int]: ...
    def GetDataOrigin(self) -> Tuple[float, float, float]: ...
    def GetDataSpacing(self) -> Tuple[float, float, float]: ...
    def GetFrameBufferSize(self) -> int: ...
    def GetFrameCount(self) -> int: ...
    def GetFrameIndex(self) -> int: ...
    def GetFrameRate(self) -> float: ...
    def GetFrameSize(self) -> Tuple[int, int, int]: ...
    @overload
    def GetFrameTimeStamp(self, frame: int) -> float: ...
    @overload
    def GetFrameTimeStamp(self) -> float: ...
    def GetInitialized(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfOutputFrames(self) -> int: ...
    def GetOpacity(self) -> float: ...
    def GetOutputFormat(self) -> int: ...
    def GetOutputWholeExtent(self) -> Tuple[int, int, int, int, int, int]: ...
    def GetPlaying(self) -> int: ...
    def GetRecording(self) -> int: ...
    def GetStartTimeStamp(self) -> float: ...
    def Grab(self) -> None: ...
    def Initialize(self) -> None: ...
    def InternalGrab(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkVideoSource: ...
    def Play(self) -> None: ...
    def Record(self) -> None: ...
    def ReleaseSystemResources(self) -> None: ...
    def Rewind(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkVideoSource: ...
    def Seek(self, n: int) -> None: ...
    def SetAutoAdvance(self, _arg: int) -> None: ...
    @overload
    def SetClipRegion(self, r: MutableSequence[int]) -> None: ...
    @overload
    def SetClipRegion(self, x0: int, x1: int, y0: int, y1: int, z0: int, z1: int) -> None: ...
    @overload
    def SetDataOrigin(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetDataOrigin(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetDataSpacing(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetDataSpacing(self, _arg: Sequence[float]) -> None: ...
    def SetFrameBufferSize(self, FrameBufferSize: int) -> None: ...
    def SetFrameCount(self, _arg: int) -> None: ...
    def SetFrameRate(self, rate: float) -> None: ...
    @overload
    def SetFrameSize(self, x: int, y: int, z: int) -> None: ...
    @overload
    def SetFrameSize(self, dim: MutableSequence[int]) -> None: ...
    def SetNumberOfOutputFrames(self, _arg: int) -> None: ...
    def SetOpacity(self, _arg: float) -> None: ...
    def SetOutputFormat(self, format: int) -> None: ...
    def SetOutputFormatToLuminance(self) -> None: ...
    def SetOutputFormatToRGB(self) -> None: ...
    def SetOutputFormatToRGBA(self) -> None: ...
    @overload
    def SetOutputWholeExtent(self, _arg1: int, _arg2: int, _arg3: int, _arg4: int, _arg5: int, _arg6: int) -> None: ...
    @overload
    def SetOutputWholeExtent(self, _arg: Sequence[int]) -> None: ...
    def SetStartTimeStamp(self, t: float) -> None: ...
    def Stop(self) -> None: ...
