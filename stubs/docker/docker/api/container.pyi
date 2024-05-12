import datetime
from _typeshed import Incomplete
from typing import Literal, TypedDict, overload, type_check_only
from typing_extensions import TypeAlias

from docker.types.daemon import CancellableStream

@type_check_only
class _HasId(TypedDict):
    Id: str

@type_check_only
class _HasID(TypedDict):
    ID: str

_Container: TypeAlias = _HasId | _HasID | str

class ContainerApiMixin:
    def attach(
        self,
        container: _Container,
        stdout: bool = True,
        stderr: bool = True,
        stream: bool = False,
        logs: bool = False,
        demux: bool = False,
    ): ...
    def attach_socket(self, container: _Container, params: Incomplete | None = None, ws: bool = False): ...
    def commit(
        self,
        container: _Container,
        repository: str | None = None,
        tag: str | None = None,
        message: Incomplete | None = None,
        author: Incomplete | None = None,
        pause: bool = True,
        changes: Incomplete | None = None,
        conf: Incomplete | None = None,
    ): ...
    def containers(
        self,
        quiet: bool = False,
        all: bool = False,
        trunc: bool = False,
        latest: bool = False,
        since: Incomplete | None = None,
        before: Incomplete | None = None,
        limit: int = -1,
        size: bool = False,
        filters: Incomplete | None = None,
    ): ...
    def create_container(
        self,
        image,
        command: Incomplete | None = None,
        hostname: Incomplete | None = None,
        user: Incomplete | None = None,
        detach: bool = False,
        stdin_open: bool = False,
        tty: bool = False,
        ports: Incomplete | None = None,
        environment: Incomplete | None = None,
        volumes: Incomplete | None = None,
        network_disabled: bool = False,
        name: Incomplete | None = None,
        entrypoint: Incomplete | None = None,
        working_dir: Incomplete | None = None,
        domainname: Incomplete | None = None,
        host_config: Incomplete | None = None,
        mac_address: Incomplete | None = None,
        labels: Incomplete | None = None,
        stop_signal: Incomplete | None = None,
        networking_config: Incomplete | None = None,
        healthcheck: Incomplete | None = None,
        stop_timeout: Incomplete | None = None,
        runtime: Incomplete | None = None,
        use_config_proxy: bool = True,
        platform: Incomplete | None = None,
    ): ...
    def create_container_config(self, *args, **kwargs): ...
    def create_container_from_config(self, config, name: Incomplete | None = None, platform: Incomplete | None = None): ...
    def create_host_config(self, *args, **kwargs): ...
    def create_networking_config(self, *args, **kwargs): ...
    def create_endpoint_config(self, *args, **kwargs): ...
    def diff(self, container: _Container): ...
    def export(self, container: _Container, chunk_size=2097152): ...
    def get_archive(self, container: _Container, path, chunk_size=2097152, encode_stream: bool = False): ...
    def inspect_container(self, container: _Container): ...
    def kill(self, container: _Container, signal: Incomplete | None = None) -> None: ...
    @overload
    def logs(
        self,
        container: _Container,
        stdout: bool = True,
        stderr: bool = True,
        *,
        stream: Literal[True],
        timestamps: bool = False,
        tail: Literal["all"] | int = "all",
        since: datetime.datetime | float | None = None,
        follow: bool | None = None,
        until: datetime.datetime | float | None = None,
    ) -> CancellableStream: ...
    @overload
    def logs(
        self,
        container: _Container,
        stdout: bool,
        stderr: bool,
        stream: Literal[True],
        timestamps: bool = False,
        tail: Literal["all"] | int = "all",
        since: datetime.datetime | float | None = None,
        follow: bool | None = None,
        until: datetime.datetime | float | None = None,
    ) -> CancellableStream: ...
    @overload
    def logs(
        self,
        container: _Container,
        stdout: bool = True,
        stderr: bool = True,
        stream: Literal[False] = False,
        timestamps: bool = False,
        tail: Literal["all"] | int = "all",
        since: datetime.datetime | float | None = None,
        follow: bool | None = None,
        until: datetime.datetime | float | None = None,
    ) -> bytes: ...
    def pause(self, container: _Container) -> None: ...
    def port(self, container: _Container, private_port): ...
    def put_archive(self, container: _Container, path, data): ...
    def prune_containers(self, filters: Incomplete | None = None): ...
    def remove_container(self, container: _Container, v: bool = False, link: bool = False, force: bool = False) -> None: ...
    def rename(self, container: _Container, name) -> None: ...
    def resize(self, container: _Container, height, width) -> None: ...
    def restart(self, container: _Container, timeout: int = 10) -> None: ...
    def start(self, container: _Container, *args, **kwargs) -> None: ...
    def stats(
        self, container: _Container, decode: Incomplete | None = None, stream: bool = True, one_shot: Incomplete | None = None
    ): ...
    def stop(self, container: _Container, timeout: Incomplete | None = None) -> None: ...
    def top(self, container: _Container, ps_args: Incomplete | None = None): ...
    def unpause(self, container: _Container) -> None: ...
    def update_container(
        self,
        container: _Container,
        blkio_weight: Incomplete | None = None,
        cpu_period: Incomplete | None = None,
        cpu_quota: Incomplete | None = None,
        cpu_shares: Incomplete | None = None,
        cpuset_cpus: Incomplete | None = None,
        cpuset_mems: Incomplete | None = None,
        mem_limit: Incomplete | None = None,
        mem_reservation: Incomplete | None = None,
        memswap_limit: Incomplete | None = None,
        kernel_memory: Incomplete | None = None,
        restart_policy: Incomplete | None = None,
    ): ...
    def wait(self, container: _Container, timeout: Incomplete | None = None, condition: Incomplete | None = None): ...
