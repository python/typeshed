from typing import Any

from ...orm.scoping import ScopedSessionMixin

class async_scoped_session(ScopedSessionMixin):
    session_factory: Any
    registry: Any
    def __init__(self, session_factory, scopefunc) -> None: ...
    async def remove(self) -> None: ...
