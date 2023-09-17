from pandas import DataFrame
from seaborn._core.typing import DataSource, VariableSpec

class PlotData:
    frame: DataFrame
    frames: dict[tuple[str, str], DataFrame]
    names: dict[str, str | None]
    ids: dict[str, str | int]
    source_data: DataSource
    source_vars: dict[str, VariableSpec]
    def __init__(self, data: DataSource, variables: dict[str, VariableSpec]) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def join(self, data: DataSource, variables: dict[str, VariableSpec] | None) -> PlotData: ...
