import datetime
from abc import ABCMeta, abstractmethod
from enum import Enum
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
from typing import Any, Dict, Generator, List, Optional, Union

from cryptography.hazmat.backends.interfaces import X509Backend
from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateKey, DSAPublicKey
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey, EllipticCurvePublicKey
from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PrivateKey, Ed448PublicKey
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives.hashes import HashAlgorithm
from cryptography.hazmat.primitives.serialization import Encoding

class ObjectIdentifier:
    def dotted_string(self) -> str: ...

class CRLEntryExtensionOID(object):
    CERTIFICATE_ISSUER: ObjectIdentifier
    CRL_REASON: ObjectIdentifier
    INVALIDITY_DATE: ObjectIdentifier

class ExtensionOID:
    AUTHORITY_INFORMATION_ACCESS: ObjectIdentifier
    AUTHORITY_KEY_IDENTIFIER: ObjectIdentifier
    BASIC_CONSTRAINTS: ObjectIdentifier
    CERTIFICATE_POLICIES: ObjectIdentifier
    CRL_DISTRIBUTION_POINTS: ObjectIdentifier
    CRL_NUMBER: ObjectIdentifier
    DELTA_CRL_INDICATOR: ObjectIdentifier
    EXTENDED_KEY_USAGE: ObjectIdentifier
    FRESHEST_CRL: ObjectIdentifier
    INHIBIT_ANY_POLICY: ObjectIdentifier
    ISSUER_ALTERNATIVE_NAME: ObjectIdentifier
    ISSUING_DISTRIBUTION_POINT: ObjectIdentifier
    KEY_USAGE: ObjectIdentifier
    NAME_CONSTRAINTS: ObjectIdentifier
    OCSP_NO_CHECK: ObjectIdentifier
    POLICY_CONSTRAINTS: ObjectIdentifier
    POLICY_MAPPINGS: ObjectIdentifier
    PRECERT_POISON: ObjectIdentifier
    PRECERT_SIGNED_CERTIFICATE_TIMESTAMPS: ObjectIdentifier
    SUBJECT_ALTERNATIVE_NAME: ObjectIdentifier
    SUBJECT_DIRECTORY_ATTRIBUTES: ObjectIdentifier
    SUBJECT_INFORMATION_ACCESS: ObjectIdentifier
    SUBJECT_KEY_IDENTIFIER: ObjectIdentifier
    TLS_FEATURE: ObjectIdentifier

class NameOID:
    BUSINESS_CATEGORY: ObjectIdentifier
    COMMON_NAME: ObjectIdentifier
    COUNTRY_NAME: ObjectIdentifier
    DN_QUALIFIER: ObjectIdentifier
    DOMAIN_COMPONENT: ObjectIdentifier
    EMAIL_ADDRESS: ObjectIdentifier
    GENERATION_QUALIFIER: ObjectIdentifier
    GIVEN_NAME: ObjectIdentifier
    JURISDICTION_COUNTRY_NAME: ObjectIdentifier
    JURISDICTION_LOCALITY_NAME: ObjectIdentifier
    JURISDICTION_STATE_OR_PROVINCE_NAME: ObjectIdentifier
    LOCALITY_NAME: ObjectIdentifier
    ORGANIZATIONAL_UNIT_NAME: ObjectIdentifier
    ORGANIZATION_NAME: ObjectIdentifier
    POSTAL_ADDRESS: ObjectIdentifier
    POSTAL_CODE: ObjectIdentifier
    PSEUDONYM: ObjectIdentifier
    SERIAL_NUMBER: ObjectIdentifier
    STATE_OR_PROVINCE_NAME: ObjectIdentifier
    STREET_ADDRESS: ObjectIdentifier
    SURNAME: ObjectIdentifier
    TITLE: ObjectIdentifier
    USER_ID: ObjectIdentifier
    X500_UNIQUE_IDENTIFIER: ObjectIdentifier

class OCSPExtensionOID:
    NONCE: ObjectIdentifier

class SignatureAlgorithmOID:
    DSA_WITH_SHA1: ObjectIdentifier
    DSA_WITH_SHA224: ObjectIdentifier
    DSA_WITH_SHA256: ObjectIdentifier
    ECDSA_WITH_SHA1: ObjectIdentifier
    ECDSA_WITH_SHA224: ObjectIdentifier
    ECDSA_WITH_SHA256: ObjectIdentifier
    ECDSA_WITH_SHA384: ObjectIdentifier
    ECDSA_WITH_SHA512: ObjectIdentifier
    ED25519: ObjectIdentifier
    ED448: ObjectIdentifier
    RSASSA_PSS: ObjectIdentifier
    RSA_WITH_MD5: ObjectIdentifier
    RSA_WITH_SHA1: ObjectIdentifier
    RSA_WITH_SHA224: ObjectIdentifier
    RSA_WITH_SHA256: ObjectIdentifier
    RSA_WITH_SHA384: ObjectIdentifier
    RSA_WITH_SHA512: ObjectIdentifier

