import abc
from _typeshed import Incomplete

from pika import connection
from pika.adapters.utils import nbio_interface

LOGGER: Incomplete

class BaseConnection(connection.Connection, metaclass=abc.ABCMeta):
    def __init__(
        self, parameters, on_open_callback, on_open_error_callback, on_close_callback, nbio, internal_connection_workflow
    ) -> None: ...
    @classmethod
    @abc.abstractmethod
    def create_connection(
        cls, connection_configs, on_done, custom_ioloop: Incomplete | None = ..., workflow: Incomplete | None = ...
    ): ...
    @property
    def ioloop(self): ...

class _StreamingProtocolShim(nbio_interface.AbstractStreamProtocol):
    connection_made: Incomplete
    connection_lost: Incomplete
    eof_received: Incomplete
    data_received: Incomplete
    conn: Incomplete
    def __init__(self, conn) -> None: ...
    def __getattr__(self, attr: str): ...
