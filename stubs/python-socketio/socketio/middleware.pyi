from _typeshed import Incomplete

import engineio

class WSGIApp(engineio.WSGIApp):
    def __init__(
        self,
        socketio_app,
        wsgi_app: Incomplete | None = None,
        static_files: Incomplete | None = None,
        socketio_path: str = "socket.io",
    ) -> None: ...

class Middleware(WSGIApp):
    def __init__(self, socketio_app, wsgi_app: Incomplete | None = None, socketio_path: str = "socket.io") -> None: ...
