from collections.abc import Callable
from typing import TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkIOCore

_Pointer = TypeVar("_Pointer")

class vtkXMLParser(vtkmodules.vtkCommonCore.vtkObject):
    def CleanupParser(self) -> int: ...
    def GetEncoding(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetIgnoreCharacterData(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def InitializeParser(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkXMLParser: ...
    @overload
    def Parse(self) -> int: ...
    @overload
    def Parse(self, inputString: str) -> int: ...
    @overload
    def Parse(self, inputString: str, length: int) -> int: ...
    def ParseChunk(self, inputString: str, length: int) -> int: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkXMLParser: ...
    def SeekG(self, position: int) -> None: ...
    def SetEncoding(self, _arg: str) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetIgnoreCharacterData(self, _arg: int) -> None: ...
    def TellG(self) -> int: ...

class vtkXMLDataParser(vtkXMLParser):
    BigEndian: int
    LittleEndian: int
    def CharacterDataHandler(self, data: str, length: int) -> None: ...
    def GetAbort(self) -> int: ...
    def GetAppendedDataPosition(self) -> int: ...
    def GetAttributesEncoding(self) -> int: ...
    def GetAttributesEncodingMaxValue(self) -> int: ...
    def GetAttributesEncodingMinValue(self) -> int: ...
    def GetCompressor(self) -> vtkmodules.vtkIOCore.vtkDataCompressor: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetProgress(self) -> float: ...
    def GetRootElement(self) -> vtkmodules.vtkCommonDataModel.vtkXMLDataElement: ...
    def GetWordTypeSize(self, wordType: int) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkXMLDataParser: ...
    def Parse(self) -> int: ...
    @overload
    def ReadAppendedData(self, offset: int, buffer: _Pointer, startWord: int, numWords: int, wordType: int) -> int: ...
    @overload
    def ReadAppendedData(self, offset: int, buffer: str, startWord: int, numWords: int) -> int: ...
    def ReadAsciiData(self, buffer: _Pointer, startWord: int, numWords: int, wordType: int) -> int: ...
    def ReadBinaryData(self, buffer: _Pointer, startWord: int, maxWords: int, wordType: int) -> int: ...
    @overload
    def ReadInlineData(
        self,
        element: vtkmodules.vtkCommonDataModel.vtkXMLDataElement,
        isAscii: int,
        buffer: _Pointer,
        startWord: int,
        numWords: int,
        wordType: int,
    ) -> int: ...
    @overload
    def ReadInlineData(
        self, element: vtkmodules.vtkCommonDataModel.vtkXMLDataElement, isAscii: int, buffer: str, startWord: int, numWords: int
    ) -> int: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkXMLDataParser: ...
    def SetAbort(self, _arg: int) -> None: ...
    def SetAttributesEncoding(self, _arg: int) -> None: ...
    def SetCompressor(self, __a: vtkmodules.vtkIOCore.vtkDataCompressor) -> None: ...
    def SetProgress(self, _arg: float) -> None: ...

class vtkXMLUtilities(vtkmodules.vtkCommonCore.vtkObject):
    @staticmethod
    def FactorElements(tree: vtkmodules.vtkCommonDataModel.vtkXMLDataElement) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkXMLUtilities: ...
    @staticmethod
    def ReadElementFromFile(filename: str, encoding: int = ...) -> vtkmodules.vtkCommonDataModel.vtkXMLDataElement: ...
    @staticmethod
    def ReadElementFromString(str: str, encoding: int = ...) -> vtkmodules.vtkCommonDataModel.vtkXMLDataElement: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkXMLUtilities: ...
    @staticmethod
    def UnFactorElements(tree: vtkmodules.vtkCommonDataModel.vtkXMLDataElement) -> None: ...
