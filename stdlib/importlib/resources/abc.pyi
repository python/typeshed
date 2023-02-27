# These are all actually defined in this file on 3.11+,
# and re-exported from importlib.abc,
# but it's much less code duplication for typeshed if we pretend that they're still defined
# in `mportlib.abc` on 3.11+, and re-exported from this file
from importlib.abc import (
    ResourceReader as ResourceReader,
    Traversable as Traversable,
    TraversableResources as TraversableResources,
)
