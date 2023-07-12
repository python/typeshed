from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

VTK_COLOR_BY_SCALAR:int
VTK_COLOR_BY_SCALE:int
VTK_COLOR_BY_VECTOR:int
VTK_DATA_SCALING_OFF:int
VTK_INDEXING_BY_SCALAR:int
VTK_INDEXING_BY_VECTOR:int
VTK_INDEXING_OFF:int
VTK_SCALE_BY_SCALAR:int
VTK_SCALE_BY_VECTOR:int
VTK_SCALE_BY_VECTORCOMPONENTS:int
VTK_USE_NORMAL:int
VTK_USE_VECTOR:int
VTK_VECTOR_ROTATION_OFF:int

class vtkGenericClip(vtkmodules.vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    def CreateDefaultLocator(self) -> None: ...
    def GenerateClipScalarsOff(self) -> None: ...
    def GenerateClipScalarsOn(self) -> None: ...
    def GenerateClippedOutputOff(self) -> None: ...
    def GenerateClippedOutputOn(self) -> None: ...
    def GetClipFunction(self) -> 'vtkImplicitFunction': ...
    def GetClippedOutput(self) -> 'vtkUnstructuredGrid': ...
    def GetGenerateClipScalars(self) -> int: ...
    def GetGenerateClippedOutput(self) -> int: ...
    def GetInputScalarsSelection(self) -> str: ...
    def GetInsideOut(self) -> int: ...
    def GetLocator(self) -> 'vtkIncrementalPointLocator': ...
    def GetMTime(self) -> int: ...
    def GetMergeTolerance(self) -> float: ...
    def GetMergeToleranceMaxValue(self) -> float: ...
    def GetMergeToleranceMinValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfOutputs(self) -> int: ...
    def GetValue(self) -> float: ...
    def InsideOutOff(self) -> None: ...
    def InsideOutOn(self) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkGenericClip': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkGenericClip': ...
    def SelectInputScalars(self, fieldName:str) -> None: ...
    def SetClipFunction(self, __a:'vtkImplicitFunction') -> None: ...
    def SetGenerateClipScalars(self, _arg:int) -> None: ...
    def SetGenerateClippedOutput(self, _arg:int) -> None: ...
    def SetInsideOut(self, _arg:int) -> None: ...
    def SetLocator(self, locator:'vtkIncrementalPointLocator') -> None: ...
    def SetMergeTolerance(self, _arg:float) -> None: ...
    def SetValue(self, _arg:float) -> None: ...

class vtkGenericContourFilter(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def ComputeGradientsOff(self) -> None: ...
    def ComputeGradientsOn(self) -> None: ...
    def ComputeNormalsOff(self) -> None: ...
    def ComputeNormalsOn(self) -> None: ...
    def ComputeScalarsOff(self) -> None: ...
    def ComputeScalarsOn(self) -> None: ...
    def CreateDefaultLocator(self) -> None: ...
    @overload
    def GenerateValues(self, numContours:int, range:MutableSequence[float]) -> None: ...
    @overload
    def GenerateValues(self, numContours:int, rangeStart:float, rangeEnd:float) -> None: ...
    def GetComputeGradients(self) -> int: ...
    def GetComputeNormals(self) -> int: ...
    def GetComputeScalars(self) -> int: ...
    def GetInputScalarsSelection(self) -> str: ...
    def GetLocator(self) -> 'vtkIncrementalPointLocator': ...
    def GetMTime(self) -> int: ...
    def GetNumberOfContours(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetValue(self, i:int) -> float: ...
    @overload
    def GetValues(self) -> Pointer: ...
    @overload
    def GetValues(self, contourValues:MutableSequence[float]) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkGenericContourFilter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkGenericContourFilter': ...
    def SelectInputScalars(self, fieldName:str) -> None: ...
    def SetComputeGradients(self, _arg:int) -> None: ...
    def SetComputeNormals(self, _arg:int) -> None: ...
    def SetComputeScalars(self, _arg:int) -> None: ...
    def SetLocator(self, locator:'vtkIncrementalPointLocator') -> None: ...
    def SetNumberOfContours(self, number:int) -> None: ...
    def SetValue(self, i:int, value:float) -> None: ...

class vtkGenericCutter(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def CreateDefaultLocator(self) -> None: ...
    def GenerateCutScalarsOff(self) -> None: ...
    def GenerateCutScalarsOn(self) -> None: ...
    @overload
    def GenerateValues(self, numContours:int, range:MutableSequence[float]) -> None: ...
    @overload
    def GenerateValues(self, numContours:int, rangeStart:float, rangeEnd:float) -> None: ...
    def GetCutFunction(self) -> 'vtkImplicitFunction': ...
    def GetGenerateCutScalars(self) -> int: ...
    def GetLocator(self) -> 'vtkIncrementalPointLocator': ...
    def GetMTime(self) -> int: ...
    def GetNumberOfContours(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetValue(self, i:int) -> float: ...
    @overload
    def GetValues(self) -> Pointer: ...
    @overload
    def GetValues(self, contourValues:MutableSequence[float]) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkGenericCutter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkGenericCutter': ...
    def SetCutFunction(self, __a:'vtkImplicitFunction') -> None: ...
    def SetGenerateCutScalars(self, _arg:int) -> None: ...
    def SetLocator(self, locator:'vtkIncrementalPointLocator') -> None: ...
    def SetNumberOfContours(self, number:int) -> None: ...
    def SetValue(self, i:int, value:float) -> None: ...

class vtkGenericDataSetTessellator(vtkmodules.vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    def CreateDefaultLocator(self) -> None: ...
    def GetKeepCellIds(self) -> int: ...
    def GetLocator(self) -> 'vtkIncrementalPointLocator': ...
    def GetMTime(self) -> int: ...
    def GetMerging(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def KeepCellIdsOff(self) -> None: ...
    def KeepCellIdsOn(self) -> None: ...
    def MergingOff(self) -> None: ...
    def MergingOn(self) -> None: ...
    def NewInstance(self) -> 'vtkGenericDataSetTessellator': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkGenericDataSetTessellator': ...
    def SetKeepCellIds(self, _arg:int) -> None: ...
    def SetLocator(self, locator:'vtkIncrementalPointLocator') -> None: ...
    def SetMerging(self, _arg:int) -> None: ...

class vtkGenericGeometryFilter(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def CellClippingOff(self) -> None: ...
    def CellClippingOn(self) -> None: ...
    def CreateDefaultLocator(self) -> None: ...
    def ExtentClippingOff(self) -> None: ...
    def ExtentClippingOn(self) -> None: ...
    def GetCellClipping(self) -> int: ...
    def GetCellMaximum(self) -> int: ...
    def GetCellMaximumMaxValue(self) -> int: ...
    def GetCellMaximumMinValue(self) -> int: ...
    def GetCellMinimum(self) -> int: ...
    def GetCellMinimumMaxValue(self) -> int: ...
    def GetCellMinimumMinValue(self) -> int: ...
    def GetExtent(self) -> Pointer: ...
    def GetExtentClipping(self) -> int: ...
    def GetLocator(self) -> 'vtkIncrementalPointLocator': ...
    def GetMTime(self) -> int: ...
    def GetMerging(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetPassThroughCellIds(self) -> int: ...
    def GetPointClipping(self) -> int: ...
    def GetPointMaximum(self) -> int: ...
    def GetPointMaximumMaxValue(self) -> int: ...
    def GetPointMaximumMinValue(self) -> int: ...
    def GetPointMinimum(self) -> int: ...
    def GetPointMinimumMaxValue(self) -> int: ...
    def GetPointMinimumMinValue(self) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def MergingOff(self) -> None: ...
    def MergingOn(self) -> None: ...
    def NewInstance(self) -> 'vtkGenericGeometryFilter': ...
    def PassThroughCellIdsOff(self) -> None: ...
    def PassThroughCellIdsOn(self) -> None: ...
    def PointClippingOff(self) -> None: ...
    def PointClippingOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkGenericGeometryFilter': ...
    def SetCellClipping(self, _arg:int) -> None: ...
    def SetCellMaximum(self, _arg:int) -> None: ...
    def SetCellMinimum(self, _arg:int) -> None: ...
    @overload
    def SetExtent(self, xMin:float, xMax:float, yMin:float, yMax:float, zMin:float, zMax:float) -> None: ...
    @overload
    def SetExtent(self, extent:MutableSequence[float]) -> None: ...
    def SetExtentClipping(self, _arg:int) -> None: ...
    def SetLocator(self, locator:'vtkIncrementalPointLocator') -> None: ...
    def SetMerging(self, _arg:int) -> None: ...
    def SetPassThroughCellIds(self, _arg:int) -> None: ...
    def SetPointClipping(self, _arg:int) -> None: ...
    def SetPointMaximum(self, _arg:int) -> None: ...
    def SetPointMinimum(self, _arg:int) -> None: ...

class vtkGenericGlyph3DFilter(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def ClampingOff(self) -> None: ...
    def ClampingOn(self) -> None: ...
    def GeneratePointIdsOff(self) -> None: ...
    def GeneratePointIdsOn(self) -> None: ...
    def GetClamping(self) -> int: ...
    def GetColorMode(self) -> int: ...
    def GetColorModeAsString(self) -> str: ...
    def GetGeneratePointIds(self) -> int: ...
    def GetIndexMode(self) -> int: ...
    def GetIndexModeAsString(self) -> str: ...
    def GetInputNormalsSelection(self) -> str: ...
    def GetInputScalarsSelection(self) -> str: ...
    def GetInputVectorsSelection(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetOrient(self) -> int: ...
    def GetPointIdsName(self) -> str: ...
    def GetRange(self) -> Tuple[float, float]: ...
    def GetScaleFactor(self) -> float: ...
    def GetScaleMode(self) -> int: ...
    def GetScaleModeAsString(self) -> str: ...
    def GetScaling(self) -> int: ...
    def GetSource(self, id:int=0) -> 'vtkPolyData': ...
    def GetVectorMode(self) -> int: ...
    def GetVectorModeAsString(self) -> str: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkGenericGlyph3DFilter': ...
    def OrientOff(self) -> None: ...
    def OrientOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkGenericGlyph3DFilter': ...
    def ScalingOff(self) -> None: ...
    def ScalingOn(self) -> None: ...
    def SelectInputNormals(self, fieldName:str) -> None: ...
    def SelectInputScalars(self, fieldName:str) -> None: ...
    def SelectInputVectors(self, fieldName:str) -> None: ...
    def SetClamping(self, _arg:int) -> None: ...
    def SetColorMode(self, _arg:int) -> None: ...
    def SetColorModeToColorByScalar(self) -> None: ...
    def SetColorModeToColorByScale(self) -> None: ...
    def SetColorModeToColorByVector(self) -> None: ...
    def SetGeneratePointIds(self, _arg:int) -> None: ...
    def SetIndexMode(self, _arg:int) -> None: ...
    def SetIndexModeToOff(self) -> None: ...
    def SetIndexModeToScalar(self) -> None: ...
    def SetIndexModeToVector(self) -> None: ...
    def SetOrient(self, _arg:int) -> None: ...
    def SetPointIdsName(self, _arg:str) -> None: ...
    @overload
    def SetRange(self, _arg1:float, _arg2:float) -> None: ...
    @overload
    def SetRange(self, _arg:Sequence[float]) -> None: ...
    def SetScaleFactor(self, _arg:float) -> None: ...
    def SetScaleMode(self, _arg:int) -> None: ...
    def SetScaleModeToDataScalingOff(self) -> None: ...
    def SetScaleModeToScaleByScalar(self) -> None: ...
    def SetScaleModeToScaleByVector(self) -> None: ...
    def SetScaleModeToScaleByVectorComponents(self) -> None: ...
    def SetScaling(self, _arg:int) -> None: ...
    @overload
    def SetSourceData(self, pd:'vtkPolyData') -> None: ...
    @overload
    def SetSourceData(self, id:int, pd:'vtkPolyData') -> None: ...
    def SetVectorMode(self, _arg:int) -> None: ...
    def SetVectorModeToUseNormal(self) -> None: ...
    def SetVectorModeToUseVector(self) -> None: ...
    def SetVectorModeToVectorRotationOff(self) -> None: ...

class vtkGenericOutlineFilter(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkGenericOutlineFilter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkGenericOutlineFilter': ...

class vtkGenericProbeFilter(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetSource(self) -> 'vtkGenericDataSet': ...
    def GetValidPoints(self) -> 'vtkIdTypeArray': ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkGenericProbeFilter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkGenericProbeFilter': ...
    def SetSourceData(self, source:'vtkGenericDataSet') -> None: ...

class vtkGenericStreamTracer(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    class Units(int): ...
    class Solvers(int): ...
    class ReasonForTermination(int): ...
    BACKWARD:int
    BOTH:int
    CELL_LENGTH_UNIT:'Units'
    FORWARD:int
    LENGTH_UNIT:'Units'
    NONE:'Solvers'
    NOT_INITIALIZED:'ReasonForTermination'
    OUT_OF_DOMAIN:'ReasonForTermination'
    OUT_OF_STEPS:'ReasonForTermination'
    OUT_OF_TIME:'ReasonForTermination'
    RUNGE_KUTTA2:'Solvers'
    RUNGE_KUTTA4:'Solvers'
    RUNGE_KUTTA45:'Solvers'
    STAGNATION:'ReasonForTermination'
    TIME_UNIT:'Units'
    UNEXPECTED_VALUE:'ReasonForTermination'
    UNKNOWN:'Solvers'
    def AddInputData(self, in_:'vtkGenericDataSet') -> None: ...
    def ComputeVorticityOff(self) -> None: ...
    def ComputeVorticityOn(self) -> None: ...
    def FillInputPortInformation(self, port:int, info:'vtkInformation') -> int: ...
    def GetComputeVorticity(self) -> int: ...
    def GetInitialIntegrationStep(self) -> float: ...
    def GetInitialIntegrationStepUnit(self) -> int: ...
    def GetInputVectorsSelection(self) -> str: ...
    def GetIntegrationDirection(self) -> int: ...
    def GetIntegrationDirectionMaxValue(self) -> int: ...
    def GetIntegrationDirectionMinValue(self) -> int: ...
    def GetIntegrator(self) -> 'vtkInitialValueProblemSolver': ...
    def GetIntegratorType(self) -> int: ...
    def GetMaximumError(self) -> float: ...
    def GetMaximumIntegrationStep(self) -> float: ...
    def GetMaximumIntegrationStepUnit(self) -> int: ...
    def GetMaximumNumberOfSteps(self) -> int: ...
    def GetMaximumPropagation(self) -> float: ...
    def GetMaximumPropagationUnit(self) -> int: ...
    def GetMinimumIntegrationStep(self) -> float: ...
    def GetMinimumIntegrationStepUnit(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetRotationScale(self) -> float: ...
    def GetSource(self) -> 'vtkDataSet': ...
    def GetStartPosition(self) -> Tuple[float, float, float]: ...
    def GetTerminalSpeed(self) -> float: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkGenericStreamTracer': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkGenericStreamTracer': ...
    def SelectInputVectors(self, fieldName:str) -> None: ...
    def SetComputeVorticity(self, _arg:int) -> None: ...
    @overload
    def SetInitialIntegrationStep(self, unit:int, step:float) -> None: ...
    @overload
    def SetInitialIntegrationStep(self, step:float) -> None: ...
    def SetInitialIntegrationStepUnit(self, unit:int) -> None: ...
    def SetInitialIntegrationStepUnitToCellLengthUnit(self) -> None: ...
    def SetInitialIntegrationStepUnitToLengthUnit(self) -> None: ...
    def SetInitialIntegrationStepUnitToTimeUnit(self) -> None: ...
    def SetIntegrationDirection(self, _arg:int) -> None: ...
    def SetIntegrationDirectionToBackward(self) -> None: ...
    def SetIntegrationDirectionToBoth(self) -> None: ...
    def SetIntegrationDirectionToForward(self) -> None: ...
    def SetIntegrationStepUnit(self, unit:int) -> None: ...
    def SetIntegrator(self, __a:'vtkInitialValueProblemSolver') -> None: ...
    def SetIntegratorType(self, type:int) -> None: ...
    def SetIntegratorTypeToRungeKutta2(self) -> None: ...
    def SetIntegratorTypeToRungeKutta4(self) -> None: ...
    def SetIntegratorTypeToRungeKutta45(self) -> None: ...
    def SetInterpolatorPrototype(self, ivf:'vtkGenericInterpolatedVelocityField') -> None: ...
    def SetMaximumError(self, _arg:float) -> None: ...
    @overload
    def SetMaximumIntegrationStep(self, unit:int, step:float) -> None: ...
    @overload
    def SetMaximumIntegrationStep(self, step:float) -> None: ...
    def SetMaximumIntegrationStepUnit(self, unit:int) -> None: ...
    def SetMaximumIntegrationStepUnitToCellLengthUnit(self) -> None: ...
    def SetMaximumIntegrationStepUnitToLengthUnit(self) -> None: ...
    def SetMaximumIntegrationStepUnitToTimeUnit(self) -> None: ...
    def SetMaximumNumberOfSteps(self, _arg:int) -> None: ...
    @overload
    def SetMaximumPropagation(self, unit:int, max:float) -> None: ...
    @overload
    def SetMaximumPropagation(self, max:float) -> None: ...
    def SetMaximumPropagationUnit(self, unit:int) -> None: ...
    def SetMaximumPropagationUnitToCellLengthUnit(self) -> None: ...
    def SetMaximumPropagationUnitToLengthUnit(self) -> None: ...
    def SetMaximumPropagationUnitToTimeUnit(self) -> None: ...
    @overload
    def SetMinimumIntegrationStep(self, unit:int, step:float) -> None: ...
    @overload
    def SetMinimumIntegrationStep(self, step:float) -> None: ...
    def SetMinimumIntegrationStepUnit(self, unit:int) -> None: ...
    def SetMinimumIntegrationStepUnitToCellLengthUnit(self) -> None: ...
    def SetMinimumIntegrationStepUnitToLengthUnit(self) -> None: ...
    def SetMinimumIntegrationStepUnitToTimeUnit(self) -> None: ...
    def SetRotationScale(self, _arg:float) -> None: ...
    def SetSourceConnection(self, algOutput:'vtkAlgorithmOutput') -> None: ...
    def SetSourceData(self, source:'vtkDataSet') -> None: ...
    @overload
    def SetStartPosition(self, _arg1:float, _arg2:float, _arg3:float) -> None: ...
    @overload
    def SetStartPosition(self, _arg:Sequence[float]) -> None: ...
    def SetTerminalSpeed(self, _arg:float) -> None: ...

