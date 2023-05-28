from _typeshed import Incomplete
from typing import Any

__all__ = ["DJANGO_VERSION", "MIN_DJANGO_VERSION", "get_preset_config", "quirks"]

DJANGO_VERSION: tuple[Any, ...]
MIN_DJANGO_VERSION: tuple[int, int]

class quirks:
    none_causes_check_password_error: Any
    empty_is_usable_password: Any
    invalid_is_usable_password: Any

def get_preset_config(name): ...

class DjangoTranslator:
    context: Any
    def __init__(self, context: Incomplete | None = None, **kwds) -> None: ...
    def reset_hashers(self) -> None: ...
    def passlib_to_django_name(self, passlib_name): ...
    def passlib_to_django(self, passlib_hasher, cached: bool = True): ...
    def django_to_passlib_name(self, django_name): ...
    def django_to_passlib(self, django_name, cached: bool = True): ...
    def resolve_django_hasher(self, django_name, cached: bool = True): ...

class DjangoContextAdapter(DjangoTranslator):
    context: Any
    is_password_usable: Any
    enabled: bool
    patched: bool
    log: Any
    def __init__(self, context: Incomplete | None = None, get_user_category: Incomplete | None = None, **kwds) -> None: ...
    def reset_hashers(self) -> None: ...
    def get_hashers(self): ...
    def get_hasher(self, algorithm: str = "default"): ...
    def identify_hasher(self, encoded): ...
    def make_password(self, password, salt: Incomplete | None = None, hasher: str = "default"): ...
    def check_password(self, password, encoded, setter: Incomplete | None = None, preferred: str = "default"): ...
    def user_check_password(self, user, password): ...
    def user_set_password(self, user, password) -> None: ...
    def get_user_category(self, user): ...
    HASHERS_PATH: str
    MODELS_PATH: str
    USER_CLASS_PATH: Any
    FORMS_PATH: str
    patch_locations: Any
    def install_patch(self): ...
    def remove_patch(self): ...
    def load_model(self) -> None: ...

class ProxyProperty:
    attr: Any
    def __init__(self, attr) -> None: ...
    def __get__(self, obj, cls): ...
    def __set__(self, obj, value) -> None: ...
    def __delete__(self, obj) -> None: ...
