from collections.abc import Callable, MutableSequence
from typing import TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonMath
import vtkmodules.vtkIOExport
import vtkmodules.vtkRenderingContext2D
import vtkmodules.vtkRenderingCore

_Pointer = TypeVar("_Pointer")

class vtkPDFContextDevice2D(vtkmodules.vtkRenderingContext2D.vtkContextDevice2D):
    def ComputeJustifiedStringBounds(self, string: str, bounds: MutableSequence[float]) -> None: ...
    def ComputeStringBounds(self, string: str, bounds: MutableSequence[float]) -> None: ...
    def DrawColoredPolygon(
        self, points: MutableSequence[float], numPoints: int, colors: MutableSequence[int] = ..., nc_comps: int = 0
    ) -> None: ...
    def DrawEllipseWedge(
        self, x: float, y: float, outRx: float, outRy: float, inRx: float, inRy: float, startAngle: float, stopAngle: float
    ) -> None: ...
    def DrawEllipticArc(self, x: float, y: float, rX: float, rY: float, startAngle: float, stopAngle: float) -> None: ...
    @overload
    def DrawImage(self, p: MutableSequence[float], scale: float, image: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    @overload
    def DrawImage(
        self, pos: vtkmodules.vtkCommonDataModel.vtkRectf, image: vtkmodules.vtkCommonDataModel.vtkImageData
    ) -> None: ...
    def DrawLines(self, f: MutableSequence[float], n: int, colors: MutableSequence[int] = ..., nc_comps: int = 0) -> None: ...
    def DrawMarkers(
        self,
        shape: int,
        highlight: bool,
        points: MutableSequence[float],
        n: int,
        colors: MutableSequence[int] = ...,
        nc_comps: int = 0,
    ) -> None: ...
    def DrawMathTextString(self, point: MutableSequence[float], str: str) -> None: ...
    def DrawPointSprites(
        self,
        sprite: vtkmodules.vtkCommonDataModel.vtkImageData,
        points: MutableSequence[float],
        n: int,
        colors: MutableSequence[int] = ...,
        nc_comps: int = 0,
    ) -> None: ...
    def DrawPoints(
        self, points: MutableSequence[float], n: int, colors: MutableSequence[int] = ..., nc_comps: int = 0
    ) -> None: ...
    def DrawPoly(self, points: MutableSequence[float], n: int, colors: MutableSequence[int] = ..., nc_comps: int = 0) -> None: ...
    def DrawPolyData(
        self,
        p: MutableSequence[float],
        scale: float,
        polyData: vtkmodules.vtkCommonDataModel.vtkPolyData,
        colors: vtkmodules.vtkCommonCore.vtkUnsignedCharArray,
        scalarMode: int,
    ) -> None: ...
    def DrawPolygon(self, __a: MutableSequence[float], __b: int) -> None: ...
    def DrawQuad(self, __a: MutableSequence[float], __b: int) -> None: ...
    def DrawQuadStrip(self, __a: MutableSequence[float], __b: int) -> None: ...
    def DrawString(self, point: MutableSequence[float], string: str) -> None: ...
    def EnableClipping(self, enable: bool) -> None: ...
    def GetMatrix(self, m: vtkmodules.vtkCommonMath.vtkMatrix3x3) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MultiplyMatrix(self, m: vtkmodules.vtkCommonMath.vtkMatrix3x3) -> None: ...
    def NewInstance(self) -> vtkPDFContextDevice2D: ...
    def PopMatrix(self) -> None: ...
    def PushMatrix(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPDFContextDevice2D: ...
    def SetClipping(self, x: MutableSequence[int]) -> None: ...
    def SetColor4(self, color: MutableSequence[int]) -> None: ...
    def SetHaruObjects(self, doc: _Pointer, page: _Pointer) -> None: ...
    def SetLineType(self, type: int) -> None: ...
    def SetLineWidth(self, width: float) -> None: ...
    def SetMatrix(self, m: vtkmodules.vtkCommonMath.vtkMatrix3x3) -> None: ...
    def SetPointSize(self, size: float) -> None: ...
    def SetRenderer(self, __a: vtkmodules.vtkRenderingCore.vtkRenderer) -> None: ...
    def SetTexture(self, image: vtkmodules.vtkCommonDataModel.vtkImageData, properties: int) -> None: ...

class vtkPDFExporter(vtkmodules.vtkIOExport.vtkExporter):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTitle(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPDFExporter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPDFExporter: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetTitle(self, _arg: str) -> None: ...
