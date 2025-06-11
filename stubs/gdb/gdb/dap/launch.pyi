from collections.abc import Mapping, Sequence

def launch(
    *,
    program: str | None = None,
    cwd: str | None = None,
    args: Sequence[str] = (),
    env: Mapping[str, str] | None = None,
    stopAtBeginningOfMainSubprogram: bool = False,
    **extra,
): ...  # extra argument is unused
def attach(
    *, program: str | None = None, pid: int | None = None, target: str | None = None, **args
) -> None: ...  # args argument is unused
def config_done(**args) -> None: ...  # args argument is unused
