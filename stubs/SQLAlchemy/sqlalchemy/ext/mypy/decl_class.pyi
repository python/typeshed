# mypy_test can't find mypy import
from mypy.plugin import SemanticAnalyzerPluginInterface  # type: ignore[import]

from . import util

def scan_declarative_assignments_and_apply_types(
    cls, api: SemanticAnalyzerPluginInterface, is_mixin_scan: bool = ...
) -> list[util.SQLAlchemyAttribute] | None: ...
