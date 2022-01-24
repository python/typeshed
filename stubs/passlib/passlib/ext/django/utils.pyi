from typing import Any

from django import VERSION as DJANGO_VERSION

MIN_DJANGO_VERSION: Any

class quirks:
    none_causes_check_password_error: Any
    empty_is_usable_password: Any
    invalid_is_usable_password: Any

def get_preset_config(name): ...

class DjangoTranslator:
    context: Any
    def __init__(self, context: Any | None = ..., **kwds) -> None: ...
    def reset_hashers(self) -> None: ...
    def passlib_to_django_name(self, passlib_name): ...
    def passlib_to_django(self, passlib_hasher, cached: bool = ...): ...
    def django_to_passlib_name(self, django_name): ...
    def django_to_passlib(self, django_name, cached: bool = ...): ...
    def resolve_django_hasher(self, django_name, cached: bool = ...): ...

class DjangoContextAdapter(DjangoTranslator):
    context: Any
    is_password_usable: Any
    enabled: bool
    patched: bool
    log: Any
    def __init__(self, context: Any | None = ..., get_user_category: Any | None = ..., **kwds) -> None: ...
    def reset_hashers(self) -> None: ...
    def get_hashers(self): ...
    def get_hasher(self, algorithm: str = ...): ...
    def identify_hasher(self, encoded): ...
    def make_password(self, password, salt: Any | None = ..., hasher: str = ...): ...
    def check_password(self, password, encoded, setter: Any | None = ..., preferred: str = ...): ...
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

class _PasslibHasherWrapper:
    passlib_handler: Any
    rounds: Any
    iterations: Any
    def __init__(self, passlib_handler) -> None: ...
    def __name__(self): ...
    def algorithm(self): ...
    def salt(self): ...
    def verify(self, password, encoded): ...
    def encode(self, password, salt: Any | None = ..., rounds: Any | None = ..., iterations: Any | None = ...): ...
    def safe_summary(self, encoded): ...
    def must_update(self, encoded): ...

class _PatchManager:
    log: Any
    def __init__(self, log: Any | None = ...) -> None: ...
    def isactive(self): ...
    __bool__: Any
    __nonzero__: Any
    def get(self, path, default: Any | None = ...): ...
    def getorig(self, path, default: Any | None = ...): ...
    def check_all(self, strict: bool = ...) -> None: ...
    def patch(self, path, value, wrap: bool = ...): ...
    @classmethod
    def peek_unpatched_func(cls, value): ...
    def monkeypatch(self, parent, name: Any | None = ..., enable: bool = ..., wrap: bool = ...): ...
    def unpatch(self, path, unpatch_conflicts: bool = ...) -> None: ...
    def unpatch_all(self, **kwds) -> None: ...
