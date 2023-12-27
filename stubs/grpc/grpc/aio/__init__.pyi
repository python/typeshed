import asyncio
import typing
from concurrent import futures
from types import TracebackType
from grpc import (
    _Options,
    _PartialStubMustCastOrIgnore,
    RpcError,
    Compression,
    GenericRpcHandler,
    ServerCredentials,
    StatusCode,
    ChannelCredentials,
    CallCredentials,
    ChannelConnectivity,
    HandlerCallDetails,
    RpcMethodHandler,
)

"""Exceptions"""
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
        details: typing.Optional[str],
        debug_error_string: typing.Optional[str],
    ) -> None:
        ...

    # FIXME: confirm if these are present in the parent type. The remaining
    # methods already exist.
    def debug_error_string(self) -> str: ...
    def initial_metadata(self) -> Metadata: ...


"""Create Client"""

ClientInterceptor = _PartialStubMustCastOrIgnore

def insecure_channel(
    target: str,
    options: typing.Optional[_Options] = None,
    compression: typing.Optional[Compression] = None,
    interceptors: typing.Optional[typing.Sequence[ClientInterceptor]] = None,
) -> Channel: ...
def secure_channel(
    target: str,
    credentials: ChannelCredentials,
    options: typing.Optional[_Options] = None,
    compression: typing.Optional[Compression] = None,
    interceptors: typing.Optional[typing.Sequence[ClientInterceptor]] = None,
) -> Channel: ...


"""Create Server"""

def server(
    migration_thread_pool: typing.Optional[futures.Executor] = None,
    handlers: typing.Optional[typing.Sequence[GenericRpcHandler]] = None,
    interceptors: typing.Optional[typing.Sequence[ServerInterceptor]] = None,
    options: typing.Optional[_Options] = None,
    maximum_concurrent_rpcs: typing.Optional[int] = None,
    compression: typing.Optional[Compression] = None,
) -> Server: ...


"""Channel Object"""

# XXX: The docs suggest these type signatures for aio, but not for non-async,
# and it's unclear why;
# https://grpc.github.io/grpc/python/grpc_asyncio.html#grpc.aio.Channel.stream_stream
RequestSerializer = typing.Callable[[typing.Any], bytes]
ResponseDeserializer = typing.Callable[[bytes], typing.Any]

class Channel:
    async def close(self, grace: typing.Optional[float]) -> None: ...

    def get_state(self, try_to_connect: bool = False) -> ChannelConnectivity: ...

    async def wait_for_state_change(self, last_observed_state: ChannelConnectivity) -> None: ...

    def stream_stream(
        self,
        method: str,
        request_serializer: typing.Optional[RequestSerializer],
        response_deserializer: typing.Optional[ResponseDeserializer],
    ) -> StreamStreamMultiCallable: ...

    def stream_unary(
        self,
        method: str,
        request_serializer: typing.Optional[RequestSerializer],
        response_deserializer: typing.Optional[ResponseDeserializer],
    ) -> StreamUnaryMultiCallable: ...

    def unary_stream(
        self,
        method: str,
        request_serializer: typing.Optional[RequestSerializer],
        response_deserializer: typing.Optional[ResponseDeserializer],
    ) -> UnaryStreamMultiCallable: ...

    def unary_unary(
        self,
        method: str,
        request_serializer: typing.Optional[RequestSerializer],
        response_deserializer: typing.Optional[ResponseDeserializer],
    ) -> UnaryUnaryMultiCallable: ...

    async def __aenter__(self) -> Channel: ...

    async def __aexit__(
        self,
        exc_type: typing.Optional[typing.Type[BaseException]],
        exc_val: typing.Optional[BaseException],
        exc_tb: typing.Optional[TracebackType],
    ) -> typing.Optional[bool]: ...

    async def channel_ready(self) -> None: ...

"""Server Object"""

