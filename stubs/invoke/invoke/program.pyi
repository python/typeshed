from typing import Any

class Program:
    def core_args(self): ...
    def task_args(self): ...
    leading_indent_width: int
    leading_indent: str
    indent_width: int
    indent: str
    col_padding: int
    version: Any
    namespace: Any
    argv: Any
    loader_class: Any
    executor_class: Any
    config_class: Any
    def __init__(
        self,
        version=None,
        namespace=None,
        name=None,
        binary=None,
        loader_class=None,
        executor_class=None,
        config_class=None,
        binary_names=None,
    ) -> None: ...
    config: Any
    def create_config(self) -> None: ...
    def update_config(self, merge: bool = True) -> None: ...
    def run(self, argv=None, exit: bool = True) -> None: ...
    def parse_core(self, argv) -> None: ...
    collection: Any
    list_root: Any
    list_depth: Any
    list_format: str
    scoped_collection: Any
    def parse_collection(self) -> None: ...
    def parse_cleanup(self) -> None: ...
    def no_tasks_given(self) -> None: ...
    def execute(self) -> None: ...
    def normalize_argv(self, argv) -> None: ...
    @property
    def name(self): ...
    @property
    def called_as(self): ...
    @property
    def binary(self): ...
    @property
    def binary_names(self): ...
    @property
    def args(self): ...
    @property
    def initial_context(self): ...
    def print_version(self) -> None: ...
    def print_help(self) -> None: ...
    core: Any
    def parse_core_args(self) -> None: ...
    def load_collection(self) -> None: ...
    parser: Any
    core_via_tasks: Any
    tasks: Any
    def parse_tasks(self) -> None: ...
    def print_task_help(self, name) -> None: ...
    def list_tasks(self) -> None: ...
    def list_flat(self) -> None: ...
    def list_nested(self) -> None: ...
    def list_json(self) -> None: ...
    def task_list_opener(self, extra: str = ''): ...
    def display_with_columns(self, pairs, extra: str = '') -> None: ...
    def print_columns(self, tuples) -> None: ...
