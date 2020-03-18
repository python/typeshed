from hammurabi.config import config as config
from hammurabi.law import Law as Law
from hammurabi.mixins import GitHubMixin as GitHubMixin
from hammurabi.rules.base import Rule as Rule
from typing import Any, List, Set

class Pillar(GitHubMixin):
    __laws: Any = ...
    __lock_file: Any = ...
    def __init__(self) -> None: ...
    @property
    def laws(self) -> Set[Law]: ...
    @property
    def rules(self) -> List[Rule]: ...
    def create_lock_file(self) -> None: ...
    def release_lock_file(self) -> None: ...
    def get_law(self, name: str) -> Law: ...
    def get_rule(self, name: str) -> Rule: ...
    def register(self, law: Law) -> Any: ...
    def enforce(self) -> None: ...
