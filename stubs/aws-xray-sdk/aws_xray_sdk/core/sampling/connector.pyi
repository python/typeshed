class ServiceConnector:
    def __init__(self) -> None: ...
    def fetch_sampling_rules(self): ...
    def fetch_sampling_target(self, rules): ...
    def setup_xray_client(self, ip, port, client) -> None: ...
    @property
    def context(self): ...
    @context.setter
    def context(self, v) -> None: ...
