from collections.abc import Callable, MutableSequence
from typing import TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonMath
import vtkmodules.vtkRenderingCore
import vtkmodules.vtkRenderingOpenGL2

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkOpenGLGL2PSHelperImpl(vtkmodules.vtkRenderingOpenGL2.vtkOpenGLGL2PSHelper):
    def Draw3DPath(
        self,
        path: vtkmodules.vtkCommonDataModel.vtkPath,
        actorMatrix: vtkmodules.vtkCommonMath.vtkMatrix4x4,
        rasterPos: MutableSequence[float],
        actorColor: MutableSequence[int],
        ren: vtkmodules.vtkRenderingCore.vtkRenderer,
        label: str = ...,
    ) -> None: ...
    def DrawImage(self, input: vtkmodules.vtkCommonDataModel.vtkImageData, pos: MutableSequence[float]) -> None: ...
    def DrawPath(
        self,
        path: vtkmodules.vtkCommonDataModel.vtkPath,
        rasterPos: MutableSequence[float],
        windowPos: MutableSequence[float],
        rgba: MutableSequence[int],
        scale: MutableSequence[float] = ...,
        rotateAngle: float = 0.0,
        strokeWidth: float = -1,
        label: str = ...,
    ) -> None: ...
    def DrawString(
        self,
        str: str,
        tprop: vtkmodules.vtkRenderingCore.vtkTextProperty,
        pos: MutableSequence[float],
        backgroundDepth: float,
        ren: vtkmodules.vtkRenderingCore.vtkRenderer,
    ) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOpenGLGL2PSHelperImpl: ...
    @overload
    def ProcessTransformFeedback(
        self,
        tfc: vtkmodules.vtkRenderingOpenGL2.vtkTransformFeedback,
        ren: vtkmodules.vtkRenderingCore.vtkRenderer,
        act: vtkmodules.vtkRenderingCore.vtkActor,
    ) -> None: ...
    @overload
    def ProcessTransformFeedback(
        self,
        tfc: vtkmodules.vtkRenderingOpenGL2.vtkTransformFeedback,
        ren: vtkmodules.vtkRenderingCore.vtkRenderer,
        col: MutableSequence[int],
    ) -> None: ...
    @overload
    def ProcessTransformFeedback(
        self,
        tfc: vtkmodules.vtkRenderingOpenGL2.vtkTransformFeedback,
        ren: vtkmodules.vtkRenderingCore.vtkRenderer,
        col: MutableSequence[float],
    ) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOpenGLGL2PSHelperImpl: ...
