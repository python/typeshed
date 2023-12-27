import asyncio
import typing
from _typeshed import Incomplete
from collections.abc import AsyncIterable, AsyncIterator, Awaitable, Callable, Generator, Iterable, Iterator, Mapping, Sequence
from concurrent import futures
from types import TracebackType
from typing_extensions import Self, TypeAlias

from grpc import (
    CallCredentials,
    ChannelConnectivity,
    ChannelCredentials,
    Compression,
    GenericRpcHandler,
    HandlerCallDetails,
    RpcError,
    RpcMethodHandler,
    ServerCredentials,
    StatusCode,
    _Options,
    _PartialStubMustCastOrIgnore,
)

_TRequest = typing.TypeVar("_TRequest")
_TResponse = typing.TypeVar("_TResponse")

# Exceptions:

class BaseError(Exception): ...
class UsageError(BaseError): ...
class AbortError(BaseError): ...
class InternalError(BaseError): ...

class AioRpcError(RpcError):
    def __init__(
        self,
        code: StatusCode,
        initial_metadata: Metadata,
        trailing_metadata: Metadata,
        details: str | None,
        debug_error_string: str | None,
    ) -> None: ...

    # FIXME: confirm if these are present in the parent type. The remaining
    # methods already exist.
    def debug_error_string(self) -> str: ...
    def initial_metadata(self) -> Metadata: ...

# Create Client:

ClientInterceptor: TypeAlias = _PartialStubMustCastOrIgnore

def insecure_channel(
    target: str,
    options: _Options | None = ...,
    compression: Compression | None = ...,
    interceptors: Sequence[ClientInterceptor] | None = ...,
) -> Channel: ...
def secure_channel(
    target: str,
    credentials: ChannelCredentials,
    options: _Options | None = ...,
    compression: Compression | None = ...,
    interceptors: Sequence[ClientInterceptor] | None = ...,
) -> Channel: ...

# Create Server:

def server(
    migration_thread_pool: futures.Executor | None = ...,
    handlers: Sequence[GenericRpcHandler[typing.Any, typing.Any]] | None = ...,
    interceptors: Sequence[ServerInterceptor[typing.Any, typing.Any]] | None = ...,
    options: _Options | None = ...,
    maximum_concurrent_rpcs: int | None = ...,
    compression: Compression | None = ...,
) -> Server: ...

# Channel Object:

# XXX: The docs suggest these type signatures for aio, but not for non-async,
# and it's unclear why;
# https://grpc.github.io/grpc/python/grpc_asyncio.html#grpc.aio.Channel.stream_stream
RequestSerializer: TypeAlias = Callable[[typing.Any], bytes]
ResponseDeserializer: TypeAlias = Callable[[bytes], typing.Any]

class Channel:
    async def close(self, grace: float | None) -> None: ...
    def get_state(self, try_to_connect: bool = ...) -> ChannelConnectivity: ...
    async def wait_for_state_change(self, last_observed_state: ChannelConnectivity) -> None: ...
    def stream_stream(
        self, method: str, request_serializer: RequestSerializer | None, response_deserializer: ResponseDeserializer | None
    ) -> StreamStreamMultiCallable[typing.Any, typing.Any]: ...
    def stream_unary(
        self, method: str, request_serializer: RequestSerializer | None, response_deserializer: ResponseDeserializer | None
    ) -> StreamUnaryMultiCallable[typing.Any, typing.Any]: ...
    def unary_stream(
        self, method: str, request_serializer: RequestSerializer | None, response_deserializer: ResponseDeserializer | None
    ) -> UnaryStreamMultiCallable[typing.Any, typing.Any]: ...
    def unary_unary(
        self, method: str, request_serializer: RequestSerializer | None, response_deserializer: ResponseDeserializer | None
    ) -> UnaryUnaryMultiCallable[typing.Any, typing.Any]: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool | None: ...
    async def channel_ready(self) -> None: ...

# Server Object:

class Server:
    def add_generic_rpc_handlers(self, generic_rpc_handlers: Iterable[GenericRpcHandler[typing.Any, typing.Any]]) -> None: ...

    # Returns an integer port on which server will accept RPC requests.
    def add_insecure_port(self, address: str) -> int: ...

    # Returns an integer port on which server will accept RPC requests.
    def add_secure_port(self, address: str, server_credentials: ServerCredentials) -> int: ...
    async def start(self) -> None: ...

    # Grace period is in seconds.
    async def stop(self, grace: float | None = ...) -> None: ...

    # Returns a bool indicates if the operation times out. Timeout is in seconds.
    async def wait_for_termination(self, timeout: float | None = ...) -> bool: ...

# Client-Side Context:

DoneCallbackType: TypeAlias = Callable[[typing.Any], None]
EOFType: TypeAlias = object

class RpcContext:
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def time_remaining(self) -> float | None: ...
    def cancel(self) -> bool: ...
    def add_done_callback(self, callback: DoneCallbackType) -> None: ...

class Call(RpcContext):
    async def initial_metadata(self) -> Metadata: ...
    async def trailing_metadata(self) -> Metadata: ...
    async def code(self) -> StatusCode: ...
    async def details(self) -> str: ...
    async def wait_for_connection(self) -> None: ...

