from collections.abc import Mapping, Sequence
from typing import Final, Protocol, TypeAlias, TypeVar, overload, type_check_only
from typing_extensions import deprecated

from dateutil.tz import tzfile as tzfile

_T = TypeVar("_T")
_MetadataType: TypeAlias = bool | int | float | str | Sequence[_MetadataType] | Mapping[str, _MetadataType] | None

@type_check_only
class _ArchiveReader(Protocol):
    def read(self, size: int = -1, /) -> bytes: ...
    def seek(self, offset: int, whence: int = 0, /) -> int: ...
    def tell(self) -> int: ...

__all__ = ["get_zonefile_instance", "gettz", "gettz_db_metadata"]

ZONEFILENAME: Final[None]
METADATA_FN: Final[str]

class ZoneInfoFile:
    zones: dict[str, tzfile]
    metadata: _MetadataType | None
    def __init__(self, zonefile_stream: _ArchiveReader | None = None) -> None: ...

    @overload
    def get(self, name: str, default: None = None) -> tzfile | None: ...
    @overload
    def get(self, name: str, default: tzfile) -> tzfile: ...
    @overload
    def get(self, name: str, default: _T) -> tzfile | _T: ...

def get_zonefile_instance(new_instance: bool = False) -> ZoneInfoFile: ...
@deprecated(
    "zoneinfo.gettz() will be removed in future versions, to use the dateutil-provided "
    "zoneinfo files, instantiate a ZoneInfoFile object and use ZoneInfoFile.zones.get() instead."
)
def gettz(name: str) -> tzfile | None: ...
@deprecated(
    "zoneinfo.gettz_db_metadata() will be removed in future versions, to use the "
    "dateutil-provided zoneinfo files, ZoneInfoFile object and query the 'metadata' attribute instead."
)
def gettz_db_metadata() -> _MetadataType: ...
