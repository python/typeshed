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
import tensorflow.core.protobuf.data_service_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class DispatcherConfig(google.protobuf.message.Message):
    """Configuration for a tf.data service DispatchServer.
    Next id: 13
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PORT_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    WORK_DIR_FIELD_NUMBER: builtins.int
    FAULT_TOLERANT_MODE_FIELD_NUMBER: builtins.int
    WORKER_ADDRESSES_FIELD_NUMBER: builtins.int
    DEPLOYMENT_MODE_FIELD_NUMBER: builtins.int
    JOB_GC_CHECK_INTERVAL_MS_FIELD_NUMBER: builtins.int
    JOB_GC_TIMEOUT_MS_FIELD_NUMBER: builtins.int
    GC_DYNAMIC_SHARDING_JOBS_FIELD_NUMBER: builtins.int
    CLIENT_TIMEOUT_MS_FIELD_NUMBER: builtins.int
    WORKER_TIMEOUT_MS_FIELD_NUMBER: builtins.int
    WORKER_MAX_CONCURRENT_SNAPSHOTS_FIELD_NUMBER: builtins.int
    port: builtins.int
    """The port for the dispatcher to bind to. A value of 0 indicates that the
    dispatcher may bind to any available port.
    """
    protocol: builtins.str
    """The protocol for the dispatcher to use when connecting to workers."""
    work_dir: builtins.str
    """A work directory to use for storing dispatcher state, and for recovering
    during restarts. The empty string indicates not to use any work directory.
    """
    fault_tolerant_mode: builtins.bool
    """Whether to run in fault tolerant mode, where dispatcher state is saved
    across restarts. Requires that `work_dir` is nonempty.
    """
    deployment_mode: tensorflow.core.protobuf.data_service_pb2.DeploymentMode.ValueType
    """(Optional.) tf.data service deployment mode. Supported values are "REMOTE",
    "COLOCATED", and "HYBRID". If unspecified, it is assumed to be "REMOTE".
    """
    job_gc_check_interval_ms: builtins.int
    """How often the dispatcher should scan through to delete old and unused
    jobs. A value of 0 indicates that the decision should be left up to the
    runtime.
    """
    job_gc_timeout_ms: builtins.int
    """How long a job needs to be unused before it becomes a candidate for garbage
    collection. A value of -1 indicates that jobs should never be garbage
    collected. A value of 0 indicates that the decision should be left up to
    the runtime. Note: This does not apply to dynamic sharding unless users
    explicitly opt-in by enabling `gc_dynamic_sharding_jobs` below.
    """
    gc_dynamic_sharding_jobs: builtins.bool
    """Whether dynamically sharded jobs should be eligible for garbage collection.
    These jobs are not garbage collected by default, since if a job is garbage
    collected and then re-created, it will revisit all data from the start. If
    revisiting data is acceptible and you want automatic reclamation of
    iterator memory, set `gc_dynamic_sharding_jobs` to `true`.
    """
    client_timeout_ms: builtins.int
    """How long to wait before garbage-collecting a client that hasn't
    heartbeated to the dispatcher. A value of 0 indicates that the timeout
    should be left to the runtime.
    """
    worker_timeout_ms: builtins.int
    """How long to wait for a worker to heartbeat before considering it missing.
    A value of 0 indicates that the timeout should be left to the runtime.
    """
    worker_max_concurrent_snapshots: builtins.int
    """The maximum number of snapshots that a worker can concurrently process at a
    given point in time. This is a tradeoff between worker resource usage and
    snapshot wall time. A value of 0 indicates that the decision should be left
    up to the runtime.
    """
    @property
    def worker_addresses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """(Optional.) If the job uses auto-sharding, it needs to specify a fixed list
        of worker addresses that will register with the dispatcher. The worker
        addresses should be in the format "host" or "host:port", where "port" is an
        integer, named port, or %port% to match any port.
        """

    def __init__(
        self,
        *,
        port: builtins.int | None = ...,
        protocol: builtins.str | None = ...,
        work_dir: builtins.str | None = ...,
        fault_tolerant_mode: builtins.bool | None = ...,
        worker_addresses: collections.abc.Iterable[builtins.str] | None = ...,
        deployment_mode: tensorflow.core.protobuf.data_service_pb2.DeploymentMode.ValueType | None = ...,
        job_gc_check_interval_ms: builtins.int | None = ...,
        job_gc_timeout_ms: builtins.int | None = ...,
        gc_dynamic_sharding_jobs: builtins.bool | None = ...,
        client_timeout_ms: builtins.int | None = ...,
        worker_timeout_ms: builtins.int | None = ...,
        worker_max_concurrent_snapshots: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["client_timeout_ms", b"client_timeout_ms", "deployment_mode", b"deployment_mode", "fault_tolerant_mode", b"fault_tolerant_mode", "gc_dynamic_sharding_jobs", b"gc_dynamic_sharding_jobs", "job_gc_check_interval_ms", b"job_gc_check_interval_ms", "job_gc_timeout_ms", b"job_gc_timeout_ms", "port", b"port", "protocol", b"protocol", "work_dir", b"work_dir", "worker_addresses", b"worker_addresses", "worker_max_concurrent_snapshots", b"worker_max_concurrent_snapshots", "worker_timeout_ms", b"worker_timeout_ms"]) -> None: ...

global___DispatcherConfig = DispatcherConfig

@typing.final
class WorkerConfig(google.protobuf.message.Message):
    """Configuration for a tf.data service WorkerServer.
    Next id: 13
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PORT_FIELD_NUMBER: builtins.int
    PROTOCOL_FIELD_NUMBER: builtins.int
    DISPATCHER_ADDRESS_FIELD_NUMBER: builtins.int
    WORKER_ADDRESS_FIELD_NUMBER: builtins.int
    WORKER_TAGS_FIELD_NUMBER: builtins.int
    HEARTBEAT_INTERVAL_MS_FIELD_NUMBER: builtins.int
    DISPATCHER_TIMEOUT_MS_FIELD_NUMBER: builtins.int
    DATA_TRANSFER_PROTOCOL_FIELD_NUMBER: builtins.int
    DATA_TRANSFER_ADDRESS_FIELD_NUMBER: builtins.int
    CROSS_TRAINER_CACHE_SIZE_BYTES_FIELD_NUMBER: builtins.int
    SNAPSHOT_MAX_CHUNK_SIZE_BYTES_FIELD_NUMBER: builtins.int
    SHUTDOWN_QUIET_PERIOD_MS_FIELD_NUMBER: builtins.int
    port: builtins.int
    """The port for the worker to bind to. A value of 0 indicates that the
    worker may bind to any available port.
    """
    protocol: builtins.str
    """The protocol for the worker to use when connecting to the dispatcher."""
    dispatcher_address: builtins.str
    """The address of the dispatcher to register with."""
    worker_address: builtins.str
    """The address of the worker server. The substring "%port%", if specified,
    will be replaced with the worker's bound port. This is useful when the port
    is set to `0`.
    """
    heartbeat_interval_ms: builtins.int
    """How often the worker should heartbeat to the master. A value of 0 indicates
    that the decision should be left up to the runtime.
    """
    dispatcher_timeout_ms: builtins.int
    """How long to retry requests to the dispatcher before giving up and reporting
    an error. A value of 0 indicates that the decision should be left up to the
    runtime.
    """
    data_transfer_protocol: builtins.str
    """The protocol for the worker to use when transferring data to clients."""
    data_transfer_address: builtins.str
    """The data transfer address of the worker server. The substring "%port%", if
    specified, will be replaced with the worker's bound port. This is useful
    when the port is set to `0`.
    """
    cross_trainer_cache_size_bytes: builtins.int
    """Maximum size of the cross-trainer cache in bytes. If enabled, make sure
    your training job provides sufficient memory resources.
    """
    snapshot_max_chunk_size_bytes: builtins.int
    """The maximum size of a distributed snapshot chunk file. A value of 0
    indicates that the decision should be left up to the runtime.
    """
    shutdown_quiet_period_ms: builtins.int
    """When shutting down a worker, how long to wait for the gRPC server to
    process the final requests. This is used to achieve clean shutdown in unit
    tests.
    """
    @property
    def worker_tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Tags attached to the worker. This allows reading from selected workers.
        For example, by applying a "COLOCATED" tag, tf.data service is able to read
        from the local tf.data worker if one exists, then from off-TF-host workers,
        to avoid cross-TF-host reads.
        """

    def __init__(
        self,
        *,
        port: builtins.int | None = ...,
        protocol: builtins.str | None = ...,
        dispatcher_address: builtins.str | None = ...,
        worker_address: builtins.str | None = ...,
        worker_tags: collections.abc.Iterable[builtins.str] | None = ...,
        heartbeat_interval_ms: builtins.int | None = ...,
        dispatcher_timeout_ms: builtins.int | None = ...,
        data_transfer_protocol: builtins.str | None = ...,
        data_transfer_address: builtins.str | None = ...,
        cross_trainer_cache_size_bytes: builtins.int | None = ...,
        snapshot_max_chunk_size_bytes: builtins.int | None = ...,
        shutdown_quiet_period_ms: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cross_trainer_cache_size_bytes", b"cross_trainer_cache_size_bytes", "data_transfer_address", b"data_transfer_address", "data_transfer_protocol", b"data_transfer_protocol", "dispatcher_address", b"dispatcher_address", "dispatcher_timeout_ms", b"dispatcher_timeout_ms", "heartbeat_interval_ms", b"heartbeat_interval_ms", "port", b"port", "protocol", b"protocol", "shutdown_quiet_period_ms", b"shutdown_quiet_period_ms", "snapshot_max_chunk_size_bytes", b"snapshot_max_chunk_size_bytes", "worker_address", b"worker_address", "worker_tags", b"worker_tags"]) -> None: ...

global___WorkerConfig = WorkerConfig
