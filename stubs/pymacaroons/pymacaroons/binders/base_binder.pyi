import abc
from _typeshed import Incomplete, ReadableBuffer
from abc import abstractmethod

from pymacaroons import Macaroon


class BaseBinder(metaclass=abc.ABCMeta):
    __metaclass__: type
    root: Incomplete
    def __init__(self, root: Macaroon) -> None: ...
    def bind(self, discharge: Macaroon) -> Macaroon: ...
    @abstractmethod
    def bind_signature(self, signature: str | ReadableBuffer) -> bytes: ...
