from abc import abstractmethod

from pymacaroons import Macaroon

class BaseSerializer:
    __metaclass__: type
    @abstractmethod
    def serialize(self, macaroon: Macaroon) -> str: ...
    @abstractmethod
    def deserialize(self, serialized: str) -> Macaroon: ...
