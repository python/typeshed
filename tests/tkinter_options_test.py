#!/usr/bin/env python3
"""
This script checks that the widget options specified in tkinter stubs are
actually supported by the Tk widgets at runtime. Unfortunately stubtest isn't
sufficient for checking this because the python code uses **kwargs for the
options. This script creates values that those options can be set to according
to the type hints and then tries to set the options. For example, if the stubs
say that an option should be bool, then this script sets it to True and then to
False, and fails if an exception is raised.

In particular, this script does NOT check whether all options supported by the
widgets are also supported by the stubs. This way CI builds don't break when a
new release of Tcl/Tk with new widget options comes out. There's a big comment
in tkinter/__init__.pyi describing how to add new options to the stubs.

It's best to run this file only in the latest supported Python version
(corresponding to latest Tcl/Tk version):
  - The latest Tcl/Tk includes all widget options of the previous Tcl/Tk
    releases. There's currently no way to say that a widget option is available
    only starting at Tk version X.Y, and tkinter generally doesn't make a big
    effort to document those things either. The CI build fails if a widget
    option is missing from the Tcl/Tk that tkinter is using.
  - It's nice to use new Python features in this file.

This script parses a subset of Python's type hint syntax with ast. Only
configure() methods defined in tkinter's widget classes are checked.
"""

import ast
import builtins
import itertools
import pathlib
import sys
import tkinter
import tkinter.font
import tkinter.ttk
from typing import Dict, Iterable, List, Sequence, Tuple, Union, cast


def create_child_widgets(parent: tkinter.Misc) -> Dict[str, tkinter.Misc]:
    # TODO: remove ignore comment when image_names() has type hints
    img: str = tkinter.image_names()[0]  # type: ignore

    # image can't be given to __init__, must config afterwards
    nonttk_optionmenu = tkinter.OptionMenu(parent, tkinter.StringVar(), "foo")
    ttk_optionmenu = tkinter.ttk.OptionMenu(parent, tkinter.StringVar(), "foo")
    nonttk_optionmenu.config(image=img)
    ttk_optionmenu.config(image=img)

    return {
        # width and height can be arbitrary _ScreenUnits only if these widgets have an image
        "tkinter.Button": tkinter.Button(image=img),
        "tkinter.Checkbutton": tkinter.Checkbutton(image=img),
        "tkinter.Label": tkinter.Label(image=img),
        "tkinter.Menubutton": tkinter.Menubutton(image=img),
        "tkinter.OptionMenu": nonttk_optionmenu,
        "tkinter.Radiobutton": tkinter.Radiobutton(image=img),
        "tkinter.ttk.Button": tkinter.ttk.Button(image=img),
        "tkinter.ttk.Checkbutton": tkinter.ttk.Checkbutton(image=img),
        "tkinter.ttk.Label": tkinter.ttk.Label(image=img),
        "tkinter.ttk.Menubutton": tkinter.ttk.Menubutton(image=img),
        "tkinter.ttk.OptionMenu": ttk_optionmenu,
        "tkinter.ttk.Radiobutton": tkinter.ttk.Radiobutton(image=img),
        # these don't need image
        "tkinter.Canvas": tkinter.Canvas(),
        "tkinter.Entry": tkinter.Entry(),
        "tkinter.Frame": tkinter.Frame(),
        "tkinter.LabelFrame": tkinter.LabelFrame(),
        "tkinter.Listbox": tkinter.Listbox(),
        "tkinter.Menu": tkinter.Menu(),
        "tkinter.Message": tkinter.Message(),
        "tkinter.PanedWindow": tkinter.PanedWindow(),
        "tkinter.Scale": tkinter.Scale(),
        "tkinter.Scrollbar": tkinter.Scrollbar(),
        "tkinter.Spinbox": tkinter.Spinbox(),
        "tkinter.Text": tkinter.Text(),
        "tkinter.ttk.Combobox": tkinter.ttk.Combobox(),
        "tkinter.ttk.Entry": tkinter.ttk.Entry(),
        "tkinter.ttk.Frame": tkinter.ttk.Frame(),
        "tkinter.ttk.Labelframe": tkinter.ttk.Labelframe(),
        "tkinter.ttk.Notebook": tkinter.ttk.Notebook(),
        "tkinter.ttk.Panedwindow": tkinter.ttk.Panedwindow(),
        "tkinter.ttk.Progressbar": tkinter.ttk.Progressbar(),
        "tkinter.ttk.Scale": tkinter.ttk.Scale(),
        "tkinter.ttk.Scrollbar": tkinter.ttk.Scrollbar(),
        "tkinter.ttk.Separator": tkinter.ttk.Separator(),
        "tkinter.ttk.Sizegrip": tkinter.ttk.Sizegrip(),
        "tkinter.ttk.Spinbox": tkinter.ttk.Spinbox(),
        "tkinter.ttk.Treeview": tkinter.ttk.Treeview(),
    }


