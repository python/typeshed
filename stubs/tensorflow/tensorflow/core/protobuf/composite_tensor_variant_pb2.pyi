"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import tensorflow.core.protobuf.struct_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CompositeTensorVariantMetadata(google.protobuf.message.Message):
    """Metadata for CompositeTensorVariant, used when serializing as Variant.

    We define a new message here (rather than directly using TypeSpecProto for
    the metadata string) to retain flexibility to change the metadata encoding
    to support additional features.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_SPEC_PROTO_FIELD_NUMBER: builtins.int
    @property
    def type_spec_proto(self) -> tensorflow.core.protobuf.struct_pb2.TypeSpecProto: ...
    def __init__(
        self,
        *,
        type_spec_proto: tensorflow.core.protobuf.struct_pb2.TypeSpecProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["type_spec_proto", b"type_spec_proto"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["type_spec_proto", b"type_spec_proto"]) -> None: ...

global___CompositeTensorVariantMetadata = CompositeTensorVariantMetadata
