from _typeshed import Incomplete

from .common import CtrlNode, PlottingCtrlNode, metaArrayWrapper

class Downsample(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Subsample(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Bessel(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Butterworth(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class ButterworthNotch(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Mean(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    @metaArrayWrapper
    def processData(self, data): ...

class Median(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    @metaArrayWrapper
    def processData(self, data): ...

class Mode(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    @metaArrayWrapper
    def processData(self, data): ...

class Denoise(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class Gaussian(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    @metaArrayWrapper
    def processData(self, data): ...

class Derivative(CtrlNode):
    nodeName: str
    def processData(self, data): ...

class Integral(CtrlNode):
    nodeName: str
    @metaArrayWrapper
    def processData(self, data): ...

class Detrend(CtrlNode):
    nodeName: str
    @metaArrayWrapper
    def processData(self, data): ...

class RemoveBaseline(PlottingCtrlNode):
    nodeName: str
    line: Incomplete
    def __init__(self, name) -> None: ...
    def connectToPlot(self, node) -> None: ...
    def disconnectFromPlot(self, plot) -> None: ...
    def processData(self, data): ...
    def adjustXPositions(self, pts, data): ...

class AdaptiveDetrend(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class HistogramDetrend(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...

class RemovePeriodic(CtrlNode):
    nodeName: str
    uiTemplate: Incomplete
    def processData(self, data): ...
