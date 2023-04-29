from _typeshed import Incomplete, Unused
from abc import abstractmethod
from collections.abc import Iterable, Mapping
from operator import attrgetter
from re import Pattern
from typing import NamedTuple, NoReturn, TypeVar
from typing_extensions import Self

from ..engine.default import DefaultDialect
from ..engine.interfaces import Dialect
from ..sql.base import prefix_anon_map
from ..util._collections import OrderedDict
from ..util.langhelpers import EnsureKWArgType, memoized_property
from .base import CompileState
from .elements import BindParameter, ClauseElement, ColumnElement, quoted_name

_Q = TypeVar("_Q", str, quoted_name)

RESERVED_WORDS: set[str]
LEGAL_CHARACTERS: Pattern[str]
LEGAL_CHARACTERS_PLUS_SPACE: Pattern[str]
ILLEGAL_INITIAL_CHARACTERS: set[str]
FK_ON_DELETE: Pattern[str]
FK_ON_UPDATE: Pattern[str]
FK_INITIALLY: Pattern[str]
BIND_PARAMS: Pattern[str]
BIND_PARAMS_ESC: Pattern[str]
BIND_TEMPLATES: dict[str, str]
OPERATORS: dict[Incomplete, str]
FUNCTIONS: dict[Incomplete, str]
EXTRACT_MAP: dict[str, str]
COMPOUND_KEYWORDS: dict[Incomplete, str]
RM_RENDERED_NAME: int
RM_NAME: int
RM_OBJECTS: int
RM_TYPE: int

class ExpandedState(NamedTuple):
    statement: Incomplete
    additional_parameters: Incomplete
    processors: Incomplete
    positiontup: Incomplete
    parameter_expansion: Incomplete

NO_LINTING: Incomplete
COLLECT_CARTESIAN_PRODUCTS: Incomplete
WARN_LINTING: Incomplete
FROM_LINTING: Incomplete

class FromLinter:
    def lint(self, start: Incomplete | None = None): ...
    def warn(self) -> None: ...

class Compiled:
    schema_translate_map: Incomplete  # Can be unbound
    execution_options: Incomplete
    compile_state: Incomplete
    dml_compile_state: CompileState | None
    cache_key: Incomplete
    dialect: DefaultDialect
    preparer: IdentifierPreparer
    statement: ClauseElement  # Can be unbound
    can_execute: bool  # Can be unbound
    string: str | None  # Can be unbound
    def __init__(
        self,
        dialect: DefaultDialect,
        statement: ClauseElement | None,
        schema_translate_map: Incomplete | None = None,
        render_schema_translate: bool = False,
        compile_kwargs: Mapping[Incomplete, Incomplete] = ...,
    ) -> None: ...
    def visit_unsupported_compilation(self, element, err) -> None: ...
    @property
    @abstractmethod
    def sql_compiler(self) -> SQLCompiler: ...
    def process(self, obj, **kwargs) -> str: ...
    @abstractmethod
    def construct_params(
        self,
        params: Mapping[str, Incomplete] | None = None,
        extracted_parameters: Incomplete | None = None,
        escape_names: bool = True,
    ) -> dict[str, Incomplete] | None: ...
    @property
    def params(self) -> dict[str, Incomplete] | None: ...

class TypeCompiler(metaclass=EnsureKWArgType):
    ensure_kwarg: str
    dialect: Dialect
    def __init__(self, dialect: Dialect) -> None: ...
    def process(self, type_, **kw): ...
    def visit_unsupported_compilation(self, element, err, **kw) -> None: ...

class _CompileLabel(ColumnElement[Incomplete]):
    __visit_name__: str
    element: Incomplete
    name: Incomplete
    def __init__(self, col, name, alt_names=()) -> None: ...
    @property
    def proxy_set(self): ...
    @property
    def type(self): ...
    def self_group(self, **kw: Unused) -> Self: ...  # type: ignore[override]  # Different params

