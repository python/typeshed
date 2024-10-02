"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class TPUHardwareFeature(google.protobuf.message.Message):
    """Describes features of a tpu."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _EmbeddingFeature:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _EmbeddingFeatureEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TPUHardwareFeature._EmbeddingFeature.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNSUPPORTED: TPUHardwareFeature._EmbeddingFeature.ValueType  # 0
        """No embedding lookup accelerator available on the tpu."""
        V1: TPUHardwareFeature._EmbeddingFeature.ValueType  # 1
        """Embedding lookup accelerator V1. The embedding lookup operation can only
        be placed at the beginning of computation. Only one instance of embedding
        lookup layer is allowed.
        """
        V2: TPUHardwareFeature._EmbeddingFeature.ValueType  # 2
        """Embedding lookup accelerator V2. The embedding lookup operation can be
        placed anywhere of the computation. Multiple instances of embedding
        lookup layer is allowed.
        """

    class EmbeddingFeature(_EmbeddingFeature, metaclass=_EmbeddingFeatureEnumTypeWrapper):
        """Embedding feature of a tpu."""

    UNSUPPORTED: TPUHardwareFeature.EmbeddingFeature.ValueType  # 0
    """No embedding lookup accelerator available on the tpu."""
    V1: TPUHardwareFeature.EmbeddingFeature.ValueType  # 1
    """Embedding lookup accelerator V1. The embedding lookup operation can only
    be placed at the beginning of computation. Only one instance of embedding
    lookup layer is allowed.
    """
    V2: TPUHardwareFeature.EmbeddingFeature.ValueType  # 2
    """Embedding lookup accelerator V2. The embedding lookup operation can be
    placed anywhere of the computation. Multiple instances of embedding
    lookup layer is allowed.
    """

    EMBEDDING_FEATURE_FIELD_NUMBER: builtins.int
    NUM_EMBEDDING_DEVICES_PER_CHIP_FIELD_NUMBER: builtins.int
    embedding_feature: global___TPUHardwareFeature.EmbeddingFeature.ValueType
    num_embedding_devices_per_chip: builtins.int
    """Number of embedding accelerator devices per chip."""
    def __init__(
        self,
        *,
        embedding_feature: global___TPUHardwareFeature.EmbeddingFeature.ValueType | None = ...,
        num_embedding_devices_per_chip: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["embedding_feature", b"embedding_feature", "num_embedding_devices_per_chip", b"num_embedding_devices_per_chip"]) -> None: ...

global___TPUHardwareFeature = TPUHardwareFeature

@typing.final
class TopologyProto(google.protobuf.message.Message):
    """Describes the geometry of a TPU mesh."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESH_SHAPE_FIELD_NUMBER: builtins.int
    NUM_TASKS_FIELD_NUMBER: builtins.int
    NUM_TPU_DEVICES_PER_TASK_FIELD_NUMBER: builtins.int
    DEVICE_COORDINATES_FIELD_NUMBER: builtins.int
    TPU_HARDWARE_FEATURE_FIELD_NUMBER: builtins.int
    num_tasks: builtins.int
    """Number of TensorFlow tasks in the cluster."""
    num_tpu_devices_per_task: builtins.int
    """Number of TPU devices per task."""
    @property
    def mesh_shape(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """The dimensions of the TPU topology, in cores. Typically, this is a 4D
        topology [x, y, z, core], where the major dimensions correspond to TPU
        chips, and the minor dimension describes the number of cores on a multicore
        chip.
        """

    @property
    def device_coordinates(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """A flattened rank 3 int32 array with shape
        [num_tasks, num_tpu_devices_per_task, len(mesh_shape)].
        `tasks` is the number of tasks in the TPU cluster, `devices` is the number
        of TPU devices per task, and the minor dimension corresponds to a position
        in the TPU mesh topology. Each entry [task, device, axis] gives the
        `axis`-th coordinate in the topology of a task/device pair.
        """

    @property
    def tpu_hardware_feature(self) -> global___TPUHardwareFeature:
        """TPU supported features."""

    def __init__(
        self,
        *,
        mesh_shape: collections.abc.Iterable[builtins.int] | None = ...,
        num_tasks: builtins.int | None = ...,
        num_tpu_devices_per_task: builtins.int | None = ...,
        device_coordinates: collections.abc.Iterable[builtins.int] | None = ...,
        tpu_hardware_feature: global___TPUHardwareFeature | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["tpu_hardware_feature", b"tpu_hardware_feature"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["device_coordinates", b"device_coordinates", "mesh_shape", b"mesh_shape", "num_tasks", b"num_tasks", "num_tpu_devices_per_task", b"num_tpu_devices_per_task", "tpu_hardware_feature", b"tpu_hardware_feature"]) -> None: ...

global___TopologyProto = TopologyProto
