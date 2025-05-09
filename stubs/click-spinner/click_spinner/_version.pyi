from typing import Literal

version_json: str

def get_versions() -> dict[Literal["dirty", "error", "full-revisionid", "version"], str | bool | None]: ...
