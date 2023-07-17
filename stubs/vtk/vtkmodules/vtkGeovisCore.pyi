from collections.abc import MutableSequence, Sequence
from typing import TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonTransforms
import vtkmodules.vtkInteractionWidgets
import vtkmodules.vtkRenderingCore

Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkCompassRepresentation(vtkmodules.vtkInteractionWidgets.vtkContinuousValueWidgetRepresentation):
    class InteractionStateType(int): ...
    Adjusting: InteractionStateType
    DistanceAdjusting: InteractionStateType
    DistanceIn: InteractionStateType
    DistanceOut: InteractionStateType
    Inside: InteractionStateType
    Outside: InteractionStateType
    TiltAdjusting: InteractionStateType
    TiltDown: InteractionStateType
    TiltUp: InteractionStateType
    def BuildRepresentation(self) -> None: ...
    def ComputeInteractionState(self, X: int, Y: int, modify: int = 0) -> int: ...
    def DistanceWidgetInteraction(self, eventPos: MutableSequence[float]) -> None: ...
    def EndDistance(self) -> None: ...
    def EndTilt(self) -> None: ...
    def GetActors(self, __a: vtkmodules.vtkRenderingCore.vtkPropCollection) -> None: ...
    def GetDistance(self) -> float: ...
    def GetHeading(self) -> float: ...
    def GetLabelProperty(self) -> vtkmodules.vtkRenderingCore.vtkTextProperty: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPoint1Coordinate(self) -> vtkmodules.vtkRenderingCore.vtkCoordinate: ...
    def GetPoint2Coordinate(self) -> vtkmodules.vtkRenderingCore.vtkCoordinate: ...
    def GetRingProperty(self) -> vtkmodules.vtkRenderingCore.vtkProperty2D: ...
    def GetSelectedProperty(self) -> vtkmodules.vtkRenderingCore.vtkProperty2D: ...
    def GetTilt(self) -> float: ...
    def Highlight(self, __a: int) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCompassRepresentation: ...
    def PlaceWidget(self, bounds: MutableSequence[float]) -> None: ...
    def ReleaseGraphicsResources(self, __a: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    def RenderOpaqueGeometry(self, __a: vtkmodules.vtkRenderingCore.vtkViewport) -> int: ...
    def RenderOverlay(self, __a: vtkmodules.vtkRenderingCore.vtkViewport) -> int: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCompassRepresentation: ...
    def SetDistance(self, value: float) -> None: ...
    def SetHeading(self, value: float) -> None: ...
    def SetRenderer(self, ren: vtkmodules.vtkRenderingCore.vtkRenderer) -> None: ...
    def SetTilt(self, value: float) -> None: ...
    def StartWidgetInteraction(self, eventPos: MutableSequence[float]) -> None: ...
    def TiltWidgetInteraction(self, eventPos: MutableSequence[float]) -> None: ...
    def UpdateDistance(self, time: float) -> None: ...
    def UpdateTilt(self, time: float) -> None: ...
    def WidgetInteraction(self, eventPos: MutableSequence[float]) -> None: ...

class vtkCompassWidget(vtkmodules.vtkInteractionWidgets.vtkAbstractWidget):
    def CreateDefaultRepresentation(self) -> None: ...
    def GetDistance(self) -> float: ...
    def GetHeading(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTilt(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCompassWidget: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCompassWidget: ...
    def SetDistance(self, value: float) -> None: ...
    def SetHeading(self, v: float) -> None: ...
    def SetRepresentation(self, r: vtkCompassRepresentation) -> None: ...
    def SetTilt(self, value: float) -> None: ...

class vtkGeoProjection(vtkmodules.vtkCommonCore.vtkObject):
    def ClearOptionalParameters(self) -> None: ...
    def GetCentralMeridian(self) -> float: ...
    def GetDescription(self) -> str: ...
    def GetIndex(self) -> int: ...
    def GetName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfOptionalParameters(self) -> int: ...
    @staticmethod
    def GetNumberOfProjections() -> int: ...
    def GetOptionalParameterKey(self, index: int) -> str: ...
    def GetOptionalParameterValue(self, index: int) -> str: ...
    def GetPROJ4String(self) -> str: ...
    @staticmethod
    def GetProjectionDescription(projection: int) -> str: ...
    @staticmethod
    def GetProjectionName(projection: int) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGeoProjection: ...
    def RemoveOptionalParameter(self, __a: str) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGeoProjection: ...
    def SetCentralMeridian(self, _arg: float) -> None: ...
    def SetName(self, _arg: str) -> None: ...
    def SetOptionalParameter(self, key: str, value: str) -> None: ...
    def SetPROJ4String(self, _arg: str) -> None: ...

class vtkGeoTransform(vtkmodules.vtkCommonTransforms.vtkAbstractTransform):
    @overload
    @staticmethod
    def ComputeUTMZone(lon: float, lat: float) -> int: ...
    @overload
    @staticmethod
    def ComputeUTMZone(lonlat: MutableSequence[float]) -> int: ...
    def GetDestinationProjection(self) -> vtkGeoProjection: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSourceProjection(self) -> vtkGeoProjection: ...
    def InternalTransformDerivative(
        self, in_: Sequence[float], out: MutableSequence[float], derivative: MutableSequence[MutableSequence[float]]
    ) -> None: ...
    def InternalTransformPoint(self, in_: Sequence[float], out: MutableSequence[float]) -> None: ...
    def Inverse(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkmodules.vtkCommonTransforms.vtkAbstractTransform: ...
    def NewInstance(self) -> vtkGeoTransform: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGeoTransform: ...
    def SetDestinationProjection(self, dest: vtkGeoProjection) -> None: ...
    def SetSourceProjection(self, source: vtkGeoProjection) -> None: ...
    def TransformPoints(self, src: vtkmodules.vtkCommonCore.vtkPoints, dst: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...
