from concurrent import futures
from grpc import ServicerContext
from grpc_health.v1 import health_pb2 as _health_pb2
from grpc_health.v1 import health_pb2_grpc as _health_pb2_grpc
from typing import Callable, Optional

SERVICE_NAME: str
OVERALL_HEALTH: str

class _Watcher:
    def __init__(self) -> None:
        ...

    def __iter__(self) -> _Watcher:
        ...

    def next(self) -> _health_pb2.HealthCheckResponse:
        ...

    def __next__(self) -> _health_pb2.HealthCheckResponse:
        ...

    def add(self, response: _health_pb2.HealthCheckResponse) -> None:
        ...

    def close(self) -> None:
        ...

class HealthServicer(_health_pb2_grpc.HealthServicer):
    def __init__(self, experimental_non_blocking: bool = ..., experimental_thread_pool: Optional[futures.ThreadPoolExecutor] = ...) -> None:
        ...

    def Check(self, request: _health_pb2.HealthCheckRequest, context: ServicerContext) -> _health_pb2.HealthCheckResponse:
        ...

    def Watch(self, request: _health_pb2.HealthCheckRequest, context: ServicerContext, send_response_callback: Optional[Callable] = ...) -> _health_pb2.HealthCheckResponse:
        ...

    def set(self, service: str, status: _health_pb2.HealthCheckResponse.ServingStatus) -> None:
        ...

    def enter_graceful_shutdown(self) -> None:
        ...
