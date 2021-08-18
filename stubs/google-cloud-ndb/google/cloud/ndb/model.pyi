import datetime
from collections.abc import Iterable, Sequence
from typing import Callable, List, NoReturn, Optional, Tuple, Type, Union
from typing_extensions import Literal

import six
from google.cloud.ndb import exceptions, key as key_module, query as query_module, tasklets as tasklets_module

Key: key_module.Key
Rollback: exceptions.Rollback
BlobKey: object
GeoPt: object

class KindError(exceptions.BadValueError): ...
class InvalidPropertyError(exceptions.Error): ...

BadProjectionError = InvalidPropertyError

class UnprojectedPropertyError(exceptions.Error): ...
class ReadonlyPropertyError(exceptions.Error): ...
class ComputedPropertyError(ReadonlyPropertyError): ...
class UserNotFoundError(exceptions.Error): ...

class _NotEqualMixin:
    def __ne__(self, other: object) -> bool: ...

DirectionT = Literal["asc", "desc"]

class IndexProperty(_NotEqualMixin):
    def __new__(cls, name: str, direction: DirectionT) -> IndexProperty: ...
    @property
    def name(self) -> str: ...
    @property
    def direction(self) -> DirectionT: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class Index(_NotEqualMixin):
    def __new__(cls, kind: str, properties: List[IndexProperty], ancestor: bool) -> Index: ...
    @property
    def kind(self) -> str: ...
    @property
    def properties(self) -> List[IndexProperty]: ...
    @property
    def ancestor(self) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

class IndexState(_NotEqualMixin):
    def __new__(cls, definition, state, id): ...
    @property
    def definition(self): ...
    @property
    def state(self): ...
    @property
    def id(self): ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

class ModelAdapter:
    def __new__(cls, *args, **kwargs) -> ModelAdapter: ...

def make_connection(*args, **kwargs) -> NoReturn: ...

class ModelAttribute: ...

class _BaseValue(_NotEqualMixin):
    b_val: object = ...
    def __init__(self, b_val) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

class Property(ModelAttribute):
    def __init__(
        self,
        name: Optional[str] = ...,
        indexed: Optional[bool] = ...,
        repeated: Optional[bool] = ...,
        required: Optional[bool] = ...,
        default: Optional[object] = ...,
        choices: Optional[Iterable[object]] = ...,
        validator: Optional[Callable[[Property], object]] = ...,
        verbose_name: Optional[str] = ...,
        write_empty_list: Optional[bool] = ...,
    ) -> None: ...
    def __eq__(self, value: object) -> query_module.FilterNode: ...  # type: ignore[override]
    def __ne__(self, value: object) -> query_module.FilterNode: ...  # type: ignore[override]
    def __lt__(self, value: object) -> query_module.FilterNode: ...
    def __le__(self, value: object) -> query_module.FilterNode: ...
    def __gt__(self, value: object) -> query_module.FilterNode: ...
    def __ge__(self, value: object) -> query_module.FilterNode: ...
    def IN(
        self, value: Iterable[object]
    ) -> Union[query_module.DisjunctionNode, query_module.FilterNode, query_module.FalseNode]: ...
    def __neg__(self) -> query_module.PropertyOrder: ...
    def __pos__(self) -> query_module.PropertyOrder: ...
    def __set__(self, entity: Model, value: object) -> None: ...
    def __delete__(self, entity: Model) -> None: ...

class ModelKey(Property):
    def __init__(self) -> None: ...
    def __get__(
        self, entity: Model, unused_cls: Optional[Type[Model]] = ...
    ) -> Union[None, key_module.Key, List[key_module.Key]]: ...

class BooleanProperty(Property):
    def __get__(self, entity: Model, unused_cls: Optional[Type[Model]] = ...) -> Union[None, bool, List[bool]]: ...

class IntegerProperty(Property):
    def __get__(self, entity: Model, unused_cls: Optional[Type[Model]] = ...) -> Union[None, int, List[int]]: ...

class FloatProperty(Property): ...

class _CompressedValue(six.binary_type):
    z_val: bytes = ...
    def __init__(self, z_val: bytes) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> NoReturn: ...