class SQLCompiler(Compiled):
    extract_map: dict[str, str]
    compound_keywords: dict[Incomplete, str]
    isdelete: bool
    isinsert: bool
    isupdate: bool
    isplaintext: bool
    returning: tuple[Incomplete, ...] | None
    returning_precedes_values: bool
    render_table_with_column_in_update_from: bool
    ansi_bind_rules: bool
    insert_single_values_expr: Incomplete
    literal_execute_params: Incomplete
    post_compile_params: Incomplete
    escaped_bind_names: Incomplete
    has_out_parameters: bool
    insert_prefetch: tuple[Incomplete, ...]
    update_prefetch: tuple[Incomplete, ...]
    postfetch_lastrowid: bool
    positiontup: Incomplete
    positiontup_level: dict[str, int] | None
    inline: bool
    column_keys: Iterable[str] | None
    cache_key: Incomplete
    for_executemany: Incomplete
    linting: Incomplete
    binds: dict[str, BindParameter[Incomplete]]
    bind_names: dict[BindParameter[Incomplete], str]
    stack: list[dict[str, Incomplete]]
    positional: bool
    bindtemplate: str
    ctes: OrderedDict[str, Incomplete] | None
    label_length: int
    anon_map: prefix_anon_map
    truncated_names: dict[tuple[str, str] | str, str | int]
    def __init__(
        self,
        dialect: DefaultDialect,
        statement: ClauseElement,
        cache_key: Incomplete | None = None,
        column_keys: Iterable[str] | None = None,
        for_executemany: bool = False,
        linting=...,
        **kwargs,
    ) -> None: ...
    @property
    def current_executable(self): ...
    @property
    def prefetch(self) -> list[Incomplete]: ...
    def is_subquery(self) -> bool: ...
    @property
    def sql_compiler(self) -> Self: ...
    def construct_params(  # type: ignore[override]
        self,
        params: Mapping[str, Incomplete] | None = None,
        _group_number: Incomplete | None = None,
        _check: bool = True,
        extracted_parameters: Incomplete | None = None,
        escape_names: bool = True,
    ) -> dict[str, Incomplete]: ...
    @property
    def params(self) -> dict[str, Incomplete]: ...
    def default_from(self) -> str: ...
    def visit_grouping(self, grouping, asfrom: bool = False, **kwargs) -> str: ...
    def visit_select_statement_grouping(self, grouping, **kwargs) -> str: ...
    def visit_label_reference(self, element, within_columns_clause: bool = False, **kwargs) -> str: ...
    def visit_textual_label_reference(self, element, within_columns_clause: bool = False, **kwargs) -> str: ...
    def visit_label(
        self,
        label,
        add_to_result_map: Incomplete | None = None,
        within_label_clause: bool = False,
        within_columns_clause: bool = False,
        render_label_as_label: Incomplete | None = None,
        result_map_targets=(),
        **kw,
    ) -> str: ...
    def visit_lambda_element(self, element, **kw) -> str: ...
    def visit_column(
        self, column, add_to_result_map: Incomplete | None = None, include_table: bool = True, result_map_targets=(), **kwargs
    ) -> str: ...
    def visit_collation(self, element, **kw) -> str: ...
    def visit_fromclause(self, fromclause, **kwargs) -> str: ...
    def visit_index(self, index, **kwargs) -> str: ...
    def visit_typeclause(self, typeclause, **kw) -> str: ...
    def post_process_text(self, text: str) -> str: ...
    def escape_literal_column(self, text: str) -> str: ...
    def visit_textclause(self, textclause, add_to_result_map: Incomplete | None = None, **kw) -> str: ...
    def visit_textual_select(self, taf, compound_index: int | None = None, asfrom: bool = False, **kw) -> str: ...
    def visit_null(self, expr, **kw) -> str: ...
    def visit_true(self, expr, **kw) -> str: ...
    def visit_false(self, expr, **kw) -> str: ...
    def visit_tuple(self, clauselist, **kw) -> str: ...
    def visit_clauselist(self, clauselist, **kw) -> str: ...
    def visit_case(self, clause, **kwargs) -> str: ...
    def visit_type_coerce(self, type_coerce, **kw) -> str: ...
    def visit_cast(self, cast, **kwargs) -> str: ...
    def visit_over(self, over, **kwargs) -> str: ...
    def visit_withingroup(self, withingroup, **kwargs) -> str: ...
    def visit_funcfilter(self, funcfilter, **kwargs) -> str: ...
    def visit_extract(self, extract, **kwargs) -> str: ...
    def visit_scalar_function_column(self, element, **kw) -> str: ...
    def visit_function(self, func, add_to_result_map: Incomplete | None = None, **kwargs) -> str: ...
    def visit_next_value_func(self, next_value, **kw) -> str: ...
    # Is meant to be overriden, but not all instanciated subtypes declares it
    def visit_sequence(self, sequence, **kw) -> NoReturn | str: ...
    def function_argspec(self, func, **kwargs): ...
    compile_state: Incomplete
    def visit_compound_select(self, cs, asfrom: bool = False, compound_index: int | None = None, **kwargs) -> str: ...
    def visit_unary(self, unary, add_to_result_map: Incomplete | None = None, result_map_targets=(), **kw) -> str: ...
    def visit_is_true_unary_operator(self, element, operator, **kw) -> str: ...
    def visit_is_false_unary_operator(self, element, operator, **kw) -> str: ...
    def visit_not_match_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_not_in_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_empty_set_op_expr(self, type_, expand_op) -> str: ...
    # Is meant to be overriden, but not all instanciated subtypes declares it
    def visit_empty_set_expr(self, element_types) -> NoReturn | str: ...
    def visit_binary(
        self,
        binary,
        override_operator: Incomplete | None = None,
        eager_grouping: bool = False,
        from_linter: Incomplete | None = None,
        lateral_from_linter: Incomplete | None = None,
        **kw,
    ) -> str: ...
    def visit_function_as_comparison_op_binary(self, element, operator, **kw) -> str: ...
    def visit_mod_binary(self, binary, operator, **kw) -> str: ...
    def visit_custom_op_binary(self, element, operator, **kw) -> str: ...
    def visit_custom_op_unary_operator(self, element, operator, **kw) -> str: ...
    def visit_custom_op_unary_modifier(self, element, operator, **kw) -> str: ...
    def visit_contains_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_not_contains_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_startswith_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_not_startswith_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_endswith_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_not_endswith_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_like_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_not_like_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_ilike_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_not_ilike_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_between_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_not_between_op_binary(self, binary, operator, **kw) -> str: ...
    # Is meant to be overriden, but not all instanciated subtypes declares it
    def visit_regexp_match_op_binary(self, binary, operator, **kw) -> NoReturn | str: ...
    # Is meant to be overriden, but not all instanciated subtypes declares it
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw) -> NoReturn | str: ...
    # Is meant to be overriden, but not all instanciated subtypes declares it
    def visit_regexp_replace_op_binary(self, binary, operator, **kw) -> NoReturn | str: ...
    def visit_bindparam(
        self,
        bindparam,
        within_columns_clause: bool = False,
        literal_binds: bool = False,
        skip_bind_expression: bool = False,
        literal_execute: bool = False,
        render_postcompile: bool = False,
        **kwargs,
    ) -> str: ...
    def render_literal_bindparam(
        self, bindparam, render_literal_value=..., bind_expression_template: Incomplete | None = None, **kw
    ) -> str: ...
    def render_literal_value(self, value, type_) -> str: ...
    def bindparam_string(
        self,
        name,
        positional_names: Incomplete | None = None,
        post_compile: bool = False,
        expanding: bool = False,
        escaped_from: Incomplete | None = None,
        **kw,
    ) -> str: ...
    execution_options: Incomplete
    ctes_recursive: bool
    def visit_cte(
        self,
        cte,
        asfrom: bool = False,
        ashint: bool = False,
        fromhints: Incomplete | None = None,
        visiting_cte: Incomplete | None = None,
        from_linter: Incomplete | None = None,
        **kwargs,
    ) -> str: ...
    def visit_table_valued_alias(self, element, **kw) -> str: ...
    def visit_table_valued_column(self, element, **kw) -> str: ...
    def visit_alias(
        self,
        alias,
        asfrom: bool = False,
        ashint: bool = False,
        iscrud: bool = False,
        fromhints: Incomplete | None = None,
        subquery: bool = False,
        lateral: bool = False,
        enclosing_alias: Incomplete | None = None,
        from_linter: Incomplete | None = None,
        **kwargs,
    ) -> str: ...
    def visit_subquery(self, subquery, **kw) -> str: ...
    def visit_lateral(self, lateral_, **kw) -> str: ...
    def visit_tablesample(self, tablesample, asfrom: bool = False, **kw) -> str: ...
    def visit_values(self, element, asfrom: bool = False, from_linter: Incomplete | None = None, **kw) -> str: ...
    def get_render_as_alias_suffix(self, alias_name_text) -> str: ...
    def format_from_hint_text(self, sqltext, table, hint, iscrud: bool) -> str: ...
    def get_select_hint_text(self, byfroms) -> None: ...
    def get_from_hint_text(self, table, text: str) -> None: ...
    def get_crud_hint_text(self, table, text: str) -> None: ...
    def get_statement_hint_text(self, hint_texts: Iterable[str]) -> str: ...
    translate_select_structure: Incomplete
    def visit_select(
        self,
        select_stmt,
        asfrom: bool = False,
        insert_into: bool = False,
        fromhints: Incomplete | None = None,
        compound_index: int | None = None,
        select_wraps_for: Incomplete | None = None,
        lateral: bool = False,
        from_linter: Incomplete | None = None,
        **kwargs,
    ) -> str: ...
    def get_cte_preamble(self, recursive) -> str: ...
    def get_select_precolumns(self, select, **kw) -> str: ...
    def group_by_clause(self, select, **kw) -> str: ...
    def order_by_clause(self, select, **kw) -> str: ...
    def for_update_clause(self, select, **kw) -> str: ...
    # Is meant to be overriden, but not all instanciated subtypes declares it
    def returning_clause(self, stmt, returning_cols) -> NoReturn | str: ...
    def limit_clause(self, select, **kw) -> str: ...
    def fetch_clause(self, select, **kw) -> str: ...
    def visit_table(
        self,
        table,
        asfrom: bool = False,
        iscrud: bool = False,
        ashint: bool = False,
        fromhints: Incomplete | None = None,
        use_schema: bool = True,
        from_linter: Incomplete | None = None,
        **kwargs,
    ) -> str: ...
    def visit_join(self, join, asfrom: bool = False, from_linter: Incomplete | None = None, **kwargs) -> str: ...
    def visit_insert(self, insert_stmt, **kw) -> str: ...
    def update_limit_clause(self, update_stmt) -> None: ...
    def update_tables_clause(self, update_stmt, from_table, extra_froms, **kw) -> str: ...
    # Is meant to be overriden, but not all instanciated subtypes declares it
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw) -> NoReturn | str | None: ...
    def visit_update(self, update_stmt, **kw) -> str: ...
    # Is meant to be overriden, but not all instanciated subtypes declares it
    def delete_extra_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw) -> NoReturn | str: ...
    def delete_table_clause(self, delete_stmt, from_table, extra_froms) -> str: ...
    def visit_delete(self, delete_stmt, **kw) -> str: ...
    def visit_savepoint(self, savepoint_stmt) -> str: ...
    def visit_rollback_to_savepoint(self, savepoint_stmt) -> str: ...
    def visit_release_savepoint(self, savepoint_stmt) -> str: ...

