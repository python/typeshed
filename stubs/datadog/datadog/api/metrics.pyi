from _typeshed import Incomplete

from datadog.api.resources import ListableAPIResource, SearchableAPIResource, SendableAPIResource

class Metric(SearchableAPIResource, SendableAPIResource, ListableAPIResource):
    @classmethod
    def list(cls, from_epoch): ...
    @classmethod
    def send(
        cls, metrics: Incomplete | None = None, attach_host_name: bool = True, compress_payload: bool = False, **single_metric
    ): ...
    @classmethod
    def query(cls, **params): ...
