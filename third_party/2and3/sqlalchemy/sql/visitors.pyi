# Stubs for sqlalchemy.sql.visitors (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class VisitableType(type):
    def __init__(cls, clsname, bases, clsdict) -> None: ...

class Visitable: ...

class ClauseVisitor:
    __traverse_options__ = ... # type: Any
    def traverse_single(self, obj, **kw): ...
    def iterate(self, obj): ...
    def traverse(self, obj): ...
    def chain(self, visitor): ...

class CloningVisitor(ClauseVisitor):
    def copy_and_process(self, list_): ...
    def traverse(self, obj): ...

class ReplacingCloningVisitor(CloningVisitor):
    def replace(self, elem): ...
    def traverse(self, obj): ...

def iterate(obj, opts): ...
def iterate_depthfirst(obj, opts): ...
def traverse_using(iterator, obj, visitors): ...
def traverse(obj, opts, visitors): ...
def traverse_depthfirst(obj, opts, visitors): ...
def cloned_traverse(obj, opts, visitors): ...
def replacement_traverse(obj, opts, replace): ...
