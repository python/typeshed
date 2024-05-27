from _typeshed import Incomplete
from typing import TypedDict, type_check_only
from typing_extensions import TypeAlias

@type_check_only
class _HasId(TypedDict):
    Id: str

@type_check_only
class _HasID(TypedDict):
    ID: str

_Network: TypeAlias = _HasId | _HasID | str
_Container: TypeAlias = _HasId | _HasID | str

class NetworkApiMixin:
    def networks(self, names: Incomplete | None = None, ids: Incomplete | None = None, filters: Incomplete | None = None): ...
    def create_network(
        self,
        name,
        driver: Incomplete | None = None,
        options: Incomplete | None = None,
        ipam: Incomplete | None = None,
        check_duplicate: Incomplete | None = None,
        internal: bool = False,
        labels: Incomplete | None = None,
        enable_ipv6: bool = False,
        attachable: Incomplete | None = None,
        scope: Incomplete | None = None,
        ingress: Incomplete | None = None,
    ): ...
    def prune_networks(self, filters: Incomplete | None = None): ...
    def remove_network(self, net_id: _Network) -> None: ...
    def inspect_network(self, net_id: _Network, verbose: Incomplete | None = None, scope: Incomplete | None = None): ...
    def connect_container_to_network(
        self,
        container: _Container,
        net_id: str,
        ipv4_address: Incomplete | None = None,
        ipv6_address: Incomplete | None = None,
        aliases: Incomplete | None = None,
        links: Incomplete | None = None,
        link_local_ips: Incomplete | None = None,
        driver_opt: Incomplete | None = None,
        mac_address: Incomplete | None = None,
    ) -> None: ...
    def disconnect_container_from_network(self, container: _Container, net_id: str, force: bool = False) -> None: ...
