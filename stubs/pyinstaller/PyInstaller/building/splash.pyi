from _typeshed import Incomplete

from PyInstaller.building.datastruct import Target

splash_requirements: Incomplete

# Referenced in https://pyinstaller.org/en/stable/spec-files.html#example-merge-spec-file
# Not to be imported during runtime, but is the type reference for spec files which are executed as python code
class Splash(Target):
    image_file: Incomplete
    full_tk: Incomplete
    name: Incomplete
    script_name: Incomplete
    minify_script: Incomplete
    rundir: Incomplete
    max_img_size: Incomplete
    text_pos: Incomplete
    text_size: Incomplete
    text_font: Incomplete
    text_color: Incomplete
    text_default: Incomplete
    always_on_top: Incomplete
    uses_tkinter: Incomplete
    script: Incomplete
    splash_requirements: Incomplete
    binaries: Incomplete
    def __init__(self, image_file, binaries, datas, **kwargs) -> None: ...
    def assemble(self): ...
    def test_tk_version(self) -> None: ...
    def generate_script(self): ...
