import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkCommonCore
from typing import Callable, MutableSequence, Sequence, TypeVar, Union, overload

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")


VTK_ASCII: int
VTK_BINARY: int


class vtkTextCodec(vtkmodules.vtkCommonCore.vtkObject):
    def CanHandle(self, NameString: str) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def Name(self) -> str: ...
    def NewInstance(self) -> vtkTextCodec: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTextCodec: ...


class vtkASCIITextCodec(vtkTextCodec):
    def CanHandle(self, NameString: str) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def Name(self) -> str: ...
    def NewInstance(self) -> vtkASCIITextCodec: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkASCIITextCodec: ...


class vtkWriter(vtkmodules.vtkCommonExecutionModel.vtkAlgorithm):
    def EncodeString(self, resname: str, name: str,
                     doublePercent: bool) -> None: ...

    @overload
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkDataObject: ...

    @overload
    def GetInput(
        self, port: int) -> vtkmodules.vtkCommonDataModel.vtkDataObject: ...

    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWriter: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWriter: ...

    @overload
    def SetInputData(
        self, input: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...

    @overload
    def SetInputData(
        self, index: int, input: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...

    def Write(self) -> int: ...


class vtkAbstractParticleWriter(vtkWriter):
    def CloseFile(self) -> None: ...
    def GetCollectiveIO(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTimeStep(self) -> int: ...
    def GetTimeValue(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkAbstractParticleWriter: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkAbstractParticleWriter: ...

    def SetCollectiveIO(self, _arg: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetTimeStep(self, _arg: int) -> None: ...
    def SetTimeValue(self, _arg: float) -> None: ...
    def SetWriteModeToCollective(self) -> None: ...
    def SetWriteModeToIndependent(self) -> None: ...


class vtkAbstractPolyDataReader(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkAbstractPolyDataReader: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkAbstractPolyDataReader: ...

    def SetFileName(self, _arg: str) -> None: ...


class vtkArrayDataReader(vtkmodules.vtkCommonExecutionModel.vtkArrayDataAlgorithm):
    def GetFileName(self) -> str: ...
    def GetInputString(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetReadFromInputString(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkArrayDataReader: ...
    @staticmethod
    def Read(str: str) -> vtkmodules.vtkCommonDataModel.vtkArrayData: ...
    def ReadFromInputStringOff(self) -> None: ...
    def ReadFromInputStringOn(self) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkArrayDataReader: ...

    def SetFileName(self, _arg: str) -> None: ...
    def SetInputString(self, string: str) -> None: ...
    def SetReadFromInputString(self, _arg: bool) -> None: ...


class vtkArrayDataWriter(vtkWriter):
    def BinaryOff(self) -> None: ...
    def BinaryOn(self) -> None: ...
    def GetBinary(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputString(self) -> str: ...
    def GetWriteToOutputString(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkArrayDataWriter: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkArrayDataWriter: ...

    def SetBinary(self, _arg: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetWriteToOutputString(self, _arg: bool) -> None: ...
    @overload
    def Write(self) -> int: ...
    @overload
    def Write(self, FileName: str, WriteBinary: bool = False) -> bool: ...

    @overload
    @staticmethod
    def Write(array: vtkmodules.vtkCommonDataModel.vtkArrayData,
              file_name: str, WriteBinary: bool = False) -> bool: ...

    @overload
    def Write(self, WriteBinary: bool) -> str: ...

    @overload
    @staticmethod
    def Write(array: vtkmodules.vtkCommonDataModel.vtkArrayData,
              WriteBinary: bool = False) -> str: ...

    def WriteToOutputStringOff(self) -> None: ...
    def WriteToOutputStringOn(self) -> None: ...


class vtkArrayReader(vtkmodules.vtkCommonExecutionModel.vtkArrayDataAlgorithm):
    def GetFileName(self) -> str: ...
    def GetInputString(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetReadFromInputString(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkArrayReader: ...
    @staticmethod
    def Read(str: str) -> vtkmodules.vtkCommonCore.vtkArray: ...
    def ReadFromInputStringOff(self) -> None: ...
    def ReadFromInputStringOn(self) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkArrayReader: ...

    def SetFileName(self, _arg: str) -> None: ...
    def SetInputString(self, string: str) -> None: ...
    def SetReadFromInputString(self, _arg: bool) -> None: ...


class vtkArrayWriter(vtkWriter):
    def BinaryOff(self) -> None: ...
    def BinaryOn(self) -> None: ...
    def GetBinary(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputString(self) -> str: ...
    def GetWriteToOutputString(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkArrayWriter: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkArrayWriter: ...

    def SetBinary(self, _arg: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetWriteToOutputString(self, _arg: bool) -> None: ...
    @overload
    def Write(self) -> int: ...
    @overload
    def Write(self, FileName: str, WriteBinary: bool = False) -> bool: ...

    @overload
    @staticmethod
    def Write(array: vtkmodules.vtkCommonCore.vtkArray,
              file_name: str, WriteBinary: bool = False) -> bool: ...

    @overload
    def Write(self, WriteBinary: bool) -> str: ...

    @overload
    @staticmethod
    def Write(array: vtkmodules.vtkCommonCore.vtkArray,
              WriteBinary: bool = False) -> str: ...

    def WriteToOutputStringOff(self) -> None: ...
    def WriteToOutputStringOn(self) -> None: ...


class vtkInputStream(vtkmodules.vtkCommonCore.vtkObject):
    def EndReading(self) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkInputStream: ...
    def Read(self, data: Pointer, length: int) -> int: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkInputStream: ...

    def Seek(self, offset: int) -> int: ...
    def StartReading(self) -> None: ...


class vtkBase64InputStream(vtkInputStream):
    def EndReading(self) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkBase64InputStream: ...
    def Read(self, data: Pointer, length: int) -> int: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkBase64InputStream: ...

    def Seek(self, offset: int) -> int: ...
    def StartReading(self) -> None: ...


class vtkOutputStream(vtkmodules.vtkCommonCore.vtkObject):
    def EndWriting(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOutputStream: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOutputStream: ...

    def StartWriting(self) -> int: ...
    def Write(self, data: Pointer, length: int) -> int: ...


class vtkBase64OutputStream(vtkOutputStream):
    def EndWriting(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkBase64OutputStream: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkBase64OutputStream: ...

    def StartWriting(self) -> int: ...
    def Write(self, data: Pointer, length: int) -> int: ...


class vtkBase64Utilities(vtkmodules.vtkCommonCore.vtkObject):
    @staticmethod
    def DecodeSafely(input: Sequence[int], inputLen: int,
                     output: MutableSequence[int], outputLen: int) -> int: ...

    @staticmethod
    def DecodeTriplet(
        i0: int, i1: int, i2: int, i3: int, o0: MutableSequence[int], o1: MutableSequence[int], o2: MutableSequence[int]
    ) -> int: ...

    @staticmethod
    def Encode(input: Sequence[int], length: int,
               output: MutableSequence[int], mark_end: int = 0) -> int: ...

    @staticmethod
    def EncodePair(
        i0: int, i1: int, o0: MutableSequence[int], o1: MutableSequence[int], o2: MutableSequence[int], o3: MutableSequence[int]
    ) -> None: ...

    @staticmethod
    def EncodeSingle(
        i0: int, o0: MutableSequence[int], o1: MutableSequence[int], o2: MutableSequence[int], o3: MutableSequence[int]
    ) -> None: ...

    @staticmethod
    def EncodeTriplet(
        i0: int,
        i1: int,
        i2: int,
        o0: MutableSequence[int],
        o1: MutableSequence[int],
        o2: MutableSequence[int],
        o3: MutableSequence[int],
    ) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkBase64Utilities: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkBase64Utilities: ...


class vtkDataCompressor(vtkmodules.vtkCommonCore.vtkObject):
    @overload
    def Compress(
        self, uncompressedData: Sequence[int], uncompressedSize: int, compressedData: MutableSequence[int], compressionSpace: int
    ) -> int: ...

    @overload
    def Compress(
        self, uncompressedData: Sequence[int], uncompressedSize: int
    ) -> vtkmodules.vtkCommonCore.vtkUnsignedCharArray: ...
    def GetCompressionLevel(self) -> int: ...
    def GetMaximumCompressionSpace(self, size: int) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkDataCompressor: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkDataCompressor: ...

    def SetCompressionLevel(self, compressionLevel: int) -> None: ...

    @overload
    def Uncompress(
        self, compressedData: Sequence[int], compressedSize: int, uncompressedData: MutableSequence[int], uncompressedSize: int
    ) -> int: ...

    @overload
    def Uncompress(
        self, compressedData: Sequence[int], compressedSize: int, uncompressedSize: int
    ) -> vtkmodules.vtkCommonCore.vtkUnsignedCharArray: ...


class vtkDelimitedTextWriter(vtkWriter):
    def GetFieldDelimiter(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetString(self, string: str) -> str: ...
    def GetStringDelimiter(self) -> str: ...
    def GetUseStringDelimiter(self) -> bool: ...
    def GetWriteToOutputString(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkDelimitedTextWriter: ...
    def RegisterAndGetOutputString(self) -> str: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkDelimitedTextWriter: ...

    def SetFieldDelimiter(self, _arg: str) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetStringDelimiter(self, _arg: str) -> None: ...
    def SetUseStringDelimiter(self, _arg: bool) -> None: ...
    def SetWriteToOutputString(self, _arg: bool) -> None: ...
    def WriteToOutputStringOff(self) -> None: ...
    def WriteToOutputStringOn(self) -> None: ...


class vtkGlobFileNames(vtkmodules.vtkCommonCore.vtkObject):
    def AddFileNames(self, pattern: str) -> int: ...
    def GetDirectory(self) -> str: ...
    def GetFileNames(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetNthFileName(self, index: int) -> str: ...
    def GetNumberOfFileNames(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRecurse(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkGlobFileNames: ...
    def RecurseOff(self) -> None: ...
    def RecurseOn(self) -> None: ...
    def Reset(self) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkGlobFileNames: ...

    def SetDirectory(self, _arg: str) -> None: ...
    def SetRecurse(self, _arg: int) -> None: ...


class vtkJavaScriptDataWriter(vtkWriter):
    def GetFileName(self) -> str: ...
    def GetIncludeFieldNames(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetVariableName(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkJavaScriptDataWriter: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkJavaScriptDataWriter: ...

    def SetFileName(self, _arg: str) -> None: ...
    def SetIncludeFieldNames(self, _arg: bool) -> None: ...
    def SetVariableName(self, _arg: str) -> None: ...


class vtkLZ4DataCompressor(vtkDataCompressor):
    def GetAccelerationLevel(self) -> int: ...
    def GetAccelerationLevelMaxValue(self) -> int: ...
    def GetAccelerationLevelMinValue(self) -> int: ...
    def GetCompressionLevel(self) -> int: ...
    def GetMaximumCompressionSpace(self, size: int) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLZ4DataCompressor: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLZ4DataCompressor: ...

    def SetAccelerationLevel(self, _arg: int) -> None: ...
    def SetCompressionLevel(self, compressionLevel: int) -> None: ...


class vtkLZMADataCompressor(vtkDataCompressor):
    def GetCompressionLevel(self) -> int: ...
    def GetMaximumCompressionSpace(self, size: int) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLZMADataCompressor: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLZMADataCompressor: ...

    def SetCompressionLevel(self, compressionLevel: int) -> None: ...


class vtkNumberToString:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __a: vtkNumberToString) -> None: ...


class vtkSortFileNames(vtkmodules.vtkCommonCore.vtkObject):
    def GetFileNames(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetGrouping(self) -> int: ...
    def GetIgnoreCase(self) -> int: ...
    def GetInputFileNames(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetNthGroup(
        self, i: int) -> vtkmodules.vtkCommonCore.vtkStringArray: ...

    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfGroups(self) -> int: ...
    def GetNumericSort(self) -> int: ...
    def GetSkipDirectories(self) -> int: ...
    def GroupingOff(self) -> None: ...
    def GroupingOn(self) -> None: ...
    def IgnoreCaseOff(self) -> None: ...
    def IgnoreCaseOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSortFileNames: ...
    def NumericSortOff(self) -> None: ...
    def NumericSortOn(self) -> None: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSortFileNames: ...

    def SetGrouping(self, _arg: int) -> None: ...
    def SetIgnoreCase(self, _arg: int) -> None: ...
    def SetInputFileNames(
        self, input: vtkmodules.vtkCommonCore.vtkStringArray) -> None: ...

    def SetNumericSort(self, _arg: int) -> None: ...
    def SetSkipDirectories(self, _arg: int) -> None: ...
    def SkipDirectoriesOff(self) -> None: ...
    def SkipDirectoriesOn(self) -> None: ...
    def Update(self) -> None: ...


class vtkTextCodecFactory(vtkmodules.vtkCommonCore.vtkObject):
    @staticmethod
    def CodecForName(CodecName: str) -> vtkTextCodec: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    @staticmethod
    def Initialize() -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTextCodecFactory: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTextCodecFactory: ...

    @staticmethod
    def UnRegisterAllCreateCallbacks() -> None: ...


class vtkUTF16TextCodec(vtkTextCodec):
    def CanHandle(self, NameString: str) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def Name(self) -> str: ...
    def NewInstance(self) -> vtkUTF16TextCodec: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkUTF16TextCodec: ...

    def SetBigEndian(self, __a: bool) -> None: ...


class vtkUTF8TextCodec(vtkTextCodec):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def Name(self) -> str: ...
    def NewInstance(self) -> vtkUTF8TextCodec: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkUTF8TextCodec: ...


class vtkZLibDataCompressor(vtkDataCompressor):
    def GetCompressionLevel(self) -> int: ...
    def GetMaximumCompressionSpace(self, size: int) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkZLibDataCompressor: ...

    @staticmethod
    def SafeDownCast(
        o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkZLibDataCompressor: ...

    def SetCompressionLevel(self, compressionLevel: int) -> None: ...
