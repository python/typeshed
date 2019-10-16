
from typing import TypeVar, Callable, Union, Tuple, Any, Optional


_Type = TypeVar("_Type", bound=type)
_Reduce = Union[Tuple[Callable[[...], _Type], Tuple[...]], Tuple[Callable[[...], _Type], Tuple[...], Optional[Any]]]

def pickle(ob_type: _Type, pickle_function: Callable[[_Type], Union[str, _Reduce]], constructor_ob: Optional[Callable[[_Reduce], _Type]] = ...) -> None: ...
def constructor(object: Callable[[_Reduce], _Type]) -> None: ...
