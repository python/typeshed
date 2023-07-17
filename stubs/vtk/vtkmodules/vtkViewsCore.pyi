from collections.abc import MutableSequence, Sequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkRenderingCore

_Pointer = TypeVar("_Pointer")

class vtkConvertSelectionDomain(vtkmodules.vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkConvertSelectionDomain: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkConvertSelectionDomain: ...

class vtkDataRepresentation(vtkmodules.vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    @overload
    def Annotate(self, view: vtkView, annotations: vtkmodules.vtkCommonDataModel.vtkAnnotationLayers) -> None: ...
    @overload
    def Annotate(self, view: vtkView, annotations: vtkmodules.vtkCommonDataModel.vtkAnnotationLayers, extend: bool) -> None: ...
    def ApplyViewTheme(self, theme: vtkViewTheme) -> None: ...
    def ConvertSelection(
        self, view: vtkView, selection: vtkmodules.vtkCommonDataModel.vtkSelection
    ) -> vtkmodules.vtkCommonDataModel.vtkSelection: ...
    def GetAnnotationLink(self) -> vtkmodules.vtkFiltersGeneral.vtkAnnotationLink: ...
    def GetInputConnection(self, port: int = 0, index: int = 0) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    @overload
    def GetInternalAnnotationOutputPort(self) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    @overload
    def GetInternalAnnotationOutputPort(self, port: int) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    @overload
    def GetInternalAnnotationOutputPort(self, port: int, conn: int) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    @overload
    def GetInternalOutputPort(self) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    @overload
    def GetInternalOutputPort(self, port: int) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    @overload
    def GetInternalOutputPort(self, port: int, conn: int) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    @overload
    def GetInternalSelectionOutputPort(self) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    @overload
    def GetInternalSelectionOutputPort(self, port: int) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    @overload
    def GetInternalSelectionOutputPort(self, port: int, conn: int) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSelectable(self) -> bool: ...
    def GetSelectionArrayName(self) -> str: ...
    def GetSelectionArrayNames(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetSelectionType(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkDataRepresentation: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkDataRepresentation: ...
    @overload
    def Select(self, view: vtkView, selection: vtkmodules.vtkCommonDataModel.vtkSelection) -> None: ...
    @overload
    def Select(self, view: vtkView, selection: vtkmodules.vtkCommonDataModel.vtkSelection, extend: bool) -> None: ...
    def SelectableOff(self) -> None: ...
    def SelectableOn(self) -> None: ...
    def SetAnnotationLink(self, link: vtkmodules.vtkFiltersGeneral.vtkAnnotationLink) -> None: ...
    def SetSelectable(self, _arg: bool) -> None: ...
    def SetSelectionArrayName(self, name: str) -> None: ...
    def SetSelectionArrayNames(self, names: vtkmodules.vtkCommonCore.vtkStringArray) -> None: ...
    def SetSelectionType(self, _arg: int) -> None: ...
    @overload
    def UpdateAnnotations(self, annotations: vtkmodules.vtkCommonDataModel.vtkAnnotationLayers) -> None: ...
    @overload
    def UpdateAnnotations(self, annotations: vtkmodules.vtkCommonDataModel.vtkAnnotationLayers, extend: bool) -> None: ...
    @overload
    def UpdateSelection(self, selection: vtkmodules.vtkCommonDataModel.vtkSelection) -> None: ...
    @overload
    def UpdateSelection(self, selection: vtkmodules.vtkCommonDataModel.vtkSelection, extend: bool) -> None: ...

class vtkEmptyRepresentation(vtkDataRepresentation):
    @overload
    def GetInternalAnnotationOutputPort(self) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    @overload
    def GetInternalAnnotationOutputPort(self, port: int) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    @overload
    def GetInternalAnnotationOutputPort(self, port: int, conn: int) -> vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkEmptyRepresentation: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkEmptyRepresentation: ...

class vtkView(vtkmodules.vtkCommonCore.vtkObject):
    def AddRepresentation(self, rep: vtkDataRepresentation) -> None: ...
    def AddRepresentationFromInput(self, input: vtkmodules.vtkCommonDataModel.vtkDataObject) -> vtkDataRepresentation: ...
    def AddRepresentationFromInputConnection(
        self, conn: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput
    ) -> vtkDataRepresentation: ...
    def ApplyViewTheme(self, theme: vtkViewTheme) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfRepresentations(self) -> int: ...
    def GetObserver(self) -> vtkmodules.vtkCommonCore.vtkCommand: ...
    def GetRepresentation(self, index: int = 0) -> vtkDataRepresentation: ...
    def IsA(self, type: str) -> int: ...
    def IsRepresentationPresent(self, rep: vtkDataRepresentation) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkView: ...
    def RegisterProgress(self, algorithm: vtkmodules.vtkCommonCore.vtkObject, message: str = ...) -> None: ...
    def RemoveAllRepresentations(self) -> None: ...
    @overload
    def RemoveRepresentation(self, rep: vtkDataRepresentation) -> None: ...
    @overload
    def RemoveRepresentation(self, rep: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkView: ...
    def SetRepresentation(self, rep: vtkDataRepresentation) -> None: ...
    def SetRepresentationFromInput(self, input: vtkmodules.vtkCommonDataModel.vtkDataObject) -> vtkDataRepresentation: ...
    def SetRepresentationFromInputConnection(
        self, conn: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput
    ) -> vtkDataRepresentation: ...
    def UnRegisterProgress(self, algorithm: vtkmodules.vtkCommonCore.vtkObject) -> None: ...
    def Update(self) -> None: ...

class vtkRenderViewBase(vtkView):
    def GetInteractor(self) -> vtkmodules.vtkRenderingCore.vtkRenderWindowInteractor: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRenderWindow(self) -> vtkmodules.vtkRenderingCore.vtkRenderWindow: ...
    def GetRenderer(self) -> vtkmodules.vtkRenderingCore.vtkRenderer: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkRenderViewBase: ...
    def Render(self) -> None: ...
    def ResetCamera(self) -> None: ...
    def ResetCameraClippingRange(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkRenderViewBase: ...
    def SetInteractor(self, __a: vtkmodules.vtkRenderingCore.vtkRenderWindowInteractor) -> None: ...
    def SetRenderWindow(self, win: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> None: ...
    def SetRenderer(self, ren: vtkmodules.vtkRenderingCore.vtkRenderer) -> None: ...

class vtkViewTheme(vtkmodules.vtkCommonCore.vtkObject):
    @staticmethod
    def CreateMellowTheme() -> vtkViewTheme: ...
    @staticmethod
    def CreateNeonTheme() -> vtkViewTheme: ...
    @staticmethod
    def CreateOceanTheme() -> vtkViewTheme: ...
    def GetBackgroundColor(self) -> Tuple[float, float, float]: ...
    def GetBackgroundColor2(self) -> Tuple[float, float, float]: ...
    @overload
    def GetCellAlphaRange(self) -> Pointer: ...
    @overload
    def GetCellAlphaRange(self, mn: float, mx: float) -> None: ...
    @overload
    def GetCellAlphaRange(self, rng: MutableSequence[float]) -> None: ...
    def GetCellColor(self) -> Tuple[float, float, float]: ...
    @overload
    def GetCellHueRange(self) -> Pointer: ...
    @overload
    def GetCellHueRange(self, mn: float, mx: float) -> None: ...
    @overload
    def GetCellHueRange(self, rng: MutableSequence[float]) -> None: ...
    def GetCellLookupTable(self) -> vtkmodules.vtkCommonCore.vtkScalarsToColors: ...
    def GetCellOpacity(self) -> float: ...
    @overload
    def GetCellSaturationRange(self) -> Pointer: ...
    @overload
    def GetCellSaturationRange(self, mn: float, mx: float) -> None: ...
    @overload
    def GetCellSaturationRange(self, rng: MutableSequence[float]) -> None: ...
    def GetCellTextProperty(self) -> vtkmodules.vtkRenderingCore.vtkTextProperty: ...
    @overload
    def GetCellValueRange(self) -> Pointer: ...
    @overload
    def GetCellValueRange(self, mn: float, mx: float) -> None: ...
    @overload
    def GetCellValueRange(self, rng: MutableSequence[float]) -> None: ...
    @overload
    def GetEdgeLabelColor(self) -> Pointer: ...
    @overload
    def GetEdgeLabelColor(self, r: float, g: float, b: float) -> None: ...
    @overload
    def GetEdgeLabelColor(self, c: MutableSequence[float]) -> None: ...
    def GetLineWidth(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutlineColor(self) -> Tuple[float, float, float]: ...
    @overload
    def GetPointAlphaRange(self) -> Pointer: ...
    @overload
    def GetPointAlphaRange(self, mn: float, mx: float) -> None: ...
    @overload
    def GetPointAlphaRange(self, rng: MutableSequence[float]) -> None: ...
    def GetPointColor(self) -> Tuple[float, float, float]: ...
    @overload
    def GetPointHueRange(self) -> Pointer: ...
    @overload
    def GetPointHueRange(self, mn: float, mx: float) -> None: ...
    @overload
    def GetPointHueRange(self, rng: MutableSequence[float]) -> None: ...
    def GetPointLookupTable(self) -> vtkmodules.vtkCommonCore.vtkScalarsToColors: ...
    def GetPointOpacity(self) -> float: ...
    @overload
    def GetPointSaturationRange(self) -> Pointer: ...
    @overload
    def GetPointSaturationRange(self, mn: float, mx: float) -> None: ...
    @overload
    def GetPointSaturationRange(self, rng: MutableSequence[float]) -> None: ...
    def GetPointSize(self) -> float: ...
    def GetPointTextProperty(self) -> vtkmodules.vtkRenderingCore.vtkTextProperty: ...
    @overload
    def GetPointValueRange(self) -> Pointer: ...
    @overload
    def GetPointValueRange(self, mn: float, mx: float) -> None: ...
    @overload
    def GetPointValueRange(self, rng: MutableSequence[float]) -> None: ...
    def GetScaleCellLookupTable(self) -> bool: ...
    def GetScalePointLookupTable(self) -> bool: ...
    def GetSelectedCellColor(self) -> Tuple[float, float, float]: ...
    def GetSelectedCellOpacity(self) -> float: ...
    def GetSelectedPointColor(self) -> Tuple[float, float, float]: ...
    def GetSelectedPointOpacity(self) -> float: ...
    @overload
    def GetVertexLabelColor(self) -> Pointer: ...
    @overload
    def GetVertexLabelColor(self, r: float, g: float, b: float) -> None: ...
    @overload
    def GetVertexLabelColor(self, c: MutableSequence[float]) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def LookupMatchesCellTheme(self, s2c: vtkmodules.vtkCommonCore.vtkScalarsToColors) -> bool: ...
    def LookupMatchesPointTheme(self, s2c: vtkmodules.vtkCommonCore.vtkScalarsToColors) -> bool: ...
    def NewInstance(self) -> vtkViewTheme: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkViewTheme: ...
    def ScaleCellLookupTableOff(self) -> None: ...
    def ScaleCellLookupTableOn(self) -> None: ...
    def ScalePointLookupTableOff(self) -> None: ...
    def ScalePointLookupTableOn(self) -> None: ...
    @overload
    def SetBackgroundColor(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetBackgroundColor(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetBackgroundColor2(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetBackgroundColor2(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetCellAlphaRange(self, mn: float, mx: float) -> None: ...
    @overload
    def SetCellAlphaRange(self, rng: MutableSequence[float]) -> None: ...
    @overload
    def SetCellColor(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetCellColor(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetCellHueRange(self, mn: float, mx: float) -> None: ...
    @overload
    def SetCellHueRange(self, rng: MutableSequence[float]) -> None: ...
    def SetCellLookupTable(self, lut: vtkmodules.vtkCommonCore.vtkScalarsToColors) -> None: ...
    def SetCellOpacity(self, _arg: float) -> None: ...
    @overload
    def SetCellSaturationRange(self, mn: float, mx: float) -> None: ...
    @overload
    def SetCellSaturationRange(self, rng: MutableSequence[float]) -> None: ...
    def SetCellTextProperty(self, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty) -> None: ...
    @overload
    def SetCellValueRange(self, mn: float, mx: float) -> None: ...
    @overload
    def SetCellValueRange(self, rng: MutableSequence[float]) -> None: ...
    @overload
    def SetEdgeLabelColor(self, r: float, g: float, b: float) -> None: ...
    @overload
    def SetEdgeLabelColor(self, c: MutableSequence[float]) -> None: ...
    def SetLineWidth(self, _arg: float) -> None: ...
    @overload
    def SetOutlineColor(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetOutlineColor(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetPointAlphaRange(self, mn: float, mx: float) -> None: ...
    @overload
    def SetPointAlphaRange(self, rng: MutableSequence[float]) -> None: ...
    @overload
    def SetPointColor(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetPointColor(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetPointHueRange(self, mn: float, mx: float) -> None: ...
    @overload
    def SetPointHueRange(self, rng: MutableSequence[float]) -> None: ...
    def SetPointLookupTable(self, lut: vtkmodules.vtkCommonCore.vtkScalarsToColors) -> None: ...
    def SetPointOpacity(self, _arg: float) -> None: ...
    @overload
    def SetPointSaturationRange(self, mn: float, mx: float) -> None: ...
    @overload
    def SetPointSaturationRange(self, rng: MutableSequence[float]) -> None: ...
    def SetPointSize(self, _arg: float) -> None: ...
    def SetPointTextProperty(self, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty) -> None: ...
    @overload
    def SetPointValueRange(self, mn: float, mx: float) -> None: ...
    @overload
    def SetPointValueRange(self, rng: MutableSequence[float]) -> None: ...
    def SetScaleCellLookupTable(self, _arg: bool) -> None: ...
    def SetScalePointLookupTable(self, _arg: bool) -> None: ...
    @overload
    def SetSelectedCellColor(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetSelectedCellColor(self, _arg: Sequence[float]) -> None: ...
    def SetSelectedCellOpacity(self, _arg: float) -> None: ...
    @overload
    def SetSelectedPointColor(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetSelectedPointColor(self, _arg: Sequence[float]) -> None: ...
    def SetSelectedPointOpacity(self, _arg: float) -> None: ...
    @overload
    def SetVertexLabelColor(self, r: float, g: float, b: float) -> None: ...
    @overload
    def SetVertexLabelColor(self, c: MutableSequence[float]) -> None: ...
