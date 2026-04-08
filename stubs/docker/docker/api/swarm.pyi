import logging
from typing import Any, Literal, TypedDict, type_check_only
from typing_extensions import TypeAlias

from docker.types.swarm import SwarmExternalCA, SwarmSpec

log: logging.Logger

@type_check_only
class _HasId(TypedDict):
    Id: str

@type_check_only
class _HasID(TypedDict):
    ID: str

_Node: TypeAlias = _HasId | _HasID | str

@type_check_only
class _NodeSpec(TypedDict, total=False):
    Name: str
    Labels: dict[str, str]
    Role: Literal["worker", "manager"]
    Availability: Literal["active", "pause", "drain"]

@type_check_only
class _UnlockKeyResponse(TypedDict):
    UnlockKey: str

class SwarmApiMixin:
    def create_swarm_spec(
        self,
        *args: Any,  # Any: forwarded to SwarmSpec.__init__
        external_ca: SwarmExternalCA | None = None,
        **kwargs: Any,  # Any: forwarded to SwarmSpec.__init__
    ) -> SwarmSpec: ...
    def get_unlock_key(self) -> _UnlockKeyResponse: ...
    def init_swarm(
        self,
        advertise_addr: str | None = None,
        listen_addr: str = "0.0.0.0:2377",
        force_new_cluster: bool = False,
        swarm_spec: dict[str, Any] | None = None,  # Any: arbitrary SwarmSpec configuration body
        default_addr_pool: list[str] | None = None,
        subnet_size: int | None = None,
        data_path_addr: str | None = None,
        data_path_port: int | None = None,
    ) -> str: ...
    def inspect_swarm(self) -> dict[str, Any]: ...  # Any: deeply nested ClusterInfo + JoinTokens
    def inspect_node(self, node_id: _Node) -> dict[str, Any]: ...  # Any: deeply nested Node object
    def join_swarm(
        self,
        remote_addrs: list[str],
        join_token: str,
        listen_addr: str = "0.0.0.0:2377",
        advertise_addr: str | None = None,
        data_path_addr: str | None = None,
    ) -> Literal[True]: ...
    def leave_swarm(self, force: bool = False) -> Literal[True]: ...
    def nodes(self, filters: dict[str, Any] | None = None) -> list[dict[str, Any]]: ...  # Any: filter values + Node response
    def remove_node(self, node_id: _Node, force: bool = False) -> Literal[True]: ...
    def unlock_swarm(self, key: str | _UnlockKeyResponse) -> Literal[True]: ...
    def update_node(self, node_id: _Node, version: int, node_spec: _NodeSpec | None = None) -> Literal[True]: ...
    def update_swarm(
        self,
        version: int,
        swarm_spec: dict[str, Any] | None = None,  # Any: arbitrary SwarmSpec configuration body
        rotate_worker_token: bool = False,
        rotate_manager_token: bool = False,
        rotate_manager_unlock_key: bool = False,
    ) -> Literal[True]: ...