class NameAttribute:
    oid: ObjectIdentifier
    value: str
    def __init__(self, oid: ObjectIdentifier, value: str) -> None: ...
    def rfc4514_string(self) -> str: ...

class RelativeDistinguishedName:
    def __init__(self, attributes: List[NameAttribute]) -> None: ...
    def __iter__(self) -> Generator[NameAttribute, None, None]: ...
    def get_attributes_for_oid(self, oid: ObjectIdentifier) -> List[NameAttribute]: ...
    def rfc4514_string(self) -> str: ...

class Name:
    rdns: List[RelativeDistinguishedName]
    def __init__(self, attributes: List[Union[NameAttribute, RelativeDistinguishedName]]) -> None: ...
    def __iter__(self) -> Generator[NameAttribute, None, None]: ...
    def get_attributes_for_oid(self, oid: ObjectIdentifier) -> List[NameAttribute]: ...
    def public_bytes(self, backend: X509Backend) -> bytes: ...
    def rfc4514_string(self) -> str: ...

class Version(Enum):
    v1: int
    v3: int

class Certificate(metaclass=ABCMeta):
    extensions: Extensions
    issuer: Name
    not_valid_after: datetime.datetime
    not_valid_before: datetime.datetime
    serial_number: int
    signature: bytes
    signature_algorithm_oid: ObjectIdentifier
    signature_hash_algorithm: HashAlgorithm
    tbs_certificate_bytes: bytes
    subject: Name
    version: Version
    @abstractmethod
    def fingerprint(self, algorithm: HashAlgorithm) -> bytes: ...
    @abstractmethod
    def public_bytes(self, encoding: Encoding) -> bytes: ...
    @abstractmethod
    def public_key(self) -> Union[DSAPublicKey, Ed25519PublicKey, Ed448PublicKey, EllipticCurvePublicKey, RSAPublicKey]: ...

class CertificateBuilder:
    def add_extension(self, extension: ExtensionType, critical: bool) -> CertificateBuilder: ...
    def issuer_name(self, name: Name) -> CertificateBuilder: ...
    def not_valid_after(self, time: datetime.datetime) -> CertificateBuilder: ...
    def not_valid_before(self, time: datetime.datetime) -> CertificateBuilder: ...
    def public_key(
        self, public_key: Union[DSAPublicKey, Ed25519PublicKey, Ed448PublicKey, EllipticCurvePublicKey, RSAPublicKey]
    ) -> CertificateBuilder: ...
    def serial_number(self, serial_number: int) -> CertificateBuilder: ...
    def sign(
        self,
        private_key: Union[DSAPrivateKey, Ed25519PrivateKey, Ed448PrivateKey, EllipticCurvePrivateKey, RSAPrivateKey],
        algorithm: Optional[HashAlgorithm],
        backend: X509Backend,
    ) -> Certificate: ...
    def subject_name(self, name: Name) -> CertificateBuilder: ...

class CertificateRevocationList(metaclass=ABCMeta):
    extensions: Extensions
    issuer: Name
    last_update: datetime.datetime
    next_update: datetime.datetime
    signature: bytes
    signature_algorithm_oid: ObjectIdentifier
    signature_hash_algorithm: HashAlgorithm
    tbs_certlist_bytes: bytes
    @abstractmethod
    def fingerprint(self, algorithm: HashAlgorithm) -> bytes: ...
    @abstractmethod
    def get_revoked_certificate_by_serial_number(self, serial_number: int) -> RevokedCertificate: ...
    @abstractmethod
    def is_signature_valid(
        self, public_key: Union[DSAPublicKey, Ed25519PublicKey, Ed448PublicKey, EllipticCurvePublicKey, RSAPublicKey]
    ) -> bool: ...
    @abstractmethod
    def public_bytes(self, encoding: Encoding) -> bytes: ...

class CertificateRevocationListBuilder:
    def add_extension(self, extension: ExtensionType, critical: bool) -> CertificateRevocationListBuilder: ...
    def add_revoked_certificate(self, revoked_certificate: RevokedCertificate) -> CertificateRevocationListBuilder: ...
    def issuer_name(self, name: Name) -> CertificateRevocationListBuilder: ...
    def last_update(self, time: datetime.datetime) -> CertificateRevocationListBuilder: ...
    def next_update(self, time: datetime.datetime) -> CertificateRevocationListBuilder: ...
    def sign(
        self,
        private_key: Union[DSAPrivateKey, Ed25519PrivateKey, Ed448PrivateKey, EllipticCurvePrivateKey, RSAPrivateKey],
        algorithm: Optional[HashAlgorithm],
        backend: X509Backend,
    ) -> CertificateRevocationList: ...

