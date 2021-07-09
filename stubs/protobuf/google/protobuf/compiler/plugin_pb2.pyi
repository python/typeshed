"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.descriptor_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Version(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MAJOR_FIELD_NUMBER: builtins.int
    MINOR_FIELD_NUMBER: builtins.int
    PATCH_FIELD_NUMBER: builtins.int
    SUFFIX_FIELD_NUMBER: builtins.int
    major: builtins.int = ...
    minor: builtins.int = ...
    patch: builtins.int = ...
    suffix: typing.Text = ...

    def __init__(self,
        *,
        major : typing.Optional[builtins.int] = ...,
        minor : typing.Optional[builtins.int] = ...,
        patch : typing.Optional[builtins.int] = ...,
        suffix : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"major",b"major",u"minor",b"minor",u"patch",b"patch",u"suffix",b"suffix"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"major",b"major",u"minor",b"minor",u"patch",b"patch",u"suffix",b"suffix"]) -> None: ...
global___Version = Version

class CodeGeneratorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FILE_TO_GENERATE_FIELD_NUMBER: builtins.int
    PARAMETER_FIELD_NUMBER: builtins.int
    PROTO_FILE_FIELD_NUMBER: builtins.int
    COMPILER_VERSION_FIELD_NUMBER: builtins.int

    @property
    def file_to_generate(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    parameter: typing.Text = ...

    @property
    def proto_file(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.descriptor_pb2.FileDescriptorProto]: ...

    @property
    def compiler_version(self) -> global___Version: ...

    def __init__(self,
        *,
        file_to_generate : typing.Optional[typing.Iterable[typing.Text]] = ...,
        parameter : typing.Optional[typing.Text] = ...,
        proto_file : typing.Optional[typing.Iterable[google.protobuf.descriptor_pb2.FileDescriptorProto]] = ...,
        compiler_version : typing.Optional[global___Version] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"compiler_version",b"compiler_version",u"parameter",b"parameter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"compiler_version",b"compiler_version",u"file_to_generate",b"file_to_generate",u"parameter",b"parameter",u"proto_file",b"proto_file"]) -> None: ...
global___CodeGeneratorRequest = CodeGeneratorRequest

class CodeGeneratorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Feature(metaclass=_Feature):
        V = typing.NewType('V', builtins.int)

    FEATURE_NONE = CodeGeneratorResponse.Feature.V(0)
    FEATURE_PROTO3_OPTIONAL = CodeGeneratorResponse.Feature.V(1)

    class _Feature(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Feature.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        FEATURE_NONE = CodeGeneratorResponse.Feature.V(0)
        FEATURE_PROTO3_OPTIONAL = CodeGeneratorResponse.Feature.V(1)

    class File(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        NAME_FIELD_NUMBER: builtins.int
        INSERTION_POINT_FIELD_NUMBER: builtins.int
        CONTENT_FIELD_NUMBER: builtins.int
        GENERATED_CODE_INFO_FIELD_NUMBER: builtins.int
        name: typing.Text = ...
        insertion_point: typing.Text = ...
        content: typing.Text = ...

        @property
        def generated_code_info(self) -> google.protobuf.descriptor_pb2.GeneratedCodeInfo: ...

        def __init__(self,
            *,
            name : typing.Optional[typing.Text] = ...,
            insertion_point : typing.Optional[typing.Text] = ...,
            content : typing.Optional[typing.Text] = ...,
            generated_code_info : typing.Optional[google.protobuf.descriptor_pb2.GeneratedCodeInfo] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"content",b"content",u"generated_code_info",b"generated_code_info",u"insertion_point",b"insertion_point",u"name",b"name"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"content",b"content",u"generated_code_info",b"generated_code_info",u"insertion_point",b"insertion_point",u"name",b"name"]) -> None: ...

    ERROR_FIELD_NUMBER: builtins.int
    SUPPORTED_FEATURES_FIELD_NUMBER: builtins.int
    FILE_FIELD_NUMBER: builtins.int
    error: typing.Text = ...
    supported_features: builtins.int = ...

    @property
    def file(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CodeGeneratorResponse.File]: ...

    def __init__(self,
        *,
        error : typing.Optional[typing.Text] = ...,
        supported_features : typing.Optional[builtins.int] = ...,
        file : typing.Optional[typing.Iterable[global___CodeGeneratorResponse.File]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"error",b"error",u"supported_features",b"supported_features"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"error",b"error",u"file",b"file",u"supported_features",b"supported_features"]) -> None: ...
global___CodeGeneratorResponse = CodeGeneratorResponse
