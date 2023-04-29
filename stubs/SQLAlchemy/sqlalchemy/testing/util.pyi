from _typeshed import Incomplete
from typing import Any

def non_refcount_gc_collect(*args) -> None: ...  # only present on Python implementations with non-refcount gc
def gc_collect(generation: int = 2) -> None: ...
def lazy_gc() -> None: ...
def picklers(): ...
def random_choices(population, k: int = 1): ...
def round_decimal(value, prec): ...

class RandomSet(set[Any]):
    def __iter__(self): ...
    def pop(self): ...
    def union(self, other): ...
    def difference(self, other): ...
    def intersection(self, other): ...
    def copy(self) -> RandomSet: ...

def conforms_partial_ordering(tuples, sorted_elements): ...
def all_partial_orderings(tuples, elements): ...
def function_named(fn, name): ...
def run_as_contextmanager(ctx, fn, *arg, **kw): ...
def rowset(results): ...
def fail(msg) -> None: ...
def provide_metadata(fn, *args, **kw): ...
def flag_combinations(*combinations): ...
def lambda_combinations(lambda_arg_sets, **kw): ...
def resolve_lambda(__fn, **kw): ...
def metadata_fixture(ddl: str = "function"): ...
def force_drop_names(*names): ...

class adict(dict[Any, Any]):
    def __getattribute__(self, key: str): ...
    def __call__(self, *keys): ...
    get_all: Any

def drop_all_tables_from_metadata(metadata, engine_or_connection) -> None: ...
def drop_all_tables(engine, inspector, schema: Incomplete | None = None, include_names: Incomplete | None = None) -> None: ...
def total_size(o) -> int: ...
def teardown_events(event_cls): ...
def count_cache_key_tuples(tup) -> int: ...
