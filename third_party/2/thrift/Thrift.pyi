from typing import Any

class TType:
    STOP = ...  # type: Any
    VOID = ...  # type: Any
    BOOL = ...  # type: Any
    BYTE = ...  # type: Any
    I08 = ...  # type: Any
    DOUBLE = ...  # type: Any
    I16 = ...  # type: Any
    I32 = ...  # type: Any
    I64 = ...  # type: Any
    STRING = ...  # type: Any
    UTF7 = ...  # type: Any
    STRUCT = ...  # type: Any
    MAP = ...  # type: Any
    SET = ...  # type: Any
    LIST = ...  # type: Any
    UTF8 = ...  # type: Any
    UTF16 = ...  # type: Any

class TMessageType:
    CALL = ...  # type: Any
    REPLY = ...  # type: Any
    EXCEPTION = ...  # type: Any
    ONEWAY = ...  # type: Any

class TProcessor:
    def process(iprot, oprot): ...

class TException(Exception):
    message = ...  # type: Any
    def __init__(self, message=...) -> None: ...

class TApplicationException(TException):
    UNKNOWN = ...  # type: Any
    UNKNOWN_METHOD = ...  # type: Any
    INVALID_MESSAGE_TYPE = ...  # type: Any
    WRONG_METHOD_NAME = ...  # type: Any
    BAD_SEQUENCE_ID = ...  # type: Any
    MISSING_RESULT = ...  # type: Any
    INTERNAL_ERROR = ...  # type: Any
    PROTOCOL_ERROR = ...  # type: Any
    INVALID_TRANSFORM = ...  # type: Any
    INVALID_PROTOCOL = ...  # type: Any
    UNSUPPORTED_CLIENT_TYPE = ...  # type: Any
    type = ...  # type: Any
    def __init__(self, type=..., message=...) -> None: ...
    message = ...  # type: Any
    def read(self, iprot): ...
    def write(self, oprot): ...
