from typing import  Tuple

def newer(source: str, target: str) -> bool: ...
def newer_pairwise(sources: list[str], targets: list[str]) -> list[Tuple[str, str]]: ...
def newer_group(sources: list[str], target: str, missing: str = ...) -> bool: ...
