from collections import OrderedDict
from typing import Any, Mapping, Text, overload

@overload
def alphabetize_attributes(attrs: None) -> None: ...
@overload
def alphabetize_attributes(attrs: Mapping[Any, Text]) -> OrderedDict[Any, Text]: ...