class BlobProperty(Property):
    def __init__(
        self,
        name: Optional[str] = ...,
        compressed: Optional[bool] = ...,
        indexed: Optional[bool] = ...,
        repeated: Optional[bool] = ...,
        required: Optional[bool] = ...,
        default: Optional[bytes] = ...,
        choices: Optional[Iterable[bytes]] = ...,
        validator: Optional[Callable[[Property], object]] = ...,
        verbose_name: Optional[str] = ...,
        write_empty_list: Optional[bool] = ...,
    ) -> None: ...
    def __get__(self, entity: Model, unused_cls: Optional[Type[Model]] = ...) -> Union[None, bytes, List[bytes]]: ...

class CompressedTextProperty(BlobProperty):
    def __init__(self, *args, **kwargs) -> None: ...

class TextProperty(Property):
    def __new__(cls, *args, **kwargs): ...
    def __init__(self, *args, **kwargs) -> None: ...

class StringProperty(TextProperty):
    def __init__(self, *args, **kwargs) -> None: ...
    def __get__(self, entity: Model, unused_cls: Optional[Type[Model]] = ...) -> Union[None, str, List[str]]: ...

class GeoPtProperty(Property): ...
class PickleProperty(BlobProperty): ...

class JsonProperty(BlobProperty):
    def __init__(
        self,
        name: Optional[str] = ...,
        compressed: Optional[bool] = ...,
        json_type: Optional[type] = ...,
        indexed: Optional[bool] = ...,
        repeated: Optional[bool] = ...,
        required: Optional[bool] = ...,
        default: Optional[object] = ...,
        choices: Optional[Iterable[object]] = ...,
        validator: Optional[Callable[[Property], object]] = ...,
        verbose_name: Optional[str] = ...,
        write_empty_list: Optional[bool] = ...,
    ) -> None: ...

class User:
    def __init__(self, email: Optional[str] = ..., _auth_domain: Optional[str] = ..., _user_id: Optional[str] = ...) -> None: ...
    def nickname(self) -> str: ...
    def email(self): ...
    def user_id(self) -> Optional[str]: ...
    def auth_domain(self) -> str: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...

class UserProperty(Property):
    def __init__(
        self,
        name: Optional[str] = ...,
        auto_current_user: Optional[bool] = ...,
        auto_current_user_add: Optional[bool] = ...,
        indexed: Optional[bool] = ...,
        repeated: Optional[bool] = ...,
        required: Optional[bool] = ...,
        default: Optional[bytes] = ...,
        choices: Optional[Iterable[bytes]] = ...,
        validator: Optional[Callable[[Property], object]] = ...,
        verbose_name: Optional[str] = ...,
        write_empty_list: Optional[bool] = ...,
    ) -> None: ...

class KeyProperty(Property):
    def __init__(
        self,
        name: Optional[str] = ...,
        kind: Optional[Union[Type[Model], str]] = ...,
        indexed: Optional[bool] = ...,
        repeated: Optional[bool] = ...,
        required: Optional[bool] = ...,
        default: Optional[key_module.Key] = ...,
        choices: Optional[Iterable[key_module.Key]] = ...,
        validator: Optional[Callable[[Property, key_module.Key], bool]] = ...,
        verbose_name: Optional[str] = ...,
        write_empty_list: Optional[bool] = ...,
    ) -> None: ...

class BlobKeyProperty(Property): ...

class DateTimeProperty(Property):
    def __init__(
        self,
        name: Optional[str] = ...,
        auto_now: Optional[bool] = ...,
        auto_now_add: Optional[bool] = ...,
        tzinfo: Optional[datetime.tzinfo] = ...,
        indexed: Optional[bool] = ...,
        repeated: Optional[bool] = ...,
        required: Optional[bool] = ...,
        default: Optional[datetime.datetime] = ...,
        choices: Optional[Iterable[datetime.datetime]] = ...,
        validator: Optional[Callable[[Property, object], bool]] = ...,
        verbose_name: Optional[str] = ...,
        write_empty_list: Optional[bool] = ...,
    ) -> None: ...

