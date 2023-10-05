from datadog.api.resources import CreateableAPIResource

class Logs(CreateableAPIResource):
    @classmethod
    def list(cls, data): ...
