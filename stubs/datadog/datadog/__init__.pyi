from typing import Any

from datadog.dogstatsd import DogStatsd as DogStatsd
from datadog.threadstats import (
    ThreadStats as ThreadStats,
    datadog_lambda_wrapper as datadog_lambda_wrapper,
    lambda_metric as lambda_metric,
)

def initialize(
    api_key: str | None = None,
    app_key: str | None = None,
    host_name: str | None = None,
    api_host: str | None = None,
    statsd_host: str | None = None,
    statsd_port: int | None = None,
    statsd_disable_buffering: bool = True,
    statsd_use_default_route: bool = False,
    statsd_socket_path: str | None = None,
    statsd_namespace: str | None = None,
    statsd_constant_tags: list[str] | None = None,
    return_raw_response: bool = False,
    hostname_from_config: bool = True,
    **kwargs: Any,
) -> None: ...
