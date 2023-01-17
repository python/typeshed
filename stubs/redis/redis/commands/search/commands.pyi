from _typeshed import Incomplete
from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Any
from typing_extensions import Literal, TypeAlias

from .aggregation import AggregateRequest, AggregateResult, Cursor
from .query import Query
from .result import Result

_QueryParams: TypeAlias = Mapping[str, str | float]

NUMERIC: Literal["NUMERIC"]

CREATE_CMD: Literal["FT.CREATE"]
ALTER_CMD: Literal["FT.ALTER"]
SEARCH_CMD: Literal["FT.SEARCH"]
ADD_CMD: Literal["FT.ADD"]
ADDHASH_CMD: Literal["FT.ADDHASH"]
DROP_CMD: Literal["FT.DROP"]
EXPLAIN_CMD: Literal["FT.EXPLAIN"]
EXPLAINCLI_CMD: Literal["FT.EXPLAINCLI"]
DEL_CMD: Literal["FT.DEL"]
AGGREGATE_CMD: Literal["FT.AGGREGATE"]
PROFILE_CMD: Literal["FT.PROFILE"]
CURSOR_CMD: Literal["FT.CURSOR"]
SPELLCHECK_CMD: Literal["FT.SPELLCHECK"]
DICT_ADD_CMD: Literal["FT.DICTADD"]
DICT_DEL_CMD: Literal["FT.DICTDEL"]
DICT_DUMP_CMD: Literal["FT.DICTDUMP"]
GET_CMD: Literal["FT.GET"]
MGET_CMD: Literal["FT.MGET"]
CONFIG_CMD: Literal["FT.CONFIG"]
TAGVALS_CMD: Literal["FT.TAGVALS"]
ALIAS_ADD_CMD: Literal["FT.ALIASADD"]
ALIAS_UPDATE_CMD: Literal["FT.ALIASUPDATE"]
ALIAS_DEL_CMD: Literal["FT.ALIASDEL"]
INFO_CMD: Literal["FT.INFO"]
SUGADD_COMMAND: Literal["FT.SUGADD"]
SUGDEL_COMMAND: Literal["FT.SUGDEL"]
SUGLEN_COMMAND: Literal["FT.SUGLEN"]
SUGGET_COMMAND: Literal["FT.SUGGET"]
SYNUPDATE_CMD: Literal["FT.SYNUPDATE"]
SYNDUMP_CMD: Literal["FT.SYNDUMP"]

NOOFFSETS: Literal["NOOFFSETS"]
NOFIELDS: Literal["NOFIELDS"]
STOPWORDS: Literal["STOPWORDS"]
WITHSCORES: Literal["WITHSCORES"]
FUZZY: Literal["FUZZY"]
WITHPAYLOADS: Literal["WITHPAYLOADS"]

class SearchCommands:
    def batch_indexer(self, chunk_size: int = ...): ...
    def create_index(
        self,
        fields,
        no_term_offsets: bool = ...,
        no_field_flags: bool = ...,
        stopwords: Incomplete | None = ...,
        definition: Incomplete | None = ...,
        max_text_fields: bool = ...,  # added in 4.1.1
        temporary: Incomplete | None = ...,  # added in 4.1.1
        no_highlight: bool = ...,  # added in 4.1.1
        no_term_frequencies: bool = ...,  # added in 4.1.1
        skip_initial_scan: bool = ...,  # added in 4.1.1
    ): ...
    def alter_schema_add(self, fields): ...
    def dropindex(self, delete_documents: bool = ...): ...
    def add_document(
        self,
        doc_id,
        nosave: bool = ...,
        score: float = ...,
        payload: Incomplete | None = ...,
        replace: bool = ...,
        partial: bool = ...,
        language: Incomplete | None = ...,
        no_create: bool = ...,
        **fields,
    ): ...
    def add_document_hash(self, doc_id, score: float = ..., language: Incomplete | None = ..., replace: bool = ...): ...
    def delete_document(self, doc_id, conn: Incomplete | None = ..., delete_actual_document: bool = ...): ...
    def load_document(self, id): ...
    def get(self, *ids): ...
    def info(self): ...
    def get_params_args(self, query_params: _QueryParams) -> list[Any]: ...
    def search(self, query: str | Query, query_params: _QueryParams | None = ...) -> Result: ...
    def explain(self, query: str | Query, query_params: _QueryParams | None = ...): ...
    def explain_cli(self, query): ...
    def aggregate(self, query: AggregateRequest | Cursor, query_params: _QueryParams | None = ...) -> AggregateResult: ...
    def profile(
        self, query: str | Query | AggregateRequest, limited: bool = ..., query_params: Mapping[str, str | float] | None = ...
    ) -> tuple[Incomplete, Incomplete]: ...
    def spellcheck(self, query, distance: Incomplete | None = ..., include: Incomplete | None = ..., exclude: Incomplete | None = ...): ...
    def dict_add(self, name, *terms): ...
    def dict_del(self, name, *terms): ...
    def dict_dump(self, name): ...
    def config_set(self, option: str, value: str) -> bool: ...
    def config_get(self, option: str) -> dict[str, str]: ...
    def tagvals(self, tagfield): ...
    def aliasadd(self, alias): ...
    def aliasupdate(self, alias): ...
    def aliasdel(self, alias): ...
    def sugadd(self, key, *suggestions, **kwargs): ...
    def suglen(self, key): ...
    def sugdel(self, key, string): ...
    def sugget(self, key, prefix, fuzzy: bool = ..., num: int = ..., with_scores: bool = ..., with_payloads: bool = ...): ...
    def synupdate(self, groupid, skipinitial: bool = ..., *terms): ...
    def syndump(self): ...