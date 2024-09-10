from _typeshed import Incomplete

from ..base_client import BaseApp, OAuth1Mixin, OAuth2Mixin, OpenIDMixin
from ..requests_client import OAuth1Session, OAuth2Session

class FlaskAppMixin:
    @property
    def token(self): ...
    @token.setter
    def token(self, token) -> None: ...
    def save_authorize_data(self, **kwargs) -> None: ...
    def authorize_redirect(self, redirect_uri: Incomplete | None = None, **kwargs): ...

class FlaskOAuth1App(FlaskAppMixin, OAuth1Mixin, BaseApp):
    client_cls = OAuth1Session
    token: Incomplete
    def authorize_access_token(self, **kwargs): ...

class FlaskOAuth2App(FlaskAppMixin, OAuth2Mixin, OpenIDMixin, BaseApp):
    client_cls = OAuth2Session
    token: Incomplete
    def authorize_access_token(self, **kwargs): ...
