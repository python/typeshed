from _typeshed import Incomplete
from typing_extensions import Final

class ScriptLanguage:
    FLUX: Final = "flux"
    SQL: Final = "sql"
    INFLUXQL: Final = "influxql"

    openapi_types: dict[Incomplete, Incomplete]
    attribute_map: dict[Incomplete, Incomplete]
    def to_dict(self) -> dict[Incomplete, Incomplete]: ...
    def to_str(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
