import datetime
from _typeshed import Self
from abc import ABCMeta, abstractmethod
from collections.abc import Generator, Iterable, Sequence
from enum import Enum
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
from typing import Any, ClassVar, Generic, TypeVar

from cryptography.hazmat.backends.interfaces import X509Backend
from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateKey, DSAPublicKey
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey, EllipticCurvePublicKey
from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PrivateKey, Ed448PublicKey
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives.hashes import HashAlgorithm
from cryptography.hazmat.primitives.serialization import Encoding

class ObjectIdentifier:
    @property
    def dotted_string(self) -> str: ...
    def __init__(self, dotted_string: str) -> None: ...

class CRLEntryExtensionOID:
    CERTIFICATE_ISSUER: ClassVar[ObjectIdentifier]
    CRL_REASON: ClassVar[ObjectIdentifier]
    INVALIDITY_DATE: ClassVar[ObjectIdentifier]

class ExtensionOID:
    AUTHORITY_INFORMATION_ACCESS: ClassVar[ObjectIdentifier]
    AUTHORITY_KEY_IDENTIFIER: ClassVar[ObjectIdentifier]
    BASIC_CONSTRAINTS: ClassVar[ObjectIdentifier]
    CERTIFICATE_POLICIES: ClassVar[ObjectIdentifier]
    CRL_DISTRIBUTION_POINTS: ClassVar[ObjectIdentifier]
    CRL_NUMBER: ClassVar[ObjectIdentifier]
    DELTA_CRL_INDICATOR: ClassVar[ObjectIdentifier]
    EXTENDED_KEY_USAGE: ClassVar[ObjectIdentifier]
    FRESHEST_CRL: ClassVar[ObjectIdentifier]
    INHIBIT_ANY_POLICY: ClassVar[ObjectIdentifier]
    ISSUER_ALTERNATIVE_NAME: ClassVar[ObjectIdentifier]
    ISSUING_DISTRIBUTION_POINT: ClassVar[ObjectIdentifier]
    KEY_USAGE: ClassVar[ObjectIdentifier]
    NAME_CONSTRAINTS: ClassVar[ObjectIdentifier]
    OCSP_NO_CHECK: ClassVar[ObjectIdentifier]
    POLICY_CONSTRAINTS: ClassVar[ObjectIdentifier]
    POLICY_MAPPINGS: ClassVar[ObjectIdentifier]
    PRECERT_POISON: ClassVar[ObjectIdentifier]
    PRECERT_SIGNED_CERTIFICATE_TIMESTAMPS: ClassVar[ObjectIdentifier]
    SUBJECT_ALTERNATIVE_NAME: ClassVar[ObjectIdentifier]
    SUBJECT_DIRECTORY_ATTRIBUTES: ClassVar[ObjectIdentifier]
    SUBJECT_INFORMATION_ACCESS: ClassVar[ObjectIdentifier]
    SUBJECT_KEY_IDENTIFIER: ClassVar[ObjectIdentifier]
    TLS_FEATURE: ClassVar[ObjectIdentifier]

class NameOID:
    BUSINESS_CATEGORY: ClassVar[ObjectIdentifier]
    COMMON_NAME: ClassVar[ObjectIdentifier]
    COUNTRY_NAME: ClassVar[ObjectIdentifier]
    DN_QUALIFIER: ClassVar[ObjectIdentifier]
    DOMAIN_COMPONENT: ClassVar[ObjectIdentifier]
    EMAIL_ADDRESS: ClassVar[ObjectIdentifier]
    GENERATION_QUALIFIER: ClassVar[ObjectIdentifier]
    GIVEN_NAME: ClassVar[ObjectIdentifier]
    JURISDICTION_COUNTRY_NAME: ClassVar[ObjectIdentifier]
    JURISDICTION_LOCALITY_NAME: ClassVar[ObjectIdentifier]
    JURISDICTION_STATE_OR_PROVINCE_NAME: ClassVar[ObjectIdentifier]
    LOCALITY_NAME: ClassVar[ObjectIdentifier]
    ORGANIZATIONAL_UNIT_NAME: ClassVar[ObjectIdentifier]
    ORGANIZATION_NAME: ClassVar[ObjectIdentifier]
    POSTAL_ADDRESS: ClassVar[ObjectIdentifier]
    POSTAL_CODE: ClassVar[ObjectIdentifier]
    PSEUDONYM: ClassVar[ObjectIdentifier]
    SERIAL_NUMBER: ClassVar[ObjectIdentifier]
    STATE_OR_PROVINCE_NAME: ClassVar[ObjectIdentifier]
    STREET_ADDRESS: ClassVar[ObjectIdentifier]
    SURNAME: ClassVar[ObjectIdentifier]
    TITLE: ClassVar[ObjectIdentifier]
    USER_ID: ClassVar[ObjectIdentifier]
    X500_UNIQUE_IDENTIFIER: ClassVar[ObjectIdentifier]

