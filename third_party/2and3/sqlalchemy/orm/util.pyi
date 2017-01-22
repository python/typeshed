# Stubs for sqlalchemy.orm.session (Python 2 and 3)
from typing import Optional, Any, Text

from ..sql.selectable import FromClause

class AliasedClass(object):
    def __init__(self, cls: Any, alias: Optional[FromClause] =None, name: Optional[Text] =None, flat: bool =False, adapt_on_names: bool =False,
                 with_polymorphic_mappers: Any =(), with_polymorphic_discriminator: Any =None, base_alias: Any =None, use_mapper_path: bool =False) -> None: ...
    def __getattr__(self, key): ...
    def __repr__(self): ...

def aliased(element: Any, alias: Optional[FromClause] =None, name: Optional[Text] =None, flat: bool =False, adapt_on_names: bool =False) -> AliasedClass: ...
