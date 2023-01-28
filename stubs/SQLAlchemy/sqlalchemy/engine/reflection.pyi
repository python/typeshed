from _typeshed import Incomplete

def cache(fn, self, con, *args, **kw): ...

class Inspector:
    def __init__(self, bind): ...
    @classmethod
    def from_engine(cls, bind): ...
    @property
    def default_schema_name(self): ...
    def get_schema_names(self): ...
    def get_table_names(self, schema: Incomplete | None = ...): ...
    def has_table(self, table_name, schema: Incomplete | None = ...) -> bool: ...
    def has_sequence(self, sequence_name, schema: Incomplete | None = ...) -> bool: ...
    def get_sorted_table_and_fkc_names(self, schema: Incomplete | None = ...): ...
    def get_temp_table_names(self): ...
    def get_temp_view_names(self): ...
    def get_table_options(self, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_view_names(self, schema: Incomplete | None = ...): ...
    def get_sequence_names(self, schema: Incomplete | None = ...): ...
    def get_view_definition(self, view_name, schema: Incomplete | None = ...): ...
    def get_columns(self, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_pk_constraint(self, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_foreign_keys(self, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_indexes(self, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_unique_constraints(self, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_table_comment(self, table_name, schema: Incomplete | None = ..., **kw): ...
    def get_check_constraints(self, table_name, schema: Incomplete | None = ..., **kw): ...
    def reflecttable(self, *args, **kwargs): ...
    def reflect_table(
        self, table, include_columns, exclude_columns=..., resolve_fks: bool = ..., _extend_on: Incomplete | None = ...
    ) -> None: ...
