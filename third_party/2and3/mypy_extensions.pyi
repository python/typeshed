from typing import Any, Dict, Type, TypeVar

T = TypeVar('T')


def TypedDict(typename: str, fields: Dict[str, Type[T]]) -> Type[dict]: ...

def Arg(name: Optional[str] = ..., typ: T = ...) -> T: ...

def DefaultArg(name: Optional[str] = ..., typ: T = ...) -> T: ...

def NamedArg(name: Optional[str] = ..., typ: T = ...) -> T: ...

def DefaultNamedArg(name: Optional[str] = ..., typ: T = ...) -> T: ...

def StarArg(typ: T = ...) -> T: ...

def KwArg(typ: T = ...) -> T: ...