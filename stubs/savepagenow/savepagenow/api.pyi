DEFAULT_USER_AGENT: str

def capture(
    target_url: str,
    user_agent: str = "savepagenow (https://github.com/pastpages/savepagenow)",
    accept_cache: bool = False,
    authenticate: bool = False,
) -> str: ...
def capture_or_cache(
    target_url: str, user_agent: str = "savepagenow (https://github.com/pastpages/savepagenow)", authenticate: bool = False
) -> tuple[str, bool]: ...
def cli(url: str, user_agent: str | None = ..., accept_cache: bool = ..., authenticate: bool = ...) -> None: ...
