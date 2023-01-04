from _typeshed import Incomplete

from influxdb_client.domain.notification_endpoint_discriminator import NotificationEndpointDiscriminator

class HTTPNotificationEndpoint(NotificationEndpointDiscriminator):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        url: Incomplete | None = ...,
        username: Incomplete | None = ...,
        password: Incomplete | None = ...,
        token: Incomplete | None = ...,
        method: Incomplete | None = ...,
        auth_method: Incomplete | None = ...,
        content_template: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        id: Incomplete | None = ...,
        org_id: Incomplete | None = ...,
        user_id: Incomplete | None = ...,
        created_at: Incomplete | None = ...,
        updated_at: Incomplete | None = ...,
        description: Incomplete | None = ...,
        name: Incomplete | None = ...,
        status: str = ...,
        labels: Incomplete | None = ...,
        links: Incomplete | None = ...,
        type: str = ...,
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
