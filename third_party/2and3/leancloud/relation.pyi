from typing import Any, Union, Dict

import leancloud
from leancloud.object_ import Object
from leancloud.query import Query


class Relation(object):
    def __init__(self, parent: Object, key: str=None) -> None :...

    @classmethod
    def reverse_query(cls, parent_class: Union[str, Object], relation_key: str, child: Object) -> Query:...

    def add(self, *obj_or_objs: Union[Object, List[Object]]) -> None:...

    def remove(slef, *obj_or_objs: Union[object, List[Object]]) -> None:...

    def dump(self) -> Dict:...

    @property
    def query(self) -> Query:...