class Server:
    def add_generic_rpc_handlers(
        self,
        generic_rpc_handlers: typing.Iterable[GenericRpcHandler],
    ) -> None: ...

    # Returns an integer port on which server will accept RPC requests.
    def add_insecure_port(self, address: str) -> int: ...

    # Returns an integer port on which server will accept RPC requests.
    def add_secure_port(
        self, address: str, server_credentials: ServerCredentials
    ) -> int: ...

    async def start(self) -> None: ...

    # Grace period is in seconds.
    async def stop(self, grace: typing.Optional[float] = None) -> None: ...

    # Returns a bool indicates if the operation times out. Timeout is in seconds.
    async def wait_for_termination(
        self, timeout: typing.Optional[float] = None
    ) -> bool: ...

"""Client-Side Context"""

DoneCallbackType = typing.Callable[[typing.Any], None]
EOFType = object

class RpcContext:
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def time_remaining(self) -> typing.Optional[float]: ...
    def cancel(self) -> bool: ...
    def add_done_callback(self, callback: DoneCallbackType) -> None: ...

class Call(RpcContext):
    async def initial_metadata(self) -> Metadata: ...
    async def trailing_metadata(self) -> Metadata: ...
    async def code(self) -> StatusCode: ...
    async def details(self) -> str: ...
    async def wait_for_connection(self) -> None: ...

class UnaryUnaryCall(typing.Generic[TRequest, TResponse], Call):
    def __await__(self) -> typing.Generator[None, None, TResponse]: ...

class UnaryStreamCall(typing.Generic[TRequest, TResponse], Call):
    def __aiter__(self) -> typing.AsyncIterator[TResponse]: ...
    async def read(self) -> typing.Union[EOFType, TResponse]: ...

class StreamUnaryCall(typing.Generic[TRequest, TResponse], Call):
    async def write(self, request: TRequest) -> None: ...
    async def done_writing(self) -> None: ...
    def __await__(self) -> typing.Generator[None, None, TResponse]: ...

class StreamStreamCall(typing.Generic[TRequest, TResponse], Call):
    def __aiter__(self) -> typing.AsyncIterator[TResponse]: ...
    async def read(self) -> typing.Union[EOFType, TResponse]: ...
    async def write(self, request: TRequest) -> None: ...
    async def done_writing(self) -> None: ...

TRequest = typing.TypeVar("TRequest")
TResponse = typing.TypeVar("TResponse")

"""Service-Side Context"""

class DoneCallback(typing.Generic[TRequest, TResponse]):
    def __call__(
        self,
        ctx: ServicerContext[TRequest, TResponse],
    ) -> None:
        ...

class ServicerContext(typing.Generic[TRequest, TResponse]):
    async def abort(
        self,
        code: StatusCode,
        details: str = "",
        trailing_metadata: MetadataType = tuple(),
    ) -> typing.NoReturn: ...

    async def read(self) -> TRequest: ...
    async def write(self, message: TResponse) -> None: ...
    async def send_initial_metadata(self, initial_metadata: MetadataType) -> None: ...

    def add_done_callback(self, callback: DoneCallback[TRequest, TResponse]) -> None: ...
    def set_trailing_metadata(self, trailing_metadata: MetadataType) -> None: ...
    def invocation_metadata(self) -> typing.Optional[Metadata]: ...
    def set_code(self, code: StatusCode) -> None: ...
    def set_details(self, details: str) -> None: ...
    def set_compression(self, compression: Compression) -> None: ...
    def disable_next_message_compression(self) -> None: ...
    def peer(self) -> str: ...
    def peer_identities(self) -> typing.Optional[typing.Iterable[bytes]]: ...
    def peer_identity_key(self) -> typing.Optional[str]: ...
    def auth_context(self) -> typing.Mapping[str, typing.Iterable[bytes]]: ...
    def time_remaining(self) -> float: ...
    def trailing_metadata(self) -> Metadata: ...
    def code(self) -> StatusCode: ...
    def details(self) -> str: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...


"""Client-Side Interceptor"""

class ClientCallDetails:
    def __init__(
        self,
        method: str,
        timeout: typing.Optional[float],
        metadata: typing.Optional[Metadata],
        credentials: typing.Optional[CallCredentials],
        wait_for_ready: typing.Optional[bool],
    ) -> None:
        ...

    method: str
    timeout: typing.Optional[float]
    metadata: typing.Optional[Metadata]
    credentials: typing.Optional[CallCredentials]

    # "This is an EXPERIMENTAL argument. An optional flag t enable wait for ready mechanism."
    wait_for_ready: typing.Optional[bool]

    # As at 1.53.0, this is not supported in aio:
    # compression: typing.Optional[Compression]