class StrSQLCompiler(SQLCompiler):
    def visit_unsupported_compilation(self, element, err, **kw) -> str: ...  # type: ignore[override]  # Extra **kw parameter
    def visit_getitem_binary(self, binary, operator, **kw) -> str: ...
    def visit_json_getitem_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_json_path_getitem_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_sequence(self, seq, **kw) -> str: ...  # type: ignore[override]  # Different parameter name
    def returning_clause(self, stmt, returning_cols) -> str: ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw) -> str: ...
    def delete_extra_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw) -> str: ...
    def visit_empty_set_expr(self, type_) -> str: ...
    def get_from_hint_text(self, table, text: str): ...
    def visit_regexp_match_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_not_regexp_match_op_binary(self, binary, operator, **kw) -> str: ...
    def visit_regexp_replace_op_binary(self, binary, operator, **kw) -> str: ...

class DDLCompiler(Compiled):
    @memoized_property
    def sql_compiler(self) -> SQLCompiler: ...  # type: ignore[override]  # property vs memoized_property
    @memoized_property
    def type_compiler(self) -> type[TypeCompiler]: ...
    def construct_params(
        self, params: Incomplete | None = None, extracted_parameters: Incomplete | None = None, escape_names: bool = True
    ) -> None: ...
    def visit_ddl(self, ddl, **kwargs) -> str: ...
    def visit_create_schema(self, create, **kw) -> str: ...
    def visit_drop_schema(self, drop, **kw) -> str: ...
    def visit_create_table(self, create, **kw) -> str: ...
    def visit_create_column(self, create, first_pk: bool = False, **kw) -> str: ...
    def create_table_constraints(self, table, _include_foreign_key_constraints: Incomplete | None = None, **kw) -> str: ...
    def visit_drop_table(self, drop, **kw) -> str: ...
    def visit_drop_view(self, drop, **kw) -> str: ...
    def visit_create_index(self, create, include_schema: bool = False, include_table_schema: bool = True, **kw) -> str: ...
    def visit_drop_index(self, drop, **kw) -> str: ...
    def visit_add_constraint(self, create, **kw) -> str: ...
    def visit_set_table_comment(self, create, **kw) -> str: ...
    def visit_drop_table_comment(self, drop, **kw) -> str: ...
    def visit_set_column_comment(self, create, **kw) -> str: ...
    def visit_drop_column_comment(self, drop, **kw) -> str: ...
    def get_identity_options(self, identity_options): ...
    def visit_create_sequence(self, create, prefix: Incomplete | None = None, **kw) -> str: ...
    def visit_drop_sequence(self, drop, **kw) -> str: ...
    def visit_drop_constraint(self, drop, **kw) -> str: ...
    def get_column_specification(self, column, **kwargs) -> str: ...
    def create_table_suffix(self, table) -> str: ...
    def post_create_table(self, table) -> str: ...
    def get_column_default_string(self, column) -> str | None: ...
    def visit_table_or_column_check_constraint(self, constraint, **kw) -> str: ...
    def visit_check_constraint(self, constraint, **kw) -> str: ...
    def visit_column_check_constraint(self, constraint, **kw) -> str: ...
    def visit_primary_key_constraint(self, constraint, **kw) -> str: ...
    def visit_foreign_key_constraint(self, constraint, **kw) -> str: ...
    def define_constraint_remote_table(self, constraint, table, preparer) -> str: ...
    def visit_unique_constraint(self, constraint, **kw) -> str: ...
    def define_constraint_cascades(self, constraint) -> str: ...
    def define_constraint_deferrability(self, constraint) -> str: ...
    def define_constraint_match(self, constraint) -> str: ...
    def visit_computed_column(self, generated, **kw) -> str: ...
    def visit_identity_column(self, identity, **kw) -> str: ...

