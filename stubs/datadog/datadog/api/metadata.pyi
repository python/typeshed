from datadog.api.resources import GetableAPIResource, UpdatableAPIResource

class Metadata(GetableAPIResource, UpdatableAPIResource):
    @classmethod
    def get(cls, metric_name): ...
    @classmethod
    def update(cls, metric_name, **params): ...
