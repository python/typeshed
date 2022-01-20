from typing import Any

# SQLAlchemy is not part of typeshed
_Query = Any
_SessionBase = Any

from . import utils as utils
from .model import DefaultMeta as DefaultMeta, Model as Model

models_committed: Any
before_models_committed: Any

class SignallingSession(_SessionBase):
    app: Any
    def __init__(self, db, autocommit: bool = ..., autoflush: bool = ..., **options) -> None: ...
    def get_bind(self, mapper: Any | None = ..., clause: Any | None = ...): ...

def get_debug_queries(): ...

class Pagination:
    query: Any
    page: Any
    per_page: Any
    total: Any
    items: Any
    def __init__(self, query, page, per_page, total, items) -> None: ...
    @property
    def pages(self): ...
    def prev(self, error_out: bool = ...): ...
    @property
    def prev_num(self): ...
    @property
    def has_prev(self): ...
    def next(self, error_out: bool = ...): ...
    @property
    def has_next(self): ...
    @property
    def next_num(self): ...
    def iter_pages(
        self, left_edge: int = ..., left_current: int = ..., right_current: int = ..., right_edge: int = ...
    ) -> None: ...

class BaseQuery(_Query):
    def get_or_404(self, ident, description: Any | None = ...): ...
    def first_or_404(self, description: Any | None = ...): ...
    def paginate(
        self, page: Any | None = ..., per_page: Any | None = ..., error_out: bool = ..., max_per_page: Any | None = ...
    ): ...

def get_state(app): ...

class SQLAlchemy:
    Query: Any
    use_native_unicode: Any
    session: Any
    Model: Any
    app: Any
    def __init__(
        self,
        app: Any | None = ...,
        use_native_unicode: bool = ...,
        session_options: Any | None = ...,
        metadata: Any | None = ...,
        query_class=...,
        model_class=...,
        engine_options: Any | None = ...,
    ) -> None: ...
    @property
    def metadata(self): ...
    def create_scoped_session(self, options: Any | None = ...): ...
    def create_session(self, options): ...
    def make_declarative_base(self, model, metadata: Any | None = ...): ...
    def init_app(self, app): ...
    def apply_pool_defaults(self, app, options): ...
    def apply_driver_hacks(self, app, sa_url, options): ...
    @property
    def engine(self): ...
    def make_connector(self, app: Any | None = ..., bind: Any | None = ...): ...
    def get_engine(self, app: Any | None = ..., bind: Any | None = ...): ...
    def create_engine(self, sa_url, engine_opts): ...
    def get_app(self, reference_app: Any | None = ...): ...
    def get_tables_for_bind(self, bind: Any | None = ...): ...
    def get_binds(self, app: Any | None = ...): ...
    def create_all(self, bind: str = ..., app: Any | None = ...) -> None: ...
    def drop_all(self, bind: str = ..., app: Any | None = ...) -> None: ...
    def reflect(self, bind: str = ..., app: Any | None = ...) -> None: ...

class FSADeprecationWarning(DeprecationWarning): ...
