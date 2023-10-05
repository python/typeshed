from _typeshed import Incomplete

log: Incomplete

class APIClient:
    @classmethod
    def submit(
        cls,
        method,
        path,
        api_version: Incomplete | None = None,
        body: Incomplete | None = None,
        attach_host_name: bool = False,
        response_formatter: Incomplete | None = None,
        error_formatter: Incomplete | None = None,
        suppress_response_errors_on_codes: Incomplete | None = None,
        compress_payload: bool = False,
        **params,
    ): ...
