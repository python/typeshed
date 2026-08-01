from authlib.integrations.httpx_client import AsyncOAuth2Client


async def check_introspect_token(client: AsyncOAuth2Client) -> None:
    # The response type depends on the HTTP client integration.
    await client.introspect_token(  # pyright: ignore[reportUnknownMemberType]
        "https://example.com/introspect", token="token", token_type_hint="access_token"
    )