class InterceptedCall(typing.Generic[TRequest, TResponse]):
    def __init__(self, interceptors_task: asyncio.Task) -> None: ...
    def __del__(self): ...

    def cancel(self) -> bool: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def add_done_callback(self, callback: DoneCallback[TRequest, TResponse]) -> None: ...
    def time_remaining(self) -> typing.Optional[float]: ...
    async def initial_metadata(self) -> typing.Optional[Metadata]: ...
    async def trailing_metadata(self) -> typing.Optional[Metadata]: ...
    async def code(self) -> StatusCode: ...
    async def details(self) -> str: ...
    async def debug_error_string(self) -> typing.Optional[str]: ...
    async def wait_for_connection(self) -> None: ...


class InterceptedUnaryUnaryCall(InterceptedCall[TRequest, TResponse], typing.Generic[TRequest, TResponse]):
    def __await__(self): ...

    def __init__(
        self,
        interceptors: typing.Sequence[UnaryUnaryClientInterceptor],
        request: TRequest,
        timeout: typing.Optional[float],
        metadata: Metadata,
        credentials: typing.Optional[CallCredentials],
        wait_for_ready: typing.Optional[bool],
        channel: Channel,
        method: bytes,
        request_serializer: RequestSerializer,
        response_deserializer: ResponseDeserializer,
        loop: asyncio.AbstractEventLoop,
    ) -> None:
        ...

    # pylint: disable=too-many-arguments
    async def _invoke(
        self,
        interceptors: typing.Sequence[UnaryUnaryClientInterceptor],
        method: bytes,
        timeout: typing.Optional[float],
        metadata: typing.Optional[Metadata],
        credentials: typing.Optional[CallCredentials],
        wait_for_ready: typing.Optional[bool],
        request: TRequest,
        request_serializer: RequestSerializer,
        response_deserializer: ResponseDeserializer,
    ) -> UnaryUnaryCall:
        ...

    def time_remaining(self) -> typing.Optional[float]: ...


class UnaryUnaryClientInterceptor(typing.Generic[TRequest, TResponse]):
    async def intercept_unary_unary(
        self,
        # XXX: See equivalent function in grpc types for notes about continuation:
        continuation: typing.Callable[[ClientCallDetails, TRequest], UnaryUnaryCall[TRequest, TResponse]],
        client_call_details: ClientCallDetails,
        request: TRequest,
    ) -> TResponse:
        ...


class UnaryStreamClientInterceptor(typing.Generic[TRequest, TResponse]):
    async def intercept_unary_stream(
        self,
        continuation: typing.Callable[[ClientCallDetails, TRequest], UnaryStreamCall[TRequest, TResponse]],
        client_call_details: ClientCallDetails,
        request: TRequest,
    ) -> typing.Union[
        typing.AsyncIterable[TResponse],
        UnaryStreamCall[TRequest, TResponse],
    ]:
        ...


class StreamUnaryClientInterceptor(typing.Generic[TRequest, TResponse]):
    async def intercept_stream_unary(
        self,
        continuation: typing.Callable[[ClientCallDetails, TRequest], StreamUnaryCall[TRequest, TResponse]],
        client_call_details: ClientCallDetails,
        request_iterator: typing.Union[typing.AsyncIterable[TRequest], typing.Iterable[TRequest]],
    ) -> typing.Union[
        typing.AsyncIterable[TResponse],
        UnaryStreamCall[TRequest, TResponse],
    ]:
        ...


class StreamStreamClientInterceptor(typing.Generic[TRequest, TResponse]):
    async def intercept_stream_stream(
        self,
        continuation: typing.Callable[[ClientCallDetails, TRequest], StreamStreamCall[TRequest, TResponse]],
        client_call_details: ClientCallDetails,
        request_iterator: typing.Union[typing.AsyncIterable[TRequest], typing.Iterable[TRequest]],
    ) -> typing.Union[
        typing.AsyncIterable[TResponse],
        StreamStreamCall[TRequest, TResponse],
    ]:
        ...


