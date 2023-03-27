from _typeshed import Incomplete

from influxdb_client.domain.notification_endpoint_discriminator import NotificationEndpointDiscriminator

class HTTPNotificationEndpoint(NotificationEndpointDiscriminator):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        url: Incomplete | None = None,
        username: Incomplete | None = None,
        password: Incomplete | None = None,
        token: Incomplete | None = None,
        method: Incomplete | None = None,
        auth_method: Incomplete | None = None,
        content_template: Incomplete | None = None,
        headers: Incomplete | None = None,
        id: Incomplete | None = None,
        org_id: Incomplete | None = None,
        user_id: Incomplete | None = None,
        created_at: Incomplete | None = None,
        updated_at: Incomplete | None = None,
        description: Incomplete | None = None,
        name: Incomplete | None = None,
        status: str = 'active',
        labels: Incomplete | None = None,
        links: Incomplete | None = None,
        type: str = 'http',
    ) -> None: ...
    @property
    def url(self): ...
    @url.setter
    def url(self, url) -> None: ...
    @property
    def username(self): ...
    @username.setter
    def username(self, username) -> None: ...
    @property
    def password(self): ...
    @password.setter
    def password(self, password) -> None: ...
    @property
    def token(self): ...
    @token.setter
    def token(self, token) -> None: ...
    @property
    def method(self): ...
    @method.setter
    def method(self, method) -> None: ...
    @property
    def auth_method(self): ...
    @auth_method.setter
    def auth_method(self, auth_method) -> None: ...
    @property
    def content_template(self): ...
    @content_template.setter
    def content_template(self, content_template) -> None: ...
    @property
    def headers(self): ...
    @headers.setter
    def headers(self, headers) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
