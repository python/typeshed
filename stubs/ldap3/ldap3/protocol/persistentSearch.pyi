from typing import Any

from pyasn1.type.univ import Enumerated, Sequence

class PersistentSearchControl(Sequence):
    componentType: Any

class ChangeType(Enumerated):
    namedValues: Any

class EntryChangeNotificationControl(Sequence):
    componentType: Any

def persistent_search_control(change_types, changes_only: bool = ..., return_ecs: bool = ..., criticality: bool = ...): ...
