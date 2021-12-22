from .. import event

class PoolEvents(event.Events):
    def connect(self, dbapi_connection, connection_record) -> None: ...
    def first_connect(self, dbapi_connection, connection_record) -> None: ...
    def checkout(self, dbapi_connection, connection_record, connection_proxy) -> None: ...
    def checkin(self, dbapi_connection, connection_record) -> None: ...
    def reset(self, dbapi_connection, connection_record) -> None: ...
    def invalidate(self, dbapi_connection, connection_record, exception) -> None: ...
    def soft_invalidate(self, dbapi_connection, connection_record, exception) -> None: ...
    def close(self, dbapi_connection, connection_record) -> None: ...
    def detach(self, dbapi_connection, connection_record) -> None: ...
    def close_detached(self, dbapi_connection) -> None: ...
