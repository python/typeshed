from _typeshed import Incomplete
from collections import defaultdict

class OAuth2Request:
    method: Incomplete
    uri: Incomplete
    body: Incomplete
    headers: Incomplete
    client: Incomplete
    auth_method: Incomplete
    user: Incomplete
    authorization_code: Incomplete
    refresh_token: Incomplete
    credential: Incomplete
    def __init__(self, method: str, uri: str, body: Incomplete | None = None, headers: Incomplete | None = None) -> None: ...
    @property
    def args(self): ...
    @property
    def form(self): ...
    @property
    def data(self): ...
    @property
    def datalist(self) -> defaultdict[str, list]: ...
    @property
    def client_id(self) -> str: ...
    @property
    def response_type(self) -> str: ...
    @property
    def grant_type(self) -> str: ...
    @property
    def redirect_uri(self): ...
    @property
    def scope(self) -> str: ...
    @property
    def state(self): ...

class JsonRequest:
    method: Incomplete
    uri: Incomplete
    body: Incomplete
    headers: Incomplete
    def __init__(self, method, uri, body: Incomplete | None = None, headers: Incomplete | None = None) -> None: ...
    @property
    def data(self): ...
