from . import base_dir as base_dir, get_canonical_version as get_canonical_version, list_dir as list_dir, short_versions as short_versions
from _typeshed import Incomplete

class DummyConfig:
    intersphinx_mapping: Incomplete
    intersphinx_cache_limit: Incomplete
    intersphinx_timeout: Incomplete
    user_agent: str
    tls_verify: bool
    def __init__(self, intersphinx_mapping: Incomplete | None = ..., intersphinx_cache_limit: int = ..., intersphinx_timeout: Incomplete | None = ...) -> None: ...

class DummyApp:
    srcdir: Incomplete
    warn: Incomplete
    config: Incomplete
    def __init__(self) -> None: ...
    def info(self, msg) -> None: ...

def fetch_list(version: Incomplete | None = ...) -> None: ...
