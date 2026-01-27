from _typeshed import Incomplete

from . import packet

class MsgPackPacket(packet.Packet):
    uses_binary_events: bool
    def encode(self): ...
    packet_type: Incomplete
    data: Incomplete
    id: Incomplete
    namespace: Incomplete
    def decode(self, encoded_packet) -> None: ...
