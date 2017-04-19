from typing import List, Any

class DNSResolver:
    nameservers = ...  # type: List[str]
    _channel = ...  # type: Any

    def __init__(self, lookups: str, timeout: int=..., nameservers: List[str]=...) -> None:
        self.nameservers = nameservers
