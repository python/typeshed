def mkpath(name, mode: int = ..., verbose: int = ..., dry_run: int = ...): ...
def create_tree(base_dir, files, mode: int = ..., verbose: int = ..., dry_run: int = ...) -> None: ...
def copy_tree(
    src,
    dst,
    preserve_mode: int = ...,
    preserve_times: int = ...,
    preserve_symlinks: int = ...,
    update: int = ...,
    verbose: int = ...,
    dry_run: int = ...,
): ...
def remove_tree(directory, verbose: int = ..., dry_run: int = ...) -> None: ...
def ensure_relative(path): ...
