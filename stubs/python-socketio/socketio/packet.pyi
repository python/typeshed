from _typeshed import Incomplete

CONNECT: Incomplete
DISCONNECT: Incomplete
EVENT: Incomplete
ACK: Incomplete
CONNECT_ERROR: Incomplete
BINARY_EVENT: Incomplete
BINARY_ACK: Incomplete
packet_names: Incomplete

class Packet:
    uses_binary_events: bool
    json: Incomplete
    packet_type: Incomplete
    data: Incomplete
    namespace: Incomplete
    id: Incomplete
    attachment_count: int
    attachments: Incomplete
    def __init__(
        self,
        packet_type=2,
        data: Incomplete | None = None,
        namespace: Incomplete | None = None,
        id: Incomplete | None = None,
        binary: Incomplete | None = None,
        encoded_packet: Incomplete | None = None,
    ) -> None: ...
    def encode(self): ...
    def decode(self, encoded_packet): ...
    def add_attachment(self, attachment): ...
    def reconstruct_binary(self, attachments) -> None: ...
