from collections.abc import MutableSequence, Sequence
from typing import overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkRenderingCore
import vtkmodules.vtkRenderingOpenGL2

class vtkCompositeSurfaceLICMapper(vtkmodules.vtkRenderingOpenGL2.vtkCompositePolyDataMapper2):
    def GetLICInterface(self) -> vtkSurfaceLICInterface: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCompositeSurfaceLICMapper: ...
    def Render(self, ren: vtkmodules.vtkRenderingCore.vtkRenderer, act: vtkmodules.vtkRenderingCore.vtkActor) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCompositeSurfaceLICMapper: ...

class vtkImageDataLIC2D(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetContext(self) -> vtkmodules.vtkRenderingCore.vtkRenderWindow: ...
    def GetMagnification(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOpenGLExtensionsSupported(self) -> int: ...
    def GetStepSize(self) -> float: ...
    def GetSteps(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageDataLIC2D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageDataLIC2D: ...
    def SetContext(self, context: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> int: ...
    def SetMagnification(self, _arg: int) -> None: ...
    def SetStepSize(self, _arg: float) -> None: ...
    def SetSteps(self, _arg: int) -> None: ...
    def TranslateInputExtent(self, inExt: Sequence[int], inWholeExtent: Sequence[int], outExt: MutableSequence[int]) -> None: ...

class vtkLineIntegralConvolution2D(vtkmodules.vtkCommonCore.vtkObject):
    ENHANCE_CONTRAST_OFF: int
    ENHANCE_CONTRAST_ON: int
    def AntiAliasOff(self) -> None: ...
    def AntiAliasOn(self) -> None: ...
    def EnhanceContrastOff(self) -> None: ...
    def EnhanceContrastOn(self) -> None: ...
    def EnhancedLICOff(self) -> None: ...
    def EnhancedLICOn(self) -> None: ...
    @overload
    def Execute(
        self,
        vectorTex: vtkmodules.vtkRenderingOpenGL2.vtkTextureObject,
        noiseTex: vtkmodules.vtkRenderingOpenGL2.vtkTextureObject,
    ) -> vtkmodules.vtkRenderingOpenGL2.vtkTextureObject: ...
    @overload
    def Execute(
        self,
        extent: Sequence[int],
        vectorTex: vtkmodules.vtkRenderingOpenGL2.vtkTextureObject,
        noiseTex: vtkmodules.vtkRenderingOpenGL2.vtkTextureObject,
    ) -> vtkmodules.vtkRenderingOpenGL2.vtkTextureObject: ...
    def GetAntiAlias(self) -> int: ...
    def GetAntiAliasMaxValue(self) -> int: ...
    def GetAntiAliasMinValue(self) -> int: ...
    def GetComponentIds(self) -> tuple[int, int]: ...
    def GetContext(self) -> vtkmodules.vtkRenderingOpenGL2.vtkOpenGLRenderWindow: ...
    def GetEnhanceContrast(self) -> int: ...
    def GetEnhanceContrastMaxValue(self) -> int: ...
    def GetEnhanceContrastMinValue(self) -> int: ...
    def GetEnhancedLIC(self) -> int: ...
    def GetEnhancedLICMaxValue(self) -> int: ...
    def GetEnhancedLICMinValue(self) -> int: ...
    def GetHighContrastEnhancementFactor(self) -> float: ...
    def GetHighContrastEnhancementFactorMaxValue(self) -> float: ...
    def GetHighContrastEnhancementFactorMinValue(self) -> float: ...
    def GetLowContrastEnhancementFactor(self) -> float: ...
    def GetLowContrastEnhancementFactorMaxValue(self) -> float: ...
    def GetLowContrastEnhancementFactorMinValue(self) -> float: ...
    def GetMaskThreshold(self) -> float: ...
    def GetMaskThresholdMaxValue(self) -> float: ...
    def GetMaskThresholdMinValue(self) -> float: ...
    def GetMaxNoiseValue(self) -> float: ...
    def GetMaxNoiseValueMaxValue(self) -> float: ...
    def GetMaxNoiseValueMinValue(self) -> float: ...
    def GetNormalizeVectors(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfSteps(self) -> int: ...
    def GetNumberOfStepsMaxValue(self) -> int: ...
    def GetNumberOfStepsMinValue(self) -> int: ...
    def GetStepSize(self) -> float: ...
    def GetStepSizeMaxValue(self) -> float: ...
    def GetStepSizeMinValue(self) -> float: ...
    def GetTransformVectors(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsSupported(renWin: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLineIntegralConvolution2D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLineIntegralConvolution2D: ...
    def SetAntiAlias(self, _arg: int) -> None: ...
    @overload
    def SetComponentIds(self, c0: int, c1: int) -> None: ...
    @overload
    def SetComponentIds(self, c: MutableSequence[int]) -> None: ...
    def SetContext(self, context: vtkmodules.vtkRenderingOpenGL2.vtkOpenGLRenderWindow) -> None: ...
    def SetEnhanceContrast(self, _arg: int) -> None: ...
    def SetEnhancedLIC(self, _arg: int) -> None: ...
    def SetHighContrastEnhancementFactor(self, _arg: float) -> None: ...
    def SetLowContrastEnhancementFactor(self, _arg: float) -> None: ...
    def SetMaskThreshold(self, _arg: float) -> None: ...
    def SetMaxNoiseValue(self, _arg: float) -> None: ...
    @staticmethod
    def SetNoiseTexParameters(noise: vtkmodules.vtkRenderingOpenGL2.vtkTextureObject) -> None: ...
    def SetNormalizeVectors(self, val: int) -> None: ...
    def SetNumberOfSteps(self, _arg: int) -> None: ...
    def SetStepSize(self, _arg: float) -> None: ...
    def SetTransformVectors(self, val: int) -> None: ...
    @staticmethod
    def SetVectorTexParameters(vectors: vtkmodules.vtkRenderingOpenGL2.vtkTextureObject) -> None: ...
    def WriteTimerLog(self, __a: str) -> None: ...

class vtkPainterCommunicator:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: vtkPainterCommunicator) -> None: ...
    def GetIsNull(self) -> bool: ...
    def GetMPIFinalized(self) -> bool: ...
    def GetMPIInitialized(self) -> bool: ...
    def GetRank(self) -> int: ...
    def GetSize(self) -> int: ...
    def GetWorldRank(self) -> int: ...
    def GetWorldSize(self) -> int: ...

class vtkStructuredGridLIC2D(vtkmodules.vtkCommonExecutionModel.vtkStructuredGridAlgorithm):
    def GetContext(self) -> vtkmodules.vtkRenderingCore.vtkRenderWindow: ...
    def GetFBOSuccess(self) -> int: ...
    def GetLICSuccess(self) -> int: ...
    def GetMagnification(self) -> int: ...
    def GetMagnificationMaxValue(self) -> int: ...
    def GetMagnificationMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetStepSize(self) -> float: ...
    def GetSteps(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkStructuredGridLIC2D: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkStructuredGridLIC2D: ...
    def SetContext(self, context: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> int: ...
    def SetMagnification(self, _arg: int) -> None: ...
    def SetStepSize(self, _arg: float) -> None: ...
    def SetSteps(self, _arg: int) -> None: ...

class vtkSurfaceLICComposite(vtkmodules.vtkCommonCore.vtkObject):
    COMPOSITE_AUTO: int
    COMPOSITE_BALANCED: int
    COMPOSITE_INPLACE: int
    COMPOSITE_INPLACE_DISJOINT: int
    def BuildProgram(self, __a: MutableSequence[float]) -> int: ...
    def GetCompositeExtent(self, i: int = 0) -> vtkmodules.vtkCommonDataModel.vtkPixelExtent: ...
    def GetContext(self) -> vtkmodules.vtkRenderingOpenGL2.vtkOpenGLRenderWindow: ...
    def GetDataSetExtent(self) -> vtkmodules.vtkCommonDataModel.vtkPixelExtent: ...
    def GetDisjointGuardExtent(self, i: int = 0) -> vtkmodules.vtkCommonDataModel.vtkPixelExtent: ...
    def GetGuardExtent(self, i: int = 0) -> vtkmodules.vtkCommonDataModel.vtkPixelExtent: ...
    def GetNumberOfCompositeExtents(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetStrategy(self) -> int: ...
    def GetWindowExtent(self) -> vtkmodules.vtkCommonDataModel.vtkPixelExtent: ...
    def InitializeCompositeExtents(self, vectors: MutableSequence[float]) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSurfaceLICComposite: ...
    def RestoreDefaultCommunicator(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSurfaceLICComposite: ...
    def SetContext(self, __a: vtkmodules.vtkRenderingOpenGL2.vtkOpenGLRenderWindow) -> None: ...
    def SetStrategy(self, val: int) -> None: ...

class vtkSurfaceLICInterface(vtkmodules.vtkCommonCore.vtkObject):
    COLOR_MODE_BLEND: int
    COLOR_MODE_MAP: int
    COMPOSITE_AUTO: int
    COMPOSITE_BALANCED: int
    COMPOSITE_INPLACE: int
    COMPOSITE_INPLACE_DISJOINT: int
    ENHANCE_CONTRAST_BOTH: int
    ENHANCE_CONTRAST_COLOR: int
    ENHANCE_CONTRAST_LIC: int
    ENHANCE_CONTRAST_OFF: int
    NOISE_TYPE_GAUSSIAN: int
    NOISE_TYPE_PERLIN: int
    NOISE_TYPE_UNIFORM: int
    def AntiAliasOff(self) -> None: ...
    def AntiAliasOn(self) -> None: ...
    def ApplyLIC(self) -> None: ...
    def CanRenderSurfaceLIC(self, actor: vtkmodules.vtkRenderingCore.vtkActor) -> bool: ...
    def CombineColorsAndLIC(self) -> None: ...
    def CompletedGeometry(self) -> None: ...
    def CopyToScreen(self) -> None: ...
    def CreateCommunicator(
        self,
        __a: vtkmodules.vtkRenderingCore.vtkRenderer,
        __b: vtkmodules.vtkRenderingCore.vtkActor,
        data: vtkmodules.vtkCommonDataModel.vtkDataObject,
    ) -> None: ...
    def EnableOff(self) -> None: ...
    def EnableOn(self) -> None: ...
    def EnhancedLICOff(self) -> None: ...
    def EnhancedLICOn(self) -> None: ...
    def GatherVectors(self) -> None: ...
    def GetAntiAlias(self) -> int: ...
    def GetColorMode(self) -> int: ...
    def GetCompositeStrategy(self) -> int: ...
    def GetEnable(self) -> int: ...
    def GetEnhanceContrast(self) -> int: ...
    def GetEnhancedLIC(self) -> int: ...
    def GetGenerateNoiseTexture(self) -> int: ...
    def GetHasVectors(self) -> bool: ...
    def GetHighColorContrastEnhancementFactor(self) -> float: ...
    def GetHighLICContrastEnhancementFactor(self) -> float: ...
    def GetImpulseNoiseBackgroundValue(self) -> float: ...
    def GetImpulseNoiseProbability(self) -> float: ...
    def GetLICIntensity(self) -> float: ...
    def GetLowColorContrastEnhancementFactor(self) -> float: ...
    def GetLowLICContrastEnhancementFactor(self) -> float: ...
    def GetMapModeBias(self) -> float: ...
    def GetMaskColor(self) -> tuple[float, float, float]: ...
    def GetMaskIntensity(self) -> float: ...
    def GetMaskOnSurface(self) -> int: ...
    def GetMaskThreshold(self) -> float: ...
    def GetMaxNoiseValue(self) -> float: ...
    def GetMinNoiseValue(self) -> float: ...
    def GetNoiseDataSet(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetNoiseGeneratorSeed(self) -> int: ...
    def GetNoiseGrainSize(self) -> int: ...
    def GetNoiseTextureSize(self) -> int: ...
    def GetNoiseType(self) -> int: ...
    def GetNormalizeVectors(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfNoiseLevels(self) -> int: ...
    def GetNumberOfSteps(self) -> int: ...
    def GetStepSize(self) -> float: ...
    def InitializeResources(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsSupported(context: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MaskOnSurfaceOff(self) -> None: ...
    def MaskOnSurfaceOn(self) -> None: ...
    def NewInstance(self) -> vtkSurfaceLICInterface: ...
    def NormalizeVectorsOff(self) -> None: ...
    def NormalizeVectorsOn(self) -> None: ...
    def PrepareForGeometry(self) -> None: ...
    def ReleaseGraphicsResources(self, win: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSurfaceLICInterface: ...
    def SetAntiAlias(self, val: int) -> None: ...
    def SetColorMode(self, val: int) -> None: ...
    def SetCompositeStrategy(self, val: int) -> None: ...
    def SetEnable(self, _arg: int) -> None: ...
    def SetEnhanceContrast(self, val: int) -> None: ...
    def SetEnhancedLIC(self, val: int) -> None: ...
    def SetGenerateNoiseTexture(self, shouldGenerate: int) -> None: ...
    def SetHasVectors(self, val: bool) -> None: ...
    def SetHighColorContrastEnhancementFactor(self, val: float) -> None: ...
    def SetHighLICContrastEnhancementFactor(self, val: float) -> None: ...
    def SetImpulseNoiseBackgroundValue(self, val: float) -> None: ...
    def SetImpulseNoiseProbability(self, val: float) -> None: ...
    def SetLICIntensity(self, val: float) -> None: ...
    def SetLowColorContrastEnhancementFactor(self, val: float) -> None: ...
    def SetLowLICContrastEnhancementFactor(self, val: float) -> None: ...
    def SetMapModeBias(self, val: float) -> None: ...
    @overload
    def SetMaskColor(self, val: MutableSequence[float]) -> None: ...
    @overload
    def SetMaskColor(self, r: float, g: float, b: float) -> None: ...
    def SetMaskIntensity(self, val: float) -> None: ...
    def SetMaskOnSurface(self, val: int) -> None: ...
    def SetMaskThreshold(self, val: float) -> None: ...
    def SetMaxNoiseValue(self, val: float) -> None: ...
    def SetMinNoiseValue(self, val: float) -> None: ...
    def SetNoiseDataSet(self, data: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    def SetNoiseGeneratorSeed(self, val: int) -> None: ...
    def SetNoiseGrainSize(self, val: int) -> None: ...
    def SetNoiseTextureSize(self, length: int) -> None: ...
    def SetNoiseType(self, type: int) -> None: ...
    def SetNormalizeVectors(self, val: int) -> None: ...
    def SetNumberOfNoiseLevels(self, val: int) -> None: ...
    def SetNumberOfSteps(self, val: int) -> None: ...
    def SetStepSize(self, val: float) -> None: ...
    def ShallowCopy(self, m: vtkSurfaceLICInterface) -> None: ...
    def UpdateCommunicator(
        self,
        renderer: vtkmodules.vtkRenderingCore.vtkRenderer,
        actor: vtkmodules.vtkRenderingCore.vtkActor,
        data: vtkmodules.vtkCommonDataModel.vtkDataObject,
    ) -> None: ...
    def ValidateContext(self, renderer: vtkmodules.vtkRenderingCore.vtkRenderer) -> None: ...
    def WriteTimerLog(self, __a: str) -> None: ...

class vtkSurfaceLICMapper(vtkmodules.vtkRenderingOpenGL2.vtkOpenGLPolyDataMapper):
    def GetLICInterface(self) -> vtkSurfaceLICInterface: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSurfaceLICMapper: ...
    def ReleaseGraphicsResources(self, win: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    def RenderPiece(self, ren: vtkmodules.vtkRenderingCore.vtkRenderer, act: vtkmodules.vtkRenderingCore.vtkActor) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSurfaceLICMapper: ...
    def ShallowCopy(self, __a: vtkmodules.vtkRenderingCore.vtkAbstractMapper) -> None: ...

class vtkTextureIO:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __a: vtkTextureIO) -> None: ...
    @overload
    @staticmethod
    def Write(
        filename: str,
        texture: vtkmodules.vtkRenderingOpenGL2.vtkTextureObject,
        subset: Sequence[int] = ...,
        origin: Sequence[float] = ...,
    ) -> None: ...
    @overload
    @staticmethod
    def Write(
        filename: str,
        texture: vtkmodules.vtkRenderingOpenGL2.vtkTextureObject,
        subset: vtkmodules.vtkCommonDataModel.vtkPixelExtent,
        origin: Sequence[float] = ...,
    ) -> None: ...
