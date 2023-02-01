from typing import Any

requirements: Any
db: Any
db_url: Any
db_opts: Any
file_config: Any
test_schema: Any
test_schema_2: Any
any_async: bool
ident: str

def combinations(*comb, **kw): ...
def combinations_list(arg_iterable, **kw): ...
def variation(argname, cases): ...
def fixture(*arg, **kw): ...
def get_current_test_name(): ...
def mark_base_test_class(): ...

class Config:
    db: Any
    db_opts: Any
    options: Any
    file_config: Any
    test_schema: str
    test_schema_2: str
    is_async: Any
    def __init__(self, db, db_opts, options, file_config) -> None: ...
    @classmethod
    def register(cls, db, db_opts, options, file_config) -> Config: ...
    @classmethod
    def set_as_current(cls, config, namespace) -> None: ...
    @classmethod
    def push_engine(cls, db, namespace) -> None: ...
    @classmethod
    def push(cls, config, namespace) -> None: ...
    @classmethod
    def pop(cls, namespace) -> None: ...
    @classmethod
    def reset(cls, namespace) -> None: ...
    @classmethod
    def all_configs(cls): ...
    @classmethod
    def all_dbs(cls) -> None: ...
    def skip_test(self, msg) -> None: ...

def skip_test(msg) -> None: ...
def async_test(fn): ...
