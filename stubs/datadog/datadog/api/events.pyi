from datadog.api.resources import CreateableAPIResource, GetableAPIResource, SearchableAPIResource

class Event(GetableAPIResource, CreateableAPIResource, SearchableAPIResource):
    @classmethod
    def create(cls, attach_host_name: bool = True, **params): ...
    @classmethod
    def query(cls, **params): ...
