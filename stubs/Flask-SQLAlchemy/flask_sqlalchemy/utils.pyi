def parse_version(v: str) -> tuple[str, ...]: ...
def sqlalchemy_version(op: str, val: str) -> bool: ...
def engine_config_warning(config, version: str, deprecated_config_key: str, engine_option) -> None: ...
