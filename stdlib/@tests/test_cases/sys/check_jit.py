import sys
from typing_extensions import assert_type

if sys.version_info >= (3, 14):
    assert_type(sys._jit.is_available(), bool)
    assert_type(sys._jit.is_enabled(), bool)
    assert_type(sys._jit.is_active(), bool)

    def sys_is_not_a_package():
        # This has to be put into a function, because otherwise pyright
        # applies the type: ignore on the import sys._jit to the above usages of it
        import sys._jit  # type: ignore
