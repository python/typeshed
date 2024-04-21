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
import tensorflow.core.framework.model_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _AutoShardPolicy:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _AutoShardPolicyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_AutoShardPolicy.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    AUTO: _AutoShardPolicy.ValueType  # 0
    """AUTO: Attempts FILE-based sharding, falling back to DATA-based sharding."""
    FILE: _AutoShardPolicy.ValueType  # 1
    """FILE: Shards by input files (i.e. each worker will get a set of files to
    process). When this option is selected, make sure that there is at least as
    many files as workers. If there are fewer input files than workers, a
    runtime error will be raised.
    """
    DATA: _AutoShardPolicy.ValueType  # 2
    """DATA: Shards by elements produced by the dataset. Each worker will process
    the whole dataset and discard the portion that is not for itself. Note that
    for this mode to correctly partitions the dataset elements, the dataset
    needs to produce elements in a deterministic order.
    """
    HINT: _AutoShardPolicy.ValueType  # 3
    """HINT: Looks for the presence of `shard(SHARD_HINT, ...)` which is treated
    as a placeholder to replace with `shard(num_workers, worker_index)`.
    """
    OFF: _AutoShardPolicy.ValueType  # -1
    """OFF: No sharding will be performed."""

class AutoShardPolicy(_AutoShardPolicy, metaclass=_AutoShardPolicyEnumTypeWrapper):
    """Represents the type of auto-sharding we enable."""

AUTO: AutoShardPolicy.ValueType  # 0
"""AUTO: Attempts FILE-based sharding, falling back to DATA-based sharding."""
FILE: AutoShardPolicy.ValueType  # 1
"""FILE: Shards by input files (i.e. each worker will get a set of files to
process). When this option is selected, make sure that there is at least as
many files as workers. If there are fewer input files than workers, a
runtime error will be raised.
"""
DATA: AutoShardPolicy.ValueType  # 2
"""DATA: Shards by elements produced by the dataset. Each worker will process
the whole dataset and discard the portion that is not for itself. Note that
for this mode to correctly partitions the dataset elements, the dataset
needs to produce elements in a deterministic order.
"""
HINT: AutoShardPolicy.ValueType  # 3
"""HINT: Looks for the presence of `shard(SHARD_HINT, ...)` which is treated
as a placeholder to replace with `shard(num_workers, worker_index)`.
"""
OFF: AutoShardPolicy.ValueType  # -1
"""OFF: No sharding will be performed."""
global___AutoShardPolicy = AutoShardPolicy

class _ExternalStatePolicy:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ExternalStatePolicyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ExternalStatePolicy.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    POLICY_WARN: _ExternalStatePolicy.ValueType  # 0
    POLICY_IGNORE: _ExternalStatePolicy.ValueType  # 1
    POLICY_FAIL: _ExternalStatePolicy.ValueType  # 2

class ExternalStatePolicy(_ExternalStatePolicy, metaclass=_ExternalStatePolicyEnumTypeWrapper):
    """Represents how to handle external state during serialization."""

POLICY_WARN: ExternalStatePolicy.ValueType  # 0
POLICY_IGNORE: ExternalStatePolicy.ValueType  # 1
POLICY_FAIL: ExternalStatePolicy.ValueType  # 2
global___ExternalStatePolicy = ExternalStatePolicy

