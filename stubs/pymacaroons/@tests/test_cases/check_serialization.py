"""Checks for serialization, using pymacaroons tests."""

from typing_extensions import assert_type

from pymacaroons import Macaroon
from pymacaroons.serializers import BinarySerializer, JsonSerializer

macaroons = [Macaroon.deserialize(""), Macaroon.deserialize("", JsonSerializer()), Macaroon.deserialize("", BinarySerializer())]

for macaroon in macaroons:
    assert_type(macaroon.serialize(), str)
    assert_type(macaroon.serialize(None), str)
    assert_type(macaroon.serialize(JsonSerializer()), str)
    assert_type(macaroon.serialize(BinarySerializer()), str)
