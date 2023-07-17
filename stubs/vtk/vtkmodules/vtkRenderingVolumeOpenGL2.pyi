from collections.abc import MutableSequence, Sequence
from typing import Tuple, TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonMath
import vtkmodules.vtkRenderingCore
import vtkmodules.vtkRenderingOpenGL2
import vtkmodules.vtkRenderingVolume

Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkMultiBlockUnstructuredGridVolumeMapper(vtkmodules.vtkRenderingVolume.vtkUnstructuredGridVolumeMapper):
    @overload
    def GetBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    @overload
    def GetBounds(self, bounds: MutableSequence[float]) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetUseFloatingPointFrameBuffer(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMultiBlockUnstructuredGridVolumeMapper: ...
    def ReleaseGraphicsResources(self, window: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    def Render(self, ren: vtkmodules.vtkRenderingCore.vtkRenderer, vol: vtkmodules.vtkRenderingCore.vtkVolume) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMultiBlockUnstructuredGridVolumeMapper: ...
    @overload
    def SelectScalarArray(self, arrayNum: int) -> None: ...
    @overload
    def SelectScalarArray(self, arrayName: str) -> None: ...
    def SetArrayAccessMode(self, accessMode: int) -> None: ...
    def SetBlendMode(self, mode: int) -> None: ...
    def SetScalarMode(self, ScalarMode: int) -> None: ...
    def SetUseFloatingPointFrameBuffer(self, use: bool) -> None: ...

class vtkMultiBlockVolumeMapper(vtkmodules.vtkRenderingVolume.vtkVolumeMapper):
    @overload
    def GetBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    @overload
    def GetBounds(self, bounds: MutableSequence[float]) -> None: ...
    def GetGlobalIlluminationReach(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetVectorComponent(self) -> int: ...
    def GetVectorMode(self) -> int: ...
    def GetVolumetricScatteringBlending(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMultiBlockVolumeMapper: ...
    def ReleaseGraphicsResources(self, window: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    def Render(self, ren: vtkmodules.vtkRenderingCore.vtkRenderer, vol: vtkmodules.vtkRenderingCore.vtkVolume) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMultiBlockVolumeMapper: ...
    @overload
    def SelectScalarArray(self, arrayNum: int) -> None: ...
    @overload
    def SelectScalarArray(self, arrayName: str) -> None: ...
    def SetArrayAccessMode(self, accessMode: int) -> None: ...
    def SetBlendMode(self, mode: int) -> None: ...
    def SetComputeNormalFromOpacity(self, val: bool) -> None: ...
    def SetCropping(self, mode: int) -> None: ...
    def SetCroppingRegionFlags(self, mode: int) -> None: ...
    @overload
    def SetCroppingRegionPlanes(self, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float) -> None: ...
    @overload
    def SetCroppingRegionPlanes(self, planes: Sequence[float]) -> None: ...
    def SetGlobalIlluminationReach(self, val: float) -> None: ...
    def SetRequestedRenderMode(self, __a: int) -> None: ...
    def SetScalarMode(self, ScalarMode: int) -> None: ...
    def SetTransfer2DYAxisArray(self, a: str) -> None: ...
    def SetVectorComponent(self, component: int) -> None: ...
    def SetVectorMode(self, mode: int) -> None: ...
    def SetVolumetricScatteringBlending(self, val: float) -> None: ...

class vtkOpenGLGPUVolumeRayCastMapper(vtkmodules.vtkRenderingVolume.vtkGPUVolumeRayCastMapper):
    class Passes(int): ...
    DepthPass: Passes
    RenderPass: Passes

    def GetColorImage(self, im: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    def GetColorTexture(self) -> vtkmodules.vtkRenderingOpenGL2.vtkTextureObject: ...
    def GetCurrentPass(self) -> int: ...
    def GetDepthImage(self, im: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    def GetDepthTexture(self) -> vtkmodules.vtkRenderingOpenGL2.vtkTextureObject: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOpenGLGPUVolumeRayCastMapper: ...
    def PreLoadData(self, ren: vtkmodules.vtkRenderingCore.vtkRenderer, vol: vtkmodules.vtkRenderingCore.vtkVolume) -> bool: ...
    def ReleaseGraphicsResources(self, window: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOpenGLGPUVolumeRayCastMapper: ...
    def SetPartitions(self, x: int, y: int, z: int) -> None: ...
    def SetSharedDepthTexture(self, nt: vtkmodules.vtkRenderingOpenGL2.vtkTextureObject) -> None: ...

class vtkOpenGLProjectedTetrahedraMapper(vtkmodules.vtkRenderingVolume.vtkProjectedTetrahedraMapper):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetUseFloatingPointFrameBuffer(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    def IsSupported(self, context: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOpenGLProjectedTetrahedraMapper: ...
    def ReleaseGraphicsResources(self, window: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    def Render(
        self, renderer: vtkmodules.vtkRenderingCore.vtkRenderer, volume: vtkmodules.vtkRenderingCore.vtkVolume
    ) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOpenGLProjectedTetrahedraMapper: ...
    def SetUseFloatingPointFrameBuffer(self, _arg: bool) -> None: ...
    def UseFloatingPointFrameBufferOff(self) -> None: ...
    def UseFloatingPointFrameBufferOn(self) -> None: ...

class vtkOpenGLRayCastImageDisplayHelper(vtkmodules.vtkRenderingVolume.vtkRayCastImageDisplayHelper):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOpenGLRayCastImageDisplayHelper: ...
    def ReleaseGraphicsResources(self, win: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    @overload
    def RenderTexture(
        self,
        vol: vtkmodules.vtkRenderingCore.vtkVolume,
        ren: vtkmodules.vtkRenderingCore.vtkRenderer,
        imageMemorySize: MutableSequence[int],
        imageViewportSize: MutableSequence[int],
        imageInUseSize: MutableSequence[int],
        imageOrigin: MutableSequence[int],
        requestedDepth: float,
        image: MutableSequence[int],
    ) -> None: ...
    @overload
    def RenderTexture(
        self,
        vol: vtkmodules.vtkRenderingCore.vtkVolume,
        ren: vtkmodules.vtkRenderingCore.vtkRenderer,
        image: vtkmodules.vtkRenderingVolume.vtkFixedPointRayCastImage,
        requestedDepth: float,
    ) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOpenGLRayCastImageDisplayHelper: ...

class vtkSmartVolumeMapper(vtkmodules.vtkRenderingVolume.vtkVolumeMapper):
    class VectorModeType(int): ...
    COMPONENT: VectorModeType
    DISABLED: VectorModeType
    DefaultRenderMode: int
    GPURenderMode: int
    InvalidRenderMode: int
    MAGNITUDE: VectorModeType
    OSPRayRenderMode: int
    RayCastRenderMode: int
    UndefinedRenderMode: int
    def AutoAdjustSampleDistancesOff(self) -> None: ...
    def AutoAdjustSampleDistancesOn(self) -> None: ...
    def CreateCanonicalView(
        self,
        ren: vtkmodules.vtkRenderingCore.vtkRenderer,
        volume: vtkmodules.vtkRenderingCore.vtkVolume,
        volume2: vtkmodules.vtkRenderingCore.vtkVolume,
        image: vtkmodules.vtkCommonDataModel.vtkImageData,
        blend_mode: int,
        viewDirection: MutableSequence[float],
        viewUp: MutableSequence[float],
    ) -> None: ...
    def GetAutoAdjustSampleDistances(self) -> int: ...
    def GetAutoAdjustSampleDistancesMaxValue(self) -> int: ...
    def GetAutoAdjustSampleDistancesMinValue(self) -> int: ...
    def GetFinalColorLevel(self) -> float: ...
    def GetFinalColorWindow(self) -> float: ...
    def GetGlobalIlluminationReach(self) -> float: ...
    def GetGlobalIlluminationReachMaxValue(self) -> float: ...
    def GetGlobalIlluminationReachMinValue(self) -> float: ...
    def GetInteractiveAdjustSampleDistances(self) -> int: ...
    def GetInteractiveAdjustSampleDistancesMaxValue(self) -> int: ...
    def GetInteractiveAdjustSampleDistancesMinValue(self) -> int: ...
    def GetInteractiveUpdateRate(self) -> float: ...
    def GetInteractiveUpdateRateMaxValue(self) -> float: ...
    def GetInteractiveUpdateRateMinValue(self) -> float: ...
    def GetInterpolationMode(self) -> int: ...
    def GetInterpolationModeMaxValue(self) -> int: ...
    def GetInterpolationModeMinValue(self) -> int: ...
    def GetLastUsedRenderMode(self) -> int: ...
    def GetMaxMemoryFraction(self) -> float: ...
    def GetMaxMemoryFractionMaxValue(self) -> float: ...
    def GetMaxMemoryFractionMinValue(self) -> float: ...
    def GetMaxMemoryInBytes(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRequestedRenderMode(self) -> int: ...
    def GetSampleDistance(self) -> float: ...
    def GetTransfer2DYAxisArray(self) -> str: ...
    def GetVectorComponent(self) -> int: ...
    def GetVectorComponentMaxValue(self) -> int: ...
    def GetVectorComponentMinValue(self) -> int: ...
    def GetVectorMode(self) -> int: ...
    def GetVolumetricScatteringBlending(self) -> float: ...
    def GetVolumetricScatteringBlendingMaxValue(self) -> float: ...
    def GetVolumetricScatteringBlendingMinValue(self) -> float: ...
    def InteractiveAdjustSampleDistancesOff(self) -> None: ...
    def InteractiveAdjustSampleDistancesOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSmartVolumeMapper: ...
    def ReleaseGraphicsResources(self, __a: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    def Render(self, __a: vtkmodules.vtkRenderingCore.vtkRenderer, __b: vtkmodules.vtkRenderingCore.vtkVolume) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSmartVolumeMapper: ...
    def SetAutoAdjustSampleDistances(self, _arg: int) -> None: ...
    def SetFinalColorLevel(self, _arg: float) -> None: ...
    def SetFinalColorWindow(self, _arg: float) -> None: ...
    def SetGlobalIlluminationReach(self, _arg: float) -> None: ...
    def SetInteractiveAdjustSampleDistances(self, _arg: int) -> None: ...
    def SetInteractiveUpdateRate(self, _arg: float) -> None: ...
    def SetInterpolationMode(self, _arg: int) -> None: ...
    def SetInterpolationModeToCubic(self) -> None: ...
    def SetInterpolationModeToLinear(self) -> None: ...
    def SetInterpolationModeToNearestNeighbor(self) -> None: ...
    def SetMaxMemoryFraction(self, _arg: float) -> None: ...
    def SetMaxMemoryInBytes(self, _arg: int) -> None: ...
    def SetRequestedRenderMode(self, mode: int) -> None: ...
    def SetRequestedRenderModeToDefault(self) -> None: ...
    def SetRequestedRenderModeToGPU(self) -> None: ...
    def SetRequestedRenderModeToOSPRay(self) -> None: ...
    def SetRequestedRenderModeToRayCast(self) -> None: ...
    def SetSampleDistance(self, _arg: float) -> None: ...
    def SetTransfer2DYAxisArray(self, _arg: str) -> None: ...
    def SetVectorComponent(self, _arg: int) -> None: ...
    def SetVectorMode(self, mode: int) -> None: ...
    def SetVolumetricScatteringBlending(self, _arg: float) -> None: ...

class vtkVolumeTexture(vtkmodules.vtkCommonCore.vtkObject):
    def GetLoadedScalars(self) -> vtkmodules.vtkCommonCore.vtkDataArray: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPartitions(self) -> vtkmodules.vtkCommonMath.vtkTuple_IiLi3EE: ...
    @staticmethod
    def GetScaleAndBias(scalarType: int, scalarRange: MutableSequence[float], scale: float, bias: float) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def LoadVolume(
        self,
        ren: vtkmodules.vtkRenderingCore.vtkRenderer,
        data: vtkmodules.vtkCommonDataModel.vtkDataSet,
        scalars: vtkmodules.vtkCommonCore.vtkDataArray,
        isCell: int,
        interpolation: int,
    ) -> bool: ...
    def NewInstance(self) -> vtkVolumeTexture: ...
    def ReleaseGraphicsResources(self, win: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkVolumeTexture: ...
    def SetPartitions(self, x: int, y: int, z: int) -> None: ...
    def SortBlocksBackToFront(
        self, ren: vtkmodules.vtkRenderingCore.vtkRenderer, volumeMat: vtkmodules.vtkCommonMath.vtkMatrix4x4
    ) -> None: ...
    def UpdateVolume(self, property: vtkmodules.vtkRenderingCore.vtkVolumeProperty) -> None: ...
