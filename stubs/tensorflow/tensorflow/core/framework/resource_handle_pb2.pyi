"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import tensorflow.core.framework.tensor_shape_pb2
import tensorflow.core.framework.types_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ResourceHandleProto(google.protobuf.message.Message):
    """Protocol buffer representing a handle to a tensorflow resource. Handles are
    not valid across executions, but can be serialized back and forth from within
    a single run.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class DtypeAndShape(google.protobuf.message.Message):
        """Protocol buffer representing a pair of (data type, tensor shape)."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        DTYPE_FIELD_NUMBER: builtins.int
        SHAPE_FIELD_NUMBER: builtins.int
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
        """Data type of the tensor."""
        @property
        def shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto:
            """Shape of the tensor."""

        def __init__(
            self,
            *,
            dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
            shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["shape", b"shape"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["dtype", b"dtype", "shape", b"shape"]) -> None: ...

    DEVICE_FIELD_NUMBER: builtins.int
    CONTAINER_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    HASH_CODE_FIELD_NUMBER: builtins.int
    MAYBE_TYPE_NAME_FIELD_NUMBER: builtins.int
    DTYPES_AND_SHAPES_FIELD_NUMBER: builtins.int
    device: builtins.str
    """Unique name for the device containing the resource."""
    container: builtins.str
    """Container in which this resource is placed."""
    name: builtins.str
    """Unique name of this resource."""
    hash_code: builtins.int
    """Hash code for the type of the resource. Is only valid in the same device
    and in the same execution.
    """
    maybe_type_name: builtins.str
    """For debug-only, the name of the type pointed to by this handle, if
    available.
    """
    @property
    def dtypes_and_shapes(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ResourceHandleProto.DtypeAndShape]:
        """Data types and shapes for the underlying resource."""

    def __init__(
        self,
        *,
        device: builtins.str | None = ...,
        container: builtins.str | None = ...,
        name: builtins.str | None = ...,
        hash_code: builtins.int | None = ...,
        maybe_type_name: builtins.str | None = ...,
        dtypes_and_shapes: collections.abc.Iterable[global___ResourceHandleProto.DtypeAndShape] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "container",
            b"container",
            "device",
            b"device",
            "dtypes_and_shapes",
            b"dtypes_and_shapes",
            "hash_code",
            b"hash_code",
            "maybe_type_name",
            b"maybe_type_name",
            "name",
            b"name",
        ],
    ) -> None: ...

global___ResourceHandleProto = ResourceHandleProto
