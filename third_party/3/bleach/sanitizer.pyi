from typing import List, Dict, Any, Optional, Type, Pattern, Union, Callable, Container

ALLOWED_TAGS: List[str]
ALLOWED_ATTRIBUTES: Dict[str, List[str]]
ALLOWED_STYLES: List[str]
ALLOWED_PROTOCOLS: List[str]

INVISIBLE_CHARACTERS: str
INVISIBLE_CHARACTERS_RE: Pattern[str]
INVISIBLE_REPLACEMENT_CHAR: str

# A html5lib Filter class
_Filter = Any

class Cleaner:
    def __init__(
        self,
        tags: List[str] = ...,
        attributes: Any = ...,
        styles: List[str] = ...,
        protocols: List[str] = ...,
        strip: bool = ...,
        strip_comments: bool = ...,
        filters: Optional[List[Type[_Filter]]] = ...,
    ) -> None: ...
    def clean(self, text: str) -> str: ...

_AttributeFilter = Callable[[str, str, str], bool]
_AttributeDict = Dict[str, Union[Container[str], _AttributeFilter]]

def attribute_filter_factory(attributes: Union[_AttributeFilter, _AttributeDict, List[str]]) -> _AttributeFilter: ...

class BleachSanitizerFilter:
    def __getattr__(self, item: str) -> Any: ...  # incomplete