class UnaryUnaryCall(Call, typing.Generic[_TRequest, _TResponse]):
    def __await__(self) -> Generator[None, None, _TResponse]: ...

class UnaryStreamCall(Call, typing.Generic[_TRequest, _TResponse]):
    def __aiter__(self) -> AsyncIterator[_TResponse]: ...
    async def read(self) -> EOFType | _TResponse: ...

class StreamUnaryCall(Call, typing.Generic[_TRequest, _TResponse]):
    async def write(self, request: _TRequest) -> None: ...
    async def done_writing(self) -> None: ...
    def __await__(self) -> Generator[None, None, _TResponse]: ...

class StreamStreamCall(Call, typing.Generic[_TRequest, _TResponse]):
    def __aiter__(self) -> AsyncIterator[_TResponse]: ...
    async def read(self) -> EOFType | _TResponse: ...
    async def write(self, request: _TRequest) -> None: ...
    async def done_writing(self) -> None: ...

# Service-Side Context:

class DoneCallback(typing.Generic[_TRequest, _TResponse]):
    def __call__(self, ctx: ServicerContext[_TRequest, _TResponse]) -> None: ...

class ServicerContext(typing.Generic[_TRequest, _TResponse]):
    async def abort(self, code: StatusCode, details: str = ..., trailing_metadata: MetadataType = ...) -> typing.NoReturn: ...
    async def read(self) -> _TRequest: ...
    async def write(self, message: _TResponse) -> None: ...
    async def send_initial_metadata(self, initial_metadata: MetadataType) -> None: ...
    def add_done_callback(self, callback: DoneCallback[_TRequest, _TResponse]) -> None: ...
    def set_trailing_metadata(self, trailing_metadata: MetadataType) -> None: ...
    def invocation_metadata(self) -> Metadata | None: ...
    def set_code(self, code: StatusCode) -> None: ...
    def set_details(self, details: str) -> None: ...
    def set_compression(self, compression: Compression) -> None: ...
    def disable_next_message_compression(self) -> None: ...
    def peer(self) -> str: ...
    def peer_identities(self) -> Iterable[bytes] | None: ...
    def peer_identity_key(self) -> str | None: ...
    def auth_context(self) -> Mapping[str, Iterable[bytes]]: ...
    def time_remaining(self) -> float: ...
    def trailing_metadata(self) -> Metadata: ...
    def code(self) -> StatusCode: ...
    def details(self) -> str: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...

# Client-Side Interceptor:

class ClientCallDetails:
    def __init__(
        self,
        method: str,
        timeout: float | None,
        metadata: Metadata | None,
        credentials: CallCredentials | None,
        wait_for_ready: bool | None,
    ) -> None: ...

    method: str
    timeout: float | None
    metadata: Metadata | None
    credentials: CallCredentials | None

    # "This is an EXPERIMENTAL argument. An optional flag t enable wait for ready mechanism."
    wait_for_ready: bool | None

    # As at 1.53.0, this is not supported in aio:
    # compression: Compression | None

class InterceptedCall(typing.Generic[_TRequest, _TResponse]):
    def __init__(self, interceptors_task: asyncio.Task[typing.Any]) -> None: ...
    def __del__(self) -> None: ...
    def cancel(self) -> bool: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def add_done_callback(self, callback: DoneCallback[_TRequest, _TResponse]) -> None: ...
    def time_remaining(self) -> float | None: ...
    async def initial_metadata(self) -> Metadata | None: ...
    async def trailing_metadata(self) -> Metadata | None: ...
    async def code(self) -> StatusCode: ...
    async def details(self) -> str: ...
    async def debug_error_string(self) -> str | None: ...
    async def wait_for_connection(self) -> None: ...

class InterceptedUnaryUnaryCall(InterceptedCall[_TRequest, _TResponse]):
    def __await__(self) -> Incomplete: ...
    def __init__(
        self,
        interceptors: Sequence[UnaryUnaryClientInterceptor[_TRequest, _TResponse]],
        request: _TRequest,
        timeout: float | None,
        metadata: Metadata,
        credentials: CallCredentials | None,
        wait_for_ready: bool | None,
        channel: Channel,
        method: bytes,
        request_serializer: RequestSerializer,
        response_deserializer: ResponseDeserializer,
        loop: asyncio.AbstractEventLoop,
    ) -> None: ...

    # pylint: disable=too-many-arguments
    async def _invoke(
        self,
        interceptors: Sequence[UnaryUnaryClientInterceptor[_TRequest, _TResponse]],
        method: bytes,
        timeout: float | None,
        metadata: Metadata | None,
        credentials: CallCredentials | None,
        wait_for_ready: bool | None,
        request: _TRequest,
        request_serializer: RequestSerializer,
        response_deserializer: ResponseDeserializer,
    ) -> UnaryUnaryCall[_TRequest, _TResponse]: ...
    def time_remaining(self) -> float | None: ...

