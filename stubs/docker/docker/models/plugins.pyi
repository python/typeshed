from _typeshed import Incomplete
from collections.abc import Generator

from .resource import Collection, Model

class Plugin(Model):
    @property
    def name(self): ...
    @property
    def enabled(self): ...
    @property
    def settings(self): ...
    def configure(self, options) -> None: ...
    def disable(self, force: bool = False) -> None: ...
    def enable(self, timeout: int = 0) -> None: ...
    def push(self): ...
    def remove(self, force: bool = False): ...
    def upgrade(self, remote: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...

class PluginCollection(Collection):
    model = Plugin
    def create(self, name, plugin_data_dir, gzip: bool = False): ...  # type:ignore[override]
    def get(self, name): ...
    def install(self, remote_name, local_name: Incomplete | None = None): ...
    def list(self): ...
