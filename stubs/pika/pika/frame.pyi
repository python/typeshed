from _typeshed import Incomplete

from pika import amqp_object

LOGGER: Incomplete

class Frame(amqp_object.AMQPObject):
    NAME: str
    frame_type: Incomplete
    channel_number: Incomplete
    def __init__(self, frame_type, channel_number) -> None: ...
    def marshal(self) -> None: ...

class Method(Frame):
    NAME: str
    method: Incomplete
    def __init__(self, channel_number, method) -> None: ...
    def marshal(self): ...

class Header(Frame):
    NAME: str
    body_size: Incomplete
    properties: Incomplete
    def __init__(self, channel_number, body_size, props) -> None: ...
    def marshal(self): ...

class Body(Frame):
    NAME: str
    fragment: Incomplete
    def __init__(self, channel_number, fragment) -> None: ...
    def marshal(self): ...

class Heartbeat(Frame):
    NAME: str
    def __init__(self) -> None: ...
    def marshal(self): ...

class ProtocolHeader(amqp_object.AMQPObject):
    NAME: str
    frame_type: int
    major: Incomplete
    minor: Incomplete
    revision: Incomplete
    def __init__(
        self, major: Incomplete | None = ..., minor: Incomplete | None = ..., revision: Incomplete | None = ...
    ) -> None: ...
    def marshal(self): ...

def decode_frame(data_in): ...
