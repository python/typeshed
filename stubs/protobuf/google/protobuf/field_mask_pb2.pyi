"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.well_known_types
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class FieldMask(google.protobuf.message.Message, google.protobuf.internal.well_known_types.FieldMask):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PATHS_FIELD_NUMBER: builtins.int

    @property
    def paths(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...

    def __init__(self,
        *,
        paths : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"paths",b"paths"]) -> None: ...
global___FieldMask = FieldMask
