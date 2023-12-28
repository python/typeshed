import abc
import enum
import threading
import typing
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from concurrent import futures
from types import ModuleType, TracebackType
from typing_extensions import Self, TypeAlias

__version__: str

# This class encodes an uninhabited type, requiring use of explicit casts or ignores
# in order to satisfy type checkers. This allows grpc-stubs to add proper stubs
# later, allowing those overrides to be removed.
# The alternative is typing.Any, but a future replacement of Any with a proper type
# would result in type errors where previously the type checker was happy, which
# we want to avoid. Forcing the user to use overrides provides forwards-compatibility.
class _PartialStubMustCastOrIgnore: ...

# XXX: Early attempts to tame this used literals for all the keys (gRPC is
# a bit segfaulty and doesn't adequately validate the option keys), but that
# didn't quite work out. Maybe it's something we can come back to?
_OptionKeyValue: TypeAlias = tuple[str, typing.Any]
_Options: TypeAlias = Sequence[_OptionKeyValue]

class Compression(enum.IntEnum):
    NoCompression = ...
    Deflate = ...
    Gzip = ...

@enum.unique
class LocalConnectionType(enum.Enum):
    UDS = ...
    LOCAL_TCP = ...

# XXX: not documented, needs more investigation.
# Some evidence:
# - https://github.com/grpc/grpc/blob/0e1984effd7e977ef18f1ad7fde7d10a2a153e1d/src/python/grpcio_tests/tests/unit/_metadata_test.py#L71
# - https://github.com/grpc/grpc/blob/0e1984effd7e977ef18f1ad7fde7d10a2a153e1d/src/python/grpcio_tests/tests/unit/_metadata_test.py#L58
# - https://github.com/grpc/grpc/blob/0e1984effd7e977ef18f1ad7fde7d10a2a153e1d/src/python/grpcio_tests/tests/unit/_invocation_defects_test.py#L66
Metadata: TypeAlias = tuple[tuple[str, str | bytes], ...]

_TRequest = typing.TypeVar("_TRequest")
_TResponse = typing.TypeVar("_TResponse")

# XXX: These are probably the SerializeToTring/FromString pb2 methods, but
# this needs further investigation
class RequestSerializer(typing.Protocol):
    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any: ...

class RequestDeserializer(typing.Protocol):
    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any: ...

class ResponseSerializer(typing.Protocol):
    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any: ...

class ResponseDeserializer(typing.Protocol):
    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any: ...

# Future Interfaces:

class FutureTimeoutError(Exception): ...
class FutureCancelledError(Exception): ...

_TFutureValue = typing.TypeVar("_TFutureValue")

class Future(abc.ABC, typing.Generic[_TFutureValue]):
    def add_done_callback(self, fn: Callable[[Future[_TFutureValue]], None]) -> None: ...
    def cancel(self) -> bool: ...
    def cancelled(self) -> bool: ...
    def done(self) -> bool: ...
    def exception(self) -> Exception | None: ...
    def result(self, timeout: float | None = ...) -> _TFutureValue: ...
    def running(self) -> bool: ...

    # FIXME: unsure of the exact return type here. Is it a traceback.StackSummary?
    def traceback(self, timeout: float | None = ...) -> typing.Any: ...

# Create Client:

def insecure_channel(target: str, options: _Options | None = ..., compression: Compression | None = ...) -> Channel: ...
def secure_channel(
    target: str, credentials: ChannelCredentials, options: _Options | None = ..., compression: Compression | None = ...
) -> Channel: ...

Interceptor: TypeAlias = (
    UnaryUnaryClientInterceptor[_TRequest, _TResponse]
    | UnaryStreamClientInterceptor[_TRequest, _TResponse]
    | StreamUnaryClientInterceptor[_TRequest, _TResponse]
    | StreamStreamClientInterceptor[_TRequest, _TResponse]
)

def intercept_channel(channel: Channel, *interceptors: Interceptor[_TRequest, _TResponse]) -> Channel: ...

# Create Client Credentials:

def ssl_channel_credentials(
    root_certificates: bytes | None = ..., private_key: bytes | None = ..., certificate_chain: bytes | None = ...
) -> ChannelCredentials: ...
def local_channel_credentials(local_connect_type: LocalConnectionType = ...) -> ChannelCredentials: ...
def metadata_call_credentials(metadata_plugin: AuthMetadataPlugin, name: str | None = ...) -> CallCredentials: ...
def access_token_call_credentials(access_token: str) -> CallCredentials: ...
def alts_channel_credentials(service_accounts: Sequence[str] | None = ...) -> ChannelCredentials: ...
def compute_engine_channel_credentials() -> ChannelCredentials: ...
def xds_channel_credentials(fallback_credentials: ChannelCredentials | None = ...) -> ChannelCredentials: ...

