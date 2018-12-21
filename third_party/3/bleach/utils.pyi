from collections import OrderedDict
from typing import overload, Mapping, Any

@overload
def alphabetize_attributes(attrs: None) -> None: ...
@overload
def alphabetize_attributes(attrs: Mapping[Any, str]) -> OrderedDict[Any, str]: ...
def force_unicode(text: str) -> str: ...