class OCSPExtensionOID:
    NONCE: ClassVar[ObjectIdentifier]

class SignatureAlgorithmOID:
    DSA_WITH_SHA1: ClassVar[ObjectIdentifier]
    DSA_WITH_SHA224: ClassVar[ObjectIdentifier]
    DSA_WITH_SHA256: ClassVar[ObjectIdentifier]
    ECDSA_WITH_SHA1: ClassVar[ObjectIdentifier]
    ECDSA_WITH_SHA224: ClassVar[ObjectIdentifier]
    ECDSA_WITH_SHA256: ClassVar[ObjectIdentifier]
    ECDSA_WITH_SHA384: ClassVar[ObjectIdentifier]
    ECDSA_WITH_SHA512: ClassVar[ObjectIdentifier]
    ED25519: ClassVar[ObjectIdentifier]
    ED448: ClassVar[ObjectIdentifier]
    RSASSA_PSS: ClassVar[ObjectIdentifier]
    RSA_WITH_MD5: ClassVar[ObjectIdentifier]
    RSA_WITH_SHA1: ClassVar[ObjectIdentifier]
    RSA_WITH_SHA224: ClassVar[ObjectIdentifier]
    RSA_WITH_SHA256: ClassVar[ObjectIdentifier]
    RSA_WITH_SHA384: ClassVar[ObjectIdentifier]
    RSA_WITH_SHA512: ClassVar[ObjectIdentifier]

class ExtendedKeyUsageOID:
    SERVER_AUTH: ClassVar[ObjectIdentifier]
    CLIENT_AUTH: ClassVar[ObjectIdentifier]
    CODE_SIGNING: ClassVar[ObjectIdentifier]
    EMAIL_PROTECTION: ClassVar[ObjectIdentifier]
    TIME_STAMPING: ClassVar[ObjectIdentifier]
    OCSP_SIGNING: ClassVar[ObjectIdentifier]
    ANY_EXTENDED_KEY_USAGE: ClassVar[ObjectIdentifier]

class NameAttribute:
    @property
    def oid(self) -> ObjectIdentifier: ...
    @property
    def value(self) -> str: ...
    def __init__(self, oid: ObjectIdentifier, value: str) -> None: ...
    def rfc4514_string(self) -> str: ...

class RelativeDistinguishedName:
    def __init__(self, attributes: list[NameAttribute]) -> None: ...
    def __iter__(self) -> Generator[NameAttribute, None, None]: ...
    def get_attributes_for_oid(self, oid: ObjectIdentifier) -> list[NameAttribute]: ...
    def rfc4514_string(self) -> str: ...

class Name:
    @property
    def rdns(self) -> list[RelativeDistinguishedName]: ...
    def __init__(self, attributes: Sequence[NameAttribute | RelativeDistinguishedName]) -> None: ...
    def __iter__(self) -> Generator[NameAttribute, None, None]: ...
    def __len__(self) -> int: ...
    def get_attributes_for_oid(self, oid: ObjectIdentifier) -> list[NameAttribute]: ...
    def public_bytes(self, backend: X509Backend | None = ...) -> bytes: ...
    def rfc4514_string(self) -> str: ...

class Version(Enum):
    v1: int
    v3: int

# These are actually abstractproperties on Certificate,
# but let's not worry too much about that
class Certificate(metaclass=ABCMeta):
    @property
    def extensions(self) -> Extensions: ...
    @property
    def issuer(self) -> Name: ...
    @property
    def not_valid_after(self) -> datetime.datetime: ...
    @property
    def not_valid_before(self) -> datetime.datetime: ...
    @property
    def serial_number(self) -> int: ...
    @property
    def signature(self) -> bytes: ...
    @property
    def signature_algorithm_oid(self) -> ObjectIdentifier: ...
    @property
    def signature_hash_algorithm(self) -> HashAlgorithm: ...
    @property
    def tbs_certificate_bytes(self) -> bytes: ...
    @property
    def subject(self) -> Name: ...
    @property
    def version(self) -> Version: ...
    @abstractmethod
    def fingerprint(self, algorithm: HashAlgorithm) -> bytes: ...
    @abstractmethod
    def public_bytes(self, encoding: Encoding) -> bytes: ...
    @abstractmethod
    def public_key(self) -> DSAPublicKey | Ed25519PublicKey | Ed448PublicKey | EllipticCurvePublicKey | RSAPublicKey: ...
    @abstractmethod
    def __eq__(self, __other: object) -> bool: ...
    @abstractmethod
    def __ne__(self, __other: object) -> bool: ...