# useful for detecting Tuple[foo, ...]
def is_dotdotdot(node: ast.expr) -> bool:
    return isinstance(node, ast.Constant) and node.value is Ellipsis


# attribute_string(<ast representing tkinter.Label>) --> 'tkinter.Label'
def attribute_string(typehint: ast.expr) -> str:
    if isinstance(typehint, ast.Name):
        return typehint.id
    if isinstance(typehint, ast.Attribute):
        return attribute_string(typehint.value) + "." + typehint.attr
    raise NotImplementedError(typehint)


# Convert type hint into values that should be possible to set to a widget that
# uses the type hint. Examples:
#   Literal['foo', 'bar']  -->  ['foo', 'bar']
#   bool  -->  [True, False]
#   float  -->  [123, 456.789]
class ValueGenerator:
    def __init__(
        self, import_mapping: Dict[str, str], widget: tkinter.Misc, modulename: str, images: List[tkinter.Image]
    ) -> None:
        self.import_mapping = import_mapping
        self.widget = widget
        self.modulename = modulename
        self.images = images

    def _full_name(self, name: str) -> str:
        first_part, possible_dot, possible_suffix = name.partition(".")
        try:
            # tkinter.font --> self.import_mapping['tkinter'] + '.font'
            return self.import_mapping[first_part] + possible_dot + possible_suffix
        except KeyError:
            return self.modulename + "." + name

    def _get_list_values(self, item_type: ast.expr) -> Sequence[List[object]]:
        list_value = list(self.get(item_type))
        return [[], list_value, list_value[::-1], list_value * 2]

    def get(self, typehint: ast.expr) -> Sequence[object]:
        if isinstance(typehint, (ast.Name, ast.Attribute)):
            full_name = self._full_name(attribute_string(typehint))
            if full_name in {"builtins.str", "typing.Any"}:
                # Unfortunately str doesn't always mean that *any* string is
                # acceptable. Not much can be done here.
                return []
            if full_name == "builtins.bool":
                return [True, False]
            if full_name == "builtins.int":
                return [123]
            if full_name == "builtins.float":
                return [123, 456.789]
            if full_name == "tkinter._Anchor":
                return ["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]
            if full_name == "tkinter._Bitmap":
                return ["hourglass"]
            if full_name == "tkinter._Color":
                return ["red", "#f00", "#ff0000"]
            compound_list = ["top", "left", "center", "right", "bottom", "none"]
            if full_name == "tkinter._Compound":
                return compound_list
            if full_name == "tkinter._Cursor":
                return ["hand2", ("hand2", "red"), ("hand2", "red", "blue")]
            if full_name == "tkinter._ImageSpec":
                # TODO: remove ignore comment when image_names() has type hints
                image_names: Tuple[str] = tkinter.image_names()  # type: ignore
                return cast(List[object], self.images) + list(image_names)
            if full_name == "tkinter._Padding":
                return ["2c", ("2c",), ("2c", "3c"), ("2c", "3c", "4c"), ("2c", "3c", "4c", "5c")]
            if full_name == "tkinter._Relief":
                return ["flat", "raised", "sunken", "groove", "solid", "ridge"]
            if full_name == "tkinter._ScreenUnits":
                return [12, 34.56, "78.9c"]
            if full_name == "tkinter._TakeFocusValue":
                return [True, False, "", print]
            if full_name == "tkinter.ttk._TtkCompound":
                return compound_list + ["text", "image"]
            if full_name == "tkinter._FontDescription":
                return [("Helvetica", 12, "bold"), tkinter.font.Font()]
            if full_name == "tkinter.Variable":
                return [tkinter.Variable(), tkinter.StringVar(), tkinter.IntVar(), tkinter.DoubleVar()]
            if full_name == "tkinter.DoubleVar":
                return [tkinter.DoubleVar()]
            if full_name in {"tkinter._XYScrollCommand", "tkinter._EntryValidateCommand", "tkinter._ButtonCommand"}:
                # Tkinter converts all callables to tcl commands the same way.
                return [print]

            # For widgets, return a child widget of the given widget. Some
            # options require this and others don't.
            child_widgets = create_child_widgets(self.widget)
            if full_name in child_widgets:
                return [child_widgets[full_name]]
            if full_name == "tkinter.Misc":
                # Any widget that can be put inside another widget, except Menu
                # which causes issues for whatever reason.
                return [widget for widget in child_widgets.values() if not isinstance(widget, tkinter.Menu)]

        if isinstance(typehint, ast.Subscript):  # typehint.value[typehint.slice]
            assert isinstance(typehint.value, (ast.Name, ast.Attribute))
            assert isinstance(typehint.slice, ast.Index)
            full_name = self._full_name(attribute_string(typehint.value))

            if full_name == "typing_extensions.Literal":
                if isinstance(typehint.slice.value, ast.Tuple):
                    tuple_content = typehint.slice.value.elts
                else:
                    tuple_content = [typehint.slice.value]
                assert all(isinstance(node, ast.Str) for node in tuple_content)
                return [cast(ast.Str, node).s for node in tuple_content]

            if full_name == "typing.Callable":
                return [print]

            if full_name == "typing.Union":
                assert isinstance(typehint.slice.value, ast.Tuple)
                result: List[object] = []
                for unioned_item in typehint.slice.value.elts:
                    result.extend(self.get(unioned_item))
                return result

            if full_name == "typing.Tuple":
                if isinstance(typehint.slice.value, ast.Tuple):
                    if len(typehint.slice.value.elts) == 2 and is_dotdotdot(typehint.slice.value.elts[1]):
                        # Tuple[foo, ...] is similar to List[foo]
                        list_values = self._get_list_values(typehint.slice.value.elts[0])
                        return [tuple(lizt) for lizt in list_values]
                    values_for_each_element = [self.get(element) for element in typehint.slice.value.elts]
                else:
                    values_for_each_element = [self.get(typehint.slice.value)]
                return list(itertools.product(*values_for_each_element))

            if full_name in {"tkinter._TkinterSequence", "tkinter.ttk._TkinterSequence"}:
                TkinterSequence = Union[List[object], Tuple[object, ...]]
                lists: List[TkinterSequence] = list(self._get_list_values(typehint.slice.value))
                tuples: List[TkinterSequence] = [tuple(lizt) for lizt in lists]
                return lists + tuples

        # If this error gets raised with an error message mentioning Ellipsis,
        # then make sure that you're running Python 3.8 or newer. Seems like
        # something changed in the ast.
        raise NotImplementedError(typehint, ast.dump(typehint))


# from enum import Enum --> {'Enum': 'enum.Enum'}
def get_import_mapping(parsed: ast.Module) -> Dict[str, str]:
    result = {}

    # similar to: from builtins import *
    for name in dir(builtins):
        if not name.startswith("_"):
            result[name] = "builtins." + name

    for stmt in parsed.body:
        if isinstance(stmt, ast.ImportFrom):
            for name_node in stmt.names:
                assert stmt.module is not None
                no_dots = name_node.name
                result[no_dots] = stmt.module + "." + no_dots
        elif isinstance(stmt, ast.Import):
            for name_node in stmt.names:
                assert name_node.asname is None
                # import tkinter.font --> result['tkinter'] = 'tkinter'
                first_part, *junk = name_node.name.split(".")
                result[first_part] = first_part

    return result


def find_all_classdefs(parsed: ast.Module) -> Iterable[ast.ClassDef]:
    for stmt in parsed.body:
        if isinstance(stmt, ast.ClassDef):
            yield stmt
        elif isinstance(stmt, ast.If):
            # handle classes e.g. under 'if sys.version_info >= bla'
            for inner in stmt.body:
                if isinstance(inner, ast.ClassDef):
                    yield inner


def is_configure_method_with_options_as_kwargs(node: ast.stmt) -> bool:
    if (not isinstance(node, ast.FunctionDef)) or node.name != "configure":
        return False

    self, cnf = node.args.args  # positional args
    assert cnf.arg == "cnf"
    assert cnf.annotation is not None

    [expected_cnf_annotation] = ast.parse("Dict[str, Any]").body
    assert isinstance(expected_cnf_annotation, ast.Expr)
    return ast.dump(cnf.annotation) == ast.dump(expected_cnf_annotation.value)


def find_configure_method(classname: str, classdefs: Dict[str, ast.ClassDef]) -> ast.FunctionDef:
    if classname in "tkinter.OptionMenu":
        # OptionMenus get their configure methods with inheritance
        classdef = classdefs["tkinter.Menubutton"]  # inherited from here
    elif classname in "tkinter.ttk.OptionMenu":
        classdef = classdefs["tkinter.ttk.Menubutton"]
    elif classname == "tkinter.Toplevel":
        # Toplevel does 'configure = Tk.configure'
        classdef = classdefs["tkinter.Tk"]
    else:
        classdef = classdefs[classname]

    [configure] = filter(is_configure_method_with_options_as_kwargs, classdef.body)
    assert isinstance(configure, ast.FunctionDef)
    return configure


def get_tkinter_dir() -> pathlib.Path:
    tests_dir = pathlib.Path(__file__).parent
    project_dir = tests_dir.parent
    return project_dir / "stdlib" / "3" / "tkinter"


def main() -> None:
    # tkinter.Tk must be created first, other things use that implicitly
    root = tkinter.Tk()

    print("Python version:", repr(sys.version))
    print("Tcl version:", root.tk.eval("info patchlevel"))

    test_widgets: Dict[str, tkinter.Misc] = {
        "tkinter.Tk": root,
        "tkinter.Toplevel": tkinter.Toplevel(),
        **create_child_widgets(root),
    }

    # This must be somewhat long-living because tkinter uses __del__ hack.
    test_images = [tkinter.BitmapImage(), tkinter.PhotoImage()]

    module_list = [
        ("tkinter", get_tkinter_dir() / "__init__.pyi"),
        ("tkinter.ttk", get_tkinter_dir() / "ttk.pyi"),
    ]

    import_mappings: Dict[str, Dict[str, str]] = {}
    classdefs: Dict[str, ast.ClassDef] = {}

    for modulename, path in module_list:
        print("Parsing", path)
        parsed = ast.parse(path.read_text())
        import_mappings[modulename] = get_import_mapping(parsed)
        classdefs.update({modulename + "." + classdef.name: classdef for classdef in find_all_classdefs(parsed)})

    for classname, widget in test_widgets.items():
        print("Testing", classname)
        modulename = classname.rsplit(".", 1)[0]
        value_getter = ValueGenerator(import_mappings[modulename], widget, modulename, test_images)
        configure = find_configure_method(classname, classdefs)

        for arg in configure.args.kwonlyargs:
            option_name = arg.arg.rstrip("_")  # class_=foo  -->  widget['class'] = foo

            assert arg.annotation is not None
            values = value_getter.get(arg.annotation)
            if values:
                for value in values:
                    print(f"widget[{option_name!r}] = {value!r}")
                    try:
                        widget[option_name] = value
                    except tkinter.TclError as e:
                        # these errors indicate that types were correct,
                        # but the values were wrong
                        assert str(e) in {"-to value must be greater than -from value", "Column index 123 out of bounds"}
            else:
                # Can't test option by assigning values to it according to
                # type hint, but this ensures that it exists and isn't
                # __init__ only.
                print(f"widget[{option_name!r}] gets assigned to itself")
                widget[option_name] = widget[option_name]

    print()
    print("ok")


if __name__ == "__main__":
    main()
