"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class RPCOptions(google.protobuf.message.Message):
    """RPC options for distributed runtime."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USE_RPC_FOR_INPROCESS_MASTER_FIELD_NUMBER: builtins.int
    COMPRESSION_ALGORITHM_FIELD_NUMBER: builtins.int
    COMPRESSION_LEVEL_FIELD_NUMBER: builtins.int
    CACHE_RPC_RESPONSE_FIELD_NUMBER: builtins.int
    DISABLE_SESSION_CONNECTION_SHARING_FIELD_NUMBER: builtins.int
    NUM_CHANNELS_PER_TARGET_FIELD_NUMBER: builtins.int
    use_rpc_for_inprocess_master: builtins.bool
    """If true, always use RPC to contact the session target.
    
    If false (the default option), TensorFlow may use an optimized
    transport for client-master communication that avoids the RPC
    stack. This option is primarily for used testing the RPC stack.
    """
    compression_algorithm: builtins.str
    """The compression algorithm to be used. One of "deflate", "gzip"."""
    compression_level: builtins.int
    """If compression_algorithm is set, the compression level to be used.
    From 0 (no compression), up to 3.
    """
    cache_rpc_response: builtins.bool
    """Setting cache_rpc_response to true will enable sender side caching of
    response for RecvTensorAsync and RecvBufAsync to allow receiver to retry
    requests . This is only necessary when the network fabric is experiencing a
    significant error rate.  Without it we'll fail a step on an network error,
    while with it we'll be able to complete long steps (like complex
    initializations) in the face of some network errors during RecvTensor.
    """
    disable_session_connection_sharing: builtins.bool
    """Disables TCP connection sharing when opening a new RPC channel."""
    num_channels_per_target: builtins.int
    """Setting num_channels_per_target > 0 allows uses of multiple channels to
    communicate to the same target. This can be used to improve the aggregate
    throughput on high speed links (e.g 100G) where single connection is not
    sufficient to maximize link utilization. Note that a single RPC only goes
    on a single channel, this only helps in situations where there are multiple
    transfers to the same target overlapping in time.
    """
    def __init__(
        self,
        *,
        use_rpc_for_inprocess_master: builtins.bool | None = ...,
        compression_algorithm: builtins.str | None = ...,
        compression_level: builtins.int | None = ...,
        cache_rpc_response: builtins.bool | None = ...,
        disable_session_connection_sharing: builtins.bool | None = ...,
        num_channels_per_target: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cache_rpc_response", b"cache_rpc_response", "compression_algorithm", b"compression_algorithm", "compression_level", b"compression_level", "disable_session_connection_sharing", b"disable_session_connection_sharing", "num_channels_per_target", b"num_channels_per_target", "use_rpc_for_inprocess_master", b"use_rpc_for_inprocess_master"]) -> None: ...

global___RPCOptions = RPCOptions
