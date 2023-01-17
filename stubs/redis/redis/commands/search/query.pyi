from _typeshed import Incomplete
from typing import Any

class Query:
    def __init__(self, query_string) -> None: ...
    def query_string(self): ...
    def limit_ids(self, *ids): ...
    def return_fields(self, *fields): ...
    def return_field(self, field, as_field: Incomplete | None = ...): ...
    def summarize(
        self,
        fields: Incomplete | None = ...,
        context_len: Incomplete | None = ...,
        num_frags: Incomplete | None = ...,
        sep: Incomplete | None = ...,
    ): ...
    def highlight(self, fields: Incomplete | None = ..., tags: Incomplete | None = ...): ...
    def language(self, language): ...
    def slop(self, slop): ...
    def in_order(self): ...
    def scorer(self, scorer): ...
    def get_args(self): ...
    def paging(self, offset, num): ...
    def verbatim(self): ...
    def no_content(self): ...
    def no_stopwords(self): ...
    def with_payloads(self): ...
    def with_scores(self): ...
    def limit_fields(self, *fields): ...
    def add_filter(self, flt): ...
    def sort_by(self, field, asc: bool = ...): ...
    def expander(self, expander): ...

class Filter:
    args: Any
    def __init__(self, keyword, field, *args) -> None: ...

class NumericFilter(Filter):
    INF: str
    NEG_INF: str
    def __init__(self, field, minval, maxval, minExclusive: bool = ..., maxExclusive: bool = ...) -> None: ...

class GeoFilter(Filter):
    METERS: str
    KILOMETERS: str
    FEET: str
    MILES: str
    def __init__(self, field, lon, lat, radius, unit=...) -> None: ...

class SortbyField:
    args: Any
    def __init__(self, field, asc: bool = ...) -> None: ...
