from _typeshed import Incomplete

from pyasn1.type import univ

maxInt: Incomplete

class LDAPString(univ.OctetString): ...
class LDAPOID(univ.OctetString): ...
class LDAPDN(LDAPString): ...
class RelativeLDAPDN(LDAPString): ...
class AttributeType(LDAPString): ...
class AttributeDescription(LDAPString): ...

class AttributeDescriptionList(univ.SequenceOf):
    componentType: Incomplete

class AttributeValue(univ.OctetString): ...
class AssertionValue(univ.OctetString): ...

class AttributeValueAssertion(univ.Sequence):
    componentType: Incomplete

class Attribute(univ.Sequence):
    componentType: Incomplete

class MatchingRuleId(LDAPString): ...

class Control(univ.Sequence):
    componentType: Incomplete

class Controls(univ.SequenceOf):
    componentType: Incomplete

class LDAPURL(LDAPString): ...

class Referral(univ.SequenceOf):
    componentType: Incomplete

class SaslCredentials(univ.Sequence):
    componentType: Incomplete

class AuthenticationChoice(univ.Choice):
    componentType: Incomplete

class BindRequest(univ.Sequence):
    tagSet: Incomplete
    componentType: Incomplete

class PartialAttributeList(univ.SequenceOf):
    componentType: Incomplete

class SearchResultEntry(univ.Sequence):
    tagSet: Incomplete
    componentType: Incomplete

class MatchingRuleAssertion(univ.Sequence):
    componentType: Incomplete

class SubstringFilter(univ.Sequence):
    componentType: Incomplete

class Filter3(univ.Choice):
    componentType: Incomplete

class Filter2(univ.Choice):
    componentType: Incomplete

class Filter(univ.Choice):
    componentType: Incomplete

class SearchRequest(univ.Sequence):
    tagSet: Incomplete
    componentType: Incomplete

class UnbindRequest(univ.Null):
    tagSet: Incomplete

class BindResponse(univ.Sequence):
    tagSet: Incomplete
    componentType: Incomplete

class LDAPResult(univ.Sequence):
    componentType: Incomplete

class SearchResultReference(univ.SequenceOf):
    tagSet: Incomplete
    componentType: Incomplete

class SearchResultDone(LDAPResult):
    tagSet: Incomplete

class AttributeTypeAndValues(univ.Sequence):
    componentType: Incomplete

class ModifyRequest(univ.Sequence):
    tagSet: Incomplete
    componentType: Incomplete

class ModifyResponse(LDAPResult):
    tagSet: Incomplete

class AttributeList(univ.SequenceOf):
    componentType: Incomplete

class AddRequest(univ.Sequence):
    tagSet: Incomplete
    componentType: Incomplete

class AddResponse(LDAPResult):
    tagSet: Incomplete

class DelRequest(LDAPResult):
    tagSet: Incomplete

class DelResponse(LDAPResult):
    tagSet: Incomplete

class ModifyDNRequest(univ.Sequence):
    tagSet: Incomplete
    componentType: Incomplete

class ModifyDNResponse(LDAPResult):
    tagSet: Incomplete

class CompareRequest(univ.Sequence):
    tagSet: Incomplete
    componentType: Incomplete

class CompareResponse(LDAPResult):
    tagSet: Incomplete

class AbandonRequest(LDAPResult):
    tagSet: Incomplete

class ExtendedRequest(univ.Sequence):
    tagSet: Incomplete
    componentType: Incomplete

class ExtendedResponse(univ.Sequence):
    tagSet: Incomplete
    componentType: Incomplete

class MessageID(univ.Integer):
    subtypeSpec: Incomplete

class LDAPMessage(univ.Sequence):
    componentType: Incomplete
