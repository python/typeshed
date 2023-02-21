from typing import Any

from setuptools import Command, SetuptoolsDeprecationWarning
from setuptools._distutils.filelist import FileList as _FileList
from setuptools.command.sdist import sdist

def translate_pattern(glob): ...

class InfoCommon:
    tag_build: Any
    tag_date: Any
    @property
    def name(self): ...
    def tagged_version(self): ...
    def tags(self): ...
    @property
    def vtags(self): ...

class egg_info(InfoCommon, Command):
    description: str
    user_options: Any
    boolean_options: Any
    negative_opt: Any
    egg_base: Any
    egg_name: Any
    egg_info: Any
    egg_version: Any
    broken_egg_info: bool
    def initialize_options(self) -> None: ...
    @property
    def tag_svn_revision(self) -> None: ...
    @tag_svn_revision.setter
    def tag_svn_revision(self, value) -> None: ...
    def save_version_info(self, filename) -> None: ...
    def finalize_options(self) -> None: ...
    def write_or_delete_file(self, what, filename, data, force: bool = ...) -> None: ...
    def write_file(self, what, filename, data) -> None: ...
    def delete_file(self, filename) -> None: ...
    def run(self) -> None: ...
    filelist: Any
    def find_sources(self) -> None: ...
    def check_broken_egg_info(self) -> None: ...

class FileList(_FileList):
    def __init__(self, warn=..., debug_print=..., ignore_egg_info_dir: bool = ...) -> None: ...
    def process_template_line(self, line) -> None: ...
    def include(self, pattern): ...
    def exclude(self, pattern): ...
    def recursive_include(self, dir, pattern): ...
    def recursive_exclude(self, dir, pattern): ...
    def graft(self, dir): ...
    def prune(self, dir): ...
    def global_include(self, pattern): ...
    def global_exclude(self, pattern): ...
    def append(self, item) -> None: ...
    def extend(self, paths) -> None: ...

class manifest_maker(sdist):
    template: str
    use_defaults: int
    prune: int
    manifest_only: int
    force_manifest: int
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    filelist: Any
    def run(self) -> None: ...
    def write_manifest(self) -> None: ...
    def warn(self, msg) -> None: ...
    def add_defaults(self) -> None: ...
    def add_license_files(self) -> None: ...
    def prune_file_list(self) -> None: ...

def write_file(filename, contents) -> None: ...
def write_pkg_info(cmd, basename, filename) -> None: ...
def warn_depends_obsolete(cmd, basename, filename) -> None: ...
def write_requirements(cmd, basename, filename) -> None: ...
def write_setup_requirements(cmd, basename, filename) -> None: ...
def write_toplevel_names(cmd, basename, filename) -> None: ...
def overwrite_arg(cmd, basename, filename) -> None: ...
def write_arg(cmd, basename, filename, force: bool = ...) -> None: ...
def write_entries(cmd, basename, filename) -> None: ...
def get_pkg_info_revision(): ...

class EggInfoDeprecationWarning(SetuptoolsDeprecationWarning): ...
