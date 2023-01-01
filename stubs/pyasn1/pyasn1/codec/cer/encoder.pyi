from _typeshed import Incomplete

from pyasn1.codec.ber import encoder

class BooleanEncoder(encoder.IntegerEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class RealEncoder(encoder.RealEncoder): ...

class TimeEncoderMixIn:
    Z_CHAR: Incomplete
    PLUS_CHAR: Incomplete
    MINUS_CHAR: Incomplete
    COMMA_CHAR: Incomplete
    DOT_CHAR: Incomplete
    ZERO_CHAR: Incomplete
    MIN_LENGTH: int
    MAX_LENGTH: int
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class GeneralizedTimeEncoder(TimeEncoderMixIn, encoder.OctetStringEncoder):
    MIN_LENGTH: int
    MAX_LENGTH: int

class UTCTimeEncoder(TimeEncoderMixIn, encoder.OctetStringEncoder):
    MIN_LENGTH: int
    MAX_LENGTH: int

class SetOfEncoder(encoder.SequenceOfEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class SequenceOfEncoder(encoder.SequenceOfEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class SetEncoder(encoder.SequenceEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class SequenceEncoder(encoder.SequenceEncoder):
    omitEmptyOptionals: bool

class Encoder(encoder.Encoder):
    fixedDefLengthMode: bool
    fixedChunkSize: int

encode: Encoder
