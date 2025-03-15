"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import sys
import typing

import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class PassMetrics(google.protobuf.message.Message):
    """Defines pass specific metrics."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODULE_ID_FIELD_NUMBER: builtins.int
    PASS_NAME_FIELD_NUMBER: builtins.int
    PASS_DURATION_FIELD_NUMBER: builtins.int
    CUSTOM_METRICS_FIELD_NUMBER: builtins.int
    module_id: builtins.int
    """Unique ID of the module on which the pass was run."""
    pass_name: builtins.str
    """The name of the pass."""
    @property
    def pass_duration(self) -> google.protobuf.duration_pb2.Duration:
        """Duration of the pass."""

    @property
    def custom_metrics(self) -> google.protobuf.any_pb2.Any:
        """Custom pass metrics. This is kept opaque, via `google.protobuf.Any`, in
        order to decouple pass agnostic compilation logs from possibly proprietary
        compiler passes.
        """

    def __init__(
        self,
        *,
        module_id: builtins.int | None = ...,
        pass_name: builtins.str | None = ...,
        pass_duration: google.protobuf.duration_pb2.Duration | None = ...,
        custom_metrics: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["custom_metrics", b"custom_metrics", "pass_duration", b"pass_duration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["custom_metrics", b"custom_metrics", "module_id", b"module_id", "pass_duration", b"pass_duration", "pass_name", b"pass_name"]) -> None: ...

global___PassMetrics = PassMetrics

@typing.final
class JobInfo(google.protobuf.message.Message):
    """Defines compilation job information."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    CELL_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    TASK_ID_FIELD_NUMBER: builtins.int
    TASK_UID_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the job running compilation."""
    cell: builtins.str
    """Cell in which the job is running."""
    user: builtins.str
    """User running the job."""
    uid: builtins.int
    """Unique id when combined with user and cell field."""
    task_id: builtins.int
    """Task index, which will not change across job restarts."""
    task_uid: builtins.int
    """Task unique id, which may change across job restarts."""
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        cell: builtins.str | None = ...,
        user: builtins.str | None = ...,
        uid: builtins.int | None = ...,
        task_id: builtins.int | None = ...,
        task_uid: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_cell", b"_cell", "_name", b"_name", "_task_id", b"_task_id", "_task_uid", b"_task_uid", "_uid", b"_uid", "_user", b"_user", "cell", b"cell", "name", b"name", "task_id", b"task_id", "task_uid", b"task_uid", "uid", b"uid", "user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_cell", b"_cell", "_name", b"_name", "_task_id", b"_task_id", "_task_uid", b"_task_uid", "_uid", b"_uid", "_user", b"_user", "cell", b"cell", "name", b"name", "task_id", b"task_id", "task_uid", b"task_uid", "uid", b"uid", "user", b"user"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_cell", b"_cell"]) -> typing.Literal["cell"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_name", b"_name"]) -> typing.Literal["name"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_task_id", b"_task_id"]) -> typing.Literal["task_id"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_task_uid", b"_task_uid"]) -> typing.Literal["task_uid"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_uid", b"_uid"]) -> typing.Literal["uid"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_user", b"_user"]) -> typing.Literal["user"] | None: ...

global___JobInfo = JobInfo

@typing.final
class CompilationLogEntry(google.protobuf.message.Message):
    """Defines XLA compilation metrics."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _CompilationStage:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CompilationStageEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CompilationLogEntry._CompilationStage.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNSPECIFIED: CompilationLogEntry._CompilationStage.ValueType  # 0
        END_TO_END: CompilationLogEntry._CompilationStage.ValueType  # 1
        HLO_PASSES: CompilationLogEntry._CompilationStage.ValueType  # 2
        CODE_GENERATION: CompilationLogEntry._CompilationStage.ValueType  # 3
        BACKEND_PASSES: CompilationLogEntry._CompilationStage.ValueType  # 4

    class CompilationStage(_CompilationStage, metaclass=_CompilationStageEnumTypeWrapper):
        """Defines compilation stages for which metrics are collected."""

    UNSPECIFIED: CompilationLogEntry.CompilationStage.ValueType  # 0
    END_TO_END: CompilationLogEntry.CompilationStage.ValueType  # 1
    HLO_PASSES: CompilationLogEntry.CompilationStage.ValueType  # 2
    CODE_GENERATION: CompilationLogEntry.CompilationStage.ValueType  # 3
    BACKEND_PASSES: CompilationLogEntry.CompilationStage.ValueType  # 4

    TIMESTAMP_FIELD_NUMBER: builtins.int
    STAGE_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    TASK_INDEX_FIELD_NUMBER: builtins.int
    PASS_METRICS_FIELD_NUMBER: builtins.int
    MODULE_IDS_FIELD_NUMBER: builtins.int
    JOB_INFO_FIELD_NUMBER: builtins.int
    stage: global___CompilationLogEntry.CompilationStage.ValueType
    """Compilation stage recorded by this log entry."""
    task_index: builtins.int
    """Task index from which this log entry was recorded or
    -1 if the task index could not be fetched. In the case task_index is not
    equal to -1, it is guaranteed to match the task_id in job_info.
    """
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the event captured by this log entry occurred."""

    @property
    def duration(self) -> google.protobuf.duration_pb2.Duration:
        """Duration of the given compilation stage."""

    @property
    def pass_metrics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PassMetrics]:
        """Pass specific metrics."""

    @property
    def module_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """IDs of modules on which the compilation stage was run."""

    @property
    def job_info(self) -> global___JobInfo:
        """Job information."""

    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        stage: global___CompilationLogEntry.CompilationStage.ValueType | None = ...,
        duration: google.protobuf.duration_pb2.Duration | None = ...,
        task_index: builtins.int | None = ...,
        pass_metrics: collections.abc.Iterable[global___PassMetrics] | None = ...,
        module_ids: collections.abc.Iterable[builtins.int] | None = ...,
        job_info: global___JobInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["duration", b"duration", "job_info", b"job_info", "timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["duration", b"duration", "job_info", b"job_info", "module_ids", b"module_ids", "pass_metrics", b"pass_metrics", "stage", b"stage", "task_index", b"task_index", "timestamp", b"timestamp"]) -> None: ...

global___CompilationLogEntry = CompilationLogEntry
