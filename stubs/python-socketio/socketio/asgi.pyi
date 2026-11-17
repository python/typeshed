from _typeshed import Incomplete

import engineio

class ASGIApp(engineio.ASGIApp):
    def __init__(
        self,
        socketio_server,
        other_asgi_app: Incomplete | None = None,
        static_files: Incomplete | None = None,
        socketio_path: str = "socket.io",
        on_startup: Incomplete | None = None,
        on_shutdown: Incomplete | None = None,
    ) -> None: ...
