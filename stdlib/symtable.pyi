import sys
from builtins import dict_keys
from collections.abc import Sequence
from typing import Any
from typing_extensions import deprecated

__all__ = ["symtable", "SymbolTable", "Class", "Function", "Symbol"]

if sys.version_info >= (3, 13):
    __all__ += ["SymbolTableType"]

def symtable(code: str, filename: str, compile_type: str) -> SymbolTable: ...

if sys.version_info >= (3, 13):
    from enum import StrEnum

    class SymbolTableType(StrEnum):
        MODULE = "module"
        FUNCTION = "function"
        CLASS = "class"
        ANNOTATION = "annotation"
        TYPE_ALIAS = "type alias"
        TYPE_PARAMETERS = "type parameters"
        TYPE_VARIABLE = "type variable"

class SymbolTable:
    def __init__(self, raw_table: Any, filename: str) -> None: ...
    if sys.version_info >= (3, 13):
        def get_type(self) -> SymbolTableType: ...
    else:
        def get_type(self) -> str: ...

    def get_id(self) -> int: ...
    def get_name(self) -> str: ...
    def get_lineno(self) -> int: ...
    def is_optimized(self) -> bool: ...
    def is_nested(self) -> bool: ...
    def has_children(self) -> bool: ...
    if sys.version_info < (3, 9):
        def has_exec(self) -> bool: ...

    def get_identifiers(self) -> dict_keys[str, int]: ...
    def lookup(self, name: str) -> Symbol: ...
    def get_symbols(self) -> list[Symbol]: ...
    def get_children(self) -> list[SymbolTable]: ...

class Function(SymbolTable):
    def get_parameters(self) -> tuple[str, ...]: ...
    def get_locals(self) -> tuple[str, ...]: ...
    def get_globals(self) -> tuple[str, ...]: ...
    def get_frees(self) -> tuple[str, ...]: ...
    def get_nonlocals(self) -> tuple[str, ...]: ...

class Class(SymbolTable):
    if sys.version_info < (3, 16):
        @deprecated("deprecated in Python 3.14, will be removed in Python 3.16")
        def get_methods(self) -> tuple[str, ...]: ...

class Symbol:
    def __init__(
        self, name: str, flags: int, namespaces: Sequence[SymbolTable] | None = None, *, module_scope: bool = False
    ) -> None: ...
    def is_nonlocal(self) -> bool: ...
    def get_name(self) -> str: ...
    def is_referenced(self) -> bool: ...
    def is_parameter(self) -> bool: ...
    if sys.version_info >= (3, 14):
        def is_type_parameter(self) -> bool: ...

    def is_global(self) -> bool: ...
    def is_declared_global(self) -> bool: ...
    def is_local(self) -> bool: ...
    def is_annotated(self) -> bool: ...
    def is_free(self) -> bool: ...
    if sys.version_info >= (3, 14):
        def is_free_class(self) -> bool: ...

    def is_imported(self) -> bool: ...
    def is_assigned(self) -> bool: ...
    if sys.version_info >= (3, 14):
        def is_comp_iter(self) -> bool: ...
        def is_comp_cell(self) -> bool: ...

    def is_namespace(self) -> bool: ...
    def get_namespaces(self) -> Sequence[SymbolTable]: ...
    def get_namespace(self) -> SymbolTable: ...

class SymbolTableFactory:
    def new(self, table: Any, filename: str) -> SymbolTable: ...
    def __call__(self, table: Any, filename: str) -> SymbolTable: ...
