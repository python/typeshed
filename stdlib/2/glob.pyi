from typing import List, Iterator, AnyStr

def glob(pathname: AnyStr) -> List[AnyStr]: ...
def iglob(pathname: AnyStr) -> Iterator[AnyStr]: ...
def glob1(dirname: AnyStr, pattern: AnyStr) -> List[AnyStr]: ...
def glob0(dirname: AnyStr, basename: AnyStr) -> List[AnyStr]: ...
