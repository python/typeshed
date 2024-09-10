from _typeshed import Incomplete

from ..base_client import BaseOAuth, OAuthError as OAuthError
from .apps import FlaskOAuth1App as FlaskOAuth1App, FlaskOAuth2App as FlaskOAuth2App
from .integration import FlaskIntegration as FlaskIntegration, token_update as token_update

__all__ = ["OAuth", "FlaskIntegration", "FlaskOAuth1App", "FlaskOAuth2App", "token_update", "OAuthError"]

class OAuth(BaseOAuth):
    oauth1_client_cls = FlaskOAuth1App
    oauth2_client_cls = FlaskOAuth2App
    framework_integration_cls = FlaskIntegration
    app: Incomplete
    def __init__(
        self,
        app: Incomplete | None = None,
        cache: Incomplete | None = None,
        fetch_token: Incomplete | None = None,
        update_token: Incomplete | None = None,
    ) -> None: ...
    cache: Incomplete
    fetch_token: Incomplete
    update_token: Incomplete
    def init_app(
        self, app, cache: Incomplete | None = None, fetch_token: Incomplete | None = None, update_token: Incomplete | None = None
    ) -> None: ...
    def create_client(self, name): ...
    def register(self, name, overwrite: bool = False, **kwargs): ...