@typing.final
class AutotuneOptions(google.protobuf.message.Message):
    """next: 5"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENABLED_FIELD_NUMBER: builtins.int
    CPU_BUDGET_FIELD_NUMBER: builtins.int
    RAM_BUDGET_FIELD_NUMBER: builtins.int
    AUTOTUNE_ALGORITHM_FIELD_NUMBER: builtins.int
    enabled: builtins.bool
    cpu_budget: builtins.int
    ram_budget: builtins.int
    autotune_algorithm: tensorflow.core.framework.model_pb2.AutotuneAlgorithm.ValueType
    def __init__(
        self,
        *,
        enabled: builtins.bool | None = ...,
        cpu_budget: builtins.int | None = ...,
        ram_budget: builtins.int | None = ...,
        autotune_algorithm: tensorflow.core.framework.model_pb2.AutotuneAlgorithm.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["autotune_algorithm", b"autotune_algorithm", "cpu_budget", b"cpu_budget", "enabled", b"enabled", "optional_autotune_algorithm", b"optional_autotune_algorithm", "optional_cpu_budget", b"optional_cpu_budget", "optional_enabled", b"optional_enabled", "optional_ram_budget", b"optional_ram_budget", "ram_budget", b"ram_budget"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["autotune_algorithm", b"autotune_algorithm", "cpu_budget", b"cpu_budget", "enabled", b"enabled", "optional_autotune_algorithm", b"optional_autotune_algorithm", "optional_cpu_budget", b"optional_cpu_budget", "optional_enabled", b"optional_enabled", "optional_ram_budget", b"optional_ram_budget", "ram_budget", b"ram_budget"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_autotune_algorithm", b"optional_autotune_algorithm"]) -> typing.Literal["autotune_algorithm"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_cpu_budget", b"optional_cpu_budget"]) -> typing.Literal["cpu_budget"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_enabled", b"optional_enabled"]) -> typing.Literal["enabled"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_ram_budget", b"optional_ram_budget"]) -> typing.Literal["ram_budget"] | None: ...

global___AutotuneOptions = AutotuneOptions

@typing.final
class CardinalityOptions(google.protobuf.message.Message):
    """next: 2"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ComputeLevel:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ComputeLevelEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CardinalityOptions._ComputeLevel.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        CARDINALITY_COMPUTE_UNSPECIFIED: CardinalityOptions._ComputeLevel.ValueType  # 0
        CARDINALITY_COMPUTE_LOW: CardinalityOptions._ComputeLevel.ValueType  # 1
        """Cardinality will only be computed if it can be determined in a cheap
        manner (ie. without reading from file sources). If the cardinality would
        be nontrivial to compute, Cardinality() will return UNKNOWN_CARDINALITY.
        """
        CARDINALITY_COMPUTE_MODERATE: CardinalityOptions._ComputeLevel.ValueType  # 2
        """Moderate effort will be made to determine cardinality, such as reading
        index data from source files. If significant work is needed to compute
        cardinality (e.g. reading entire source file contents or executing user
        defined functions), Cardinality() will return UNKNOWN_CARDINALITY.
        """

    class ComputeLevel(_ComputeLevel, metaclass=_ComputeLevelEnumTypeWrapper): ...
    CARDINALITY_COMPUTE_UNSPECIFIED: CardinalityOptions.ComputeLevel.ValueType  # 0
    CARDINALITY_COMPUTE_LOW: CardinalityOptions.ComputeLevel.ValueType  # 1
    """Cardinality will only be computed if it can be determined in a cheap
    manner (ie. without reading from file sources). If the cardinality would
    be nontrivial to compute, Cardinality() will return UNKNOWN_CARDINALITY.
    """
    CARDINALITY_COMPUTE_MODERATE: CardinalityOptions.ComputeLevel.ValueType  # 2
    """Moderate effort will be made to determine cardinality, such as reading
    index data from source files. If significant work is needed to compute
    cardinality (e.g. reading entire source file contents or executing user
    defined functions), Cardinality() will return UNKNOWN_CARDINALITY.
    """

    COMPUTE_LEVEL_FIELD_NUMBER: builtins.int
    compute_level: global___CardinalityOptions.ComputeLevel.ValueType
    def __init__(
        self,
        *,
        compute_level: global___CardinalityOptions.ComputeLevel.ValueType | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["compute_level", b"compute_level"]) -> None: ...

global___CardinalityOptions = CardinalityOptions

