from typing import Any

from ldap.schema.models import *

SCHEMA_CLASS_MAPPING: Any  # TODO: Precise type
SCHEMA_ATTR_MAPPING: Any  # TODO: Precise type
SCHEMA_ATTRS: Any  # TODO: Precise type

class SubschemaError(ValueError): ...

class OIDNotUnique(SubschemaError):
    desc: Any  # TODO: Precise type
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class NameNotUnique(SubschemaError):
    desc: Any  # TODO: Precise type
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class SubSchema:
    name2oid: Any  # TODO: Precise type
    sed: Any  # TODO: Precise type
    non_unique_oids: Any  # TODO: Precise type
    non_unique_names: Any  # TODO: Precise type
    def __init__(self, sub_schema_sub_entry, check_uniqueness: int = 1) -> None: ...
    def ldap_entry(self): ...
    def listall(
        self, schema_element_class, schema_element_filters: Any | None = None
    ): ...  # TODO: Precise type for schema_element_filters
    def tree(
        self, schema_element_class, schema_element_filters: Any | None = None
    ): ...  # TODO: Precise type for schema_element_filters
    def getoid(self, se_class, nameoroid, raise_keyerror: int = 0): ...
    def get_inheritedattr(self, se_class, nameoroid, name): ...
    def get_obj(
        self, se_class, nameoroid, default: Any | None = None, raise_keyerror: int = 0
    ): ...  # TODO: Precise type for default
    def get_inheritedobj(self, se_class, nameoroid, inherited: Any | None = None): ...  # TODO: Precise type for inherited
    def get_syntax(self, nameoroid): ...
    def get_structural_oc(self, oc_list): ...
    def get_applicable_aux_classes(self, nameoroid): ...
    def attribute_types(
        self, object_class_list, attr_type_filter: Any | None = None, raise_keyerror: int = 1, ignore_dit_content_rule: int = 0
    ): ...  # TODO: Precise type for attr_type_filter

def urlfetch(uri, trace_level: int = 0): ...