# GRPC docs say there should be at least two:
def composite_call_credentials(creds1: CallCredentials, creds2: CallCredentials, *rest: CallCredentials) -> CallCredentials: ...

# Compose a ChannelCredentials and one or more CallCredentials objects.
def composite_channel_credentials(
    channel_credentials: ChannelCredentials, call_credentials: CallCredentials, *rest: CallCredentials
) -> ChannelCredentials: ...

# Create Server:

def server(
    thread_pool: futures.ThreadPoolExecutor,
    handlers: list[GenericRpcHandler[typing.Any, typing.Any]] | None = ...,
    interceptors: list[ServerInterceptor[typing.Any, typing.Any]] | None = ...,
    options: _Options | None = ...,
    maximum_concurrent_rpcs: int | None = ...,
    compression: Compression | None = ...,
    xds: bool = ...,
) -> Server: ...

# Create Server Credentials:

CertificateChainPair: TypeAlias = tuple[bytes, bytes]

def ssl_server_credentials(
    private_key_certificate_chain_pairs: list[CertificateChainPair],
    root_certificates: bytes | None = ...,
    require_client_auth: bool = ...,
) -> ServerCredentials: ...
def local_server_credentials(local_connect_type: LocalConnectionType = ...) -> ServerCredentials: ...
def ssl_server_certificate_configuration(
    private_key_certificate_chain_pairs: list[CertificateChainPair], root_certificates: bytes | None = ...
) -> ServerCertificateConfiguration: ...
def dynamic_ssl_server_credentials(
    initial_certificate_configuration: ServerCertificateConfiguration,
    certificate_configuration_fetcher: Callable[[], ServerCertificateConfiguration],
    require_client_authentication: bool = ...,
) -> ServerCredentials: ...
def alts_server_credentials() -> ServerCredentials: ...
def insecure_server_credentials() -> ServerCredentials: ...
def xds_server_credentials(fallback_credentials: ServerCredentials) -> ServerCredentials: ...

# RPC Method Handlers:

# XXX: This is probably what appears in the add_FooServicer_to_server function
# in the _pb2_grpc files that get generated, which points to the FooServicer
# handler functions that get generated, which look like this:
#
#    def FloobDoob(self, request, context):
#       return response
#
class Behaviour(typing.Protocol):
    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any: ...

def unary_unary_rpc_method_handler(
    behavior: Behaviour,
    request_deserializer: RequestDeserializer | None = ...,
    response_serializer: ResponseSerializer | None = ...,
) -> RpcMethodHandler[typing.Any, typing.Any]: ...
def unary_stream_rpc_method_handler(
    behavior: Behaviour,
    request_deserializer: RequestDeserializer | None = ...,
    response_serializer: ResponseSerializer | None = ...,
) -> RpcMethodHandler[typing.Any, typing.Any]: ...
def stream_unary_rpc_method_handler(
    behavior: Behaviour,
    request_deserializer: RequestDeserializer | None = ...,
    response_serializer: ResponseSerializer | None = ...,
) -> RpcMethodHandler[typing.Any, typing.Any]: ...
def stream_stream_rpc_method_handler(
    behavior: Behaviour,
    request_deserializer: RequestDeserializer | None = ...,
    response_serializer: ResponseSerializer | None = ...,
) -> RpcMethodHandler[typing.Any, typing.Any]: ...
def method_handlers_generic_handler(
    service: str, method_handlers: dict[str, RpcMethodHandler[typing.Any, typing.Any]]
) -> GenericRpcHandler[typing.Any, typing.Any]: ...

# Channel Ready Future:

def channel_ready_future(channel: Channel) -> Future[None]: ...

# Channel Connectivity:

class ChannelConnectivity(enum.Enum):
    IDLE = ...
    CONNECTING = ...
    READY = ...
    TRANSIENT_FAILURE = ...
    SHUTDOWN = ...

# gRPC Status Code:

class Status(abc.ABC):
    code: StatusCode

    # XXX: misnamed property, does not align with status.proto, where it is called 'message':
    details: str

    trailing_metadata: Metadata