@typing.final
class DistributeOptions(google.protobuf.message.Message):
    """next: 3"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUTO_SHARD_POLICY_FIELD_NUMBER: builtins.int
    NUM_DEVICES_FIELD_NUMBER: builtins.int
    auto_shard_policy: global___AutoShardPolicy.ValueType
    num_devices: builtins.int
    def __init__(
        self,
        *,
        auto_shard_policy: global___AutoShardPolicy.ValueType | None = ...,
        num_devices: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["num_devices", b"num_devices", "optional_num_devices", b"optional_num_devices"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["auto_shard_policy", b"auto_shard_policy", "num_devices", b"num_devices", "optional_num_devices", b"optional_num_devices"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["optional_num_devices", b"optional_num_devices"]) -> typing.Literal["num_devices"] | None: ...

global___DistributeOptions = DistributeOptions

@typing.final
class OptimizationOptions(google.protobuf.message.Message):
    """next: 20"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    APPLY_DEFAULT_OPTIMIZATIONS_FIELD_NUMBER: builtins.int
    FILTER_FUSION_FIELD_NUMBER: builtins.int
    MAP_AND_BATCH_FUSION_FIELD_NUMBER: builtins.int
    MAP_AND_FILTER_FUSION_FIELD_NUMBER: builtins.int
    MAP_FUSION_FIELD_NUMBER: builtins.int
    MAP_PARALLELIZATION_FIELD_NUMBER: builtins.int
    NOOP_ELIMINATION_FIELD_NUMBER: builtins.int
    PARALLEL_BATCH_FIELD_NUMBER: builtins.int
    SHUFFLE_AND_REPEAT_FUSION_FIELD_NUMBER: builtins.int
    FILTER_PARALLELIZATION_FIELD_NUMBER: builtins.int
    INJECT_PREFETCH_FIELD_NUMBER: builtins.int
    apply_default_optimizations: builtins.bool
    filter_fusion: builtins.bool
    map_and_batch_fusion: builtins.bool
    map_and_filter_fusion: builtins.bool
    map_fusion: builtins.bool
    map_parallelization: builtins.bool
    noop_elimination: builtins.bool
    parallel_batch: builtins.bool
    shuffle_and_repeat_fusion: builtins.bool
    filter_parallelization: builtins.bool
    inject_prefetch: builtins.bool
    def __init__(
        self,
        *,
        apply_default_optimizations: builtins.bool | None = ...,
        filter_fusion: builtins.bool | None = ...,
        map_and_batch_fusion: builtins.bool | None = ...,
        map_and_filter_fusion: builtins.bool | None = ...,
        map_fusion: builtins.bool | None = ...,
        map_parallelization: builtins.bool | None = ...,
        noop_elimination: builtins.bool | None = ...,
        parallel_batch: builtins.bool | None = ...,
        shuffle_and_repeat_fusion: builtins.bool | None = ...,
        filter_parallelization: builtins.bool | None = ...,
        inject_prefetch: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["apply_default_optimizations", b"apply_default_optimizations", "filter_fusion", b"filter_fusion", "filter_parallelization", b"filter_parallelization", "inject_prefetch", b"inject_prefetch", "map_and_batch_fusion", b"map_and_batch_fusion", "map_and_filter_fusion", b"map_and_filter_fusion", "map_fusion", b"map_fusion", "map_parallelization", b"map_parallelization", "noop_elimination", b"noop_elimination", "optional_apply_default_optimizations", b"optional_apply_default_optimizations", "optional_filter_fusion", b"optional_filter_fusion", "optional_filter_parallelization", b"optional_filter_parallelization", "optional_inject_prefetch", b"optional_inject_prefetch", "optional_map_and_batch_fusion", b"optional_map_and_batch_fusion", "optional_map_and_filter_fusion", b"optional_map_and_filter_fusion", "optional_map_fusion", b"optional_map_fusion", "optional_map_parallelization", b"optional_map_parallelization", "optional_noop_elimination", b"optional_noop_elimination", "optional_parallel_batch", b"optional_parallel_batch", "optional_shuffle_and_repeat_fusion", b"optional_shuffle_and_repeat_fusion", "parallel_batch", b"parallel_batch", "shuffle_and_repeat_fusion", b"shuffle_and_repeat_fusion"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["apply_default_optimizations", b"apply_default_optimizations", "filter_fusion", b"filter_fusion", "filter_parallelization", b"filter_parallelization", "inject_prefetch", b"inject_prefetch", "map_and_batch_fusion", b"map_and_batch_fusion", "map_and_filter_fusion", b"map_and_filter_fusion", "map_fusion", b"map_fusion", "map_parallelization", b"map_parallelization", "noop_elimination", b"noop_elimination", "optional_apply_default_optimizations", b"optional_apply_default_optimizations", "optional_filter_fusion", b"optional_filter_fusion", "optional_filter_parallelization", b"optional_filter_parallelization", "optional_inject_prefetch", b"optional_inject_prefetch", "optional_map_and_batch_fusion", b"optional_map_and_batch_fusion", "optional_map_and_filter_fusion", b"optional_map_and_filter_fusion", "optional_map_fusion", b"optional_map_fusion", "optional_map_parallelization", b"optional_map_parallelization", "optional_noop_elimination", b"optional_noop_elimination", "optional_parallel_batch", b"optional_parallel_batch", "optional_shuffle_and_repeat_fusion", b"optional_shuffle_and_repeat_fusion", "parallel_batch", b"parallel_batch", "shuffle_and_repeat_fusion", b"shuffle_and_repeat_fusion"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_apply_default_optimizations", b"optional_apply_default_optimizations"]) -> typing.Literal["apply_default_optimizations"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_filter_fusion", b"optional_filter_fusion"]) -> typing.Literal["filter_fusion"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_filter_parallelization", b"optional_filter_parallelization"]) -> typing.Literal["filter_parallelization"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_inject_prefetch", b"optional_inject_prefetch"]) -> typing.Literal["inject_prefetch"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_map_and_batch_fusion", b"optional_map_and_batch_fusion"]) -> typing.Literal["map_and_batch_fusion"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_map_and_filter_fusion", b"optional_map_and_filter_fusion"]) -> typing.Literal["map_and_filter_fusion"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_map_fusion", b"optional_map_fusion"]) -> typing.Literal["map_fusion"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_map_parallelization", b"optional_map_parallelization"]) -> typing.Literal["map_parallelization"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_noop_elimination", b"optional_noop_elimination"]) -> typing.Literal["noop_elimination"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_parallel_batch", b"optional_parallel_batch"]) -> typing.Literal["parallel_batch"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_shuffle_and_repeat_fusion", b"optional_shuffle_and_repeat_fusion"]) -> typing.Literal["shuffle_and_repeat_fusion"] | None: ...

global___OptimizationOptions = OptimizationOptions

@typing.final
class ThreadingOptions(google.protobuf.message.Message):
    """next: 3"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MAX_INTRA_OP_PARALLELISM_FIELD_NUMBER: builtins.int
    PRIVATE_THREADPOOL_SIZE_FIELD_NUMBER: builtins.int
    max_intra_op_parallelism: builtins.int
    private_threadpool_size: builtins.int
    def __init__(
        self,
        *,
        max_intra_op_parallelism: builtins.int | None = ...,
        private_threadpool_size: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["max_intra_op_parallelism", b"max_intra_op_parallelism", "optional_max_intra_op_parallelism", b"optional_max_intra_op_parallelism", "optional_private_threadpool_size", b"optional_private_threadpool_size", "private_threadpool_size", b"private_threadpool_size"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["max_intra_op_parallelism", b"max_intra_op_parallelism", "optional_max_intra_op_parallelism", b"optional_max_intra_op_parallelism", "optional_private_threadpool_size", b"optional_private_threadpool_size", "private_threadpool_size", b"private_threadpool_size"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_max_intra_op_parallelism", b"optional_max_intra_op_parallelism"]) -> typing.Literal["max_intra_op_parallelism"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_private_threadpool_size", b"optional_private_threadpool_size"]) -> typing.Literal["private_threadpool_size"] | None: ...

global___ThreadingOptions = ThreadingOptions

@typing.final
class Options(google.protobuf.message.Message):
    """Message stored with Dataset objects to control how datasets are processed and
    optimized.

    next: 9
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DETERMINISTIC_FIELD_NUMBER: builtins.int
    AUTOTUNE_OPTIONS_FIELD_NUMBER: builtins.int
    DISTRIBUTE_OPTIONS_FIELD_NUMBER: builtins.int
    OPTIMIZATION_OPTIONS_FIELD_NUMBER: builtins.int
    SLACK_FIELD_NUMBER: builtins.int
    THREADING_OPTIONS_FIELD_NUMBER: builtins.int
    EXTERNAL_STATE_POLICY_FIELD_NUMBER: builtins.int
    SYMBOLIC_CHECKPOINT_FIELD_NUMBER: builtins.int
    deterministic: builtins.bool
    slack: builtins.bool
    external_state_policy: global___ExternalStatePolicy.ValueType
    symbolic_checkpoint: builtins.bool
    @property
    def autotune_options(self) -> global___AutotuneOptions:
        """The distribution strategy options associated with the dataset."""

    @property
    def distribute_options(self) -> global___DistributeOptions:
        """The distribution strategy options associated with the dataset."""

    @property
    def optimization_options(self) -> global___OptimizationOptions:
        """The optimization options associated with the dataset."""

    @property
    def threading_options(self) -> global___ThreadingOptions:
        """The threading options associated with the dataset."""

    def __init__(
        self,
        *,
        deterministic: builtins.bool | None = ...,
        autotune_options: global___AutotuneOptions | None = ...,
        distribute_options: global___DistributeOptions | None = ...,
        optimization_options: global___OptimizationOptions | None = ...,
        slack: builtins.bool | None = ...,
        threading_options: global___ThreadingOptions | None = ...,
        external_state_policy: global___ExternalStatePolicy.ValueType | None = ...,
        symbolic_checkpoint: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["autotune_options", b"autotune_options", "deterministic", b"deterministic", "distribute_options", b"distribute_options", "external_state_policy", b"external_state_policy", "optimization_options", b"optimization_options", "optional_deterministic", b"optional_deterministic", "optional_external_state_policy", b"optional_external_state_policy", "optional_slack", b"optional_slack", "optional_symbolic_checkpoint", b"optional_symbolic_checkpoint", "slack", b"slack", "symbolic_checkpoint", b"symbolic_checkpoint", "threading_options", b"threading_options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["autotune_options", b"autotune_options", "deterministic", b"deterministic", "distribute_options", b"distribute_options", "external_state_policy", b"external_state_policy", "optimization_options", b"optimization_options", "optional_deterministic", b"optional_deterministic", "optional_external_state_policy", b"optional_external_state_policy", "optional_slack", b"optional_slack", "optional_symbolic_checkpoint", b"optional_symbolic_checkpoint", "slack", b"slack", "symbolic_checkpoint", b"symbolic_checkpoint", "threading_options", b"threading_options"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_deterministic", b"optional_deterministic"]) -> typing.Literal["deterministic"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_external_state_policy", b"optional_external_state_policy"]) -> typing.Literal["external_state_policy"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_slack", b"optional_slack"]) -> typing.Literal["slack"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["optional_symbolic_checkpoint", b"optional_symbolic_checkpoint"]) -> typing.Literal["symbolic_checkpoint"] | None: ...

global___Options = Options
