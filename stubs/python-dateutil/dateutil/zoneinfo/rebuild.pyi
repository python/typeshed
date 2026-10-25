from typing_extensions import deprecated

__all__ = ["rebuild", "RebuildDeprecationWarning"]

class RebuildDeprecationWarning(FutureWarning): ...

@deprecated("dateutil no longer ships a zoneinfo tarball; use tzdata or system time zone data instead")
def rebuild(
    filename: object, tag: object = None, format: object = "gz", zonegroups: object = [], metadata: object = None
) -> None: ...
