import abc
from _typeshed import Incomplete

import pika.compat

class AbstractIOServices(pika.compat.AbstractBase, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_native_ioloop(self): ...
    @abc.abstractmethod
    def close(self): ...
    @abc.abstractmethod
    def run(self): ...
    @abc.abstractmethod
    def stop(self): ...
    @abc.abstractmethod
    def add_callback_threadsafe(self, callback): ...
    @abc.abstractmethod
    def call_later(self, delay, callback): ...
    @abc.abstractmethod
    def getaddrinfo(self, host, port, on_done, family: int = ..., socktype: int = ..., proto: int = ..., flags: int = ...): ...
    @abc.abstractmethod
    def connect_socket(self, sock, resolved_addr, on_done): ...
    @abc.abstractmethod
    def create_streaming_connection(
        self, protocol_factory, sock, on_done, ssl_context: Incomplete | None = ..., server_hostname: Incomplete | None = ...
    ): ...

class AbstractFileDescriptorServices(pika.compat.AbstractBase, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_reader(self, fd, on_readable): ...
    @abc.abstractmethod
    def remove_reader(self, fd): ...
    @abc.abstractmethod
    def set_writer(self, fd, on_writable): ...
    @abc.abstractmethod
    def remove_writer(self, fd): ...

class AbstractTimerReference(pika.compat.AbstractBase, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def cancel(self): ...

class AbstractIOReference(pika.compat.AbstractBase, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def cancel(self): ...

class AbstractStreamProtocol(pika.compat.AbstractBase, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def connection_made(self, transport): ...
    @abc.abstractmethod
    def connection_lost(self, error): ...
    @abc.abstractmethod
    def eof_received(self): ...
    @abc.abstractmethod
    def data_received(self, data): ...

class AbstractStreamTransport(pika.compat.AbstractBase, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def abort(self): ...
    @abc.abstractmethod
    def get_protocol(self): ...
    @abc.abstractmethod
    def write(self, data): ...
    @abc.abstractmethod
    def get_write_buffer_size(self): ...
