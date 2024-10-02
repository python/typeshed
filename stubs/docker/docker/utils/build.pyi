from _typeshed import Incomplete

def match_tag(tag: str) -> bool: ...
def tar(
    path,
    exclude: Incomplete | None = None,
    dockerfile: Incomplete | None = None,
    fileobj: Incomplete | None = None,
    gzip: bool = False,
): ...
def exclude_paths(root, patterns, dockerfile: Incomplete | None = None): ...
def build_file_list(root): ...
def create_archive(
    root,
    files: Incomplete | None = None,
    fileobj: Incomplete | None = None,
    gzip: bool = False,
    extra_files: Incomplete | None = None,
): ...
def mkbuildcontext(dockerfile): ...
def split_path(p): ...
def normalize_slashes(p): ...
def walk(root, patterns, default: bool = True): ...

class PatternMatcher:
    patterns: Incomplete
    def __init__(self, patterns) -> None: ...
    def matches(self, filepath): ...
    def walk(self, root): ...

class Pattern:
    exclusion: bool
    dirs: Incomplete
    cleaned_pattern: Incomplete
    def __init__(self, pattern_str) -> None: ...
    @classmethod
    def normalize(cls, p): ...
    def match(self, filepath): ...
