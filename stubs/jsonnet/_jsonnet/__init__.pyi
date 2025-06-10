from collections.abc import Callable

# Gleaned from https://github.com/google/jsonnet/blob/master/python/_jsonnet.c
version: str

def evaluate_file(
    filename: str,
    *,
    jpathdir: str | list[str] | None = None,
    max_stack: int = 500,
    gc_min_objects: int = 1000,
    gc_growth_trigger: float = 2,
    ext_vars: dict[str, str] | None = None,
    ext_codes: dict[str, str] | None = None,
    tla_var: dict[str, str] | None = None,
    tla_codes: dict[str, str] | None = None,
    max_trace: int = 20,
    import_callback: Callable[[str, str], tuple[str, object | None]] | None = None,
    native_callbacks: dict[str, tuple[tuple[str, ...], Callable[..., object]]] | None = None,
) -> str: ...
def evaluate_snippet(
    filename: str,
    src: str,
    *,
    jpathdir: str | list[str] | None = None,
    max_stack: int = 500,
    gc_min_objects: int = 1000,
    gc_growth_trigger: float = 2,
    ext_vars: dict[str, str] | None = None,
    ext_codes: dict[str, str] | None = None,
    tla_var: dict[str, str] | None = None,
    tla_codes: dict[str, str] | None = None,
    max_trace: int = 20,
    import_callback: Callable[[str, str], tuple[str, object | None]] | None = None,
    native_callbacks: dict[str, tuple[tuple[str, ...], Callable[..., object]]] | None = None,
) -> str: ...
