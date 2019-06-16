# fmt: off
from collections import OrderedDict
from typing import Any, Mapping, Text, overload

# fmt:on
@overload
def alphabetize_attributes(attrs: None) -> None: ...
@overload
def alphabetize_attributes(attrs: Mapping[Any, Text]) -> OrderedDict[Any, Text]: ...
def force_unicode(text: Text) -> Text: ...
