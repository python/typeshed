from _typeshed import Incomplete

class EndpointConfig(dict[str, Incomplete]):
    def __init__(
        self,
        version: str,
        aliases: list[Incomplete] | None = None,
        links: list[Incomplete] | None = None,
        ipv4_address: str | None = None,
        ipv6_address: str | None = None,
        link_local_ips: list[str] | None = None,
        driver_opt: Incomplete | None = None,
        mac_address: str | None = None,
    ) -> None: ...

class NetworkingConfig(dict[str, Incomplete]):
    def __init__(self, endpoints_config: EndpointConfig | None = None) -> None: ...

class IPAMConfig(dict[str, Incomplete]):
    def __init__(
        self,
        driver: str = "default",
        pool_configs: list[IPAMPool] | None = None,
        options: dict[Incomplete, Incomplete] | None = None,
    ) -> None: ...

class IPAMPool(dict[str, Incomplete]):
    def __init__(
        self,
        subnet: str | None = None,
        iprange: str | None = None,
        gateway: str | None = None,
        aux_addresses: dict[str, str] | None = None,
    ) -> None: ...
