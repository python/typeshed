from collections.abc import MutableSequence, Sequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkCommonTransforms
import vtkmodules.vtkFiltersGeneral
import vtkmodules.vtkRenderingCore

Buffer = TypeVar("Buffer")

VTK_LABEL_FIELD_DATA: int
VTK_LABEL_IDS: int
VTK_LABEL_NORMALS: int
VTK_LABEL_SCALARS: int
VTK_LABEL_TCOORDS: int
VTK_LABEL_TENSORS: int
VTK_LABEL_VECTORS: int

class vtkLabeledDataMapper(vtkmodules.vtkRenderingCore.vtkMapper2D):
    class Coordinates(int): ...
    DISPLAY: Coordinates
    WORLD: Coordinates
    def CoordinateSystemDisplay(self) -> None: ...
    def CoordinateSystemWorld(self) -> None: ...
    def GetComponentSeparator(self) -> str: ...
    def GetCoordinateSystem(self) -> int: ...
    def GetCoordinateSystemMaxValue(self) -> int: ...
    def GetCoordinateSystemMinValue(self) -> int: ...
    def GetFieldDataArray(self) -> int: ...
    def GetFieldDataName(self) -> str: ...
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkDataSet: ...
    def GetLabelFormat(self) -> str: ...
    def GetLabelMode(self) -> int: ...
    def GetLabelPosition(self, label: int, pos: MutableSequence[float]) -> None: ...
    def GetLabelText(self, label: int) -> str: ...
    @overload
    def GetLabelTextProperty(self) -> vtkmodules.vtkRenderingCore.vtkTextProperty: ...
    @overload
    def GetLabelTextProperty(self, type: int) -> vtkmodules.vtkRenderingCore.vtkTextProperty: ...
    def GetLabeledComponent(self) -> int: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfLabels(self) -> int: ...
    def GetTransform(self) -> vtkmodules.vtkCommonTransforms.vtkTransform: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLabeledDataMapper: ...
    def ReleaseGraphicsResources(self, __a: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    def RenderOpaqueGeometry(
        self, viewport: vtkmodules.vtkRenderingCore.vtkViewport, actor: vtkmodules.vtkRenderingCore.vtkActor2D
    ) -> None: ...
    def RenderOverlay(
        self, viewport: vtkmodules.vtkRenderingCore.vtkViewport, actor: vtkmodules.vtkRenderingCore.vtkActor2D
    ) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLabeledDataMapper: ...
    def SetComponentSeparator(self, _arg: str) -> None: ...
    def SetCoordinateSystem(self, _arg: int) -> None: ...
    def SetFieldDataArray(self, arrayIndex: int) -> None: ...
    def SetFieldDataName(self, arrayName: str) -> None: ...
    def SetInputData(self, __a: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetLabelFormat(self, _arg: str) -> None: ...
    def SetLabelMode(self, _arg: int) -> None: ...
    def SetLabelModeToLabelFieldData(self) -> None: ...
    def SetLabelModeToLabelIds(self) -> None: ...
    def SetLabelModeToLabelNormals(self) -> None: ...
    def SetLabelModeToLabelScalars(self) -> None: ...
    def SetLabelModeToLabelTCoords(self) -> None: ...
    def SetLabelModeToLabelTensors(self) -> None: ...
    def SetLabelModeToLabelVectors(self) -> None: ...
    @overload
    def SetLabelTextProperty(self, p: vtkmodules.vtkRenderingCore.vtkTextProperty) -> None: ...
    @overload
    def SetLabelTextProperty(self, p: vtkmodules.vtkRenderingCore.vtkTextProperty, type: int) -> None: ...
    def SetLabeledComponent(self, _arg: int) -> None: ...
    def SetTransform(self, t: vtkmodules.vtkCommonTransforms.vtkTransform) -> None: ...

class vtkDynamic2DLabelMapper(vtkLabeledDataMapper):
    def GetLabelHeightPadding(self) -> float: ...
    def GetLabelWidthPadding(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetReversePriority(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkDynamic2DLabelMapper: ...
    def RenderOpaqueGeometry(
        self, viewport: vtkmodules.vtkRenderingCore.vtkViewport, actor: vtkmodules.vtkRenderingCore.vtkActor2D
    ) -> None: ...
    def RenderOverlay(
        self, viewport: vtkmodules.vtkRenderingCore.vtkViewport, actor: vtkmodules.vtkRenderingCore.vtkActor2D
    ) -> None: ...
    def ReversePriorityOff(self) -> None: ...
    def ReversePriorityOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkDynamic2DLabelMapper: ...
    def SetLabelHeightPadding(self, _arg: float) -> None: ...
    def SetLabelWidthPadding(self, _arg: float) -> None: ...
    def SetPriorityArrayName(self, name: str) -> None: ...
    def SetReversePriority(self, _arg: bool) -> None: ...

class vtkLabelRenderStrategy(vtkmodules.vtkCommonCore.vtkObject):
    def ComputeLabelBounds(
        self, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, label: str, bds: MutableSequence[float]
    ) -> None: ...
    def EndFrame(self) -> None: ...
    def GetDefaultTextProperty(self) -> vtkmodules.vtkRenderingCore.vtkTextProperty: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRenderer(self) -> vtkmodules.vtkRenderingCore.vtkRenderer: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLabelRenderStrategy: ...
    def ReleaseGraphicsResources(self, __a: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    @overload
    def RenderLabel(self, x: MutableSequence[int], tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, label: str) -> None: ...
    @overload
    def RenderLabel(
        self, x: MutableSequence[int], tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, label: str, maxWidth: int
    ) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLabelRenderStrategy: ...
    def SetDefaultTextProperty(self, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty) -> None: ...
    def SetRenderer(self, ren: vtkmodules.vtkRenderingCore.vtkRenderer) -> None: ...
    def StartFrame(self) -> None: ...
    def SupportsBoundedSize(self) -> bool: ...
    def SupportsRotation(self) -> bool: ...

class vtkFreeTypeLabelRenderStrategy(vtkLabelRenderStrategy):
    def ComputeLabelBounds(
        self, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, label: str, bds: MutableSequence[float]
    ) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkFreeTypeLabelRenderStrategy: ...
    def ReleaseGraphicsResources(self, window: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    def RenderLabel(self, x: MutableSequence[int], tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, label: str) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkFreeTypeLabelRenderStrategy: ...
    def SupportsBoundedSize(self) -> bool: ...
    def SupportsRotation(self) -> bool: ...

class vtkLabelHierarchy(vtkmodules.vtkCommonDataModel.vtkPointSet):
    class IteratorType(int): ...
    DEPTH_FIRST: IteratorType
    FRUSTUM: IteratorType
    FULL_SORT: IteratorType
    QUEUE: IteratorType
    def ComputeHierarchy(self) -> None: ...
    @overload
    def FindCell(
        self,
        __a: MutableSequence[float],
        __b: vtkmodules.vtkCommonDataModel.vtkCell,
        __c: int,
        __d: float,
        __e: int,
        __f: MutableSequence[float],
        __g: MutableSequence[float],
    ) -> int: ...
    @overload
    def FindCell(
        self,
        __a: MutableSequence[float],
        __b: vtkmodules.vtkCommonDataModel.vtkCell,
        __c: vtkmodules.vtkCommonDataModel.vtkGenericCell,
        __d: int,
        __e: float,
        __f: int,
        __g: MutableSequence[float],
        __h: MutableSequence[float],
    ) -> int: ...
    @staticmethod
    def GetAnchorFrustumPlanes(
        frustumPlanes: MutableSequence[float],
        ren: vtkmodules.vtkRenderingCore.vtkRenderer,
        anchorTransform: vtkmodules.vtkRenderingCore.vtkCoordinate,
    ) -> None: ...
    def GetBoundedSizes(self) -> vtkmodules.vtkCommonCore.vtkDataArray: ...
    @overload
    def GetCell(self, __a: int) -> vtkmodules.vtkCommonDataModel.vtkCell: ...
    @overload
    def GetCell(self, __a: int, __b: vtkmodules.vtkCommonDataModel.vtkGenericCell) -> None: ...
    @overload
    def GetCell(self, i: int, j: int, k: int) -> vtkmodules.vtkCommonDataModel.vtkCell: ...
    def GetCellPoints(self, __a: int, __b: vtkmodules.vtkCommonCore.vtkIdList) -> None: ...
    def GetCellType(self, __a: int) -> int: ...
    def GetCenterPts(self) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    def GetCoincidentPoints(self) -> vtkmodules.vtkFiltersGeneral.vtkCoincidentPoints: ...
    def GetDiscreteNodeCoordinatesFromWorldPoint(
        self, ijk: MutableSequence[int], pt: MutableSequence[float], level: int
    ) -> None: ...
    def GetIconIndices(self) -> vtkmodules.vtkCommonCore.vtkIntArray: ...
    def GetLabels(self) -> vtkmodules.vtkCommonCore.vtkAbstractArray: ...
    def GetMaxCellSize(self) -> int: ...
    def GetMaximumDepth(self) -> int: ...
    def GetNumberOfCells(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOrientations(self) -> vtkmodules.vtkCommonCore.vtkDataArray: ...
    @staticmethod
    def GetPathForNodalCoordinates(path: MutableSequence[int], ijk: MutableSequence[int], level: int) -> bool: ...
    def GetPointCells(self, __a: int, __b: vtkmodules.vtkCommonCore.vtkIdList) -> None: ...
    def GetPriorities(self) -> vtkmodules.vtkCommonCore.vtkDataArray: ...
    def GetSizes(self) -> vtkmodules.vtkCommonCore.vtkDataArray: ...
    def GetTargetLabelCount(self) -> int: ...
    def GetTextProperty(self) -> vtkmodules.vtkRenderingCore.vtkTextProperty: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLabelHierarchy: ...
    def NewIterator(
        self,
        type: int,
        ren: vtkmodules.vtkRenderingCore.vtkRenderer,
        cam: vtkmodules.vtkRenderingCore.vtkCamera,
        frustumPlanes: MutableSequence[float],
        positionsAsNormals: bool,
        bucketSize: MutableSequence[float],
    ) -> vtkLabelHierarchyIterator: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLabelHierarchy: ...
    def SetBoundedSizes(self, arr: vtkmodules.vtkCommonCore.vtkDataArray) -> None: ...
    def SetIconIndices(self, arr: vtkmodules.vtkCommonCore.vtkIntArray) -> None: ...
    def SetLabels(self, arr: vtkmodules.vtkCommonCore.vtkAbstractArray) -> None: ...
    def SetMaximumDepth(self, _arg: int) -> None: ...
    def SetOrientations(self, arr: vtkmodules.vtkCommonCore.vtkDataArray) -> None: ...
    def SetPoints(self, __a: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...
    def SetPriorities(self, arr: vtkmodules.vtkCommonCore.vtkDataArray) -> None: ...
    def SetSizes(self, arr: vtkmodules.vtkCommonCore.vtkDataArray) -> None: ...
    def SetTargetLabelCount(self, _arg: int) -> None: ...
    def SetTextProperty(self, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty) -> None: ...

class vtkLabelHierarchyAlgorithm(vtkmodules.vtkCommonExecutionModel.vtkAlgorithm):
    @overload
    def AddInputData(self, __a: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    @overload
    def AddInputData(self, __a: int, __b: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    @overload
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkDataObject: ...
    @overload
    def GetInput(self, port: int) -> vtkmodules.vtkCommonDataModel.vtkDataObject: ...
    def GetLabelHierarchyInput(self, port: int) -> vtkLabelHierarchy: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    @overload
    def GetOutput(self) -> vtkLabelHierarchy: ...
    @overload
    def GetOutput(self, __a: int) -> vtkLabelHierarchy: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLabelHierarchyAlgorithm: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLabelHierarchyAlgorithm: ...
    @overload
    def SetInputData(self, __a: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    @overload
    def SetInputData(self, __a: int, __b: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetOutput(self, d: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...

class vtkLabelHierarchyIterator(vtkmodules.vtkCommonCore.vtkObject):
    def Begin(self, __a: vtkmodules.vtkCommonCore.vtkIdTypeArray) -> None: ...
    def BoxAllNodes(self, __a: vtkmodules.vtkCommonDataModel.vtkPolyData) -> None: ...
    def BoxNode(self) -> None: ...
    def GetAllBounds(self) -> int: ...
    def GetBoundedSize(self, sz: MutableSequence[float]) -> None: ...
    def GetHierarchy(self) -> vtkLabelHierarchy: ...
    def GetLabel(self) -> str: ...
    def GetLabelId(self) -> int: ...
    def GetNodeGeometry(self, ctr: MutableSequence[float], size: float) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOrientation(self) -> float: ...
    def GetPoint(self, x: MutableSequence[float]) -> None: ...
    def GetSize(self, sz: MutableSequence[float]) -> None: ...
    def GetType(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    def IsAtEnd(self) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLabelHierarchyIterator: ...
    def Next(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLabelHierarchyIterator: ...
    def SetAllBounds(self, _arg: int) -> None: ...
    def SetTraversedBounds(self, __a: vtkmodules.vtkCommonDataModel.vtkPolyData) -> None: ...

class vtkLabelHierarchyCompositeIterator(vtkLabelHierarchyIterator):
    @overload
    def AddIterator(self, it: vtkLabelHierarchyIterator) -> None: ...
    @overload
    def AddIterator(self, it: vtkLabelHierarchyIterator, count: int) -> None: ...
    def Begin(self, __a: vtkmodules.vtkCommonCore.vtkIdTypeArray) -> None: ...
    def BoxAllNodes(self, __a: vtkmodules.vtkCommonDataModel.vtkPolyData) -> None: ...
    def BoxNode(self) -> None: ...
    def ClearIterators(self) -> None: ...
    def GetHierarchy(self) -> vtkLabelHierarchy: ...
    def GetLabelId(self) -> int: ...
    def GetNodeGeometry(self, ctr: MutableSequence[float], size: float) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    def IsAtEnd(self) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLabelHierarchyCompositeIterator: ...
    def Next(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLabelHierarchyCompositeIterator: ...

class vtkLabelPlacementMapper(vtkmodules.vtkRenderingCore.vtkMapper2D):
    class LabelStyle(int): ...
    class LabelShape(int): ...
    FILLED: LabelStyle
    NONE: LabelShape
    NUMBER_OF_LABEL_SHAPES: LabelShape
    NUMBER_OF_LABEL_STYLES: LabelStyle
    OUTLINE: LabelStyle
    RECT: LabelShape
    ROUNDED_RECT: LabelShape
    def GeneratePerturbedLabelSpokesOff(self) -> None: ...
    def GeneratePerturbedLabelSpokesOn(self) -> None: ...
    def GetAnchorTransform(self) -> vtkmodules.vtkRenderingCore.vtkCoordinate: ...
    def GetBackgroundColor(self) -> Tuple[float, float, float]: ...
    def GetBackgroundOpacity(self) -> float: ...
    def GetBackgroundOpacityMaxValue(self) -> float: ...
    def GetBackgroundOpacityMinValue(self) -> float: ...
    def GetGeneratePerturbedLabelSpokes(self) -> bool: ...
    def GetIteratorType(self) -> int: ...
    def GetMargin(self) -> float: ...
    def GetMaximumLabelFraction(self) -> float: ...
    def GetMaximumLabelFractionMaxValue(self) -> float: ...
    def GetMaximumLabelFractionMinValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputTraversedBounds(self) -> bool: ...
    def GetPlaceAllLabels(self) -> bool: ...
    def GetPositionsAsNormals(self) -> bool: ...
    def GetRenderStrategy(self) -> vtkLabelRenderStrategy: ...
    def GetShape(self) -> int: ...
    def GetShapeMaxValue(self) -> int: ...
    def GetShapeMinValue(self) -> int: ...
    def GetStyle(self) -> int: ...
    def GetStyleMaxValue(self) -> int: ...
    def GetStyleMinValue(self) -> int: ...
    def GetUseDepthBuffer(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLabelPlacementMapper: ...
    def OutputTraversedBoundsOff(self) -> None: ...
    def OutputTraversedBoundsOn(self) -> None: ...
    def PlaceAllLabelsOff(self) -> None: ...
    def PlaceAllLabelsOn(self) -> None: ...
    def PositionsAsNormalsOff(self) -> None: ...
    def PositionsAsNormalsOn(self) -> None: ...
    def ReleaseGraphicsResources(self, __a: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    def RenderOverlay(
        self, viewport: vtkmodules.vtkRenderingCore.vtkViewport, actor: vtkmodules.vtkRenderingCore.vtkActor2D
    ) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLabelPlacementMapper: ...
    @overload
    def SetBackgroundColor(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetBackgroundColor(self, _arg: Sequence[float]) -> None: ...
    def SetBackgroundOpacity(self, _arg: float) -> None: ...
    def SetGeneratePerturbedLabelSpokes(self, _arg: bool) -> None: ...
    def SetIteratorType(self, _arg: int) -> None: ...
    def SetMargin(self, _arg: float) -> None: ...
    def SetMaximumLabelFraction(self, _arg: float) -> None: ...
    def SetOutputTraversedBounds(self, _arg: bool) -> None: ...
    def SetPlaceAllLabels(self, _arg: bool) -> None: ...
    def SetPositionsAsNormals(self, _arg: bool) -> None: ...
    def SetRenderStrategy(self, s: vtkLabelRenderStrategy) -> None: ...
    def SetShape(self, _arg: int) -> None: ...
    def SetShapeToNone(self) -> None: ...
    def SetShapeToRect(self) -> None: ...
    def SetShapeToRoundedRect(self) -> None: ...
    def SetStyle(self, _arg: int) -> None: ...
    def SetStyleToFilled(self) -> None: ...
    def SetStyleToOutline(self) -> None: ...
    def SetUseDepthBuffer(self, _arg: bool) -> None: ...
    def UseDepthBufferOff(self) -> None: ...
    def UseDepthBufferOn(self) -> None: ...

class vtkLabelPlacer(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    class LabelGravity(int): ...
    class OutputCoordinates(int): ...
    BaselineCenter: LabelGravity
    BaselineLeft: LabelGravity
    BaselineRight: LabelGravity
    CenterCenter: LabelGravity
    CenterLeft: LabelGravity
    CenterRight: LabelGravity
    DISPLAY: OutputCoordinates
    HorizontalBitMask: LabelGravity
    HorizontalCenterBit: LabelGravity
    HorizontalLeftBit: LabelGravity
    HorizontalRightBit: LabelGravity
    LowerCenter: LabelGravity
    LowerLeft: LabelGravity
    LowerRight: LabelGravity
    UpperCenter: LabelGravity
    UpperLeft: LabelGravity
    UpperRight: LabelGravity
    VerticalBaselineBit: LabelGravity
    VerticalBitMask: LabelGravity
    VerticalBottomBit: LabelGravity
    VerticalCenterBit: LabelGravity
    VerticalTopBit: LabelGravity
    WORLD: OutputCoordinates
    def GeneratePerturbedLabelSpokesOff(self) -> None: ...
    def GeneratePerturbedLabelSpokesOn(self) -> None: ...
    def GetAnchorTransform(self) -> vtkmodules.vtkRenderingCore.vtkCoordinate: ...
    def GetGeneratePerturbedLabelSpokes(self) -> bool: ...
    def GetGravity(self) -> int: ...
    def GetIteratorType(self) -> int: ...
    def GetMTime(self) -> int: ...
    def GetMaximumLabelFraction(self) -> float: ...
    def GetMaximumLabelFractionMaxValue(self) -> float: ...
    def GetMaximumLabelFractionMinValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputCoordinateSystem(self) -> int: ...
    def GetOutputCoordinateSystemMaxValue(self) -> int: ...
    def GetOutputCoordinateSystemMinValue(self) -> int: ...
    def GetOutputTraversedBounds(self) -> bool: ...
    def GetPositionsAsNormals(self) -> bool: ...
    def GetRenderer(self) -> vtkmodules.vtkRenderingCore.vtkRenderer: ...
    def GetUseDepthBuffer(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLabelPlacer: ...
    def OutputCoordinateSystemDisplay(self) -> None: ...
    def OutputCoordinateSystemWorld(self) -> None: ...
    def OutputTraversedBoundsOff(self) -> None: ...
    def OutputTraversedBoundsOn(self) -> None: ...
    def PositionsAsNormalsOff(self) -> None: ...
    def PositionsAsNormalsOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLabelPlacer: ...
    def SetGeneratePerturbedLabelSpokes(self, _arg: bool) -> None: ...
    def SetGravity(self, gravity: int) -> None: ...
    def SetIteratorType(self, _arg: int) -> None: ...
    def SetMaximumLabelFraction(self, _arg: float) -> None: ...
    def SetOutputCoordinateSystem(self, _arg: int) -> None: ...
    def SetOutputTraversedBounds(self, _arg: bool) -> None: ...
    def SetPositionsAsNormals(self, _arg: bool) -> None: ...
    def SetRenderer(self, __a: vtkmodules.vtkRenderingCore.vtkRenderer) -> None: ...
    def SetUseDepthBuffer(self, _arg: bool) -> None: ...
    def UseDepthBufferOff(self) -> None: ...
    def UseDepthBufferOn(self) -> None: ...

class vtkLabelSizeCalculator(vtkmodules.vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    def GetDPI(self) -> int: ...
    def GetFontProperty(self, type: int = 0) -> vtkmodules.vtkRenderingCore.vtkTextProperty: ...
    def GetLabelSizeArrayName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLabelSizeCalculator: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLabelSizeCalculator: ...
    def SetDPI(self, _arg: int) -> None: ...
    def SetFontProperty(self, fontProp: vtkmodules.vtkRenderingCore.vtkTextProperty, type: int = 0) -> None: ...
    def SetLabelSizeArrayName(self, _arg: str) -> None: ...

class vtkLabeledTreeMapDataMapper(vtkLabeledDataMapper):
    def GetChildMotion(self) -> int: ...
    def GetClipTextMode(self) -> int: ...
    def GetDynamicLevel(self) -> int: ...
    def GetFontSizeRange(self, range: MutableSequence[int]) -> None: ...
    def GetInputTree(self) -> vtkmodules.vtkCommonDataModel.vtkTree: ...
    def GetLevelRange(self, range: MutableSequence[int]) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLabeledTreeMapDataMapper: ...
    def ReleaseGraphicsResources(self, __a: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    def RenderOpaqueGeometry(
        self, viewport: vtkmodules.vtkRenderingCore.vtkViewport, actor: vtkmodules.vtkRenderingCore.vtkActor2D
    ) -> None: ...
    def RenderOverlay(
        self, viewport: vtkmodules.vtkRenderingCore.vtkViewport, actor: vtkmodules.vtkRenderingCore.vtkActor2D
    ) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLabeledTreeMapDataMapper: ...
    def SetChildMotion(self, _arg: int) -> None: ...
    def SetClipTextMode(self, _arg: int) -> None: ...
    def SetDynamicLevel(self, _arg: int) -> None: ...
    def SetFontSizeRange(self, maxSize: int, minSize: int, delta: int = 4) -> None: ...
    def SetLevelRange(self, startLevel: int, endLevel: int) -> None: ...
    def SetRectanglesArrayName(self, name: str) -> None: ...

class vtkPointSetToLabelHierarchy(vtkLabelHierarchyAlgorithm):
    def GetBoundedSizeArrayName(self) -> str: ...
    def GetIconIndexArrayName(self) -> str: ...
    def GetLabelArrayName(self) -> str: ...
    def GetMaximumDepth(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOrientationArrayName(self) -> str: ...
    def GetPriorityArrayName(self) -> str: ...
    def GetSizeArrayName(self) -> str: ...
    def GetTargetLabelCount(self) -> int: ...
    def GetTextProperty(self) -> vtkmodules.vtkRenderingCore.vtkTextProperty: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPointSetToLabelHierarchy: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPointSetToLabelHierarchy: ...
    def SetBoundedSizeArrayName(self, name: str) -> None: ...
    def SetIconIndexArrayName(self, name: str) -> None: ...
    def SetLabelArrayName(self, name: str) -> None: ...
    def SetMaximumDepth(self, _arg: int) -> None: ...
    def SetOrientationArrayName(self, name: str) -> None: ...
    def SetPriorityArrayName(self, name: str) -> None: ...
    def SetSizeArrayName(self, name: str) -> None: ...
    def SetTargetLabelCount(self, _arg: int) -> None: ...
    def SetTextProperty(self, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty) -> None: ...