class CertificateBuilder:
    def __init__(
        self,
        issuer_name: Name | None = ...,
        subject_name: Name | None = ...,
        public_key: DSAPublicKey | Ed25519PublicKey | Ed448PublicKey | EllipticCurvePublicKey | RSAPublicKey | None = ...,
        serial_number: int | None = ...,
        not_valid_before: datetime.datetime | None = ...,
        not_valid_after: datetime.datetime | None = ...,
        extensions: Iterable[ExtensionType] | None = ...,
    ) -> None: ...
    def add_extension(self, extension: ExtensionType, critical: bool) -> CertificateBuilder: ...
    def issuer_name(self, name: Name) -> CertificateBuilder: ...
    def not_valid_after(self, time: datetime.datetime) -> CertificateBuilder: ...
    def not_valid_before(self, time: datetime.datetime) -> CertificateBuilder: ...
    def public_key(
        self, public_key: DSAPublicKey | Ed25519PublicKey | Ed448PublicKey | EllipticCurvePublicKey | RSAPublicKey
    ) -> CertificateBuilder: ...
    def serial_number(self, serial_number: int) -> CertificateBuilder: ...
    def sign(
        self,
        private_key: DSAPrivateKey | Ed25519PrivateKey | Ed448PrivateKey | EllipticCurvePrivateKey | RSAPrivateKey,
        algorithm: HashAlgorithm | None,
        backend: X509Backend | None = ...,
    ) -> Certificate: ...
    def subject_name(self, name: Name) -> CertificateBuilder: ...

class CertificateRevocationList(metaclass=ABCMeta):
    @property
    def extensions(self) -> Extensions: ...
    @property
    def issuer(self) -> Name: ...
    @property
    def last_update(self) -> datetime.datetime: ...
    @property
    def next_update(self) -> datetime.datetime: ...
    @property
    def signature(self) -> bytes: ...
    @property
    def signature_algorithm_oid(self) -> ObjectIdentifier: ...
    @property
    def signature_hash_algorithm(self) -> HashAlgorithm: ...
    @property
    def tbs_certlist_bytes(self) -> bytes: ...
    @abstractmethod
    def fingerprint(self, algorithm: HashAlgorithm) -> bytes: ...
    @abstractmethod
    def get_revoked_certificate_by_serial_number(self, serial_number: int) -> RevokedCertificate: ...
    @abstractmethod
    def is_signature_valid(
        self, public_key: DSAPublicKey | Ed25519PublicKey | Ed448PublicKey | EllipticCurvePublicKey | RSAPublicKey
    ) -> bool: ...
    @abstractmethod
    def public_bytes(self, encoding: Encoding) -> bytes: ...
    @abstractmethod
    def __eq__(self, __other: object) -> bool: ...
    @abstractmethod
    def __ne__(self, __other: object) -> bool: ...

class CertificateRevocationListBuilder:
    def add_extension(self, extension: ExtensionType, critical: bool) -> CertificateRevocationListBuilder: ...
    def add_revoked_certificate(self, revoked_certificate: RevokedCertificate) -> CertificateRevocationListBuilder: ...
    def issuer_name(self, name: Name) -> CertificateRevocationListBuilder: ...
    def last_update(self, time: datetime.datetime) -> CertificateRevocationListBuilder: ...
    def next_update(self, time: datetime.datetime) -> CertificateRevocationListBuilder: ...
    def sign(
        self,
        private_key: DSAPrivateKey | Ed25519PrivateKey | Ed448PrivateKey | EllipticCurvePrivateKey | RSAPrivateKey,
        algorithm: HashAlgorithm | None,
        backend: X509Backend | None = ...,
    ) -> CertificateRevocationList: ...

