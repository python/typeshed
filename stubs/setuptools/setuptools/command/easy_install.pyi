from _typeshed import Incomplete
from collections.abc import Iterable, Iterator
from typing import Any, ClassVar, Literal, TypedDict, type_check_only
from typing_extensions import Self

from pkg_resources import Environment
from setuptools.package_index import PackageIndex

from .. import Command, SetuptoolsDeprecationWarning

__all__ = ["easy_install", "PthDistributions", "extract_wininst_cfg", "get_exe_prefixes"]

class easy_install(Command):
    description: str
    command_consumes_arguments: bool
    user_options: ClassVar[list[tuple[str, str | None, str]]]
    boolean_options: ClassVar[list[str]]
    negative_opt: ClassVar[dict[str, str]]
    create_index: ClassVar[type[PackageIndex]]
    user: bool
    zip_ok: Incomplete
    install_dir: Incomplete
    index_url: Incomplete
    find_links: Incomplete
    build_directory: Incomplete
    args: Incomplete
    optimize: Incomplete
    upgrade: Incomplete
    editable: Incomplete
    root: Incomplete
    version: Incomplete
    install_purelib: Incomplete
    install_platlib: Incomplete
    install_headers: Incomplete
    install_lib: Incomplete
    install_scripts: Incomplete
    install_data: Incomplete
    install_base: Incomplete
    install_platbase: Incomplete
    install_userbase: str | None
    install_usersite: str | None
    no_find_links: Incomplete
    package_index: Incomplete
    pth_file: Incomplete
    site_dirs: Incomplete
    installed_projects: Incomplete
    verbose: bool | Literal[0, 1]
    def initialize_options(self) -> None: ...
    def delete_blockers(self, blockers) -> None: ...
    config_vars: dict[str, Any]
    script_dir: Incomplete
    all_site_dirs: list[str]
    shadow_path: list[str]
    local_index: Environment
    outputs: list[Incomplete]
    def finalize_options(self) -> None: ...
    def expand_basedirs(self) -> None: ...
    def expand_dirs(self) -> None: ...
    def run(self, show_deprecation: bool = True) -> None: ...
    def pseudo_tempname(self): ...
    def warn_deprecated_options(self) -> None: ...
    def check_site_dir(self) -> None: ...
    def cant_write_to_target(self) -> None: ...
    def check_pth_processing(self): ...
    def install_egg_scripts(self, dist) -> None: ...
    def add_output(self, path) -> None: ...
    def not_editable(self, spec) -> None: ...
    def check_editable(self, spec) -> None: ...
    def easy_install(self, spec, deps: bool = False): ...
    def install_item(self, spec, download, tmpdir, deps, install_needed: bool = False): ...
    def select_scheme(self, name) -> None: ...
    def process_distribution(self, requirement, dist, deps: bool = True, *info) -> None: ...
    def should_unzip(self, dist): ...
    def maybe_move(self, spec, dist_filename, setup_base): ...
    def install_wrapper_scripts(self, dist) -> None: ...
    def install_script(self, dist, script_name, script_text, dev_path: Incomplete | None = None) -> None: ...
    def write_script(self, script_name, contents, mode: str = "t", blockers=()) -> None: ...
    def install_eggs(self, spec, dist_filename, tmpdir): ...
    def egg_distribution(self, egg_path): ...
    def install_egg(self, egg_path, tmpdir): ...
    def install_exe(self, dist_filename, tmpdir): ...
    def exe_to_egg(self, dist_filename, egg_tmp): ...
    def install_wheel(self, wheel_path, tmpdir): ...
    def installation_report(self, req, dist, what: str = "Installed"): ...
    def report_editable(self, spec, setup_script): ...
    def run_setup(self, setup_script, setup_base, args) -> None: ...
    def build_and_install(self, setup_script, setup_base): ...
    def update_pth(self, dist) -> None: ...
    def unpack_progress(self, src, dst): ...
    def unpack_and_compile(self, egg_path, destination): ...
    def byte_compile(self, to_compile) -> None: ...
    def create_home_path(self) -> None: ...
    INSTALL_SCHEMES: ClassVar[dict[str, dict[str, str]]]
    DEFAULT_SCHEME: ClassVar[dict[str, str]]

def extract_wininst_cfg(dist_filename): ...
def get_exe_prefixes(exe_filename): ...

class PthDistributions(Environment):
    dirty: bool
    filename: Incomplete
    sitedirs: list[str]
    basedir: Incomplete
    paths: list[str]
    def __init__(self, filename, sitedirs=()) -> None: ...
    def save(self) -> None: ...
    def add(self, dist) -> None: ...
    def remove(self, dist) -> None: ...
    def make_relative(self, path): ...

class RewritePthDistributions(PthDistributions):
    prelude: str
    postlude: str

@type_check_only
class _SplitArgs(TypedDict, total=False):
    comments: bool
    posix: bool

class CommandSpec(list[str]):
    options: list[str]
    split_args: ClassVar[_SplitArgs]
    @classmethod
    def best(cls) -> type[CommandSpec]: ...
    @classmethod
    def from_param(cls, param: Self | str | Iterable[str] | None) -> Self: ...
    @classmethod
    def from_environment(cls) -> CommandSpec: ...
    @classmethod
    def from_string(cls, string: str) -> CommandSpec: ...
    def install_options(self, script_text: str) -> None: ...
    def as_header(self) -> str: ...

class WindowsCommandSpec(CommandSpec): ...

class ScriptWriter:
    template: ClassVar[str]
    command_spec_class: ClassVar[type[CommandSpec]]
    @classmethod
    def get_args(cls, dist, header: Incomplete | None = None) -> Iterator[tuple[str, str]]: ...
    @classmethod
    def best(cls) -> type[ScriptWriter]: ...
    @classmethod
    def get_header(cls, script_text: str = "", executable: str | CommandSpec | Iterable[str] | None = None) -> str: ...

class WindowsScriptWriter(ScriptWriter):
    command_spec_class: ClassVar[type[WindowsCommandSpec]]
    @classmethod
    def best(cls) -> type[WindowsScriptWriter]: ...

class WindowsExecutableLauncherWriter(WindowsScriptWriter): ...
class EasyInstallDeprecationWarning(SetuptoolsDeprecationWarning): ...
