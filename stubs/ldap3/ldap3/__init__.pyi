from typing import Any, Type

from .abstract.attrDef import AttrDef as AttrDef
from .abstract.attribute import (
    Attribute as Attribute,
    OperationalAttribute as OperationalAttribute,
    WritableAttribute as WritableAttribute,
)
from .abstract.cursor import Reader as Reader, Writer as Writer
from .abstract.entry import Entry as Entry, WritableEntry as WritableEntry
from .abstract.objectDef import ObjectDef as ObjectDef
from .core.connection import Connection as Connection
from .core.pooling import ServerPool as ServerPool
from .core.rdns import ReverseDnsSetting as ReverseDnsSetting
from .core.server import Server as Server
from .core.tls import Tls as Tls
from .protocol.rfc4512 import DsaInfo as DsaInfo, SchemaInfo as SchemaInfo
from .utils.config import get_config_parameter as get_config_parameter, set_config_parameter as set_config_parameter
from .version import __description__ as __description__, __status__ as __status__, __url__ as __url__

ANONYMOUS: str
SIMPLE: str
SASL: str
NTLM: str
EXTERNAL: str
DIGEST_MD5: str
KERBEROS: str
GSSAPI: str
PLAIN: str
AUTO_BIND_DEFAULT: str
AUTO_BIND_NONE: str
AUTO_BIND_NO_TLS: str
AUTO_BIND_TLS_BEFORE_BIND: str
AUTO_BIND_TLS_AFTER_BIND: str
IP_SYSTEM_DEFAULT: str
IP_V4_ONLY: str
IP_V6_ONLY: str
IP_V4_PREFERRED: str
IP_V6_PREFERRED: str
BASE: str
LEVEL: str
SUBTREE: str
DEREF_NEVER: str
DEREF_SEARCH: str
DEREF_BASE: str
DEREF_ALWAYS: str
ALL_ATTRIBUTES: str
NO_ATTRIBUTES: str
ALL_OPERATIONAL_ATTRIBUTES: str
MODIFY_ADD: str
MODIFY_DELETE: str
MODIFY_REPLACE: str
MODIFY_INCREMENT: str
SYNC: str
SAFE_SYNC: str
SAFE_RESTARTABLE: str
ASYNC: str
LDIF: str
RESTARTABLE: str
REUSABLE: str
MOCK_SYNC: str
MOCK_ASYNC: str
ASYNC_STREAM: str
NONE: str
DSA: str
SCHEMA: str
ALL: str
OFFLINE_EDIR_8_8_8: str
OFFLINE_EDIR_9_1_4: str
OFFLINE_AD_2012_R2: str
OFFLINE_SLAPD_2_4: str
OFFLINE_DS389_1_3_3: str
FIRST: str
ROUND_ROBIN: str
RANDOM: str
HASHED_NONE: str
HASHED_SHA: str
HASHED_SHA256: str
HASHED_SHA384: str
HASHED_SHA512: str
HASHED_MD5: str
HASHED_SALTED_SHA: str
HASHED_SALTED_SHA256: str
HASHED_SALTED_SHA384: str
HASHED_SALTED_SHA512: str
HASHED_SALTED_MD5: str
NUMERIC_TYPES: Any
INTEGER_TYPES: Any
STRING_TYPES: tuple[Type[Any], ...]
SEQUENCE_TYPES: tuple[Type[Any], ...]
