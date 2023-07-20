from collections.abc import MutableSequence, Sequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkCommonMisc

_Pointer = TypeVar("_Pointer")

class vtkStatisticsAlgorithm(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    class InputPorts(int): ...
    class OutputIndices(int): ...
    INPUT_DATA: InputPorts
    INPUT_MODEL: InputPorts
    LEARN_PARAMETERS: InputPorts
    OUTPUT_DATA: OutputIndices
    OUTPUT_MODEL: OutputIndices
    OUTPUT_TEST: OutputIndices
    def AddColumn(self, namCol: str) -> None: ...
    def AddColumnPair(self, namColX: str, namColY: str) -> None: ...
    def Aggregate(
        self, __a: vtkmodules.vtkCommonDataModel.vtkDataObjectCollection, __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet
    ) -> None: ...
    def GetAssessNames(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetAssessOption(self) -> bool: ...
    @overload
    def GetColumnForRequest(self, r: int, c: int) -> str: ...
    @overload
    def GetColumnForRequest(self, r: int, c: int, columnName: str) -> int: ...
    def GetDeriveOption(self) -> bool: ...
    def GetLearnOption(self) -> bool: ...
    def GetNumberOfColumnsForRequest(self, request: int) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfPrimaryTables(self) -> int: ...
    def GetNumberOfRequests(self) -> int: ...
    def GetTestOption(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkStatisticsAlgorithm: ...
    def RequestSelectedColumns(self) -> int: ...
    def ResetAllColumnStates(self) -> None: ...
    def ResetRequests(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkStatisticsAlgorithm: ...
    def SetAssessNames(self, __a: vtkmodules.vtkCommonCore.vtkStringArray) -> None: ...
    def SetAssessOption(self, _arg: bool) -> None: ...
    def SetColumnStatus(self, namCol: str, status: int) -> None: ...
    def SetDeriveOption(self, _arg: bool) -> None: ...
    def SetInputModel(self, model: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetInputModelConnection(self, model: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetLearnOption(self, _arg: bool) -> None: ...
    def SetLearnOptionParameterConnection(self, params: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetLearnOptionParameters(self, params: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetNumberOfPrimaryTables(self, _arg: int) -> None: ...
    def SetParameter(self, parameter: str, index: int, value: vtkmodules.vtkCommonCore.vtkVariant) -> bool: ...
    def SetTestOption(self, _arg: bool) -> None: ...

class vtkAutoCorrelativeStatistics(vtkStatisticsAlgorithm):
    def Aggregate(
        self, __a: vtkmodules.vtkCommonDataModel.vtkDataObjectCollection, __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet
    ) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSliceCardinality(self) -> int: ...
    def GetSliceCardinalityMaxValue(self) -> int: ...
    def GetSliceCardinalityMinValue(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkAutoCorrelativeStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkAutoCorrelativeStatistics: ...
    def SetSliceCardinality(self, _arg: int) -> None: ...

class vtkBivariateLinearTableThreshold(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    class LinearThresholdType(int): ...
    class OutputPorts(int): ...
    BLT_ABOVE: LinearThresholdType
    BLT_BELOW: LinearThresholdType
    BLT_BETWEEN: LinearThresholdType
    BLT_NEAR: LinearThresholdType
    OUTPUT_ROW_DATA: OutputPorts
    OUTPUT_ROW_IDS: OutputPorts
    def AddColumnToThreshold(self, column: int, component: int) -> None: ...
    @overload
    def AddLineEquation(self, p1: MutableSequence[float], p2: MutableSequence[float]) -> None: ...
    @overload
    def AddLineEquation(self, p: MutableSequence[float], slope: float) -> None: ...
    @overload
    def AddLineEquation(self, a: float, b: float, c: float) -> None: ...
    def ClearColumnsToThreshold(self) -> None: ...
    def ClearLineEquations(self) -> None: ...
    @overload
    @staticmethod
    def ComputeImplicitLineFunction(
        p1: MutableSequence[float], p2: MutableSequence[float], abc: MutableSequence[float]
    ) -> None: ...
    @overload
    @staticmethod
    def ComputeImplicitLineFunction(p: MutableSequence[float], slope: float, abc: MutableSequence[float]) -> None: ...
    def GetColumnRanges(self) -> tuple[float, float]: ...
    def GetColumnToThreshold(self, idx: int, column: int, component: int) -> None: ...
    def GetDistanceThreshold(self) -> float: ...
    def GetInclusive(self) -> int: ...
    def GetLinearThresholdType(self) -> int: ...
    def GetNumberOfColumnsToThreshold(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSelectedRowIds(self, selection: int = 0) -> vtkmodules.vtkCommonCore.vtkIdTypeArray: ...
    def GetUseNormalizedDistance(self) -> int: ...
    def Initialize(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkBivariateLinearTableThreshold: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkBivariateLinearTableThreshold: ...
    @overload
    def SetColumnRanges(self, _arg1: float, _arg2: float) -> None: ...
    @overload
    def SetColumnRanges(self, _arg: Sequence[float]) -> None: ...
    def SetDistanceThreshold(self, _arg: float) -> None: ...
    def SetInclusive(self, _arg: int) -> None: ...
    def SetLinearThresholdType(self, _arg: int) -> None: ...
    def SetLinearThresholdTypeToAbove(self) -> None: ...
    def SetLinearThresholdTypeToBelow(self) -> None: ...
    def SetLinearThresholdTypeToBetween(self) -> None: ...
    def SetLinearThresholdTypeToNear(self) -> None: ...
    def SetUseNormalizedDistance(self, _arg: int) -> None: ...
    def UseNormalizedDistanceOff(self) -> None: ...
    def UseNormalizedDistanceOn(self) -> None: ...

class vtkComputeQuantiles(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfIntervals(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkComputeQuantiles: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkComputeQuantiles: ...
    def SetNumberOfIntervals(self, _arg: int) -> None: ...

class vtkComputeQuartiles(vtkComputeQuantiles):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkComputeQuartiles: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkComputeQuartiles: ...

class vtkContingencyStatistics(vtkStatisticsAlgorithm):
    def Aggregate(
        self, __a: vtkmodules.vtkCommonDataModel.vtkDataObjectCollection, __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet
    ) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkContingencyStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkContingencyStatistics: ...

class vtkCorrelativeStatistics(vtkStatisticsAlgorithm):
    def Aggregate(
        self, __a: vtkmodules.vtkCommonDataModel.vtkDataObjectCollection, __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet
    ) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCorrelativeStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCorrelativeStatistics: ...

class vtkDescriptiveStatistics(vtkStatisticsAlgorithm):
    def Aggregate(
        self, __a: vtkmodules.vtkCommonDataModel.vtkDataObjectCollection, __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet
    ) -> None: ...
    def G1SkewnessOff(self) -> None: ...
    def G1SkewnessOn(self) -> None: ...
    def G2KurtosisOff(self) -> None: ...
    def G2KurtosisOn(self) -> None: ...
    def GetG1Skewness(self) -> int: ...
    def GetG2Kurtosis(self) -> int: ...
    def GetGhostsToSkip(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSampleEstimate(self) -> bool: ...
    def GetSignedDeviations(self) -> int: ...
    def GetUnbiasedVariance(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkDescriptiveStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkDescriptiveStatistics: ...
    def SampleEstimateOff(self) -> None: ...
    def SampleEstimateOn(self) -> None: ...
    def SetG1Skewness(self, __a: int) -> None: ...
    def SetG2Kurtosis(self, __a: int) -> None: ...
    def SetGhostsToSkip(self, _arg: int) -> None: ...
    def SetSampleEstimate(self, _arg: bool) -> None: ...
    def SetSignedDeviations(self, _arg: int) -> None: ...
    def SetUnbiasedVariance(self, __a: int) -> None: ...
    def SignedDeviationsOff(self) -> None: ...
    def SignedDeviationsOn(self) -> None: ...
    def UnbiasedVarianceOff(self) -> None: ...
    def UnbiasedVarianceOn(self) -> None: ...

class vtkExtractFunctionalBagPlot(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkExtractFunctionalBagPlot: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkExtractFunctionalBagPlot: ...
    def SetDensityForP50(self, _arg: float) -> None: ...
    def SetDensityForPUser(self, _arg: float) -> None: ...
    def SetPUser(self, _arg: int) -> None: ...

class vtkExtractHistogram(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    def AccumulationOff(self) -> None: ...
    def AccumulationOn(self) -> None: ...
    def CalculateAveragesOff(self) -> None: ...
    def CalculateAveragesOn(self) -> None: ...
    def CenterBinsAroundMinAndMaxOff(self) -> None: ...
    def CenterBinsAroundMinAndMaxOn(self) -> None: ...
    def GetAccumulation(self) -> bool: ...
    def GetBinAccumulationArrayName(self) -> str: ...
    def GetBinCount(self) -> int: ...
    def GetBinCountMaxValue(self) -> int: ...
    def GetBinCountMinValue(self) -> int: ...
    def GetBinExtentsArrayName(self) -> str: ...
    def GetBinRange(self) -> tuple[float, float]: ...
    def GetBinValuesArrayName(self) -> str: ...
    def GetCalculateAverages(self) -> bool: ...
    def GetCenterBinsAroundMinAndMax(self) -> bool: ...
    def GetComponent(self) -> int: ...
    def GetComponentMaxValue(self) -> int: ...
    def GetComponentMinValue(self) -> int: ...
    def GetCustomBinRanges(self) -> tuple[float, float]: ...
    def GetNormalize(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetUseCustomBinRanges(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkExtractHistogram: ...
    def NormalizeOff(self) -> None: ...
    def NormalizeOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkExtractHistogram: ...
    def SetAccumulation(self, _arg: bool) -> None: ...
    def SetBinAccumulationArrayName(self, _arg: str) -> None: ...
    def SetBinCount(self, _arg: int) -> None: ...
    def SetBinExtentsArrayName(self, _arg: str) -> None: ...
    def SetBinValuesArrayName(self, _arg: str) -> None: ...
    def SetCalculateAverages(self, _arg: bool) -> None: ...
    def SetCenterBinsAroundMinAndMax(self, _arg: bool) -> None: ...
    def SetComponent(self, _arg: int) -> None: ...
    @overload
    def SetCustomBinRanges(self, _arg1: float, _arg2: float) -> None: ...
    @overload
    def SetCustomBinRanges(self, _arg: Sequence[float]) -> None: ...
    def SetNormalize(self, _arg: bool) -> None: ...
    def SetUseCustomBinRanges(self, _arg: bool) -> None: ...
    def UseCustomBinRangesOff(self) -> None: ...
    def UseCustomBinRangesOn(self) -> None: ...

class vtkHighestDensityRegionsStatistics(vtkStatisticsAlgorithm):
    def Aggregate(
        self, __a: vtkmodules.vtkCommonDataModel.vtkDataObjectCollection, __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet
    ) -> None: ...
    @overload
    def ComputeHDR(
        self, inObservations: vtkmodules.vtkCommonCore.vtkDataArray, outDensity: vtkmodules.vtkCommonCore.vtkDataArray
    ) -> float: ...
    @overload
    def ComputeHDR(
        self,
        inObs: vtkmodules.vtkCommonCore.vtkDataArray,
        inPOI: vtkmodules.vtkCommonCore.vtkDataArray,
        outDensity: vtkmodules.vtkCommonCore.vtkDataArray,
    ) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkHighestDensityRegionsStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkHighestDensityRegionsStatistics: ...
    def SetSigma(self, sigma: float) -> None: ...
    def SetSigmaMatrix(self, s11: float, s12: float, s21: float, s22: float) -> None: ...

class vtkKMeansDistanceFunctor(vtkmodules.vtkCommonCore.vtkObject):
    def AllocateElementArray(self, size: int) -> _Pointer: ...
    def CreateCoordinateArray(self) -> vtkmodules.vtkCommonCore.vtkAbstractArray: ...
    def DeallocateElementArray(self, __a: _Pointer) -> None: ...
    def GetDataType(self) -> int: ...
    def GetEmptyTuple(self, dimension: int) -> vtkmodules.vtkCommonCore.vtkVariantArray: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkKMeansDistanceFunctor: ...
    def PackElements(self, curTable: vtkmodules.vtkCommonDataModel.vtkTable, vElements: _Pointer) -> None: ...
    def PairwiseUpdate(
        self,
        clusterCenters: vtkmodules.vtkCommonDataModel.vtkTable,
        row: int,
        data: vtkmodules.vtkCommonCore.vtkVariantArray,
        dataCardinality: int,
        totalCardinality: int,
    ) -> None: ...
    def PerturbElement(
        self,
        __a: vtkmodules.vtkCommonDataModel.vtkTable,
        __b: vtkmodules.vtkCommonDataModel.vtkTable,
        __c: int,
        __d: int,
        __e: int,
        __f: float,
    ) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkKMeansDistanceFunctor: ...
    @overload
    def UnPackElements(
        self,
        curTable: vtkmodules.vtkCommonDataModel.vtkTable,
        newTable: vtkmodules.vtkCommonDataModel.vtkTable,
        vLocalElements: _Pointer,
        vGlobalElements: _Pointer,
        np: int,
    ) -> None: ...
    @overload
    def UnPackElements(
        self, curTable: vtkmodules.vtkCommonDataModel.vtkTable, vLocalElements: _Pointer, numRows: int, numCols: int
    ) -> None: ...

class vtkKMeansDistanceFunctorCalculator(vtkKMeansDistanceFunctor):
    def GetDistanceExpression(self) -> str: ...
    def GetFunctionParser(self) -> vtkmodules.vtkCommonMisc.vtkFunctionParser: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkKMeansDistanceFunctorCalculator: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkKMeansDistanceFunctorCalculator: ...
    def SetDistanceExpression(self, _arg: str) -> None: ...
    def SetFunctionParser(self, __a: vtkmodules.vtkCommonMisc.vtkFunctionParser) -> None: ...

class vtkKMeansStatistics(vtkStatisticsAlgorithm):
    def Aggregate(
        self, __a: vtkmodules.vtkCommonDataModel.vtkDataObjectCollection, __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet
    ) -> None: ...
    def GetDefaultNumberOfClusters(self) -> int: ...
    def GetDistanceFunctor(self) -> vtkKMeansDistanceFunctor: ...
    def GetGhostsToSkip(self) -> int: ...
    def GetKValuesArrayName(self) -> str: ...
    def GetMaxNumIterations(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTolerance(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkKMeansStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkKMeansStatistics: ...
    def SetDefaultNumberOfClusters(self, _arg: int) -> None: ...
    def SetDistanceFunctor(self, __a: vtkKMeansDistanceFunctor) -> None: ...
    def SetGhostsToSkip(self, _arg: int) -> None: ...
    def SetKValuesArrayName(self, _arg: str) -> None: ...
    def SetMaxNumIterations(self, _arg: int) -> None: ...
    def SetParameter(self, parameter: str, index: int, value: vtkmodules.vtkCommonCore.vtkVariant) -> bool: ...
    def SetTolerance(self, _arg: float) -> None: ...

class vtkLengthDistribution(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    def GetLengthQuantile(self, qq: float = 0.5) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSampleSize(self) -> int: ...
    def GetSortSample(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLengthDistribution: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLengthDistribution: ...
    def SetSampleSize(self, _arg: int) -> None: ...
    def SetSortSample(self, _arg: bool) -> None: ...
    def SortSampleOff(self) -> None: ...
    def SortSampleOn(self) -> None: ...

class vtkMultiCorrelativeStatistics(vtkStatisticsAlgorithm):
    def Aggregate(
        self, __a: vtkmodules.vtkCommonDataModel.vtkDataObjectCollection, __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet
    ) -> None: ...
    def GetGhostsToSkip(self) -> int: ...
    def GetMedianAbsoluteDeviation(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MedianAbsoluteDeviationOff(self) -> None: ...
    def MedianAbsoluteDeviationOn(self) -> None: ...
    def NewInstance(self) -> vtkMultiCorrelativeStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMultiCorrelativeStatistics: ...
    def SetGhostsToSkip(self, _arg: int) -> None: ...
    def SetMedianAbsoluteDeviation(self, _arg: bool) -> None: ...

class vtkOrderStatistics(vtkStatisticsAlgorithm):
    class QuantileDefinitionType(int): ...
    InverseCDF: QuantileDefinitionType
    InverseCDFAveragedSteps: QuantileDefinitionType
    NearestObservation: QuantileDefinitionType

    def Aggregate(
        self, __a: vtkmodules.vtkCommonDataModel.vtkDataObjectCollection, __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet
    ) -> None: ...
    def GetGhostsToSkip(self) -> int: ...
    def GetMaximumHistogramSize(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfIntervals(self) -> int: ...
    def GetQuantileDefinition(self) -> int: ...
    def GetQuantize(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOrderStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOrderStatistics: ...
    def SetGhostsToSkip(self, _arg: int) -> None: ...
    def SetMaximumHistogramSize(self, _arg: int) -> None: ...
    def SetNumberOfIntervals(self, _arg: int) -> None: ...
    def SetParameter(self, parameter: str, index: int, value: vtkmodules.vtkCommonCore.vtkVariant) -> bool: ...
    @overload
    def SetQuantileDefinition(self, _arg: QuantileDefinitionType) -> None: ...
    @overload
    def SetQuantileDefinition(self, __a: int) -> None: ...
    def SetQuantize(self, _arg: bool) -> None: ...

class vtkPCAStatistics(vtkMultiCorrelativeStatistics):
    class NormalizationType(int): ...
    class ProjectionType(int): ...
    DIAGONAL_SPECIFIED: NormalizationType
    DIAGONAL_VARIANCE: NormalizationType
    FIXED_BASIS_ENERGY: ProjectionType
    FIXED_BASIS_SIZE: ProjectionType
    FULL_BASIS: ProjectionType
    NONE: NormalizationType
    NUM_BASIS_SCHEMES: ProjectionType
    NUM_NORMALIZATION_SCHEMES: NormalizationType
    TRIANGLE_SPECIFIED: NormalizationType
    def GetBasisScheme(self) -> int: ...
    def GetBasisSchemeName(self, schemeIndex: int) -> str: ...
    @overload
    def GetEigenvalue(self, request: int, i: int) -> float: ...
    @overload
    def GetEigenvalue(self, i: int) -> float: ...
    @overload
    def GetEigenvalues(self, request: int, __b: vtkmodules.vtkCommonCore.vtkDoubleArray) -> None: ...
    @overload
    def GetEigenvalues(self, __a: vtkmodules.vtkCommonCore.vtkDoubleArray) -> None: ...
    @overload
    def GetEigenvector(self, i: int, eigenvector: vtkmodules.vtkCommonCore.vtkDoubleArray) -> None: ...
    @overload
    def GetEigenvector(self, request: int, i: int, eigenvector: vtkmodules.vtkCommonCore.vtkDoubleArray) -> None: ...
    @overload
    def GetEigenvectors(self, request: int, eigenvectors: vtkmodules.vtkCommonCore.vtkDoubleArray) -> None: ...
    @overload
    def GetEigenvectors(self, eigenvectors: vtkmodules.vtkCommonCore.vtkDoubleArray) -> None: ...
    def GetFixedBasisEnergy(self) -> float: ...
    def GetFixedBasisEnergyMaxValue(self) -> float: ...
    def GetFixedBasisEnergyMinValue(self) -> float: ...
    def GetFixedBasisSize(self) -> int: ...
    def GetNormalizationScheme(self) -> int: ...
    def GetNormalizationSchemeName(self, scheme: int) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSpecifiedNormalization(self) -> vtkmodules.vtkCommonDataModel.vtkTable: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPCAStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPCAStatistics: ...
    def SetBasisScheme(self, _arg: int) -> None: ...
    def SetBasisSchemeByName(self, schemeName: str) -> None: ...
    def SetFixedBasisEnergy(self, _arg: float) -> None: ...
    def SetFixedBasisSize(self, _arg: int) -> None: ...
    def SetNormalizationScheme(self, _arg: int) -> None: ...
    def SetNormalizationSchemeByName(self, schemeName: str) -> None: ...
    def SetParameter(self, parameter: str, index: int, value: vtkmodules.vtkCommonCore.vtkVariant) -> bool: ...
    def SetSpecifiedNormalization(self, __a: vtkmodules.vtkCommonDataModel.vtkTable) -> None: ...

class vtkStrahlerMetric(vtkmodules.vtkCommonExecutionModel.vtkTreeAlgorithm):
    def GetMaxStrahler(self) -> float: ...
    def GetNormalize(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkStrahlerMetric: ...
    def NormalizeOff(self) -> None: ...
    def NormalizeOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkStrahlerMetric: ...
    def SetMetricArrayName(self, _arg: str) -> None: ...
    def SetNormalize(self, _arg: int) -> None: ...

class vtkStreamingStatistics(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    class InputPorts(int): ...
    class OutputIndices(int): ...
    INPUT_DATA: InputPorts
    INPUT_MODEL: InputPorts
    LEARN_PARAMETERS: InputPorts
    OUTPUT_DATA: OutputIndices
    OUTPUT_MODEL: OutputIndices
    OUTPUT_TEST: OutputIndices
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkStreamingStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkStreamingStatistics: ...
    def SetStatisticsAlgorithm(self, __a: vtkStatisticsAlgorithm) -> None: ...