class GenericTypeCompiler(TypeCompiler):
    def visit_FLOAT(self, type_, **kw) -> str: ...
    def visit_REAL(self, type_, **kw) -> str: ...
    def visit_NUMERIC(self, type_, **kw) -> str: ...
    def visit_DECIMAL(self, type_, **kw) -> str: ...
    def visit_INTEGER(self, type_, **kw) -> str: ...
    def visit_SMALLINT(self, type_, **kw) -> str: ...
    def visit_BIGINT(self, type_, **kw) -> str: ...
    def visit_TIMESTAMP(self, type_, **kw) -> str: ...
    def visit_DATETIME(self, type_, **kw) -> str: ...
    def visit_DATE(self, type_, **kw) -> str: ...
    def visit_TIME(self, type_, **kw) -> str: ...
    def visit_CLOB(self, type_, **kw) -> str: ...
    def visit_NCLOB(self, type_, **kw) -> str: ...
    def visit_CHAR(self, type_, **kw) -> str: ...
    def visit_NCHAR(self, type_, **kw) -> str: ...
    def visit_VARCHAR(self, type_, **kw) -> str: ...
    def visit_NVARCHAR(self, type_, **kw) -> str: ...
    def visit_TEXT(self, type_, **kw) -> str: ...
    def visit_BLOB(self, type_, **kw) -> str: ...
    def visit_BINARY(self, type_, **kw) -> str: ...
    def visit_VARBINARY(self, type_, **kw) -> str: ...
    def visit_BOOLEAN(self, type_, **kw) -> str: ...
    def visit_large_binary(self, type_, **kw) -> str: ...
    def visit_boolean(self, type_, **kw) -> str: ...
    def visit_time(self, type_, **kw) -> str: ...
    def visit_datetime(self, type_, **kw) -> str: ...
    def visit_date(self, type_, **kw) -> str: ...
    def visit_big_integer(self, type_, **kw) -> str: ...
    def visit_small_integer(self, type_, **kw) -> str: ...
    def visit_integer(self, type_, **kw) -> str: ...
    def visit_real(self, type_, **kw) -> str: ...
    def visit_float(self, type_, **kw) -> str: ...
    def visit_numeric(self, type_, **kw) -> str: ...
    def visit_string(self, type_, **kw) -> str: ...
    def visit_unicode(self, type_, **kw) -> str: ...
    def visit_text(self, type_, **kw) -> str: ...
    def visit_unicode_text(self, type_, **kw) -> str: ...
    def visit_enum(self, type_, **kw) -> str: ...
    # Is meant to be overriden
    def visit_null(self, type_, **kw) -> NoReturn | str: ...
    def visit_type_decorator(self, type_, **kw) -> str: ...
    def visit_user_defined(self, type_, **kw) -> str: ...

