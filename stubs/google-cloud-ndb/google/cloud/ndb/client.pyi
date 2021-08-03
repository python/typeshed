from typing import Any

from google.api_core import client_info as client_info
from google.cloud import client as google_client, environment_vars as environment_vars
from google.cloud.datastore_v1.gapic import datastore_client as datastore_client
from google.cloud.datastore_v1.proto import datastore_pb2_grpc as datastore_pb2_grpc

DATASTORE_API_HOST: Any

class Client(google_client.ClientWithProject):
    SCOPE: Any
    namespace: Any
    host: Any
    client_info: Any
    secure: Any
    stub: Any
    def __init__(self, project: Any | None = ..., namespace: Any | None = ..., credentials: Any | None = ...) -> None: ...
    def context(
        self,
        namespace=...,
        cache_policy: Any | None = ...,
        global_cache: Any | None = ...,
        global_cache_policy: Any | None = ...,
        global_cache_timeout_policy: Any | None = ...,
        legacy_data: bool = ...,
    ) -> None: ...
