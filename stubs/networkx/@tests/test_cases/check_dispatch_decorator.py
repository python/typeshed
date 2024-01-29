from typing_extensions import assert_type

from networkx.utils.backends import _dispatch


@_dispatch
def some_method(int_p: int, str_p: str) -> float:
    ...


# Wrong param / order
some_method("", 0)  # type: ignore
# backend is kw-only
some_method(0, "", None)  # type: ignore
# No backend means no backend_kwargs allowed
some_method(0, "", backend_arg="")  # type: ignore
some_method(0, "", backend=None, backend_arg="")  # type: ignore

# Correct usage
assert_type(some_method(0, ""), float)
# type system doesn't allow this yet (see comment in networkx/utils/backends.pyi)
# assert_type(some_method(0, "", backend=None), float)
assert_type(some_method(0, "", backend="custom backend", backend_arg=""), float)
