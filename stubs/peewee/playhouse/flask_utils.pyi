from collections.abc import Container

from flask import Flask
from peewee import Model, Proxy

class FlaskDB:
    # Omitting undocumented base_model_class on purpose, use FlaskDB.Model instead
    database: Database | Proxy
    def __init__(
        self,
        app: Flask | None = None,
        database: Database | Proxy = None,
        model_class: type[Model] = ...,
        excluded_routes: Container[str] | None = None,
    ) -> None: ...
    def init_app(self, app: Flask) -> None: ...
    def get_model_class(self) -> type[Model]: ...
    @property
    def Model(self) -> type[Model]: ...
    def connect_db(self) -> None: ...
    def close_db(self, exc: Unused) -> None: ...
