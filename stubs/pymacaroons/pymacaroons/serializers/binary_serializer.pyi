from typing import NamedTuple

from pymacaroons import Macaroon
from pymacaroons.serializers.base_serializer import BaseSerializer

class PacketV2(NamedTuple):
    field_type: int
    data: bytes | None

class BinarySerializer(BaseSerializer):
    PACKET_PREFIX_LENGTH: int
    def serialize(self, macaroon: Macaroon) -> str: ...
    def serialize_raw(self, macaroon: Macaroon) -> bytes: ...
    def deserialize(self, serialized: str | bytes) -> Macaroon: ...
    def deserialize_raw(self, serialized: bytes) -> Macaroon: ...
