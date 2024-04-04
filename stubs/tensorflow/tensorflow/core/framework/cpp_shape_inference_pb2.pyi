"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import typing as typing_extensions

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import tensorflow.core.framework.full_type_pb2
import tensorflow.core.framework.tensor_shape_pb2
import tensorflow.core.framework.types_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CppShapeInferenceResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class HandleShapeAndType(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SHAPE_FIELD_NUMBER: builtins.int
        DTYPE_FIELD_NUMBER: builtins.int
        TYPE_FIELD_NUMBER: builtins.int
        @property
        def shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto: ...
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
        @property
        def type(self) -> tensorflow.core.framework.full_type_pb2.FullTypeDef: ...
        def __init__(
            self,
            *,
            shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
            dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
            type: tensorflow.core.framework.full_type_pb2.FullTypeDef | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["shape", b"shape", "type", b"type"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["dtype", b"dtype", "shape", b"shape", "type", b"type"]) -> None: ...

    @typing_extensions.final
    class HandleData(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        IS_SET_FIELD_NUMBER: builtins.int
        SHAPE_AND_TYPE_FIELD_NUMBER: builtins.int
        is_set: builtins.bool
        @property
        def shape_and_type(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CppShapeInferenceResult.HandleShapeAndType]:
            """Only valid if <is_set>."""
        def __init__(
            self,
            *,
            is_set: builtins.bool | None = ...,
            shape_and_type: collections.abc.Iterable[global___CppShapeInferenceResult.HandleShapeAndType] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["is_set", b"is_set", "shape_and_type", b"shape_and_type"]) -> None: ...

    SHAPE_FIELD_NUMBER: builtins.int
    HANDLE_DATA_FIELD_NUMBER: builtins.int
    @property
    def shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto: ...
    @property
    def handle_data(self) -> global___CppShapeInferenceResult.HandleData: ...
    def __init__(
        self,
        *,
        shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
        handle_data: global___CppShapeInferenceResult.HandleData | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["handle_data", b"handle_data", "shape", b"shape"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["handle_data", b"handle_data", "shape", b"shape"]) -> None: ...

global___CppShapeInferenceResult = CppShapeInferenceResult

@typing_extensions.final
class CppShapeInferenceInputsNeeded(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INPUT_TENSORS_NEEDED_FIELD_NUMBER: builtins.int
    INPUT_TENSORS_AS_SHAPES_NEEDED_FIELD_NUMBER: builtins.int
    @property
    def input_tensors_needed(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def input_tensors_as_shapes_needed(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        input_tensors_needed: collections.abc.Iterable[builtins.int] | None = ...,
        input_tensors_as_shapes_needed: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["input_tensors_as_shapes_needed", b"input_tensors_as_shapes_needed", "input_tensors_needed", b"input_tensors_needed"]) -> None: ...

global___CppShapeInferenceInputsNeeded = CppShapeInferenceInputsNeeded
