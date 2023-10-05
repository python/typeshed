from datadog.api.resources import ActionAPIResource, SearchableAPIResource

class Host(ActionAPIResource):
    @classmethod
    def mute(cls, host_name, **body): ...
    @classmethod
    def unmute(cls, host_name): ...

class Hosts(ActionAPIResource, SearchableAPIResource):
    @classmethod
    def search(cls, **params): ...
    @classmethod
    def totals(cls): ...