class CertificateSigningRequest(metaclass=ABCMeta):
    extensions: Extensions
    is_signature_valid: bool
    signature: bytes
    signature_algorithm_oid: ObjectIdentifier
    signature_hash_algorithm: HashAlgorithm
    subject: Name
    tbs_certrequest_bytes: bytes
    @abstractmethod
    def public_bytes(self) -> bytes: ...
    @abstractmethod
    def public_key(self) -> Union[DSAPublicKey, Ed25519PublicKey, Ed448PublicKey, EllipticCurvePublicKey, RSAPublicKey]: ...

class CertificateSigningRequestBuilder:
    def add_extension(self, extension: ExtensionType, critical: bool) -> CertificateSigningRequestBuilder: ...
    def subject_name(self, name: Name) -> CertificateSigningRequestBuilder: ...
    def sign(
        self,
        private_key: Union[DSAPrivateKey, Ed25519PrivateKey, Ed448PrivateKey, EllipticCurvePrivateKey, RSAPrivateKey],
        algorithm: Optional[HashAlgorithm],
        backend: X509Backend,
    ) -> CertificateSigningRequest: ...

class RevokedCertificate(metaclass=ABCMeta):
    extensions: Extensions
    revocation_date: datetime.datetime
    serial_number: int

class RevokedCertificateBuilder:
    def add_extension(self, extension: ExtensionType, critical: bool) -> RevokedCertificateBuilder: ...
    def build(self, backend: X509Backend) -> RevokedCertificate: ...
    def revocation_date(self, time: datetime.datetime) -> RevokedCertificateBuilder: ...
    def serial_number(self, serial_number: int) -> RevokedCertificateBuilder: ...

# General Name Classes

class GeneralName(metaclass=ABCMeta): ...

class DirectoryName(GeneralName):
    value: Name
    def __init__(self, value: Name) -> None: ...

class DNSName(GeneralName):
    value: str
    def __init__(self, value: str) -> None: ...

class IPAddress(GeneralName):
    value: Union[IPv4Address, IPv6Address, IPv4Network, IPv6Network]
    def __init__(self, value: Union[IPv4Address, IPv6Address, IPv4Network, IPv6Network]) -> None: ...

class OtherName(GeneralName):
    type_id: ObjectIdentifier
    value: bytes
    def __init__(self, type_id: ObjectIdentifier, value: bytes) -> None: ...

class RegisteredID(GeneralName):
    value: ObjectIdentifier
    def __init__(self, value: ObjectIdentifier) -> None: ...

class RFC822Name(GeneralName):
    value: str
    def __init__(self, value: str) -> None: ...

class UniformResourceIdentifier(GeneralName):
    value: str
    def __init__(self, value: str) -> None: ...

# X.509 Extensions

class Extension:
    critical: bool
    oid: ExtensionOID
    value: ExtensionType

class ExtensionType(metaclass=ABCMeta):
    oid: ExtensionOID

class Extensions:
    def __init__(self, general_names: List[Extension]) -> None: ...
    def __iter__(self) -> Generator[Extension, None, None]: ...
    def get_extension_for_oid(self, oid: ObjectIdentifier) -> Extension: ...
    def get_extension_for_class(self, extclass: ExtensionType) -> Extension: ...

class IssuerAlternativeName(ExtensionType):
    def __init__(self, general_names: List[GeneralName]) -> None: ...
    def __iter__(self) -> Generator[GeneralName, None, None]: ...

class SubjectAlternativeName(ExtensionType):
    def __init__(self, general_names: List[GeneralName]) -> None: ...
    def __iter__(self) -> Generator[GeneralName, None, None]: ...

def load_der_x509_certificate(data: bytes, backend: X509Backend) -> Certificate: ...
def load_pem_x509_certificate(data: bytes, backend: X509Backend) -> Certificate: ...
def load_der_x509_crl(data: bytes, backend: X509Backend) -> CertificateRevocationList: ...
def load_pem_x509_crl(data: bytes, backend: X509Backend) -> CertificateRevocationList: ...
def load_der_x509_csr(data: bytes, backend: X509Backend) -> CertificateSigningRequest: ...
def load_pem_x509_csr(data: bytes, backend: X509Backend) -> CertificateSigningRequest: ...
def __getattr__(name: str) -> Any: ...  # incomplete
