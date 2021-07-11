from typing import Any

re_validPackage: Any
re_paren: Any
re_splitComparison: Any

def splitUp(pred): ...

compmap: Any

class VersionPredicate:
    pred: Any
    def __init__(self, versionPredicateStr) -> None: ...
    def satisfied_by(self, version): ...

def split_provision(value): ...
