from collections.abc import Generator
from typing import Any

class CryptPolicy:
    @classmethod
    def from_path(cls, path, section: str = ..., encoding: str = ...): ...
    @classmethod
    def from_string(cls, source, section: str = ..., encoding: str = ...): ...
    @classmethod
    def from_source(cls, source, _warn: bool = ...): ...
    @classmethod
    def from_sources(cls, sources, _warn: bool = ...): ...
    def replace(self, *args, **kwds): ...
    def __init__(self, *args, **kwds) -> None: ...
    def has_schemes(self): ...
    def iter_handlers(self): ...
    def schemes(self, resolve: bool = ...): ...
    def get_handler(self, name: Any | None = ..., category: Any | None = ..., required: bool = ...): ...
    def get_min_verify_time(self, category: Any | None = ...): ...
    def get_options(self, name, category: Any | None = ...): ...
    def handler_is_deprecated(self, name, category: Any | None = ...): ...
    def iter_config(self, ini: bool = ..., resolve: bool = ...): ...
    def to_dict(self, resolve: bool = ...): ...
    def to_file(self, stream, section: str = ...) -> None: ...
    def to_string(self, section: str = ..., encoding: Any | None = ...): ...

class _CryptConfig:
    handlers: Any
    schemes: Any
    categories: Any
    context_kwds: Any
    def __init__(self, source) -> None: ...
    def get_context_optionmap(self, key, _default=...): ...
    def get_context_option_with_flag(self, category, key): ...
    def get_base_handler(self, scheme): ...
    @staticmethod
    def expand_settings(handler): ...
    def get_scheme_options_with_flag(self, scheme, category): ...
    def default_scheme(self, category): ...
    def is_deprecated_with_flag(self, scheme, category): ...
    def get_record(self, scheme, category): ...
    def identify_record(self, hash, category, required: bool = ...): ...
    def disabled_record(self): ...
    def iter_config(self, resolve: bool = ...) -> Generator[Any, None, None]: ...

class CryptContext:
    @classmethod
    def from_string(cls, source, section: str = ..., encoding: str = ...): ...
    @classmethod
    def from_path(cls, path, section: str = ..., encoding: str = ...): ...
    def copy(self, **kwds): ...
    def using(self, **kwds): ...
    def replace(self, **kwds): ...
    def __init__(self, schemes: Any | None = ..., policy=..., _autoload: bool = ..., **kwds) -> None: ...
    policy: Any
    def load_path(self, path, update: bool = ..., section: str = ..., encoding: str = ...): ...
    def load(self, source, update: bool = ..., section: str = ..., encoding: str = ...) -> None: ...
    def update(self, *args, **kwds) -> None: ...
    def schemes(self, resolve: bool = ..., category: Any | None = ..., unconfigured: bool = ...): ...
    def default_scheme(self, category: Any | None = ..., resolve: bool = ..., unconfigured: bool = ...): ...
    def handler(self, scheme: Any | None = ..., category: Any | None = ..., unconfigured: bool = ...): ...
    @property
    def context_kwds(self): ...
    def to_dict(self, resolve: bool = ...): ...
    def to_string(self, section: str = ...): ...
    mvt_estimate_max_samples: int
    mvt_estimate_min_samples: int
    mvt_estimate_max_time: int
    mvt_estimate_resolution: float
    harden_verify: Any
    min_verify_time: int
    def reset_min_verify_time(self) -> None: ...
    def needs_update(self, hash, scheme: Any | None = ..., category: Any | None = ..., secret: Any | None = ...): ...
    def hash_needs_update(self, hash, scheme: Any | None = ..., category: Any | None = ...): ...
    def genconfig(self, scheme: Any | None = ..., category: Any | None = ..., **settings): ...
    def genhash(self, secret, config, scheme: Any | None = ..., category: Any | None = ..., **kwds): ...
    def identify(self, hash, category: Any | None = ..., resolve: bool = ..., required: bool = ..., unconfigured: bool = ...): ...
    def hash(self, secret, scheme: Any | None = ..., category: Any | None = ..., **kwds): ...
    def encrypt(self, *args, **kwds): ...
    def verify(self, secret, hash, scheme: Any | None = ..., category: Any | None = ..., **kwds): ...
    def verify_and_update(self, secret, hash, scheme: Any | None = ..., category: Any | None = ..., **kwds): ...
    def dummy_verify(self, elapsed: int = ...): ...
    def is_enabled(self, hash): ...
    def disable(self, hash: Any | None = ...): ...
    def enable(self, hash): ...

class LazyCryptContext(CryptContext):
    def __init__(self, schemes: Any | None = ..., **kwds) -> None: ...
    def __getattribute__(self, attr): ...
