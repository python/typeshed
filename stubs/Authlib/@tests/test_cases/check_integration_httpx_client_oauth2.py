from __future__ import annotations

from authlib.integrations.httpx_client import AsyncOAuth2Client


# ================================================================================
# Test for AsyncOAuth2Client contex manager being correctly inherited and present.
# ================================================================================
async def test_client_contex_manager() -> None:
    async with AsyncOAuth2Client():
        pass
