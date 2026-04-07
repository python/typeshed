import abc
from _typeshed import Incomplete

from google.auth import _credentials_async as credentials_async
from google.auth.transport import Request as _Request
from google.oauth2 import service_account

class Credentials(service_account.Credentials, credentials_async.Scoped, credentials_async.Credentials, metaclass=abc.ABCMeta):
    token: Incomplete
    expiry: Incomplete

    async def refresh(self, request: _Request) -> None: ...

class IDTokenCredentials(service_account.IDTokenCredentials, credentials_async.Signing, credentials_async.Credentials):
    token: Incomplete
    expiry: Incomplete

    async def refresh(self, request: _Request) -> None: ...
