"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import tensorflow.core.framework.tensor_pb2
import tensorflow.core.framework.tensor_shape_pb2
import tensorflow.core.framework.types_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CompressedComponentMetadata(google.protobuf.message.Message):
    """This file contains protocol buffers for working with tf.data Datasets.

    Metadata describing a compressed component of a dataset element.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DTYPE_FIELD_NUMBER: builtins.int
    TENSOR_SHAPE_FIELD_NUMBER: builtins.int
    UNCOMPRESSED_BYTES_FIELD_NUMBER: builtins.int
    dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
    """The dtype of the component tensor."""
    @property
    def tensor_shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto:
        """The shape of the component tensor."""
    @property
    def uncompressed_bytes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """The amount of uncompressed tensor data.
        - For string tensors, there is an element for each string indicating the
        size of the string.
        - For all other tensors, there is a single element indicating the size of
        the tensor.
        """
    def __init__(
        self,
        *,
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
        tensor_shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
        uncompressed_bytes: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tensor_shape", b"tensor_shape"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dtype", b"dtype", "tensor_shape", b"tensor_shape", "uncompressed_bytes", b"uncompressed_bytes"]) -> None: ...

global___CompressedComponentMetadata = CompressedComponentMetadata

@typing_extensions.final
class CompressedElement(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    COMPONENT_METADATA_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    """Compressed tensor bytes for all components of the element."""
    @property
    def component_metadata(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CompressedComponentMetadata]:
        """Metadata for the components of the element."""
    version: builtins.int
    """Version of the CompressedElement. CompressedElements may be stored on disk
    and read back by later versions of code, so we store a version number to
    help readers understand which version they are reading. When you add a new
    field to this proto, you need to increment kCompressedElementVersion in
    tensorflow/core/data/compression_utils.cc.
    """
    def __init__(
        self,
        *,
        data: builtins.bytes | None = ...,
        component_metadata: collections.abc.Iterable[global___CompressedComponentMetadata] | None = ...,
        version: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["component_metadata", b"component_metadata", "data", b"data", "version", b"version"]) -> None: ...

global___CompressedElement = CompressedElement

@typing_extensions.final
class UncompressedElement(google.protobuf.message.Message):
    """An uncompressed dataset element."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMPONENTS_FIELD_NUMBER: builtins.int
    @property
    def components(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.core.framework.tensor_pb2.TensorProto]: ...
    def __init__(
        self,
        *,
        components: collections.abc.Iterable[tensorflow.core.framework.tensor_pb2.TensorProto] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["components", b"components"]) -> None: ...

global___UncompressedElement = UncompressedElement
