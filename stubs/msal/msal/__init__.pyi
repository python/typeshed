from .application import (
    ClientApplication as ClientApplication,
    ConfidentialClientApplication as ConfidentialClientApplication,
    PublicClientApplication as PublicClientApplication,
)
from .auth_scheme import PopAuthScheme as PopAuthScheme
from .managed_identity import (
    ArcPlatformNotSupportedError as ArcPlatformNotSupportedError,
    ManagedIdentityClient as ManagedIdentityClient,
    ManagedIdentityError as ManagedIdentityError,
    SystemAssignedManagedIdentity as SystemAssignedManagedIdentity,
    UserAssignedManagedIdentity as UserAssignedManagedIdentity,
)
from .oauth2cli.assertion import AutoRefresher as AutoRefresher
from .oauth2cli.oauth2 import BrowserInteractionTimeoutError as BrowserInteractionTimeoutError
from .oauth2cli.oidc import IdTokenError as IdTokenError, Prompt as Prompt
from .sku import __version__ as __version__
from .token_cache import SerializableTokenCache as SerializableTokenCache, TokenCache as TokenCache