class UnaryUnaryClientInterceptor(typing.Generic[_TRequest, _TResponse]):
    async def intercept_unary_unary(
        self,
        # XXX: See equivalent function in grpc types for notes about continuation:
        continuation: Callable[[ClientCallDetails, _TRequest], UnaryUnaryCall[_TRequest, _TResponse]],
        client_call_details: ClientCallDetails,
        request: _TRequest,
    ) -> _TResponse: ...

class UnaryStreamClientInterceptor(typing.Generic[_TRequest, _TResponse]):
    async def intercept_unary_stream(
        self,
        continuation: Callable[[ClientCallDetails, _TRequest], UnaryStreamCall[_TRequest, _TResponse]],
        client_call_details: ClientCallDetails,
        request: _TRequest,
    ) -> AsyncIterable[_TResponse] | UnaryStreamCall[_TRequest, _TResponse]: ...

class StreamUnaryClientInterceptor(typing.Generic[_TRequest, _TResponse]):
    async def intercept_stream_unary(
        self,
        continuation: Callable[[ClientCallDetails, _TRequest], StreamUnaryCall[_TRequest, _TResponse]],
        client_call_details: ClientCallDetails,
        request_iterator: AsyncIterable[_TRequest] | Iterable[_TRequest],
    ) -> AsyncIterable[_TResponse] | UnaryStreamCall[_TRequest, _TResponse]: ...

class StreamStreamClientInterceptor(typing.Generic[_TRequest, _TResponse]):
    async def intercept_stream_stream(
        self,
        continuation: Callable[[ClientCallDetails, _TRequest], StreamStreamCall[_TRequest, _TResponse]],
        client_call_details: ClientCallDetails,
        request_iterator: AsyncIterable[_TRequest] | Iterable[_TRequest],
    ) -> AsyncIterable[_TResponse] | StreamStreamCall[_TRequest, _TResponse]: ...

# Server-Side Interceptor:

class ServerInterceptor(typing.Generic[_TRequest, _TResponse]):
    async def intercept_service(
        self,
        continuation: Callable[[HandlerCallDetails], Awaitable[RpcMethodHandler[_TRequest, _TResponse]]],
        handler_call_details: HandlerCallDetails,
    ) -> RpcMethodHandler[_TRequest, _TResponse]: ...

# Multi-Callable Interfaces:

class UnaryUnaryMultiCallable(typing.Generic[_TRequest, _TResponse]):
    def __call__(
        self,
        request: _TRequest,
        timeout: float | None = ...,
        metadata: MetadataType | None = ...,
        credentials: CallCredentials | None = ...,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: bool | None = ...,
        compression: Compression | None = ...,
    ) -> UnaryUnaryCall[_TRequest, _TResponse]: ...

class UnaryStreamMultiCallable(typing.Generic[_TRequest, _TResponse]):
    def __call__(
        self,
        request: _TRequest,
        timeout: float | None = ...,
        metadata: MetadataType | None = ...,
        credentials: CallCredentials | None = ...,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: bool | None = ...,
        compression: Compression | None = ...,
    ) -> UnaryStreamCall[_TRequest, _TResponse]: ...

class StreamUnaryMultiCallable(typing.Generic[_TRequest, _TResponse]):
    def __call__(
        self,
        request_iterator: AsyncIterator[_TRequest] | Iterator[_TRequest] | None,
        timeout: float | None = ...,
        metadata: MetadataType | None = ...,
        credentials: CallCredentials | None = ...,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: bool | None = ...,
        compression: Compression | None = ...,
    ) -> StreamUnaryCall[_TRequest, _TResponse]: ...

class StreamStreamMultiCallable(typing.Generic[_TRequest, _TResponse]):
    def __call__(
        self,
        request_iterator: AsyncIterator[_TRequest] | Iterator[_TRequest] | None,
        timeout: float | None = ...,
        metadata: MetadataType | None = ...,
        credentials: CallCredentials | None = ...,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: bool | None = ...,
        compression: Compression | None = ...,
    ) -> StreamStreamCall[_TRequest, _TResponse]: ...

# Metadata:

MetadataKey: TypeAlias = str
MetadataValue: TypeAlias = str | bytes
MetadatumType: TypeAlias = tuple[MetadataKey, MetadataValue]
MetadataType: TypeAlias = Metadata | Sequence[MetadatumType]

class Metadata(Mapping[MetadataKey, MetadataValue]):
    def __init__(self, *args: tuple[MetadataKey, MetadataValue]) -> None: ...
    @classmethod
    def from_tuple(cls, raw_metadata: tuple[MetadataKey, MetadataValue]) -> Metadata: ...
    def add(self, key: MetadataKey, value: MetadataValue) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: MetadataKey) -> MetadataValue: ...
    def __setitem__(self, key: MetadataKey, value: MetadataValue) -> None: ...
    def __delitem__(self, key: MetadataKey) -> None: ...
    def delete_all(self, key: MetadataKey) -> None: ...
    def __iter__(self) -> Iterator[MetadataKey]: ...
    def get_all(self, key: MetadataKey) -> list[MetadataValue]: ...
    def set_all(self, key: MetadataKey, values: list[MetadataValue]) -> None: ...
    def __contains__(self, key: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __add__(self, other: typing.Any) -> Metadata: ...
