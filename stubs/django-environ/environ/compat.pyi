from typing import Final

from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured

def choose_rediscache_driver() -> str: ...
def choose_postgres_driver() -> str: ...
def choose_pymemcache_driver() -> str: ...

REDIS_DRIVER: Final[str]
DJANGO_POSTGRES: Final[str]
PYMEMCACHE_DRIVER: Final[str]