class CertificateSigningRequest(metaclass=ABCMeta):
    @property
    def extensions(self) -> Extensions: ...
    @property
    def is_signature_valid(self) -> bool: ...
    @property
    def signature(self) -> bytes: ...
    @property
    def signature_algorithm_oid(self) -> ObjectIdentifier: ...
    @property
    def signature_hash_algorithm(self) -> HashAlgorithm: ...
    @property
    def subject(self) -> Name: ...
    @property
    def tbs_certrequest_bytes(self) -> bytes: ...
    @abstractmethod
    def public_bytes(self, encoding: Encoding) -> bytes: ...
    @abstractmethod
    def public_key(self) -> DSAPublicKey | Ed25519PublicKey | Ed448PublicKey | EllipticCurvePublicKey | RSAPublicKey: ...
    @abstractmethod
    def __eq__(self, __other: object) -> bool: ...
    @abstractmethod
    def __ne__(self, __other: object) -> bool: ...

class CertificateSigningRequestBuilder:
    def add_extension(self, extension: ExtensionType, critical: bool) -> CertificateSigningRequestBuilder: ...
    def subject_name(self, name: Name) -> CertificateSigningRequestBuilder: ...
    def sign(
        self,
        private_key: DSAPrivateKey | Ed25519PrivateKey | Ed448PrivateKey | EllipticCurvePrivateKey | RSAPrivateKey,
        algorithm: HashAlgorithm | None,
        backend: X509Backend | None = ...,
    ) -> CertificateSigningRequest: ...

class RevokedCertificate(metaclass=ABCMeta):
    @property
    def extensions(self) -> Extensions: ...
    @property
    def revocation_date(self) -> datetime.datetime: ...
    @property
    def serial_number(self) -> int: ...

class RevokedCertificateBuilder:
    def add_extension(self, extension: ExtensionType, critical: bool) -> RevokedCertificateBuilder: ...
    def build(self, backend: X509Backend | None = ...) -> RevokedCertificate: ...
    def revocation_date(self, time: datetime.datetime) -> RevokedCertificateBuilder: ...
    def serial_number(self, serial_number: int) -> RevokedCertificateBuilder: ...

# General Name Classes

class GeneralName(metaclass=ABCMeta):
    @property
    def value(self): ...

class DirectoryName(GeneralName):
    @property
    def value(self) -> Name: ...
    def __init__(self, value: Name) -> None: ...

class DNSName(GeneralName):
    @property
    def value(self) -> str: ...
    def __init__(self, value: str) -> None: ...

class IPAddress(GeneralName):
    @property
    def value(self) -> IPv4Address | IPv6Address | IPv4Network | IPv6Network: ...
    def __init__(self, value: IPv4Address | IPv6Address | IPv4Network | IPv6Network) -> None: ...

class OtherName(GeneralName):
    @property
    def type_id(self) -> ObjectIdentifier: ...
    @property
    def value(self) -> bytes: ...
    def __init__(self, type_id: ObjectIdentifier, value: bytes) -> None: ...

class RegisteredID(GeneralName):
    @property
    def value(self) -> ObjectIdentifier: ...
    def __init__(self, value: ObjectIdentifier) -> None: ...

class RFC822Name(GeneralName):
    @property
    def value(self) -> str: ...
    def __init__(self, value: str) -> None: ...

class UniformResourceIdentifier(GeneralName):
    @property
    def value(self) -> str: ...
    def __init__(self, value: str) -> None: ...

# X.509 Extensions

class ExtensionType(metaclass=ABCMeta):
    oid: ObjectIdentifier

_T = TypeVar("_T", bound=ExtensionType)

class Extension(Generic[_T]):
    @property
    def critical(self) -> bool: ...
    @property
    def oid(self) -> ObjectIdentifier: ...
    @property
    def value(self) -> _T: ...

class Extensions:
    def __init__(self, general_names: list[Extension[Any]]) -> None: ...
    def __iter__(self) -> Generator[Extension[Any], None, None]: ...
    def get_extension_for_oid(self, oid: ObjectIdentifier) -> Extension[Any]: ...
    def get_extension_for_class(self, extclass: type[_T]) -> Extension[_T]: ...

class DuplicateExtension(Exception):
    oid: ObjectIdentifier
    def __init__(self, msg: str, oid: ObjectIdentifier) -> None: ...

class ExtensionNotFound(Exception):
    oid: ObjectIdentifier
    def __init__(self, msg: str, oid: ObjectIdentifier) -> None: ...

class IssuerAlternativeName(ExtensionType):
    def __init__(self, general_names: list[GeneralName]) -> None: ...
    def __iter__(self) -> Generator[GeneralName, None, None]: ...
    def get_values_for_type(self, type: type[GeneralName]) -> list[Any]: ...