class DateProperty(DateTimeProperty): ...
class TimeProperty(DateTimeProperty): ...

class StructuredProperty(Property):
    def __init__(self, model_class: type, name: Optional[str] = ..., **kwargs) -> None: ...
    def __getattr__(self, attrname): ...
    def IN(self, value: Iterable[object]) -> Union[query_module.DisjunctionNode, query_module.FalseNode]: ...

class LocalStructuredProperty(BlobProperty):
    def __init__(self, model_class: Type[Model], **kwargs) -> None: ...

class GenericProperty(Property):
    def __init__(self, name: Optional[str] = ..., compressed: bool = ..., **kwargs) -> None: ...

class ComputedProperty(GenericProperty):
    def __init__(
        self,
        func: Callable[[Model], object],
        name: Optional[str] = ...,
        indexed: Optional[bool] = ...,
        repeated: Optional[bool] = ...,
        verbose_name: Optional[str] = ...,
    ) -> None: ...

class MetaModel(type):
    def __init__(cls, name: str, bases, classdict) -> None: ...

class Model(_NotEqualMixin, metaclass=MetaModel):
    key: ModelKey = ...
    def __init__(_self, **kwargs) -> None: ...
    def __hash__(self) -> NoReturn: ...
    def __eq__(self, other: object) -> bool: ...
    @classmethod
    def gql(cls: Type[Model], query_string: str, *args, **kwargs) -> query_module.Query: ...
    def put(self, **kwargs): ...
    def put_async(self, **kwargs) -> tasklets_module.Future: ...
    @classmethod
    def query(cls: Type[Model], *args, **kwargs) -> query_module.Query: ...
    @classmethod
    def allocate_ids(
        cls: Type[Model],
        size: Optional[int] = ...,
        max: Optional[int] = ...,
        parent: Optional[key_module.Key] = ...,
        retries: Optional[int] = ...,
        timeout: Optional[float] = ...,
        deadline: Optional[float] = ...,
        use_cache: Optional[bool] = ...,
        use_global_cache: Optional[bool] = ...,
        global_cache_timeout: Optional[int] = ...,
        use_datastore: Optional[bool] = ...,
        use_memcache: Optional[bool] = ...,
        memcache_timeout: Optional[int] = ...,
        max_memcache_items: Optional[int] = ...,
        force_writes: Optional[bool] = ...,
        _options=...,
    ) -> Tuple[key_module.Key, key_module.Key]: ...
    @classmethod
    def allocate_ids_async(
        cls: Type[Model],
        size: Optional[int] = ...,
        max: Optional[int] = ...,
        parent: Optional[key_module.Key] = ...,
        retries: Optional[int] = ...,
        timeout: Optional[float] = ...,
        deadline: Optional[float] = ...,
        use_cache: Optional[bool] = ...,
        use_global_cache: Optional[bool] = ...,
        global_cache_timeout: Optional[int] = ...,
        use_datastore: Optional[bool] = ...,
        use_memcache: Optional[bool] = ...,
        memcache_timeout: Optional[int] = ...,
        max_memcache_items: Optional[int] = ...,
        force_writes: Optional[bool] = ...,
        _options=...,
    ) -> tasklets_module.Future: ...
    @classmethod
    def get_by_id(
        cls: Type[Model],
        id: Optional[Union[int, str]],
        parent: Optional[key_module.Key] = ...,
        namespace: Optional[str] = ...,
        project: Optional[str] = ...,
        app: Optional[str] = ...,
        read_consistency: Optional[Literal["EVENTUAL"]] = ...,
        read_policy: Optional[Literal["EVENTUAL"]] = ...,
        transaction: Optional[bytes] = ...,
        retries: Optional[int] = ...,
        timeout: Optional[float] = ...,
        deadline: Optional[float] = ...,
        use_cache: Optional[bool] = ...,
        use_global_cache: Optional[bool] = ...,
        global_cache_timeout: Optional[int] = ...,
        use_datastore: Optional[bool] = ...,
        use_memcache: Optional[bool] = ...,
        memcache_timeout: Optional[int] = ...,
        max_memcache_items: Optional[int] = ...,
        force_writes: Optional[bool] = ...,
        _options=...,
    ) -> tasklets_module.Future: ...
    @classmethod
    def get_by_id_async(
        cls: Type[Model],
        id: Union[int, str],
        parent: Optional[key_module.Key] = ...,
        namespace: Optional[str] = ...,
        project: Optional[str] = ...,
        app: Optional[str] = ...,
        read_consistency: Optional[Literal["EVENTUAL"]] = ...,
        read_policy: Optional[Literal["EVENTUAL"]] = ...,
        transaction: Optional[bytes] = ...,
        retries: Optional[int] = ...,
        timeout: Optional[float] = ...,
        deadline: Optional[float] = ...,
        use_cache: Optional[bool] = ...,
        use_global_cache: Optional[bool] = ...,
        global_cache_timeout: Optional[int] = ...,
        use_datastore: Optional[bool] = ...,
        use_memcache: Optional[bool] = ...,
        memcache_timeout: Optional[int] = ...,
        max_memcache_items: Optional[int] = ...,
        force_writes: Optional[bool] = ...,
        _options=...,
    ) -> Optional[Model]: ...
    @classmethod
    def get_or_insert(
        cls: Type[Model],
        name: str,
        parent: Optional[key_module.Key] = ...,
        namespace: Optional[str] = ...,
        project: Optional[str] = ...,
        app: Optional[str] = ...,
        read_consistency: Optional[Literal["EVENTUAL"]] = ...,
        read_policy: Optional[Literal["EVENTUAL"]] = ...,
        transaction: Optional[bytes] = ...,
        retries: Optional[int] = ...,
        timeout: Optional[float] = ...,
        deadline: Optional[float] = ...,
        use_cache: Optional[bool] = ...,
        use_global_cache: Optional[bool] = ...,
        global_cache_timeout: Optional[int] = ...,
        use_datastore: Optional[bool] = ...,
        use_memcache: Optional[bool] = ...,
        memcache_timeout: Optional[int] = ...,
        max_memcache_items: Optional[int] = ...,
        force_writes: Optional[bool] = ...,
        _options=...,
        **kw_model_args,
    ) -> Model: ...
    @classmethod
    def get_or_insert_async(
        cls: Type[Model],
        name: str,
        parent: Optional[key_module.Key] = ...,
        namespace: Optional[str] = ...,
        project: Optional[str] = ...,
        app: Optional[str] = ...,
        read_consistency: Optional[Literal["EVENTUAL"]] = ...,
        read_policy: Optional[Literal["EVENTUAL"]] = ...,
        transaction: Optional[bytes] = ...,
        retries: Optional[int] = ...,
        timeout: Optional[float] = ...,
        deadline: Optional[float] = ...,
        use_cache: Optional[bool] = ...,
        use_global_cache: Optional[bool] = ...,
        global_cache_timeout: Optional[int] = ...,
        use_datastore: Optional[bool] = ...,
        use_memcache: Optional[bool] = ...,
        memcache_timeout: Optional[int] = ...,
        max_memcache_items: Optional[int] = ...,
        force_writes: Optional[bool] = ...,
        _options=...,
        **kw_model_args,
    ) -> tasklets_module.Future: ...
    def populate(self, **kwargs) -> None: ...
    def has_complete_key(self) -> bool: ...
    def to_dict(
        self,
        include: Optional[Union[list[object], tuple[object, object], set[object]]] = ...,
        exclude: Optional[Union[list[object], tuple[object, object], set[object]]] = ...,
    ): ...