"""Server-Side Interceptor"""

class ServerInterceptor(typing.Generic[TRequest, TResponse]):
    async def intercept_service(
        self,
        continuation: typing.Callable[
            [HandlerCallDetails],
            typing.Awaitable[RpcMethodHandler[TRequest, TResponse]],
        ],
        handler_call_details: HandlerCallDetails,
    ) -> RpcMethodHandler[TRequest, TResponse]:
        ...


"""Multi-Callable Interfaces"""

class UnaryUnaryMultiCallable(typing.Generic[TRequest, TResponse]):
    def __call__(
        self,
        request: TRequest,
        timeout: typing.Optional[float] = None,
        metadata: typing.Optional[MetadataType] = None,
        credentials: typing.Optional[CallCredentials] = None,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: typing.Optional[bool] = None,
        compression: typing.Optional[Compression] = None,
    ) -> UnaryUnaryCall[TRequest, TResponse]: ...

class UnaryStreamMultiCallable(typing.Generic[TRequest, TResponse]):
    def __call__(
        self,
        request: TRequest,
        timeout: typing.Optional[float] = None,
        metadata: typing.Optional[MetadataType] = None,
        credentials: typing.Optional[CallCredentials] = None,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: typing.Optional[bool] = None,
        compression: typing.Optional[Compression] = None,
    ) -> UnaryStreamCall[TRequest, TResponse]: ...

class StreamUnaryMultiCallable(typing.Generic[TRequest, TResponse]):
    def __call__(
        self,
        request_iterator: typing.Optional[
            typing.Union[typing.AsyncIterator[TRequest], typing.Iterator[TRequest]]
        ],
        timeout: typing.Optional[float] = None,
        metadata: typing.Optional[MetadataType] = None,
        credentials: typing.Optional[CallCredentials] = None,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: typing.Optional[bool] = None,
        compression: typing.Optional[Compression] = None,
    ) -> StreamUnaryCall[TRequest, TResponse]: ...

class StreamStreamMultiCallable(typing.Generic[TRequest, TResponse]):
    def __call__(
        self,
        request_iterator: typing.Optional[
            typing.Union[typing.AsyncIterator[TRequest], typing.Iterator[TRequest]]
        ],
        timeout: typing.Optional[float] = None,
        metadata: typing.Optional[MetadataType] = None,
        credentials: typing.Optional[CallCredentials] = None,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: typing.Optional[bool] = None,
        compression: typing.Optional[Compression] = None,
    ) -> StreamStreamCall[TRequest, TResponse]: ...


"""Metadata"""

MetadataKey = str
MetadataValue = typing.Union[str, bytes]
MetadatumType = typing.Tuple[MetadataKey, MetadataValue]
MetadataType = typing.Union[Metadata, typing.Sequence[MetadatumType]]

class Metadata(typing.Mapping):
    def __init__(self, *args: typing.Tuple[MetadataKey, MetadataValue]) -> None: ...
    @classmethod
    def from_tuple(
        cls, raw_metadata: typing.Tuple[MetadataKey, MetadataValue]
    ) -> Metadata: ...
    def add(self, key: MetadataKey, value: MetadataValue) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: MetadataKey) -> MetadataValue: ...
    def __setitem__(self, key: MetadataKey, value: MetadataValue) -> None: ...
    def __delitem__(self, key: MetadataKey) -> None: ...
    def delete_all(self, key: MetadataKey) -> None: ...
    def __iter__(self) -> typing.Iterator[typing.Tuple[MetadataKey, MetadataValue]]: ...
    def get_all(self, key: MetadataKey) -> typing.List[MetadataValue]: ...
    def set_all(self, key: MetadataKey, values: typing.List[MetadataValue]) -> None: ...
    def __contains__(self, key: object) -> bool: ...
    def __eq__(self, other: typing.Any) -> bool: ...
    def __add__(self, other: typing.Any) -> Metadata: ...
    def __repr__(self) -> str: ...
