from mypy.plugin import SemanticAnalyzerPluginInterface

from . import util

def scan_declarative_assignments_and_apply_types(
    cls, api: SemanticAnalyzerPluginInterface, is_mixin_scan: bool = ...
) -> list[util.SQLAlchemyAttribute] | None: ...
