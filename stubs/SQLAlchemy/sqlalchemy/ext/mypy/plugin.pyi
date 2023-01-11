from collections.abc import Callable

from mypy.nodes import MypyFile
from mypy.plugin import AttributeContext, ClassDefContext, DynamicClassDefContext, Plugin
from mypy.types import Type

class SQLAlchemyPlugin(Plugin):
    def get_dynamic_class_hook(self, fullname: str) -> Callable[[DynamicClassDefContext], None] | None: ...
    def get_customize_class_mro_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None: ...
    def get_class_decorator_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None: ...
    def get_metaclass_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None: ...
    def get_base_class_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None: ...
    def get_attribute_hook(self, fullname: str) -> Callable[[AttributeContext], Type] | None: ...
    def get_additional_deps(self, file: MypyFile) -> list[tuple[int, str, int]]: ...

def plugin(version: str) -> type[SQLAlchemyPlugin]: ...
