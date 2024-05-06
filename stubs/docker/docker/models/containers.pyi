from _typeshed import Incomplete
from typing import NamedTuple

from .resource import Collection, Model

class Container(Model):
    @property
    def name(self): ...
    @property
    def image(self): ...
    @property
    def labels(self): ...
    @property
    def status(self): ...
    @property
    def health(self): ...
    @property
    def ports(self): ...
    def attach(self, **kwargs): ...
    def attach_socket(self, **kwargs): ...
    def commit(self, repository: str | None = None, tag: str | None = None, **kwargs): ...
    def diff(self): ...
    def exec_run(
        self,
        cmd,
        stdout: bool = True,
        stderr: bool = True,
        stdin: bool = False,
        tty: bool = False,
        privileged: bool = False,
        user: str = "",
        detach: bool = False,
        stream: bool = False,
        socket: bool = False,
        environment: Incomplete | None = None,
        workdir: Incomplete | None = None,
        demux: bool = False,
    ): ...
    def export(self, chunk_size=2097152): ...
    def get_archive(self, path, chunk_size=2097152, encode_stream: bool = False): ...
    def kill(self, signal: Incomplete | None = None): ...
    def logs(self, **kwargs): ...
    def pause(self): ...
    def put_archive(self, path, data): ...
    def remove(self, **kwargs) -> None: ...
    def rename(self, name): ...
    def resize(self, height, width): ...
    def restart(self, **kwargs): ...
    def start(self, **kwargs): ...
    def stats(self, **kwargs): ...
    def stop(self, **kwargs): ...
    def top(self, **kwargs): ...
    def unpause(self): ...
    def update(self, **kwargs): ...
    def wait(self, **kwargs): ...

class ContainerCollection(Collection[Container]):
    model: type[Container]
    def run(
        self, image, command: Incomplete | None = None, stdout: bool = True, stderr: bool = False, remove: bool = False, **kwargs
    ): ...
    def create(self, image, command: Incomplete | None = None, **kwargs): ...  # type:ignore[override]
    def get(self, container_id): ...
    def list(
        self,
        all: bool = False,
        before: Incomplete | None = None,
        filters: Incomplete | None = None,
        limit: int = -1,
        since: Incomplete | None = None,
        sparse: bool = False,
        ignore_removed: bool = False,
    ): ...
    def prune(self, filters: Incomplete | None = None): ...

RUN_CREATE_KWARGS: Incomplete
RUN_HOST_CONFIG_KWARGS: Incomplete

class ExecResult(NamedTuple):
    exit_code: Incomplete
    output: Incomplete