class SubjectAlternativeName(ExtensionType):
    def __init__(self, general_names: list[GeneralName]) -> None: ...
    def __iter__(self) -> Generator[GeneralName, None, None]: ...
    def get_values_for_type(self, type: type[GeneralName]) -> list[Any]: ...

class AuthorityKeyIdentifier(ExtensionType):
    @property
    def key_identifier(self) -> bytes: ...
    @property
    def authority_cert_issuer(self) -> list[GeneralName] | None: ...
    @property
    def authority_cert_serial_number(self) -> int | None: ...
    def __init__(
        self, key_identifier: bytes, authority_cert_issuer: Iterable[GeneralName] | None, authority_cert_serial_number: int | None
    ) -> None: ...
    @classmethod
    def from_issuer_public_key(
        cls: type[Self], public_key: RSAPublicKey | DSAPublicKey | EllipticCurvePublicKey | Ed25519PublicKey | Ed448PublicKey
    ) -> Self: ...
    @classmethod
    def from_issuer_subject_key_identifier(cls: type[Self], ski: SubjectKeyIdentifier) -> Self: ...

class SubjectKeyIdentifier(ExtensionType):
    @property
    def digest(self) -> bytes: ...
    def __init__(self, digest: bytes) -> None: ...
    @classmethod
    def from_public_key(
        cls: type[Self], public_key: RSAPublicKey | DSAPublicKey | EllipticCurvePublicKey | Ed25519PublicKey | Ed448PublicKey
    ) -> Self: ...

class AccessDescription:
    @property
    def access_method(self) -> ObjectIdentifier: ...
    @property
    def access_location(self) -> GeneralName: ...
    def __init__(self, access_method: ObjectIdentifier, access_location: GeneralName) -> None: ...

class AuthorityInformationAccess(ExtensionType):
    def __init__(self, descriptions: Iterable[AccessDescription]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Generator[AccessDescription, None, None]: ...
    def __getitem__(self, item: int) -> AccessDescription: ...

class SubjectInformationAccess(ExtensionType):
    def __init__(self, descriptions: Iterable[AccessDescription]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Generator[AccessDescription, None, None]: ...
    def __getitem__(self, item: int) -> AccessDescription: ...

class BasicConstraints(ExtensionType):
    @property
    def ca(self) -> bool: ...
    @property
    def path_length(self) -> int | None: ...
    def __init__(self, ca: bool, path_length: int | None) -> None: ...

class KeyUsage(ExtensionType):
    @property
    def digital_signature(self) -> bool: ...
    @property
    def content_commitment(self) -> bool: ...
    @property
    def key_encipherment(self) -> bool: ...
    @property
    def data_encipherment(self) -> bool: ...
    @property
    def key_agreement(self) -> bool: ...
    @property
    def key_cert_sign(self) -> bool: ...
    @property
    def crl_sign(self) -> bool: ...
    @property
    def encipher_only(self) -> bool: ...
    @property
    def decipher_only(self) -> bool: ...
    def __init__(
        self,
        digital_signature: bool,
        content_commitment: bool,
        key_encipherment: bool,
        data_encipherment: bool,
        key_agreement: bool,
        key_cert_sign: bool,
        crl_sign: bool,
        encipher_only: bool,
        decipher_only: bool,
    ) -> None: ...

class ExtendedKeyUsage(ExtensionType):
    def __init__(self, usages: Iterable[ObjectIdentifier]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Generator[ObjectIdentifier, None, None]: ...
    def __getitem__(self, item: int) -> ObjectIdentifier: ...

class UnrecognizedExtension(ExtensionType):
    @property
    def value(self) -> bytes: ...
    @property
    def oid(self) -> ObjectIdentifier: ...  # type: ignore[override]
    def __init__(self, oid: ObjectIdentifier, value: bytes) -> None: ...

def load_der_x509_certificate(data: bytes, backend: X509Backend | None = ...) -> Certificate: ...
def load_pem_x509_certificate(data: bytes, backend: X509Backend | None = ...) -> Certificate: ...
def load_der_x509_crl(data: bytes, backend: X509Backend | None = ...) -> CertificateRevocationList: ...
def load_pem_x509_crl(data: bytes, backend: X509Backend | None = ...) -> CertificateRevocationList: ...
def load_der_x509_csr(data: bytes, backend: X509Backend | None = ...) -> CertificateSigningRequest: ...
def load_pem_x509_csr(data: bytes, backend: X509Backend | None = ...) -> CertificateSigningRequest: ...
def __getattr__(name: str) -> Any: ...  # incomplete
