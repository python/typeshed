from _typeshed import Incomplete

logger: Incomplete

def retrieve_default(
    region: str | None = None,
    model_id: str | None = None,
    model_version: str | None = None,
    tolerate_vulnerable_model: bool = False,
    tolerate_deprecated_model: bool = False,
) -> list[dict[str, str]] | None: ...
