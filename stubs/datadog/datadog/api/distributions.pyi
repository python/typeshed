from _typeshed import Incomplete

from datadog.api.resources import SendableAPIResource

class Distribution(SendableAPIResource):
    @classmethod
    def send(
        cls,
        distributions: Incomplete | None = None,
        attach_host_name: bool = True,
        compress_payload: bool = False,
        **distribution,
    ): ...
