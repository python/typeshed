from typing import Any
from typing_extensions import assert_type

from authlib.integrations.httpx_client import AsyncOAuth2Client, OAuth2Client


async def check_async_introspect_token(client: AsyncOAuth2Client) -> None:
    response = await client.introspect_token("https://example.com/introspect")
    assert_type(response, Any)


def check_sync_introspect_token(client: OAuth2Client) -> None:
    assert_type(client.introspect_token("https://example.com/introspect"), Any)
