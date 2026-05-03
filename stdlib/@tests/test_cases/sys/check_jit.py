import sys
from typing_extensions import assert_type

if sys.version_info >= (3, 14):
    assert_type(sys._jit.is_available(), bool)
    assert_type(sys._jit.is_enabled(), bool)
    assert_type(sys._jit.is_active(), bool)

    # sys is not a package, so this should be an error
    import sys._jit # type: ignore
