from _typeshed import Incomplete

class AbstractDecoder:
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
    ) -> None: ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: Incomplete | None = ...,
        length: Incomplete | None = ...,
        state: Incomplete | None = ...,
        decodeFun: Incomplete | None = ...,
        substrateFun: Incomplete | None = ...,
        **options,
    ) -> None: ...

class AbstractSimpleDecoder(AbstractDecoder):
    @staticmethod
    def substrateCollector(asn1Object, substrate, length): ...

class ExplicitTagDecoder(AbstractSimpleDecoder):
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
    def indefLenValueDecoder(
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

class IntegerDecoder(AbstractSimpleDecoder):
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

class BooleanDecoder(IntegerDecoder):
    protoComponent: Incomplete

class BitStringDecoder(AbstractSimpleDecoder):
    protoComponent: Incomplete
    supportConstructedForm: bool
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
    def indefLenValueDecoder(
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

class OctetStringDecoder(AbstractSimpleDecoder):
    protoComponent: Incomplete
    supportConstructedForm: bool
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
    def indefLenValueDecoder(
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

class NullDecoder(AbstractSimpleDecoder):
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

class ObjectIdentifierDecoder(AbstractSimpleDecoder):
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

class RealDecoder(AbstractSimpleDecoder):
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

class AbstractConstructedDecoder(AbstractDecoder):
    protoComponent: Incomplete

class UniversalConstructedTypeDecoder(AbstractConstructedDecoder):
    protoRecordComponent: Incomplete
    protoSequenceComponent: Incomplete
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
    def indefLenValueDecoder(
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

class SequenceOrSequenceOfDecoder(UniversalConstructedTypeDecoder):
    protoRecordComponent: Incomplete
    protoSequenceComponent: Incomplete

class SequenceDecoder(SequenceOrSequenceOfDecoder):
    protoComponent: Incomplete

class SequenceOfDecoder(SequenceOrSequenceOfDecoder):
    protoComponent: Incomplete

class SetOrSetOfDecoder(UniversalConstructedTypeDecoder):
    protoRecordComponent: Incomplete
    protoSequenceComponent: Incomplete

class SetDecoder(SetOrSetOfDecoder):
    protoComponent: Incomplete

class SetOfDecoder(SetOrSetOfDecoder):
    protoComponent: Incomplete

class ChoiceDecoder(AbstractConstructedDecoder):
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
    def indefLenValueDecoder(
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

class AnyDecoder(AbstractSimpleDecoder):
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
    def indefLenValueDecoder(
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

class UTF8StringDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class NumericStringDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class PrintableStringDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class TeletexStringDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class VideotexStringDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class IA5StringDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class GraphicStringDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class VisibleStringDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class GeneralStringDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class UniversalStringDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class BMPStringDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class ObjectDescriptorDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class GeneralizedTimeDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class UTCTimeDecoder(OctetStringDecoder):
    protoComponent: Incomplete

class Decoder:
    defaultErrorState: Incomplete
    defaultRawDecoder: Incomplete
    supportIndefLength: bool
    def __init__(self, tagMap, typeMap=...) -> None: ...
    def __call__(
        self,
        substrate,
        asn1Spec: Incomplete | None = ...,
        tagSet: Incomplete | None = ...,
        length: Incomplete | None = ...,
        state=...,
        decodeFun: Incomplete | None = ...,
        substrateFun: Incomplete | None = ...,
        **options,
    ): ...

decode: Decoder
