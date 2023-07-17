from collections.abc import Callable
from typing import TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkRenderingCore

Buffer = TypeVar("Buffer")
Template = TypeVar("Template")

class vtkDataEncoder(vtkmodules.vtkCommonCore.vtkObject):
    def EncodeAsBase64Jpg(self, img: vtkmodules.vtkCommonDataModel.vtkImageData, quality: int = 50) -> str: ...
    def EncodeAsBase64Png(self, img: vtkmodules.vtkCommonDataModel.vtkImageData, compressionLevel: int = 5) -> str: ...
    def Finalize(self) -> None: ...
    def Flush(self, key: int) -> None: ...
    def GetLatestOutput(self, key: int, data: vtkmodules.vtkCommonCore.vtkUnsignedCharArray) -> bool: ...
    def GetMaxThreads(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def Initialize(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkDataEncoder: ...
    def Push(self, key: int, data: vtkmodules.vtkCommonDataModel.vtkImageData, quality: int, encoding: int = 1) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkDataEncoder: ...
    def SetMaxThreads(self, __a: int) -> None: ...

class vtkObjectIdMap(vtkmodules.vtkCommonCore.vtkObject):
    def FreeObject(self, obj: vtkmodules.vtkCommonCore.vtkObject) -> bool: ...
    def FreeObjectById(self, id: int) -> bool: ...
    def GetActiveObject(self, objectType: str) -> vtkmodules.vtkCommonCore.vtkObject: ...
    def GetGlobalId(self, obj: vtkmodules.vtkCommonCore.vtkObject) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetVTKObject(self, globalId: int) -> vtkmodules.vtkCommonCore.vtkObject: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkObjectIdMap: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkObjectIdMap: ...
    def SetActiveObject(self, objectType: str, obj: vtkmodules.vtkCommonCore.vtkObject) -> int: ...

class vtkWebApplication(vtkmodules.vtkCommonCore.vtkObject):
    COMPRESSION_JPEG: int
    COMPRESSION_NONE: int
    COMPRESSION_PNG: int
    ENCODING_BASE64: int
    ENCODING_NONE: int
    def GetHasImagesBeingProcessed(self, __a: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> bool: ...
    def GetImageCompression(self) -> int: ...
    def GetImageCompressionMaxValue(self) -> int: ...
    def GetImageCompressionMinValue(self) -> int: ...
    def GetImageEncoding(self) -> int: ...
    def GetImageEncodingMaxValue(self) -> int: ...
    def GetImageEncodingMinValue(self) -> int: ...
    def GetLastStillRenderToMTime(self) -> int: ...
    def GetNumberOfEncoderThreads(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    @staticmethod
    def GetObjectId(obj: vtkmodules.vtkCommonCore.vtkObject) -> str: ...
    def GetObjectIdMap(self) -> vtkObjectIdMap: ...
    def GetWebGLBinaryData(self, view: vtkmodules.vtkRenderingCore.vtkRenderWindow, id: str, partIndex: int) -> str: ...
    def GetWebGLSceneMetaData(self, view: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> str: ...
    def HandleInteractionEvent(
        self, view: vtkmodules.vtkRenderingCore.vtkRenderWindow, event: vtkWebInteractionEvent
    ) -> bool: ...
    def InteractiveRender(
        self, view: vtkmodules.vtkRenderingCore.vtkRenderWindow, quality: int = 50
    ) -> vtkmodules.vtkCommonCore.vtkUnsignedCharArray: ...
    def InvalidateCache(self, view: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWebApplication: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWebApplication: ...
    def SetImageCompression(self, _arg: int) -> None: ...
    def SetImageEncoding(self, _arg: int) -> None: ...
    def SetNumberOfEncoderThreads(self, __a: int) -> None: ...
    def StillRender(
        self, view: vtkmodules.vtkRenderingCore.vtkRenderWindow, quality: int = 100
    ) -> vtkmodules.vtkCommonCore.vtkUnsignedCharArray: ...
    def StillRenderToBuffer(
        self, view: vtkmodules.vtkRenderingCore.vtkRenderWindow, time: int = 0, quality: int = 100
    ) -> vtkmodules.vtkCommonCore.vtkUnsignedCharArray: ...
    def StillRenderToString(
        self, view: vtkmodules.vtkRenderingCore.vtkRenderWindow, time: int = 0, quality: int = 100
    ) -> str: ...

class vtkWebInteractionEvent(vtkmodules.vtkCommonCore.vtkObject):
    class ModifierKeys(int): ...
    class MouseButton(int): ...
    ALT_KEY: ModifierKeys
    CTRL_KEY: ModifierKeys
    LEFT_BUTTON: MouseButton
    META_KEY: ModifierKeys
    MIDDLE_BUTTON: MouseButton
    RIGHT_BUTTON: MouseButton
    SHIFT_KEY: ModifierKeys
    def GetButtons(self) -> int: ...
    def GetKeyCode(self) -> str: ...
    def GetModifiers(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRepeatCount(self) -> int: ...
    def GetScroll(self) -> float: ...
    def GetX(self) -> float: ...
    def GetY(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWebInteractionEvent: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWebInteractionEvent: ...
    def SetButtons(self, _arg: int) -> None: ...
    def SetKeyCode(self, _arg: str) -> None: ...
    def SetModifiers(self, _arg: int) -> None: ...
    def SetRepeatCount(self, _arg: int) -> None: ...
    def SetScroll(self, _arg: float) -> None: ...
    def SetX(self, _arg: float) -> None: ...
    def SetY(self, _arg: float) -> None: ...

class vtkWebUtilities(vtkmodules.vtkCommonCore.vtkObject):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWebUtilities: ...
    @overload
    @staticmethod
    def ProcessRMIs() -> None: ...
    @overload
    @staticmethod
    def ProcessRMIs(reportError: int, dont_loop: int = 0) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWebUtilities: ...
    @staticmethod
    def WriteAttributeHeadersToJavaScript(field_type: int, __b: vtkmodules.vtkCommonDataModel.vtkDataSet) -> str: ...
    @staticmethod
    def WriteAttributesToJavaScript(field_type: int, __b: vtkmodules.vtkCommonDataModel.vtkDataSet) -> str: ...
