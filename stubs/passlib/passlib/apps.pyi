from typing import Any

from .context import LazyCryptContext

__all__ = [
    "custom_app_context",
    "django_context",
    "ldap_context",
    "ldap_nocrypt_context",
    "mysql_context",
    "mysql4_context",
    "mysql3_context",
    "phpass_context",
    "phpbb3_context",
    "postgres_context",
]

master_context: LazyCryptContext
custom_app_context: LazyCryptContext
django10_context: LazyCryptContext
django14_context: LazyCryptContext
django16_context: LazyCryptContext
django110_context: LazyCryptContext
django21_context: LazyCryptContext
django_context = django21_context  # noqa: F821
std_ldap_schemes: list[str]
ldap_nocrypt_context: LazyCryptContext
ldap_context: LazyCryptContext
mysql3_context: LazyCryptContext
mysql4_context: LazyCryptContext
mysql_context = mysql4_context  # noqa: F821
postgres_context: LazyCryptContext
phpass_context: LazyCryptContext
phpbb3_context: LazyCryptContext
roundup10_context: LazyCryptContext
roundup15_context: LazyCryptContext
roundup_context = roundup15_context  # noqa: F821
