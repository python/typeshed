from collections.abc import MutableSequence, Sequence
from typing import Tuple, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkCommonTransforms
import vtkmodules.vtkFiltersGeometry
import vtkmodules.vtkRenderingCore

VTK_BSPLINE_EDGE: int
VTK_BSPLINE_ZERO: int
VTK_BSPLINE_ZERO_AT_BORDER: int
VTK_CELL_MODE: int
VTK_COLOR_MODE_LINEAR_256: int
VTK_COLOR_MODE_LUT: int
VTK_ERROR_ABSOLUTE: int
VTK_ERROR_NUMBER_OF_TRIANGLES: int
VTK_ERROR_RELATIVE: int
VTK_ERROR_SPECIFIED_REDUCTION: int
VTK_GRID_CUBIC: int
VTK_GRID_LINEAR: int
VTK_GRID_NEAREST: int
VTK_STYLE_PIXELIZE: int
VTK_STYLE_POLYGONALIZE: int
VTK_STYLE_RUN_LENGTH: int
VTK_VOXEL_MODE: int

class vtkAdaptiveDataSetSurfaceFilter(vtkmodules.vtkFiltersGeometry.vtkGeometryFilter):
    def GetBBSelection(self) -> bool: ...
    def GetCircleSelection(self) -> bool: ...
    def GetDynamicDecimateLevelMax(self) -> int: ...
    def GetFixedLevelMax(self) -> int: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRenderer(self) -> vtkmodules.vtkRenderingCore.vtkRenderer: ...
    def GetScale(self) -> float: ...
    def GetViewPointDepend(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkAdaptiveDataSetSurfaceFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkAdaptiveDataSetSurfaceFilter: ...
    def SetBBSelection(self, _arg: bool) -> None: ...
    def SetCircleSelection(self, _arg: bool) -> None: ...
    def SetDynamicDecimateLevelMax(self, _arg: int) -> None: ...
    def SetFixedLevelMax(self, _arg: int) -> None: ...
    def SetRenderer(self, ren: vtkmodules.vtkRenderingCore.vtkRenderer) -> None: ...
    def SetScale(self, _arg: float) -> None: ...
    def SetViewPointDepend(self, _arg: bool) -> None: ...

class vtkBSplineTransform(vtkmodules.vtkCommonTransforms.vtkWarpTransform):
    def GetBorderMode(self) -> int: ...
    def GetBorderModeAsString(self) -> str: ...
    def GetBorderModeMaxValue(self) -> int: ...
    def GetBorderModeMinValue(self) -> int: ...
    def GetCoefficientData(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetDisplacementScale(self) -> float: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkmodules.vtkCommonTransforms.vtkAbstractTransform: ...
    def NewInstance(self) -> vtkBSplineTransform: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkBSplineTransform: ...
    def SetBorderMode(self, _arg: int) -> None: ...
    def SetBorderModeToEdge(self) -> None: ...
    def SetBorderModeToZero(self) -> None: ...
    def SetBorderModeToZeroAtBorder(self) -> None: ...
    def SetCoefficientConnection(self, __a: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetCoefficientData(self, __a: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    def SetDisplacementScale(self, _arg: float) -> None: ...

class vtkDSPFilterDefinition(vtkmodules.vtkCommonCore.vtkObject):
    def Clear(self) -> None: ...
    def Copy(self, other: vtkDSPFilterDefinition) -> None: ...
    def GetDenominatorWeight(self, a_which: int) -> float: ...
    def GetForwardNumeratorWeight(self, a_which: int) -> float: ...
    def GetInputVariableName(self) -> str: ...
    def GetNumDenominatorWeights(self) -> int: ...
    def GetNumForwardNumeratorWeights(self) -> int: ...
    def GetNumNumeratorWeights(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumeratorWeight(self, a_which: int) -> float: ...
    def GetOutputVariableName(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    def IsThisInputVariableInstanceNeeded(self, a_timestep: int, a_outputTimestep: int) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkDSPFilterDefinition: ...
    def PushBackDenominatorWeight(self, a_value: float) -> None: ...
    def PushBackForwardNumeratorWeight(self, a_value: float) -> None: ...
    def PushBackNumeratorWeight(self, a_value: float) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkDSPFilterDefinition: ...
    def SetInputVariableName(self, a_value: str) -> None: ...
    def SetOutputVariableName(self, a_value: str) -> None: ...

class vtkDSPFilterGroup(vtkmodules.vtkCommonCore.vtkObject):
    def AddFilter(self, filter: vtkDSPFilterDefinition) -> None: ...
    def AddInputVariableInstance(self, a_name: str, a_timestep: int, a_data: vtkmodules.vtkCommonCore.vtkFloatArray) -> None: ...
    def Copy(self, other: vtkDSPFilterGroup) -> None: ...
    def GetCachedInput(self, a_whichFilter: int, a_whichTimestep: int) -> vtkmodules.vtkCommonCore.vtkFloatArray: ...
    def GetCachedOutput(self, a_whichFilter: int, a_whichTimestep: int) -> vtkmodules.vtkCommonCore.vtkFloatArray: ...
    def GetFilter(self, a_whichFilter: int) -> vtkDSPFilterDefinition: ...
    def GetInputVariableName(self, a_whichFilter: int) -> str: ...
    def GetNumFilters(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutput(
        self, a_whichFilter: int, a_whichTimestep: int, a_instancesCalculated: int
    ) -> vtkmodules.vtkCommonCore.vtkFloatArray: ...
    def IsA(self, type: str) -> int: ...
    def IsThisInputVariableInstanceCached(self, a_name: str, a_timestep: int) -> bool: ...
    def IsThisInputVariableInstanceNeeded(self, a_name: str, a_timestep: int, a_outputTimestep: int) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkDSPFilterGroup: ...
    def RemoveFilter(self, a_outputVariableName: str) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkDSPFilterGroup: ...

class vtkDepthSortPolyData(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    class Directions(int): ...
    class SortMode(int): ...
    VTK_DIRECTION_BACK_TO_FRONT: Directions
    VTK_DIRECTION_FRONT_TO_BACK: Directions
    VTK_DIRECTION_SPECIFIED_VECTOR: Directions
    VTK_SORT_BOUNDS_CENTER: SortMode
    VTK_SORT_FIRST_POINT: SortMode
    VTK_SORT_PARAMETRIC_CENTER: SortMode
    def GetCamera(self) -> vtkmodules.vtkRenderingCore.vtkCamera: ...
    def GetDepthSortMode(self) -> int: ...
    def GetDirection(self) -> int: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOrigin(self) -> Tuple[float, float, float]: ...
    def GetProp3D(self) -> vtkmodules.vtkRenderingCore.vtkProp3D: ...
    def GetSortScalars(self) -> int: ...
    def GetVector(self) -> Tuple[float, float, float]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkDepthSortPolyData: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkDepthSortPolyData: ...
    def SetCamera(self, __a: vtkmodules.vtkRenderingCore.vtkCamera) -> None: ...
    def SetDepthSortMode(self, _arg: int) -> None: ...
    def SetDepthSortModeToBoundsCenter(self) -> None: ...
    def SetDepthSortModeToFirstPoint(self) -> None: ...
    def SetDepthSortModeToParametricCenter(self) -> None: ...
    def SetDirection(self, _arg: int) -> None: ...
    def SetDirectionToBackToFront(self) -> None: ...
    def SetDirectionToFrontToBack(self) -> None: ...
    def SetDirectionToSpecifiedVector(self) -> None: ...
    @overload
    def SetOrigin(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetOrigin(self, _arg: Sequence[float]) -> None: ...
    def SetProp3D(self, __a: vtkmodules.vtkRenderingCore.vtkProp3D) -> None: ...
    def SetSortScalars(self, _arg: int) -> None: ...
    @overload
    def SetVector(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetVector(self, _arg: Sequence[float]) -> None: ...
    def SortScalarsOff(self) -> None: ...
    def SortScalarsOn(self) -> None: ...

class vtkEarthSource(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOnRatio(self) -> int: ...
    def GetOnRatioMaxValue(self) -> int: ...
    def GetOnRatioMinValue(self) -> int: ...
    def GetOutline(self) -> int: ...
    def GetRadius(self) -> float: ...
    def GetRadiusMaxValue(self) -> float: ...
    def GetRadiusMinValue(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkEarthSource: ...
    def OutlineOff(self) -> None: ...
    def OutlineOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkEarthSource: ...
    def SetOnRatio(self, _arg: int) -> None: ...
    def SetOutline(self, _arg: int) -> None: ...
    def SetRadius(self, _arg: float) -> None: ...

class vtkFacetReader(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    @staticmethod
    def CanReadFile(filename: str) -> int: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkFacetReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkFacetReader: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkForceTime(vtkmodules.vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    def GetForcedTime(self) -> float: ...
    def GetIgnorePipelineTime(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IgnorePipelineTimeOff(self) -> None: ...
    def IgnorePipelineTimeOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkForceTime: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkForceTime: ...
    def SetForcedTime(self, _arg: float) -> None: ...
    def SetIgnorePipelineTime(self, _arg: bool) -> None: ...

class vtkGenerateTimeSteps(vtkmodules.vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    def AddTimeStepValue(self, timeStepValue: float) -> None: ...
    def ClearTimeStepValues(self) -> None: ...
    def GenerateTimeStepValues(self, begin: float, end: float, step: float) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfTimeSteps(self) -> int: ...
    def GetTimeStepValues(self, timeStepValues: MutableSequence[float]) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGenerateTimeSteps: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGenerateTimeSteps: ...
    def SetTimeStepValues(self, count: int, timeStepValues: Sequence[float]) -> None: ...

class vtkGreedyTerrainDecimation(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def BoundaryVertexDeletionOff(self) -> None: ...
    def BoundaryVertexDeletionOn(self) -> None: ...
    def ComputeNormalsOff(self) -> None: ...
    def ComputeNormalsOn(self) -> None: ...
    def GetAbsoluteError(self) -> float: ...
    def GetAbsoluteErrorMaxValue(self) -> float: ...
    def GetAbsoluteErrorMinValue(self) -> float: ...
    def GetBoundaryVertexDeletion(self) -> int: ...
    def GetComputeNormals(self) -> int: ...
    def GetErrorMeasure(self) -> int: ...
    def GetErrorMeasureMaxValue(self) -> int: ...
    def GetErrorMeasureMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfTriangles(self) -> int: ...
    def GetNumberOfTrianglesMaxValue(self) -> int: ...
    def GetNumberOfTrianglesMinValue(self) -> int: ...
    def GetReduction(self) -> float: ...
    def GetReductionMaxValue(self) -> float: ...
    def GetReductionMinValue(self) -> float: ...
    def GetRelativeError(self) -> float: ...
    def GetRelativeErrorMaxValue(self) -> float: ...
    def GetRelativeErrorMinValue(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGreedyTerrainDecimation: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGreedyTerrainDecimation: ...
    def SetAbsoluteError(self, _arg: float) -> None: ...
    def SetBoundaryVertexDeletion(self, _arg: int) -> None: ...
    def SetComputeNormals(self, _arg: int) -> None: ...
    def SetErrorMeasure(self, _arg: int) -> None: ...
    def SetErrorMeasureToAbsoluteError(self) -> None: ...
    def SetErrorMeasureToNumberOfTriangles(self) -> None: ...
    def SetErrorMeasureToRelativeError(self) -> None: ...
    def SetErrorMeasureToSpecifiedReduction(self) -> None: ...
    def SetNumberOfTriangles(self, _arg: int) -> None: ...
    def SetReduction(self, _arg: float) -> None: ...
    def SetRelativeError(self, _arg: float) -> None: ...

class vtkGridTransform(vtkmodules.vtkCommonTransforms.vtkWarpTransform):
    def GetDisplacementGrid(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetDisplacementScale(self) -> float: ...
    def GetDisplacementShift(self) -> float: ...
    def GetInterpolationMode(self) -> int: ...
    def GetInterpolationModeAsString(self) -> str: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MakeTransform(self) -> vtkmodules.vtkCommonTransforms.vtkAbstractTransform: ...
    def NewInstance(self) -> vtkGridTransform: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGridTransform: ...
    def SetDisplacementGridConnection(self, __a: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetDisplacementGridData(self, __a: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    def SetDisplacementScale(self, _arg: float) -> None: ...
    def SetDisplacementShift(self, _arg: float) -> None: ...
    def SetInterpolationMode(self, mode: int) -> None: ...
    def SetInterpolationModeToCubic(self) -> None: ...
    def SetInterpolationModeToLinear(self) -> None: ...
    def SetInterpolationModeToNearestNeighbor(self) -> None: ...

class vtkImageToPolyDataFilter(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def DecimationOff(self) -> None: ...
    def DecimationOn(self) -> None: ...
    def GetColorMode(self) -> int: ...
    def GetColorModeMaxValue(self) -> int: ...
    def GetColorModeMinValue(self) -> int: ...
    def GetDecimation(self) -> int: ...
    def GetDecimationError(self) -> float: ...
    def GetDecimationErrorMaxValue(self) -> float: ...
    def GetDecimationErrorMinValue(self) -> float: ...
    def GetError(self) -> int: ...
    def GetErrorMaxValue(self) -> int: ...
    def GetErrorMinValue(self) -> int: ...
    def GetLookupTable(self) -> vtkmodules.vtkCommonCore.vtkScalarsToColors: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfSmoothingIterations(self) -> int: ...
    def GetNumberOfSmoothingIterationsMaxValue(self) -> int: ...
    def GetNumberOfSmoothingIterationsMinValue(self) -> int: ...
    def GetOutputStyle(self) -> int: ...
    def GetOutputStyleMaxValue(self) -> int: ...
    def GetOutputStyleMinValue(self) -> int: ...
    def GetSmoothing(self) -> int: ...
    def GetSubImageSize(self) -> int: ...
    def GetSubImageSizeMaxValue(self) -> int: ...
    def GetSubImageSizeMinValue(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageToPolyDataFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageToPolyDataFilter: ...
    def SetColorMode(self, _arg: int) -> None: ...
    def SetColorModeToLUT(self) -> None: ...
    def SetColorModeToLinear256(self) -> None: ...
    def SetDecimation(self, _arg: int) -> None: ...
    def SetDecimationError(self, _arg: float) -> None: ...
    def SetError(self, _arg: int) -> None: ...
    def SetLookupTable(self, __a: vtkmodules.vtkCommonCore.vtkScalarsToColors) -> None: ...
    def SetNumberOfSmoothingIterations(self, _arg: int) -> None: ...
    def SetOutputStyle(self, _arg: int) -> None: ...
    def SetOutputStyleToPixelize(self) -> None: ...
    def SetOutputStyleToPolygonalize(self) -> None: ...
    def SetOutputStyleToRunLength(self) -> None: ...
    def SetSmoothing(self, _arg: int) -> None: ...
    def SetSubImageSize(self, _arg: int) -> None: ...
    def SmoothingOff(self) -> None: ...
    def SmoothingOn(self) -> None: ...

class vtkImplicitModeller(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def AdjustBoundsOff(self) -> None: ...
    def AdjustBoundsOn(self) -> None: ...
    def Append(self, input: vtkmodules.vtkCommonDataModel.vtkDataSet) -> None: ...
    def CappingOff(self) -> None: ...
    def CappingOn(self) -> None: ...
    def ComputeModelBounds(self, input: vtkmodules.vtkCommonDataModel.vtkDataSet = ...) -> float: ...
    def EndAppend(self) -> None: ...
    def GetAdjustBounds(self) -> int: ...
    def GetAdjustDistance(self) -> float: ...
    def GetAdjustDistanceMaxValue(self) -> float: ...
    def GetAdjustDistanceMinValue(self) -> float: ...
    def GetCapValue(self) -> float: ...
    def GetCapping(self) -> int: ...
    def GetLocatorMaxLevel(self) -> int: ...
    def GetMaximumDistance(self) -> float: ...
    def GetMaximumDistanceMaxValue(self) -> float: ...
    def GetMaximumDistanceMinValue(self) -> float: ...
    def GetModelBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfThreads(self) -> int: ...
    def GetNumberOfThreadsMaxValue(self) -> int: ...
    def GetNumberOfThreadsMinValue(self) -> int: ...
    def GetOutputScalarType(self) -> int: ...
    def GetProcessMode(self) -> int: ...
    def GetProcessModeAsString(self) -> str: ...
    def GetProcessModeMaxValue(self) -> int: ...
    def GetProcessModeMinValue(self) -> int: ...
    def GetSampleDimensions(self) -> Tuple[int, int, int]: ...
    def GetScaleToMaximumDistance(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImplicitModeller: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImplicitModeller: ...
    def ScaleToMaximumDistanceOff(self) -> None: ...
    def ScaleToMaximumDistanceOn(self) -> None: ...
    def SetAdjustBounds(self, _arg: int) -> None: ...
    def SetAdjustDistance(self, _arg: float) -> None: ...
    def SetCapValue(self, value: float) -> None: ...
    def SetCapping(self, _arg: int) -> None: ...
    def SetLocatorMaxLevel(self, _arg: int) -> None: ...
    def SetMaximumDistance(self, _arg: float) -> None: ...
    @overload
    def SetModelBounds(self, _arg1: float, _arg2: float, _arg3: float, _arg4: float, _arg5: float, _arg6: float) -> None: ...
    @overload
    def SetModelBounds(self, _arg: Sequence[float]) -> None: ...
    def SetNumberOfThreads(self, _arg: int) -> None: ...
    def SetOutputScalarType(self, type: int) -> None: ...
    def SetOutputScalarTypeToChar(self) -> None: ...
    def SetOutputScalarTypeToDouble(self) -> None: ...
    def SetOutputScalarTypeToFloat(self) -> None: ...
    def SetOutputScalarTypeToInt(self) -> None: ...
    def SetOutputScalarTypeToLong(self) -> None: ...
    def SetOutputScalarTypeToShort(self) -> None: ...
    def SetOutputScalarTypeToUnsignedChar(self) -> None: ...
    def SetOutputScalarTypeToUnsignedInt(self) -> None: ...
    def SetOutputScalarTypeToUnsignedLong(self) -> None: ...
    def SetOutputScalarTypeToUnsignedShort(self) -> None: ...
    def SetProcessMode(self, _arg: int) -> None: ...
    def SetProcessModeToPerCell(self) -> None: ...
    def SetProcessModeToPerVoxel(self) -> None: ...
    @overload
    def SetSampleDimensions(self, i: int, j: int, k: int) -> None: ...
    @overload
    def SetSampleDimensions(self, dim: MutableSequence[int]) -> None: ...
    def SetScaleToMaximumDistance(self, _arg: int) -> None: ...
    def StartAppend(self) -> None: ...

class vtkPCAAnalysisFilter(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def GetEvals(self) -> vtkmodules.vtkCommonCore.vtkFloatArray: ...
    def GetModesRequiredFor(self, proportion: float) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetParameterisedShape(
        self, b: vtkmodules.vtkCommonCore.vtkFloatArray, shape: vtkmodules.vtkCommonDataModel.vtkPointSet
    ) -> None: ...
    def GetShapeParameters(
        self, shape: vtkmodules.vtkCommonDataModel.vtkPointSet, b: vtkmodules.vtkCommonCore.vtkFloatArray, bsize: int
    ) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPCAAnalysisFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPCAAnalysisFilter: ...

class vtkPolyDataSilhouette(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    class Directions(int): ...
    VTK_DIRECTION_CAMERA_ORIGIN: Directions
    VTK_DIRECTION_CAMERA_VECTOR: Directions
    VTK_DIRECTION_SPECIFIED_ORIGIN: Directions
    VTK_DIRECTION_SPECIFIED_VECTOR: Directions
    def BorderEdgesOff(self) -> None: ...
    def BorderEdgesOn(self) -> None: ...
    def GetBorderEdges(self) -> int: ...
    def GetCamera(self) -> vtkmodules.vtkRenderingCore.vtkCamera: ...
    def GetDirection(self) -> int: ...
    def GetEnableFeatureAngle(self) -> int: ...
    def GetFeatureAngle(self) -> float: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOrigin(self) -> Tuple[float, float, float]: ...
    def GetPieceInvariant(self) -> int: ...
    def GetProp3D(self) -> vtkmodules.vtkRenderingCore.vtkProp3D: ...
    def GetVector(self) -> Tuple[float, float, float]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPolyDataSilhouette: ...
    def PieceInvariantOff(self) -> None: ...
    def PieceInvariantOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPolyDataSilhouette: ...
    def SetBorderEdges(self, _arg: int) -> None: ...
    def SetCamera(self, __a: vtkmodules.vtkRenderingCore.vtkCamera) -> None: ...
    def SetDirection(self, _arg: int) -> None: ...
    def SetDirectionToCameraOrigin(self) -> None: ...
    def SetDirectionToCameraVector(self) -> None: ...
    def SetDirectionToSpecifiedOrigin(self) -> None: ...
    def SetDirectionToSpecifiedVector(self) -> None: ...
    def SetEnableFeatureAngle(self, _arg: int) -> None: ...
    def SetFeatureAngle(self, _arg: float) -> None: ...
    @overload
    def SetOrigin(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetOrigin(self, _arg: Sequence[float]) -> None: ...
    def SetPieceInvariant(self, _arg: int) -> None: ...
    def SetProp3D(self, __a: vtkmodules.vtkRenderingCore.vtkProp3D) -> None: ...
    @overload
    def SetVector(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetVector(self, _arg: Sequence[float]) -> None: ...

class vtkProcrustesAlignmentFilter(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def GetLandmarkTransform(self) -> vtkmodules.vtkCommonTransforms.vtkLandmarkTransform: ...
    def GetMeanPoints(self) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputPointsPrecision(self) -> int: ...
    def GetStartFromCentroid(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkProcrustesAlignmentFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkProcrustesAlignmentFilter: ...
    def SetOutputPointsPrecision(self, _arg: int) -> None: ...
    def SetStartFromCentroid(self, _arg: bool) -> None: ...
    def StartFromCentroidOff(self) -> None: ...
    def StartFromCentroidOn(self) -> None: ...

class vtkProjectedTerrainPath(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    HUG_PROJECTION: int
    NONOCCLUDED_PROJECTION: int
    SIMPLE_PROJECTION: int
    def GetHeightOffset(self) -> float: ...
    def GetHeightTolerance(self) -> float: ...
    def GetHeightToleranceMaxValue(self) -> float: ...
    def GetHeightToleranceMinValue(self) -> float: ...
    def GetMaximumNumberOfLines(self) -> int: ...
    def GetMaximumNumberOfLinesMaxValue(self) -> int: ...
    def GetMaximumNumberOfLinesMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetProjectionMode(self) -> int: ...
    def GetProjectionModeMaxValue(self) -> int: ...
    def GetProjectionModeMinValue(self) -> int: ...
    def GetSource(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkProjectedTerrainPath: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkProjectedTerrainPath: ...
    def SetHeightOffset(self, _arg: float) -> None: ...
    def SetHeightTolerance(self, _arg: float) -> None: ...
    def SetMaximumNumberOfLines(self, _arg: int) -> None: ...
    def SetProjectionMode(self, _arg: int) -> None: ...
    def SetProjectionModeToHug(self) -> None: ...
    def SetProjectionModeToNonOccluded(self) -> None: ...
    def SetProjectionModeToSimple(self) -> None: ...
    def SetSourceConnection(self, algOutput: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetSourceData(self, source: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...

class vtkRenderLargeImage(vtkmodules.vtkCommonExecutionModel.vtkAlgorithm):
    def GetInput(self) -> vtkmodules.vtkRenderingCore.vtkRenderer: ...
    def GetMagnification(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkRenderLargeImage: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkRenderLargeImage: ...
    def SetInput(self, __a: vtkmodules.vtkRenderingCore.vtkRenderer) -> None: ...
    def SetMagnification(self, _arg: int) -> None: ...

class vtkTemporalArrayOperatorFilter(vtkmodules.vtkCommonExecutionModel.vtkMultiTimeStepAlgorithm):
    class OperatorType(int): ...
    ADD: OperatorType
    DIV: OperatorType
    MUL: OperatorType
    SUB: OperatorType
    def GetFirstTimeStepIndex(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOperator(self) -> int: ...
    def GetOutputArrayNameSuffix(self) -> str: ...
    def GetSecondTimeStepIndex(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTemporalArrayOperatorFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTemporalArrayOperatorFilter: ...
    def SetFirstTimeStepIndex(self, _arg: int) -> None: ...
    def SetOperator(self, _arg: int) -> None: ...
    def SetOutputArrayNameSuffix(self, _arg: str) -> None: ...
    def SetSecondTimeStepIndex(self, _arg: int) -> None: ...

class vtkTemporalDataSetCache(vtkmodules.vtkCommonExecutionModel.vtkAlgorithm):
    def CacheInMemkindOff(self) -> None: ...
    def CacheInMemkindOn(self) -> None: ...
    def GetCacheInMemkind(self) -> bool: ...
    def GetCacheSize(self) -> int: ...
    def GetIsASource(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    def IsASourceOff(self) -> None: ...
    def IsASourceOn(self) -> None: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTemporalDataSetCache: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTemporalDataSetCache: ...
    def SetCacheInMemkind(self, _arg: bool) -> None: ...
    def SetCacheSize(self, size: int) -> None: ...
    def SetIsASource(self, _arg: bool) -> None: ...

class vtkTemporalFractal(vtkmodules.vtkCommonExecutionModel.vtkAlgorithm):
    def AdaptiveSubdivisionOff(self) -> None: ...
    def AdaptiveSubdivisionOn(self) -> None: ...
    def DiscreteTimeStepsOff(self) -> None: ...
    def DiscreteTimeStepsOn(self) -> None: ...
    def GenerateRectilinearGridsOff(self) -> None: ...
    def GenerateRectilinearGridsOn(self) -> None: ...
    def GetAdaptiveSubdivision(self) -> int: ...
    def GetAsymmetric(self) -> int: ...
    def GetDimensions(self) -> int: ...
    def GetDiscreteTimeSteps(self) -> int: ...
    def GetFractalValue(self) -> float: ...
    def GetGenerateRectilinearGrids(self) -> int: ...
    def GetGhostLevels(self) -> int: ...
    def GetMaximumLevel(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTwoDimensional(self) -> int: ...
    def GhostLevelsOff(self) -> None: ...
    def GhostLevelsOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTemporalFractal: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTemporalFractal: ...
    def SetAdaptiveSubdivision(self, _arg: int) -> None: ...
    def SetAsymmetric(self, _arg: int) -> None: ...
    def SetDimensions(self, _arg: int) -> None: ...
    def SetDiscreteTimeSteps(self, _arg: int) -> None: ...
    def SetFractalValue(self, _arg: float) -> None: ...
    def SetGenerateRectilinearGrids(self, _arg: int) -> None: ...
    def SetGhostLevels(self, _arg: int) -> None: ...
    def SetMaximumLevel(self, _arg: int) -> None: ...
    def SetTwoDimensional(self, _arg: int) -> None: ...
    def TwoDimensionalOff(self) -> None: ...
    def TwoDimensionalOn(self) -> None: ...

class vtkTemporalInterpolator(vtkmodules.vtkCommonExecutionModel.vtkMultiTimeStepAlgorithm):
    def GetCacheData(self) -> bool: ...
    def GetDiscreteTimeStepInterval(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetResampleFactor(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTemporalInterpolator: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTemporalInterpolator: ...
    def SetCacheData(self, _arg: bool) -> None: ...
    def SetDiscreteTimeStepInterval(self, _arg: float) -> None: ...
    def SetResampleFactor(self, _arg: int) -> None: ...

class vtkTemporalShiftScale(vtkmodules.vtkCommonExecutionModel.vtkAlgorithm):
    def GetMaximumNumberOfPeriods(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPeriodic(self) -> int: ...
    def GetPeriodicEndCorrection(self) -> int: ...
    def GetPostShift(self) -> float: ...
    def GetPreShift(self) -> float: ...
    def GetScale(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTemporalShiftScale: ...
    def PeriodicEndCorrectionOff(self) -> None: ...
    def PeriodicEndCorrectionOn(self) -> None: ...
    def PeriodicOff(self) -> None: ...
    def PeriodicOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTemporalShiftScale: ...
    def SetMaximumNumberOfPeriods(self, _arg: float) -> None: ...
    def SetPeriodic(self, _arg: int) -> None: ...
    def SetPeriodicEndCorrection(self, _arg: int) -> None: ...
    def SetPostShift(self, _arg: float) -> None: ...
    def SetPreShift(self, _arg: float) -> None: ...
    def SetScale(self, _arg: float) -> None: ...

class vtkTemporalSnapToTimeStep(vtkmodules.vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    VTK_SNAP_NEAREST: int
    VTK_SNAP_NEXTABOVE_OR_EQUAL: int
    VTK_SNAP_NEXTBELOW_OR_EQUAL: int
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSnapMode(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTemporalSnapToTimeStep: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTemporalSnapToTimeStep: ...
    def SetSnapMode(self, _arg: int) -> None: ...
    def SetSnapModeToNearest(self) -> None: ...
    def SetSnapModeToNextAboveOrEqual(self) -> None: ...
    def SetSnapModeToNextBelowOrEqual(self) -> None: ...

class vtkTransformToGrid(vtkmodules.vtkCommonExecutionModel.vtkAlgorithm):
    def GetDisplacementScale(self) -> float: ...
    def GetDisplacementShift(self) -> float: ...
    def GetGridExtent(self) -> Tuple[int, int, int, int, int, int]: ...
    def GetGridOrigin(self) -> Tuple[float, float, float]: ...
    def GetGridScalarType(self) -> int: ...
    def GetGridSpacing(self) -> Tuple[float, float, float]: ...
    def GetInput(self) -> vtkmodules.vtkCommonTransforms.vtkAbstractTransform: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTransformToGrid: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTransformToGrid: ...
    @overload
    def SetGridExtent(self, _arg1: int, _arg2: int, _arg3: int, _arg4: int, _arg5: int, _arg6: int) -> None: ...
    @overload
    def SetGridExtent(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetGridOrigin(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetGridOrigin(self, _arg: Sequence[float]) -> None: ...
    def SetGridScalarType(self, _arg: int) -> None: ...
    def SetGridScalarTypeToChar(self) -> None: ...
    def SetGridScalarTypeToDouble(self) -> None: ...
    def SetGridScalarTypeToFloat(self) -> None: ...
    def SetGridScalarTypeToShort(self) -> None: ...
    def SetGridScalarTypeToUnsignedChar(self) -> None: ...
    def SetGridScalarTypeToUnsignedShort(self) -> None: ...
    @overload
    def SetGridSpacing(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetGridSpacing(self, _arg: Sequence[float]) -> None: ...
    def SetInput(self, __a: vtkmodules.vtkCommonTransforms.vtkAbstractTransform) -> None: ...

class vtkWeightedTransformFilter(vtkmodules.vtkCommonExecutionModel.vtkPointSetAlgorithm):
    def AddInputValuesOff(self) -> None: ...
    def AddInputValuesOn(self) -> None: ...
    def GetAddInputValues(self) -> int: ...
    def GetCellDataTransformIndexArray(self) -> str: ...
    def GetCellDataWeightArray(self) -> str: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfTransforms(self) -> int: ...
    def GetTransform(self, num: int) -> vtkmodules.vtkCommonTransforms.vtkAbstractTransform: ...
    def GetTransformIndexArray(self) -> str: ...
    def GetWeightArray(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWeightedTransformFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWeightedTransformFilter: ...
    def SetAddInputValues(self, _arg: int) -> None: ...
    def SetCellDataTransformIndexArray(self, _arg: str) -> None: ...
    def SetCellDataWeightArray(self, _arg: str) -> None: ...
    def SetNumberOfTransforms(self, num: int) -> None: ...
    def SetTransform(self, transform: vtkmodules.vtkCommonTransforms.vtkAbstractTransform, num: int) -> None: ...
    def SetTransformIndexArray(self, _arg: str) -> None: ...
    def SetWeightArray(self, _arg: str) -> None: ...
