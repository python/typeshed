from typing_extensions import assert_type

from oauthlib.oauth2 import LegacyApplicationClient, OAuth2Token

client = LegacyApplicationClient("client-id")

assert_type(
    client.prepare_request_body(
        username="username", password="password", scope="read write", include_client_id=True, response_type="token"
    ),
    str,
)
assert_type(client.parse_request_body_response('{"access_token": "token"}'), OAuth2Token)
