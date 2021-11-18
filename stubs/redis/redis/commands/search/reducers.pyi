from .aggregation import Reducer as Reducer, SortDirection as SortDirection

class FieldOnlyReducer(Reducer):
    def __init__(self, field) -> None: ...

class count(Reducer):
    NAME: str
    def __init__(self) -> None: ...

class sum(FieldOnlyReducer):
    NAME: str
    def __init__(self, field) -> None: ...

class min(FieldOnlyReducer):
    NAME: str
    def __init__(self, field) -> None: ...

class max(FieldOnlyReducer):
    NAME: str
    def __init__(self, field) -> None: ...

class avg(FieldOnlyReducer):
    NAME: str
    def __init__(self, field) -> None: ...

class tolist(FieldOnlyReducer):
    NAME: str
    def __init__(self, field) -> None: ...

class count_distinct(FieldOnlyReducer):
    NAME: str
    def __init__(self, field) -> None: ...

class count_distinctish(FieldOnlyReducer):
    NAME: str

class quantile(Reducer):
    NAME: str
    def __init__(self, field, pct) -> None: ...

class stddev(FieldOnlyReducer):
    NAME: str
    def __init__(self, field) -> None: ...

class first_value(Reducer):
    NAME: str
    def __init__(self, field, *byfields) -> None: ...

class random_sample(Reducer):
    NAME: str
    def __init__(self, field, size) -> None: ...
