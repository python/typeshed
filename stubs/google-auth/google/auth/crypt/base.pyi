import abc
from collections.abc import Mapping

class Verifier(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def verify(self, message: str | bytes, signature: str | bytes) -> bool: ...

class Signer(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def key_id(self) -> str: ...
    @abc.abstractmethod
    def sign(self, message: str | bytes) -> bytes: ...

class FromServiceAccountMixin(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def from_string(cls, key: str, key_id: str | None = None) -> Signer: ...
    @classmethod
    def from_service_account_info(cls, info: Mapping[str, str]) -> Signer: ...
    @classmethod
    def from_service_account_file(cls, filename: str) -> Signer: ...
