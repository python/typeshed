from pyasn1.codec.ber import encoder as ber_encoder
from pyasn1.codec.cer import encoder
from pyasn1.type.tag import TagSet

class SetEncoder(encoder.SetEncoder): ...

tagMap: dict[TagSet, ber_encoder.AbstractItemEncoder]
typeMap: dict[int, ber_encoder.AbstractItemEncoder]

class Encoder(encoder.Encoder):
    fixedDefLengthMode: bool
    fixedChunkSize: int

encode: Encoder
