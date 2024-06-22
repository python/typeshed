from _typeshed import Incomplete
from typing import Literal

from docker.types import IPAMConfig

class NetworkApiMixin:
    def networks(self, names: Incomplete | None = None, ids: Incomplete | None = None, filters: Incomplete | None = None): ...
    def create_network(
        self,
        name: str,
        driver: str | None = None,
        options: dict[Incomplete, Incomplete] | None = None,
        ipam: IPAMConfig | None = None,
        check_duplicate: bool | None = None,
        internal: bool = False,
        labels: dict[Incomplete, Incomplete] | None = None,
        enable_ipv6: bool = False,
        attachable: bool | None = None,
        scope: Literal["local", "global", "swarm"] | None = None,
        ingress: bool | None = None,
    ) -> dict[Incomplete, Incomplete]: ...
    def prune_networks(self, filters: Incomplete | None = None): ...
    def remove_network(self, net_id) -> None: ...
    def inspect_network(self, net_id, verbose: Incomplete | None = None, scope: Incomplete | None = None): ...
    def connect_container_to_network(
        self,
        container,
        net_id,
        ipv4_address: Incomplete | None = None,
        ipv6_address: Incomplete | None = None,
        aliases: Incomplete | None = None,
        links: Incomplete | None = None,
        link_local_ips: Incomplete | None = None,
        driver_opt: Incomplete | None = None,
        mac_address: Incomplete | None = None,
    ) -> None: ...
    def disconnect_container_from_network(self, container, net_id, force: bool = False) -> None: ...
