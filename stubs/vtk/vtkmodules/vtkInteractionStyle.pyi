from collections.abc import Callable, MutableSequence, Sequence
from typing import Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkRenderingCore


VTKIS_ACTOR: int
VTKIS_CAMERA: int
VTKIS_IMAGE2D: int
VTKIS_IMAGE3D: int
VTKIS_IMAGE_SLICING: int
VTKIS_JOYSTICK: int
VTKIS_SLICE: int
VTKIS_TRACKBALL: int
VTKIS_USERINTERACTION: int
VTKIS_WINDOW_LEVEL: int
VTK_UNICAM_BUTTON_LEFT: int
VTK_UNICAM_BUTTON_MIDDLE: int
VTK_UNICAM_BUTTON_RIGHT: int
VTK_UNICAM_CAM_INT_CHOOSE: int
VTK_UNICAM_CAM_INT_DOLLY: int
VTK_UNICAM_CAM_INT_PAN: int
VTK_UNICAM_CAM_INT_ROT: int
VTK_UNICAM_NONE: int

class vtkInteractorStyleDrawPolygon(vtkmodules.vtkRenderingCore.vtkInteractorStyle):
    def DrawPolygonPixelsOff(self) -> None: ...
    def DrawPolygonPixelsOn(self) -> None: ...
    def GetDrawPolygonPixels(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleDrawPolygon: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleDrawPolygon: ...
    def SetDrawPolygonPixels(self, _arg: bool) -> None: ...

class vtkInteractorStyleFlight(vtkmodules.vtkRenderingCore.vtkInteractorStyle):
    def DisableMotionOff(self) -> None: ...
    def DisableMotionOn(self) -> None: ...
    def EndForwardFly(self) -> None: ...
    def EndReverseFly(self) -> None: ...
    def ForwardFly(self) -> None: ...
    def GetAngleAccelerationFactor(self) -> float: ...
    def GetAngleStepSize(self) -> float: ...
    def GetDefaultUpVector(self) -> Tuple[float, float, float]: ...
    def GetDisableMotion(self) -> int: ...
    def GetMotionAccelerationFactor(self) -> float: ...
    def GetMotionStepSize(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRestoreUpVector(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def JumpTo(self, campos: MutableSequence[float], focpos: MutableSequence[float]) -> None: ...
    def NewInstance(self) -> vtkInteractorStyleFlight: ...
    def OnChar(self) -> None: ...
    def OnKeyDown(self) -> None: ...
    def OnKeyUp(self) -> None: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMiddleButtonDown(self) -> None: ...
    def OnMiddleButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnRightButtonDown(self) -> None: ...
    def OnRightButtonUp(self) -> None: ...
    def OnTimer(self) -> None: ...
    def RestoreUpVectorOff(self) -> None: ...
    def RestoreUpVectorOn(self) -> None: ...
    def ReverseFly(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleFlight: ...
    def SetAngleAccelerationFactor(self, _arg: float) -> None: ...
    def SetAngleStepSize(self, _arg: float) -> None: ...
    def SetDefaultUpVector(self, data: Sequence[float]) -> None: ...
    def SetDisableMotion(self, _arg: int) -> None: ...
    def SetMotionAccelerationFactor(self, _arg: float) -> None: ...
    def SetMotionStepSize(self, _arg: float) -> None: ...
    def SetRestoreUpVector(self, _arg: int) -> None: ...
    def StartForwardFly(self) -> None: ...
    def StartReverseFly(self) -> None: ...

class vtkInteractorStyleTrackballCamera(vtkmodules.vtkRenderingCore.vtkInteractorStyle):
    def Dolly(self) -> None: ...
    def EnvironmentRotate(self) -> None: ...
    def GetMotionFactor(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleTrackballCamera: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMiddleButtonDown(self) -> None: ...
    def OnMiddleButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnMouseWheelBackward(self) -> None: ...
    def OnMouseWheelForward(self) -> None: ...
    def OnRightButtonDown(self) -> None: ...
    def OnRightButtonUp(self) -> None: ...
    def Pan(self) -> None: ...
    def Rotate(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleTrackballCamera: ...
    def SetMotionFactor(self, _arg: float) -> None: ...
    def Spin(self) -> None: ...

class vtkInteractorStyleImage(vtkInteractorStyleTrackballCamera):
    def EndPick(self) -> None: ...
    def EndSlice(self) -> None: ...
    def EndWindowLevel(self) -> None: ...
    def GetCurrentImageNumber(self) -> int: ...
    def GetCurrentImageProperty(self) -> vtkmodules.vtkRenderingCore.vtkImageProperty: ...
    def GetInteractionMode(self) -> int: ...
    def GetInteractionModeMaxValue(self) -> int: ...
    def GetInteractionModeMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetWindowLevelCurrentPosition(self) -> Tuple[int, int]: ...
    def GetWindowLevelStartPosition(self) -> Tuple[int, int]: ...
    def GetXViewRightVector(self) -> Tuple[float, float, float]: ...
    def GetXViewUpVector(self) -> Tuple[float, float, float]: ...
    def GetYViewRightVector(self) -> Tuple[float, float, float]: ...
    def GetYViewUpVector(self) -> Tuple[float, float, float]: ...
    def GetZViewRightVector(self) -> Tuple[float, float, float]: ...
    def GetZViewUpVector(self) -> Tuple[float, float, float]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleImage: ...
    def OnChar(self) -> None: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMiddleButtonDown(self) -> None: ...
    def OnMiddleButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnRightButtonDown(self) -> None: ...
    def OnRightButtonUp(self) -> None: ...
    def Pick(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleImage: ...
    def SetCurrentImageNumber(self, i: int) -> None: ...
    def SetImageOrientation(self, leftToRight: Sequence[float], bottomToTop: Sequence[float]) -> None: ...
    def SetInteractionMode(self, _arg: int) -> None: ...
    def SetInteractionModeToImage2D(self) -> None: ...
    def SetInteractionModeToImage3D(self) -> None: ...
    def SetInteractionModeToImageSlicing(self) -> None: ...
    @overload
    def SetXViewRightVector(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetXViewRightVector(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetXViewUpVector(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetXViewUpVector(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetYViewRightVector(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetYViewRightVector(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetYViewUpVector(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetYViewUpVector(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetZViewRightVector(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetZViewRightVector(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetZViewUpVector(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetZViewUpVector(self, _arg: Sequence[float]) -> None: ...
    def Slice(self) -> None: ...
    def StartPick(self) -> None: ...
    def StartSlice(self) -> None: ...
    def StartWindowLevel(self) -> None: ...
    def WindowLevel(self) -> None: ...

class vtkInteractorStyleJoystickActor(vtkmodules.vtkRenderingCore.vtkInteractorStyle):
    def Dolly(self) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleJoystickActor: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMiddleButtonDown(self) -> None: ...
    def OnMiddleButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnRightButtonDown(self) -> None: ...
    def OnRightButtonUp(self) -> None: ...
    def Pan(self) -> None: ...
    def Rotate(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleJoystickActor: ...
    def Spin(self) -> None: ...
    def UniformScale(self) -> None: ...

class vtkInteractorStyleJoystickCamera(vtkmodules.vtkRenderingCore.vtkInteractorStyle):
    def Dolly(self) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleJoystickCamera: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMiddleButtonDown(self) -> None: ...
    def OnMiddleButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnMouseWheelBackward(self) -> None: ...
    def OnMouseWheelForward(self) -> None: ...
    def OnRightButtonDown(self) -> None: ...
    def OnRightButtonUp(self) -> None: ...
    def Pan(self) -> None: ...
    def Rotate(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleJoystickCamera: ...
    def Spin(self) -> None: ...

class vtkInteractorStyleMultiTouchCamera(vtkInteractorStyleTrackballCamera):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleMultiTouchCamera: ...
    def OnEndPan(self) -> None: ...
    def OnEndPinch(self) -> None: ...
    def OnEndRotate(self) -> None: ...
    def OnPan(self) -> None: ...
    def OnPinch(self) -> None: ...
    def OnRotate(self) -> None: ...
    def OnStartPan(self) -> None: ...
    def OnStartPinch(self) -> None: ...
    def OnStartRotate(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleMultiTouchCamera: ...

class vtkInteractorStyleRubberBand2D(vtkmodules.vtkRenderingCore.vtkInteractorStyle):
    NONE: int
    PANNING: int
    SELECTING: int
    SELECT_NORMAL: int
    SELECT_UNION: int
    ZOOMING: int
    def GetEndPosition(self) -> Tuple[int, int]: ...
    def GetInteraction(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRenderOnMouseMove(self) -> bool: ...
    def GetStartPosition(self) -> Tuple[int, int]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleRubberBand2D: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMiddleButtonDown(self) -> None: ...
    def OnMiddleButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnMouseWheelBackward(self) -> None: ...
    def OnMouseWheelForward(self) -> None: ...
    def OnRightButtonDown(self) -> None: ...
    def OnRightButtonUp(self) -> None: ...
    def RenderOnMouseMoveOff(self) -> None: ...
    def RenderOnMouseMoveOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleRubberBand2D: ...
    def SetRenderOnMouseMove(self, _arg: bool) -> None: ...

class vtkInteractorStyleRubberBand3D(vtkInteractorStyleTrackballCamera):
    NONE: int
    PANNING: int
    ROTATING: int
    SELECTING: int
    SELECT_NORMAL: int
    SELECT_UNION: int
    ZOOMING: int
    def GetEndPosition(self) -> Tuple[int, int]: ...
    def GetInteraction(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRenderOnMouseMove(self) -> bool: ...
    def GetStartPosition(self) -> Tuple[int, int]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleRubberBand3D: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMiddleButtonDown(self) -> None: ...
    def OnMiddleButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnMouseWheelBackward(self) -> None: ...
    def OnMouseWheelForward(self) -> None: ...
    def OnRightButtonDown(self) -> None: ...
    def OnRightButtonUp(self) -> None: ...
    def RenderOnMouseMoveOff(self) -> None: ...
    def RenderOnMouseMoveOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleRubberBand3D: ...
    def SetRenderOnMouseMove(self, _arg: bool) -> None: ...

class vtkInteractorStyleRubberBandPick(vtkInteractorStyleTrackballCamera):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleRubberBandPick: ...
    def OnChar(self) -> None: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleRubberBandPick: ...
    def StartSelect(self) -> None: ...

class vtkInteractorStyleRubberBandZoom(vtkmodules.vtkRenderingCore.vtkInteractorStyle):
    def CenterAtStartPositionOff(self) -> None: ...
    def CenterAtStartPositionOn(self) -> None: ...
    def GetCenterAtStartPosition(self) -> bool: ...
    def GetLockAspectToViewport(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetUseDollyForPerspectiveProjection(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def LockAspectToViewportOff(self) -> None: ...
    def LockAspectToViewportOn(self) -> None: ...
    def NewInstance(self) -> vtkInteractorStyleRubberBandZoom: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleRubberBandZoom: ...
    def SetCenterAtStartPosition(self, _arg: bool) -> None: ...
    def SetLockAspectToViewport(self, _arg: bool) -> None: ...
    def SetUseDollyForPerspectiveProjection(self, _arg: bool) -> None: ...
    def UseDollyForPerspectiveProjectionOff(self) -> None: ...
    def UseDollyForPerspectiveProjectionOn(self) -> None: ...

class vtkInteractorStyleSwitch(vtkmodules.vtkRenderingCore.vtkInteractorStyleSwitchBase):
    def GetCurrentStyle(self) -> vtkmodules.vtkRenderingCore.vtkInteractorStyle: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleSwitch: ...
    def OnChar(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleSwitch: ...
    def SetAutoAdjustCameraClippingRange(self, value: int) -> None: ...
    def SetCurrentRenderer(self, __a: vtkmodules.vtkRenderingCore.vtkRenderer) -> None: ...
    def SetCurrentStyleToJoystickActor(self) -> None: ...
    def SetCurrentStyleToJoystickCamera(self) -> None: ...
    def SetCurrentStyleToMultiTouchCamera(self) -> None: ...
    def SetCurrentStyleToTrackballActor(self) -> None: ...
    def SetCurrentStyleToTrackballCamera(self) -> None: ...
    def SetDefaultRenderer(self, __a: vtkmodules.vtkRenderingCore.vtkRenderer) -> None: ...
    def SetInteractor(self, iren: vtkmodules.vtkRenderingCore.vtkRenderWindowInteractor) -> None: ...

class vtkInteractorStyleTerrain(vtkmodules.vtkRenderingCore.vtkInteractorStyle):
    def Dolly(self) -> None: ...
    def GetLatLongLines(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def LatLongLinesOff(self) -> None: ...
    def LatLongLinesOn(self) -> None: ...
    def NewInstance(self) -> vtkInteractorStyleTerrain: ...
    def OnChar(self) -> None: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMiddleButtonDown(self) -> None: ...
    def OnMiddleButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnRightButtonDown(self) -> None: ...
    def OnRightButtonUp(self) -> None: ...
    def Pan(self) -> None: ...
    def Rotate(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleTerrain: ...
    def SetLatLongLines(self, _arg: int) -> None: ...

class vtkInteractorStyleTrackball(vtkInteractorStyleSwitch):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleTrackball: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleTrackball: ...

class vtkInteractorStyleTrackballActor(vtkmodules.vtkRenderingCore.vtkInteractorStyle):
    def Dolly(self) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleTrackballActor: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMiddleButtonDown(self) -> None: ...
    def OnMiddleButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnRightButtonDown(self) -> None: ...
    def OnRightButtonUp(self) -> None: ...
    def Pan(self) -> None: ...
    def Rotate(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleTrackballActor: ...
    def Spin(self) -> None: ...
    def UniformScale(self) -> None: ...

class vtkInteractorStyleUnicam(vtkmodules.vtkRenderingCore.vtkInteractorStyle):
    BUTTON_LEFT: int
    BUTTON_MIDDLE: int
    BUTTON_RIGHT: int
    CAM_INT_CHOOSE: int
    CAM_INT_DOLLY: int
    CAM_INT_PAN: int
    CAM_INT_ROT: int
    NONE: int
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetWorldUpVector(self) -> Tuple[float, float, float]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleUnicam: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonMove(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnTimer(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleUnicam: ...
    @overload
    def SetWorldUpVector(self, a: MutableSequence[float]) -> None: ...
    @overload
    def SetWorldUpVector(self, x: float, y: float, z: float) -> None: ...

class vtkInteractorStyleUser(vtkmodules.vtkRenderingCore.vtkInteractorStyle):
    def GetButton(self) -> int: ...
    def GetChar(self) -> int: ...
    def GetCtrlKey(self) -> int: ...
    def GetKeySym(self) -> str: ...
    def GetLastPos(self) -> Tuple[int, int]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOldPos(self) -> Tuple[int, int]: ...
    def GetShiftKey(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInteractorStyleUser: ...
    def OnChar(self) -> None: ...
    def OnConfigure(self) -> None: ...
    def OnEnter(self) -> None: ...
    def OnExpose(self) -> None: ...
    def OnKeyPress(self) -> None: ...
    def OnKeyRelease(self) -> None: ...
    def OnLeave(self) -> None: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMiddleButtonDown(self) -> None: ...
    def OnMiddleButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnMouseWheelBackward(self) -> None: ...
    def OnMouseWheelForward(self) -> None: ...
    def OnRightButtonDown(self) -> None: ...
    def OnRightButtonUp(self) -> None: ...
    def OnTimer(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInteractorStyleUser: ...

class vtkParallelCoordinatesInteractorStyle(vtkInteractorStyleTrackballCamera):
    INTERACT_HOVER: int
    INTERACT_INSPECT: int
    INTERACT_PAN: int
    INTERACT_ZOOM: int
    def EndInspect(self) -> None: ...
    def EndPan(self) -> None: ...
    def EndZoom(self) -> None: ...
    @overload
    def GetCursorCurrentPosition(self) -> Tuple[int, int]: ...
    @overload
    def GetCursorCurrentPosition(
        self, viewport: vtkmodules.vtkRenderingCore.vtkViewport, pos: MutableSequence[float]
    ) -> None: ...
    @overload
    def GetCursorLastPosition(self) -> Tuple[int, int]: ...
    @overload
    def GetCursorLastPosition(self, viewport: vtkmodules.vtkRenderingCore.vtkViewport, pos: MutableSequence[float]) -> None: ...
    @overload
    def GetCursorStartPosition(self) -> Tuple[int, int]: ...
    @overload
    def GetCursorStartPosition(self, viewport: vtkmodules.vtkRenderingCore.vtkViewport, pos: MutableSequence[float]) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def Inspect(self, x: int, y: int) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkParallelCoordinatesInteractorStyle: ...
    def OnChar(self) -> None: ...
    def OnLeave(self) -> None: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMiddleButtonDown(self) -> None: ...
    def OnMiddleButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnRightButtonDown(self) -> None: ...
    def OnRightButtonUp(self) -> None: ...
    def Pan(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkParallelCoordinatesInteractorStyle: ...
    def StartInspect(self, x: int, y: int) -> None: ...
    def StartPan(self) -> None: ...
    def StartZoom(self) -> None: ...
    def Zoom(self) -> None: ...
