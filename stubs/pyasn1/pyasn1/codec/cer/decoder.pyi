from _typeshed import Incomplete

from pyasn1.codec.ber import decoder

class BooleanDecoder(decoder.AbstractSimpleDecoder):
    protoComponent: Incomplete
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: Incomplete | None = ...,
        length: Incomplete | None = ...,
        state: Incomplete | None = ...,
        decodeFun: Incomplete | None = ...,
        substrateFun: Incomplete | None = ...,
        **options,
    ): ...

BitStringDecoder = decoder.BitStringDecoder
OctetStringDecoder = decoder.OctetStringDecoder
RealDecoder = decoder.RealDecoder

class Decoder(decoder.Decoder): ...

decode: Decoder
