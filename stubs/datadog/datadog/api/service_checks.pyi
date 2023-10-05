from datadog.api.resources import ActionAPIResource

class ServiceCheck(ActionAPIResource):
    @classmethod
    def check(cls, **body): ...
