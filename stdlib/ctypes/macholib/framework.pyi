from typing import TypedDict

__all__ = ["framework_info"]

# Actual result is produced by re.match.groupdict()
class _FrameworkInfo(TypedDict):
    location: str
    name: str
    shortname: str
    version: str | None
    suffix: str | None

def framework_info(filename: str) -> _FrameworkInfo | None: ...
