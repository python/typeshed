from collections import OrderedDict
from typing import Any, Mapping, overload

@overload
def alphabetize_attributes(attrs: None) -> None: ...
@overload
def alphabetize_attributes(attrs: Mapping[Any, str]) -> OrderedDict[Any, str]: ...
