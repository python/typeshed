from collections.abc import Callable
from typing import TypeVar, Union

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkFiltersStatistics
import vtkmodules.vtkParallelCore

Template = TypeVar("Template")

class vtkPAutoCorrelativeStatistics(vtkmodules.vtkFiltersStatistics.vtkAutoCorrelativeStatistics):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def Learn(
        self,
        inData: vtkmodules.vtkCommonDataModel.vtkTable,
        inParameters: vtkmodules.vtkCommonDataModel.vtkTable,
        outMeta: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet,
    ) -> None: ...
    def NewInstance(self) -> vtkPAutoCorrelativeStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPAutoCorrelativeStatistics: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def Test(
        self,
        __a: vtkmodules.vtkCommonDataModel.vtkTable,
        __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet,
        __c: vtkmodules.vtkCommonDataModel.vtkTable,
    ) -> None: ...

class vtkPBivariateLinearTableThreshold(vtkmodules.vtkFiltersStatistics.vtkBivariateLinearTableThreshold):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPBivariateLinearTableThreshold: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPBivariateLinearTableThreshold: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...

class vtkPComputeQuantiles(vtkmodules.vtkFiltersStatistics.vtkComputeQuantiles):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPComputeQuantiles: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPComputeQuantiles: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...

class vtkPComputeQuartiles(vtkmodules.vtkFiltersStatistics.vtkComputeQuartiles):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPComputeQuartiles: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPComputeQuartiles: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...

class vtkPContingencyStatistics(vtkmodules.vtkFiltersStatistics.vtkContingencyStatistics):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def Learn(
        self,
        __a: vtkmodules.vtkCommonDataModel.vtkTable,
        __b: vtkmodules.vtkCommonDataModel.vtkTable,
        __c: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet,
    ) -> None: ...
    def NewInstance(self) -> vtkPContingencyStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPContingencyStatistics: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...

class vtkPCorrelativeStatistics(vtkmodules.vtkFiltersStatistics.vtkCorrelativeStatistics):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def Learn(
        self,
        inData: vtkmodules.vtkCommonDataModel.vtkTable,
        inParameters: vtkmodules.vtkCommonDataModel.vtkTable,
        outMeta: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet,
    ) -> None: ...
    def NewInstance(self) -> vtkPCorrelativeStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPCorrelativeStatistics: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def Test(
        self,
        __a: vtkmodules.vtkCommonDataModel.vtkTable,
        __b: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet,
        __c: vtkmodules.vtkCommonDataModel.vtkTable,
    ) -> None: ...

class vtkPDescriptiveStatistics(vtkmodules.vtkFiltersStatistics.vtkDescriptiveStatistics):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def Learn(
        self,
        inData: vtkmodules.vtkCommonDataModel.vtkTable,
        inParameters: vtkmodules.vtkCommonDataModel.vtkTable,
        outMeta: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet,
    ) -> None: ...
    def NewInstance(self) -> vtkPDescriptiveStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPDescriptiveStatistics: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...

class vtkPKMeansStatistics(vtkmodules.vtkFiltersStatistics.vtkKMeansStatistics):
    def CreateInitialClusterCenters(
        self,
        numToAllocate: int,
        numberOfClusters: vtkmodules.vtkCommonCore.vtkIdTypeArray,
        inData: vtkmodules.vtkCommonDataModel.vtkTable,
        curClusterElements: vtkmodules.vtkCommonDataModel.vtkTable,
        newClusterElements: vtkmodules.vtkCommonDataModel.vtkTable,
    ) -> None: ...
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTotalNumberOfObservations(self, numObservations: int) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPKMeansStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPKMeansStatistics: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def UpdateClusterCenters(
        self,
        newClusterElements: vtkmodules.vtkCommonDataModel.vtkTable,
        curClusterElements: vtkmodules.vtkCommonDataModel.vtkTable,
        numMembershipChanges: vtkmodules.vtkCommonCore.vtkIdTypeArray,
        numElementsInCluster: vtkmodules.vtkCommonCore.vtkIdTypeArray,
        error: vtkmodules.vtkCommonCore.vtkDoubleArray,
        startRunID: vtkmodules.vtkCommonCore.vtkIdTypeArray,
        endRunID: vtkmodules.vtkCommonCore.vtkIdTypeArray,
        computeRun: vtkmodules.vtkCommonCore.vtkIntArray,
    ) -> None: ...

class vtkPMultiCorrelativeStatistics(vtkmodules.vtkFiltersStatistics.vtkMultiCorrelativeStatistics):
    @staticmethod
    def GatherStatistics(
        curController: vtkmodules.vtkParallelCore.vtkMultiProcessController, sparseCov: vtkmodules.vtkCommonDataModel.vtkTable
    ) -> None: ...
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPMultiCorrelativeStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPMultiCorrelativeStatistics: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...

class vtkPOrderStatistics(vtkmodules.vtkFiltersStatistics.vtkOrderStatistics):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def Learn(
        self,
        __a: vtkmodules.vtkCommonDataModel.vtkTable,
        __b: vtkmodules.vtkCommonDataModel.vtkTable,
        __c: vtkmodules.vtkCommonDataModel.vtkMultiBlockDataSet,
    ) -> None: ...
    def NewInstance(self) -> vtkPOrderStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPOrderStatistics: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...

class vtkPPCAStatistics(vtkmodules.vtkFiltersStatistics.vtkPCAStatistics):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPPCAStatistics: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPPCAStatistics: ...
    def SetController(self, __a: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
