from datadog.api.resources import SearchableAPIResource

class Infrastructure(SearchableAPIResource):
    @classmethod
    def search(cls, **params): ...