class Expando(Model):
    def __getattr__(self, name: str): ...
    def __setattr__(self, name: str, value) -> None: ...
    def __delattr__(self, name: str) -> None: ...

def get_multi_async(
    keys: Sequence[Type[key_module.Key]],
    read_consistency: Optional[Literal["EVENTUAL"]] = ...,
    read_policy: Optional[Literal["EVENTUAL"]] = ...,
    transaction: Optional[bytes] = ...,
    retries: Optional[int] = ...,
    timeout: Optional[float] = ...,
    deadline: Optional[float] = ...,
    use_cache: Optional[bool] = ...,
    use_global_cache: Optional[bool] = ...,
    global_cache_timeout: Optional[int] = ...,
    use_datastore: Optional[bool] = ...,
    use_memcache: Optional[bool] = ...,
    memcache_timeout: Optional[int] = ...,
    max_memcache_items: Optional[int] = ...,
    force_writes: Optional[bool] = ...,
    _options: Optional[object] = ...,
) -> List[Type[tasklets_module.Future]]: ...
def get_multi(
    keys: Sequence[Type[key_module.Key]],
    read_consistency: Optional[Literal["EVENTUAL"]] = ...,
    read_policy: Optional[Literal["EVENTUAL"]] = ...,
    transaction: Optional[bytes] = ...,
    retries: Optional[int] = ...,
    timeout: Optional[float] = ...,
    deadline: Optional[float] = ...,
    use_cache: Optional[bool] = ...,
    use_global_cache: Optional[bool] = ...,
    global_cache_timeout: Optional[int] = ...,
    use_datastore: Optional[bool] = ...,
    use_memcache: Optional[bool] = ...,
    memcache_timeout: Optional[int] = ...,
    max_memcache_items: Optional[int] = ...,
    force_writes: Optional[bool] = ...,
    _options: Optional[object] = ...,
) -> List[Union[Type[Model], None]]: ...
def put_multi_async(
    entities: List[Type[Model]],
    retries: Optional[int] = ...,
    timeout: Optional[float] = ...,
    deadline: Optional[float] = ...,
    use_cache: Optional[bool] = ...,
    use_global_cache: Optional[bool] = ...,
    global_cache_timeout: Optional[int] = ...,
    use_datastore: Optional[bool] = ...,
    use_memcache: Optional[bool] = ...,
    memcache_timeout: Optional[int] = ...,
    max_memcache_items: Optional[int] = ...,
    force_writes: Optional[bool] = ...,
    _options: Optional[object] = ...,
) -> List[tasklets_module.Future]: ...
def put_multi(
    entities: List[Model],
    retries: Optional[int] = ...,
    timeout: Optional[float] = ...,
    deadline: Optional[float] = ...,
    use_cache: Optional[bool] = ...,
    use_global_cache: Optional[bool] = ...,
    global_cache_timeout: Optional[int] = ...,
    use_datastore: Optional[bool] = ...,
    use_memcache: Optional[bool] = ...,
    memcache_timeout: Optional[int] = ...,
    max_memcache_items: Optional[int] = ...,
    force_writes: Optional[bool] = ...,
    _options: Optional[object] = ...,
) -> List[key_module.Key]: ...
def delete_multi_async(
    keys: List[key_module.Key],
    retries: Optional[int] = ...,
    timeout: Optional[float] = ...,
    deadline: Optional[float] = ...,
    use_cache: Optional[bool] = ...,
    use_global_cache: Optional[bool] = ...,
    global_cache_timeout: Optional[int] = ...,
    use_datastore: Optional[bool] = ...,
    use_memcache: Optional[bool] = ...,
    memcache_timeout: Optional[int] = ...,
    max_memcache_items: Optional[int] = ...,
    force_writes: Optional[bool] = ...,
    _options: Optional[object] = ...,
) -> List[tasklets_module.Future]: ...
def delete_multi(
    keys: Sequence[key_module.Key],
    retries: Optional[int] = ...,
    timeout: Optional[float] = ...,
    deadline: Optional[float] = ...,
    use_cache: Optional[bool] = ...,
    use_global_cache: Optional[bool] = ...,
    global_cache_timeout: Optional[int] = ...,
    use_datastore: Optional[bool] = ...,
    use_memcache: Optional[bool] = ...,
    memcache_timeout: Optional[int] = ...,
    max_memcache_items: Optional[int] = ...,
    force_writes: Optional[bool] = ...,
    _options: Optional[object] = ...,
) -> List[None]: ...
def get_indexes_async(**options: object) -> NoReturn: ...
def get_indexes(**options: object) -> NoReturn: ...