# https://grpc.github.io/grpc/core/md_doc_statuscodes.html
class StatusCode(enum.Enum):
    OK = ...
    CANCELLED = ...
    UNKNOWN = ...
    INVALID_ARGUMENT = ...
    DEADLINE_EXCEEDED = ...
    NOT_FOUND = ...
    ALREADY_EXISTS = ...
    PERMISSION_DENIED = ...
    RESOURCE_EXHAUSTED = ...
    FAILED_PRECONDITION = ...
    ABORTED = ...
    OUT_OF_RANGE = ...
    UNIMPLEMENTED = ...
    INTERNAL = ...
    UNAVAILABLE = ...
    DATA_LOSS = ...
    UNAUTHENTICATED = ...

# Channel Object:

class Channel(abc.ABC):
    def close(self) -> None: ...
    def stream_stream(
        self, method: str, request_serializer: RequestSerializer | None, response_deserializer: ResponseDeserializer | None
    ) -> StreamStreamMultiCallable[typing.Any, typing.Any]: ...
    def stream_unary(
        self, method: str, request_serializer: RequestSerializer | None, response_deserializer: ResponseDeserializer | None
    ) -> StreamUnaryMultiCallable[typing.Any, typing.Any]: ...
    def subscribe(self, callback: Callable[[ChannelConnectivity], None], try_to_connect: bool = ...) -> None: ...
    def unary_stream(
        self, method: str, request_serializer: RequestSerializer | None, response_deserializer: ResponseDeserializer | None
    ) -> UnaryStreamMultiCallable[typing.Any, typing.Any]: ...
    def unary_unary(
        self, method: str, request_serializer: RequestSerializer | None, response_deserializer: ResponseDeserializer | None
    ) -> UnaryUnaryMultiCallable[typing.Any, typing.Any]: ...
    def unsubscribe(self, callback: Callable[[ChannelConnectivity], None]) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool | None: ...

# Server Object:

class Server(abc.ABC):
    def add_generic_rpc_handlers(self, generic_rpc_handlers: Iterable[GenericRpcHandler[typing.Any, typing.Any]]) -> None: ...

    # Returns an integer port on which server will accept RPC requests.
    def add_insecure_port(self, address: str) -> int: ...

    # Returns an integer port on which server will accept RPC requests.
    def add_secure_port(self, address: str, server_credentials: ServerCredentials) -> int: ...
    def start(self) -> None: ...

    # Grace period is in seconds.
    def stop(self, grace: float | None = ...) -> threading.Event: ...

    # Block current thread until the server stops. Returns a bool
    # indicates if the operation times out. Timeout is in seconds.
    def wait_for_termination(self, timeout: float | None = ...) -> bool: ...

# Authentication & Authorization Objects:

# This class has no supported interface
class ChannelCredentials: ...

# This class has no supported interface
class CallCredentials: ...

class AuthMetadataContext(abc.ABC):
    service_url: str
    method_name: str

class AuthMetadataPluginCallback(abc.ABC):
    def __call__(self, metadata: Metadata, error: Exception | None) -> None: ...

class AuthMetadataPlugin(abc.ABC):
    def __call__(self, context: AuthMetadataContext, callback: AuthMetadataPluginCallback) -> None: ...

# This class has no supported interface
class ServerCredentials: ...

# This class has no supported interface
class ServerCertificateConfiguration: ...

# gRPC Exceptions:

class _Metadatum:
    key: str
    value: bytes

# FIXME: There is scant documentation about what is actually available in this type.
# The properties here are the properties observed in the wild, and may be inaccurate.
# A better source to confirm their presence needs to be found at some point.
class RpcError(Exception):
    def code(self) -> StatusCode: ...

    # misnamed property, does not align with status.proto, where it is called 'message':
    def details(self) -> str | None: ...

    # XXX: This has a slightly different return type to all the other metadata:
    def trailing_metadata(self) -> tuple[_Metadatum, ...]: ...

# Shared Context:

class RpcContext(abc.ABC):
    def add_callback(self, callback: Callable[[], None]) -> bool: ...
    def cancel(self) -> bool: ...
    def is_active(self) -> bool: ...
    def time_remaining(self) -> float: ...

# Client-Side Context:

class Call(RpcContext, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def code(self) -> StatusCode: ...

    # misnamed property, does not align with status.proto, where it is called 'message':
    @abc.abstractmethod
    def details(self) -> str: ...

    @abc.abstractmethod
    def initial_metadata(self) -> Metadata: ...

    @abc.abstractmethod
    def trailing_metadata(self) -> Metadata: ...

# Client-Side Interceptor:

class ClientCallDetails(abc.ABC):
    method: str
    timeout: float | None
    metadata: Metadata | None
    credentials: CallCredentials | None

    # "This is an EXPERIMENTAL argument. An optional flag t enable wait for ready mechanism."
    wait_for_ready: bool | None

    compression: Compression | None

# An object that is both a Call for the RPC and a Future. In the event of
# RPC completion, the return Call-Future’s result value will be the
# response message of the RPC. Should the event terminate with non-OK
# status, the returned Call-Future’s exception value will be an RpcError.
#
class CallFuture(Call, Future[_TResponse]): ...

class UnaryUnaryClientInterceptor(abc.ABC, typing.Generic[_TRequest, _TResponse]):
    def intercept_unary_unary(
        self,
        # FIXME: decode these cryptic runes to confirm the typing mystery of
        # this callable's signature that was left for us by past civilisations:
        #
        #     continuation – A function that proceeds with the invocation by
        #     executing the next interceptor in chain or invoking the actual RPC
        #     on the underlying Channel. It is the interceptor’s responsibility
        #     to call it if it decides to move the RPC forward. The interceptor
        #     can use response_future = continuation(client_call_details,
        #     request) to continue with the RPC. continuation returns an object
        #     that is both a Call for the RPC and a Future. In the event of RPC
        #     completion, the return Call-Future’s result value will be the
        #     response message of the RPC. Should the event terminate with non-OK
        #     status, the returned Call-Future’s exception value will be an
        #     RpcError.
        #
        continuation: Callable[[ClientCallDetails, _TRequest], CallFuture[_TResponse]],
        client_call_details: ClientCallDetails,
        request: _TRequest,
    ) -> CallFuture[_TResponse]: ...

class CallIterator(Call, typing.Generic[_TResponse]):
    def __iter__(self) -> Iterator[_TResponse]: ...

class UnaryStreamClientInterceptor(abc.ABC, typing.Generic[_TRequest, _TResponse]):
    def intercept_unary_stream(
        self,
        continuation: Callable[[ClientCallDetails, _TRequest], CallIterator[_TResponse]],
        client_call_details: ClientCallDetails,
        request: _TRequest,
    ) -> CallIterator[_TResponse]: ...

class StreamUnaryClientInterceptor(abc.ABC, typing.Generic[_TRequest, _TResponse]):
    def intercept_stream_unary(
        self,
        continuation: Callable[[ClientCallDetails, _TRequest], CallFuture[_TResponse]],
        client_call_details: ClientCallDetails,
        request_iterator: Iterator[_TRequest],
    ) -> CallFuture[_TResponse]: ...

class StreamStreamClientInterceptor(abc.ABC, typing.Generic[_TRequest, _TResponse]):
    def intercept_stream_stream(
        self,
        continuation: Callable[[ClientCallDetails, _TRequest], CallIterator[_TResponse]],
        client_call_details: ClientCallDetails,
        request_iterator: Iterator[_TRequest],
    ) -> CallIterator[_TResponse]: ...

# Service-Side Context:

class ServicerContext(RpcContext, metaclass=abc.ABCMeta):
    # misnamed parameter 'details', does not align with status.proto, where it is called 'message':
    def abort(self, code: StatusCode, details: str) -> typing.NoReturn: ...
    def abort_with_status(self, status: Status) -> typing.NoReturn: ...

    # FIXME: The docs say "A map of strings to an iterable of bytes for each auth property".
    # Does that mean 'bytes' (which is iterable), or 'Iterable[bytes]'?
    def auth_context(self) -> Mapping[str, bytes]: ...
    def disable_next_message_compression(self) -> None: ...
    def invocation_metadata(self) -> Metadata: ...
    def peer(self) -> str: ...
    def peer_identities(self) -> Iterable[bytes] | None: ...
    def peer_identity_key(self) -> str | None: ...
    def send_initial_metadata(self, initial_metadata: Metadata) -> None: ...
    def set_code(self, code: StatusCode) -> None: ...
    def set_compression(self, compression: Compression) -> None: ...
    def set_trailing_metadata(self, trailing_metadata: Metadata) -> None: ...

    # misnamed function 'details', does not align with status.proto, where it is called 'message':
    def set_details(self, details: str) -> None: ...
    def trailing_metadata(self) -> Metadata: ...

# Service-Side Handler:

class RpcMethodHandler(abc.ABC, typing.Generic[_TRequest, _TResponse]):
    request_streaming: bool
    response_streaming: bool

    # XXX: not clear from docs whether this is optional or not
    request_deserializer: RequestDeserializer | None

    # XXX: not clear from docs whether this is optional or not
    response_serializer: ResponseSerializer | None

    unary_unary: Callable[[_TRequest, ServicerContext], _TResponse] | None

    unary_stream: Callable[[_TRequest, ServicerContext], Iterator[_TResponse]] | None

    stream_unary: Callable[[Iterator[_TRequest], ServicerContext], _TResponse] | None

    stream_stream: Callable[[Iterator[_TRequest], ServicerContext], Iterator[_TResponse]] | None

class HandlerCallDetails(abc.ABC):
    method: str
    invocation_metadata: Metadata

class GenericRpcHandler(abc.ABC, typing.Generic[_TRequest, _TResponse]):
    def service(self, handler_call_details: HandlerCallDetails) -> RpcMethodHandler[_TRequest, _TResponse] | None: ...

class ServiceRpcHandler(GenericRpcHandler[_TRequest, _TResponse], metaclass=abc.ABCMeta):
    def service_name(self) -> str: ...

# Service-Side Interceptor:

class ServerInterceptor(abc.ABC, typing.Generic[_TRequest, _TResponse]):
    def intercept_service(
        self,
        continuation: Callable[[HandlerCallDetails], RpcMethodHandler[_TRequest, _TResponse] | None],
        handler_call_details: HandlerCallDetails,
    ) -> RpcMethodHandler[_TRequest, _TResponse] | None: ...

# Multi-Callable Interfaces:

class UnaryUnaryMultiCallable(abc.ABC, typing.Generic[_TRequest, _TResponse]):
    def __call__(
        self,
        request: _TRequest,
        timeout: float | None = ...,
        metadata: Metadata | None = ...,
        credentials: CallCredentials | None = ...,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: bool | None = ...,
        compression: Compression | None = ...,
    ) -> _TResponse: ...
    def future(
        self,
        request: _TRequest,
        timeout: float | None = ...,
        metadata: Metadata | None = ...,
        credentials: CallCredentials | None = ...,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: bool | None = ...,
        compression: Compression | None = ...,
    ) -> CallFuture[_TResponse]: ...
    def with_call(
        self,
        request: _TRequest,
        timeout: float | None = ...,
        metadata: Metadata | None = ...,
        credentials: CallCredentials | None = ...,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: bool | None = ...,
        compression: Compression | None = ...,
        # FIXME: Return value is documented as "The response value for the RPC and a Call value for the RPC";
        # this is slightly unclear so this return type is a best-effort guess.
    ) -> tuple[_TResponse, Call]: ...

class UnaryStreamMultiCallable(abc.ABC, typing.Generic[_TRequest, _TResponse]):
    def __call__(
        self,
        request: _TRequest,
        timeout: float | None = ...,
        metadata: Metadata | None = ...,
        credentials: CallCredentials | None = ...,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: bool | None = ...,
        compression: Compression | None = ...,
    ) -> CallIterator[_TResponse]: ...

class StreamUnaryMultiCallable(abc.ABC, typing.Generic[_TRequest, _TResponse]):
    def __call__(
        self,
        request_iterator: Iterator[_TRequest],
        timeout: float | None = ...,
        metadata: Metadata | None = ...,
        credentials: CallCredentials | None = ...,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: bool | None = ...,
        compression: Compression | None = ...,
    ) -> _TResponse: ...
    def future(
        self,
        request_iterator: Iterator[_TRequest],
        timeout: float | None = ...,
        metadata: Metadata | None = ...,
        credentials: CallCredentials | None = ...,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: bool | None = ...,
        compression: Compression | None = ...,
    ) -> CallFuture[_TResponse]: ...
    def with_call(
        self,
        request_iterator: Iterator[_TRequest],
        timeout: float | None = ...,
        metadata: Metadata | None = ...,
        credentials: CallCredentials | None = ...,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: bool | None = ...,
        compression: Compression | None = ...,
        # FIXME: Return value is documented as "The response value for the RPC and a Call value for the RPC";
        # this is slightly unclear so this return type is a best-effort guess.
    ) -> tuple[_TResponse, Call]: ...

class StreamStreamMultiCallable(abc.ABC, typing.Generic[_TRequest, _TResponse]):
    def __call__(
        self,
        request_iterator: Iterator[_TRequest],
        timeout: float | None = ...,
        metadata: Metadata | None = ...,
        credentials: CallCredentials | None = ...,
        # FIXME: optional bool seems weird, but that's what the docs suggest
        wait_for_ready: bool | None = ...,
        compression: Compression | None = ...,
    ) -> CallIterator[_TResponse]: ...

# Runtime Protobuf Parsing:

def protos(protobuf_path: str) -> ModuleType: ...
def services(protobuf_path: str) -> ModuleType: ...
def protos_and_services(protobuf_path: str) -> tuple[ModuleType, ModuleType]: ...