class StrSQLTypeCompiler(GenericTypeCompiler):
    def process(self, type_, **kw): ...
    def __getattr__(self, key: str): ...
    def visit_null(self, type_, **kw) -> str: ...
    def visit_user_defined(self, type_, **kw) -> str: ...

class IdentifierPreparer:
    reserved_words: set[str]
    legal_characters: Pattern[str]
    illegal_initial_characters: set[str]
    schema_for_object: attrgetter[Incomplete]
    dialect: Dialect
    initial_quote: str
    final_quote: str
    escape_quote: str
    escape_to_quote: str
    omit_schema: bool
    quote_case_sensitive_collations: bool
    def __init__(
        self,
        dialect,
        initial_quote: str = '"',
        final_quote: str | None = None,
        escape_quote: str = '"',
        quote_case_sensitive_collations: bool = True,
        omit_schema: bool = False,
    ) -> None: ...
    def validate_sql_phrase(self, element, reg): ...
    def quote_identifier(self, value: str) -> str: ...
    def quote_schema(self, schema: quoted_name, force: None = None) -> str: ...
    def quote(self, ident, force: None = None) -> str: ...
    def format_collation(self, collation_name: _Q) -> _Q: ...
    def format_sequence(self, sequence, use_schema: bool = True) -> str: ...
    def format_label(self, label, name: str | None = None) -> str: ...
    def format_alias(self, alias, name: str | None = None) -> str: ...
    def format_savepoint(self, savepoint, name: str | None = None) -> str: ...
    def format_constraint(self, constraint, _alembic_quote: bool = True) -> str: ...
    def truncate_and_render_index_name(self, name: str, _alembic_quote: bool = True) -> str: ...
    def truncate_and_render_constraint_name(self, name: str, _alembic_quote: bool = True) -> str: ...
    def format_index(self, index) -> str: ...
    def format_table(self, table, use_schema: bool = True, name: str | None = None) -> str: ...
    def format_schema(self, name: str) -> str: ...
    def format_label_name(self, name: str, anon_map: Incomplete | None = None) -> str: ...
    def format_column(
        self,
        column,
        use_table: bool = False,
        name: str | None = None,
        table_name: str | None = None,
        use_schema: bool = False,
        anon_map: Incomplete | None = None,
    ) -> str: ...
    def format_table_seq(self, table, use_schema: bool = True) -> str: ...
    def unformat_identifiers(self, identifiers) -> list[Incomplete]: ...
