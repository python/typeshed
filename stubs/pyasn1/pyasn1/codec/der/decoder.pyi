from pyasn1.codec.ber import decoder as ber_decoder
from pyasn1.codec.cer import decoder
from pyasn1.type.tag import TagSet

class BitStringDecoder(decoder.BitStringDecoder):
    supportConstructedForm: bool

class OctetStringDecoder(decoder.OctetStringDecoder):
    supportConstructedForm: bool

tagMap: dict[TagSet, ber_decoder.AbstractDecoder]
typeMap: dict[int, ber_decoder.AbstractDecoder]

class Decoder(decoder.Decoder):
    supportIndefLength: bool

decode: Decoder
