from _typeshed import Incomplete

class UnsupportedData(TypeError): ...

class InputType:
    def __init__(self, *a, **kw) -> None: ...
    def get_entry_seq(self, data_seq, headers): ...

class DictInputType(InputType):
    def check_type(self, obj): ...
    def guess_headers(self, obj): ...
    def get_entry(self, obj, headers): ...
    def get_entry_seq(self, obj, headers): ...

class ObjectInputType(InputType):
    def check_type(self, obj): ...
    def guess_headers(self, obj): ...
    def get_entry(self, obj, headers): ...

class ListInputType(InputType):
    def check_type(self, obj): ...
    def guess_headers(self, obj) -> None: ...
    def get_entry(self, obj, headers): ...
    def get_entry_seq(self, obj_seq, headers): ...

class TupleInputType(InputType):
    def check_type(self, obj): ...
    def guess_headers(self, obj) -> None: ...
    def get_entry(self, obj, headers): ...
    def get_entry_seq(self, obj_seq, headers): ...

class NamedTupleInputType(InputType):
    def check_type(self, obj): ...
    def guess_headers(self, obj): ...
    def get_entry(self, obj, headers): ...
    def get_entry_seq(self, obj_seq, headers): ...

class Table:
    headers: Incomplete
    metadata: Incomplete
    def __init__(self, data: Incomplete | None = None, headers=..., metadata: Incomplete | None = None) -> None: ...
    def extend(self, data) -> None: ...
    @classmethod
    def from_dict(cls, data, headers=..., max_depth: int = 1, metadata: Incomplete | None = None): ...
    @classmethod
    def from_list(cls, data, headers=..., max_depth: int = 1, metadata: Incomplete | None = None): ...
    @classmethod
    def from_object(cls, data, headers=..., max_depth: int = 1, metadata: Incomplete | None = None): ...
    @classmethod
    def from_data(cls, data, headers=..., max_depth: int = 1, **kwargs): ...
    def __len__(self): ...
    def __getitem__(self, idx): ...
    def to_html(
        self,
        orientation: Incomplete | None = None,
        wrapped: bool = True,
        with_headers: bool = True,
        with_newlines: bool = True,
        with_metadata: bool = False,
        max_depth: int = 1,
    ): ...
    def get_cell_html(self, value): ...
    def to_text(self, with_headers: bool = True, maxlen: Incomplete | None = None): ...
