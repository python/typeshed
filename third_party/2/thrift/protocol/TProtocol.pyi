from typing import Any

from thrift.Thrift import TException
from thrift.Thrift import *  # noqa: F403

class TProtocolException(TException):
    UNKNOWN = ...  # type: Any
    INVALID_DATA = ...  # type: Any
    NEGATIVE_SIZE = ...  # type: Any
    SIZE_LIMIT = ...  # type: Any
    BAD_VERSION = ...  # type: Any
    NOT_IMPLEMENTED = ...  # type: Any
    DEPTH_LIMIT = ...  # type: Any
    type = ...  # type: Any
    def __init__(self, type=..., message=...) -> None: ...

class TProtocolBase:
    trans = ...  # type: Any
    def __init__(self, trans) -> None: ...
    def writeMessageBegin(self, name, ttype, seqid): ...
    def writeMessageEnd(self): ...
    def writeStructBegin(self, name): ...
    def writeStructEnd(self): ...
    def writeFieldBegin(self, name, ttype, fid): ...
    def writeFieldEnd(self): ...
    def writeFieldStop(self): ...
    def writeMapBegin(self, ktype, vtype, size): ...
    def writeMapEnd(self): ...
    def writeListBegin(self, etype, size): ...
    def writeListEnd(self): ...
    def writeSetBegin(self, etype, size): ...
    def writeSetEnd(self): ...
    def writeBool(self, bool_val): ...
    def writeByte(self, byte): ...
    def writeI16(self, i16): ...
    def writeI32(self, i32): ...
    def writeI64(self, i64): ...
    def writeDouble(self, dub): ...
    def writeString(self, str_val): ...
    def readMessageBegin(self): ...
    def readMessageEnd(self): ...
    def readStructBegin(self): ...
    def readStructEnd(self): ...
    def readFieldBegin(self): ...
    def readFieldEnd(self): ...
    def readMapBegin(self): ...
    def readMapEnd(self): ...
    def readListBegin(self): ...
    def readListEnd(self): ...
    def readSetBegin(self): ...
    def readSetEnd(self): ...
    def readBool(self): ...
    def readByte(self): ...
    def readI16(self): ...
    def readI32(self): ...
    def readI64(self): ...
    def readDouble(self): ...
    def readString(self): ...
    def skip(self, ttype): ...
    def readFieldByTType(self, ttype, spec): ...
    def readContainerList(self, spec): ...
    def readContainerSet(self, spec): ...
    def readContainerStruct(self, spec): ...
    def readContainerMap(self, spec): ...
    def readStruct(self, obj, thrift_spec): ...
    def writeContainerStruct(self, val, spec): ...
    def writeContainerList(self, val, spec): ...
    def writeContainerSet(self, val, spec): ...
    def writeContainerMap(self, val, spec): ...
    def writeStruct(self, obj, thrift_spec): ...
    def writeFieldByTType(self, ttype, val, spec): ...

def checkIntegerLimits(i, bits): ...

class TProtocolFactory:
    def getProtocol(self, trans): ...
