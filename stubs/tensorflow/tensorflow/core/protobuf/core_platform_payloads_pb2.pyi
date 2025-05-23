"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ErrorSourceProto(google.protobuf.message.Message):
    """If included as a payload, this message contains the error source information
    where the error was raised.
    URI: "type.googleapis.com/tensorflow.core.platform.ErrorSourceProto"
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ErrorSource:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ErrorSourceEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ErrorSourceProto._ErrorSource.ValueType], builtins.type
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: ErrorSourceProto._ErrorSource.ValueType  # 0
        TPU_COMPILE_OP: ErrorSourceProto._ErrorSource.ValueType  # 1
        TF_XLA_BRIDGE: ErrorSourceProto._ErrorSource.ValueType  # 2
        """Old bridge."""
        MLIR_BRIDGE_PHASE_1: ErrorSourceProto._ErrorSource.ValueType  # 3
        """TPUBridge."""
        MLIR_BRIDGE_PHASE_2: ErrorSourceProto._ErrorSource.ValueType  # 4
        """LegalizeToHlo."""
        EAGER_REMOTE_MGR: ErrorSourceProto._ErrorSource.ValueType  # 5
        """eager::RemoteMgr."""

    class ErrorSource(_ErrorSource, metaclass=_ErrorSourceEnumTypeWrapper): ...
    UNKNOWN: ErrorSourceProto.ErrorSource.ValueType  # 0
    TPU_COMPILE_OP: ErrorSourceProto.ErrorSource.ValueType  # 1
    TF_XLA_BRIDGE: ErrorSourceProto.ErrorSource.ValueType  # 2
    """Old bridge."""
    MLIR_BRIDGE_PHASE_1: ErrorSourceProto.ErrorSource.ValueType  # 3
    """TPUBridge."""
    MLIR_BRIDGE_PHASE_2: ErrorSourceProto.ErrorSource.ValueType  # 4
    """LegalizeToHlo."""
    EAGER_REMOTE_MGR: ErrorSourceProto.ErrorSource.ValueType  # 5
    """eager::RemoteMgr."""

    ERROR_SOURCE_FIELD_NUMBER: builtins.int
    error_source: global___ErrorSourceProto.ErrorSource.ValueType
    def __init__(self, *, error_source: global___ErrorSourceProto.ErrorSource.ValueType | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["error_source", b"error_source"]) -> None: ...

global___ErrorSourceProto = ErrorSourceProto
