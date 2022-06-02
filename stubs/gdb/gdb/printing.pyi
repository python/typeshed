from collections.abc import Callable, Iterable
from typing import Protocol

import gdb

from gdb import _PrettyPrinterLookupFunction

class PrettyPrinterProtocol(Protocol):

    name: str
    enabled: bool

    def __call__(self, val: gdb.Value): ...

class PrettyPrinter:

    name: str
    subprinters: list[SubPrettyPrinter]
    enabled: bool

    def __init__(self, name: str, subprinters: Iterable[SubPrettyPrinter] | None = ...): ...
    def __call__(self, val: gdb.Value): ...

class SubPrettyPrinter:

    name: str
    enabled: bool

    def __init__(self, name: str): ...

GenPrinterFunction = Callable[[gdb.Value], PrettyPrinter]

class RegexpCollectionPrettyPrinter(PrettyPrinter):
    def __init__(self, name: str): ...
    def add_printer(self, name: str, regexp: str, gen_printer: _PrettyPrinterLookupFunction) -> None: ...

class FlagEnumerationPrinter(PrettyPrinter):
    def __init__(self, enum_type: str): ...

def register_pretty_printer(obj: gdb.Objfile | gdb.Progspace | None, printer: PrettyPrinter, replace: bool = ...) -> None: ...
