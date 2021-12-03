from jsonschema.exceptions import UndefinedTypeCheck as UndefinedTypeCheck
from typing import Any

def is_array(checker, instance): ...
def is_bool(checker, instance): ...
def is_integer(checker, instance): ...
def is_null(checker, instance): ...
def is_number(checker, instance): ...
def is_object(checker, instance): ...
def is_string(checker, instance): ...
def is_any(checker, instance): ...

class TypeChecker:
    def is_type(self, instance, type): ...
    def redefine(self, type, fn): ...
    def redefine_many(self, definitions=...): ...
    def remove(self, *types): ...

draft3_type_checker: Any
draft4_type_checker: Any
draft6_type_checker: Any
draft7_type_checker: Any
draft201909_type_checker: Any
draft202012_type_checker: Any
