from __future__ import annotations

"""Python script to add Final annotations to all upper-case variables in a given file.

TypeVar, ParamSpec, and TypeVarTuple are special cases that are not annotated with Final.

Install `libcst` before running this script:

```bash
pip install libcst
```

Usage:
    ```bash
    python add_final.py <path>
    ```
"""

import argparse
import pathlib

import libcst as cst


def _should_skip(value: cst.BaseExpression) -> bool:
    if isinstance(value, cst.Call) and isinstance(value.func, cst.Name):
        return value.func.value in (
            "TypeVar",
            "ParamSpec",
            "TypeVarTuple",
            "NewType",
            "typing.NewType",
            "typing.TypeVar",
            "typing.ParamSpec",
            "typing.TypeVarTuple",
        )
    return False


def _build_final_annotation(existing_annotation: cst.Annotation | None = None) -> cst.Annotation | None:
    if existing_annotation is None:
        return cst.Annotation(annotation=cst.Name(value="Final"))

    if isinstance(existing_annotation.annotation, cst.Name):
        if existing_annotation.annotation.value in ("Final", "typing.Final", "TypeAlias", "typing.TypeAlias"):
            return existing_annotation

        return cst.Annotation(
            annotation=cst.Subscript(
                value=cst.Name(value="Final"), slice=[cst.SubscriptElement(slice=cst.Index(value=existing_annotation.annotation))]
            )
        )


class FinalTransformer(cst.CSTTransformer):
    def __init__(self, *, include_class_assigns: bool = True) -> None:
        super().__init__()
        self.include_class_assigns = include_class_assigns
        self.final_imported = False
        self.in_class = False

    def visit_Module(self, node: cst.Module) -> bool:
        for stmt in node.body:
            if isinstance(stmt, cst.SimpleStatementLine):
                for element in stmt.body:
                    if isinstance(element, cst.ImportFrom):
                        if element.module and element.module.value == "typing":
                            if isinstance(element.names, cst.ImportStar):
                                self.final_imported = True
                            else:
                                if any(alias.name.value == "Final" for alias in element.names):
                                    self.final_imported = True
        return True

    def leave_Module(self, original_node: cst.Module, updated_node: cst.Module) -> cst.Module:
        if not self.final_imported:
            new_import = cst.SimpleStatementLine(
                body=[cst.ImportFrom(module=cst.Name(value="typing"), names=[cst.ImportAlias(name=cst.Name(value="Final"))])]
            )
            return updated_node.with_changes(body=[new_import] + list(updated_node.body))
        return updated_node

    def visit_ClassDef(self, node: cst.ClassDef) -> bool:
        self.in_class = True
        return True

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef) -> cst.ClassDef:
        self.in_class = False
        return updated_node

    def leave_Assign(self, original_node: cst.Assign, updated_node: cst.Assign) -> cst.Assign:
        if not self.include_class_assigns and self.in_class:
            return updated_node

        if isinstance(original_node.targets[0].target, cst.Name) and original_node.targets[0].target.value.isupper():
            if _should_skip(original_node.value):
                return updated_node

            new_annotation = _build_final_annotation()
            if not new_annotation:
                return updated_node

            return cst.AnnAssign(
                target=original_node.targets[0].target, annotation=new_annotation, value=original_node.value
            )  # type: ignore
        return updated_node

    def leave_AnnAssign(self, original_node: cst.AnnAssign, updated_node: cst.AnnAssign) -> cst.AnnAssign:
        if self.in_class and not self.include_class_assigns:
            return updated_node

        if isinstance(original_node.target, cst.Name) and original_node.target.value.isupper():
            if _should_skip(original_node.target):
                return updated_node

            new_annotation = _build_final_annotation(original_node.annotation)
            if not new_annotation:
                return updated_node

            return updated_node.with_changes(annotation=new_annotation)
        return updated_node


def _update_module(module: pathlib.Path, include_class_defs: bool) -> None:
    source_code = module.read_text()
    try:
        tree = cst.parse_module(source_code)
        modified_tree = tree.visit(FinalTransformer(include_class_assigns=include_class_defs))
        pathlib.Path(module).write_text(modified_tree.code)
    except Exception as e:
        print(f"Error processing {module}: {e}. Skipping.")


def add_final_annotations(file_path: str | pathlib.Path, include_class_defs: bool = True, stubs: bool = False) -> None:
    pth = pathlib.Path(file_path)
    is_dir = pth.is_dir()
    pattern = "*.pyi" if stubs else "*.py"
    if is_dir:
        for submodule in pth.rglob(pattern):
            _update_module(submodule, include_class_defs)
    else:
        _update_module(pth, include_class_defs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add Final annotations to all uppercase variables in Python files.")
    parser.add_argument("path", type=str, help="Path to the file or directory to process, `.` for current directory.")
    parser.add_argument("-c", "--include-classes", action="store_true", help="Include class level assignments", default=False)
    parser.add_argument("-s", "--stubs", action="store_true", help="Add Final annotations to stub files", default=False)

    args = parser.parse_args()

    if args.path == ".":
        add_final_annotations(pathlib.Path.cwd(), args.include_classes, args.stubs)
    else:
        add_final_annotations(args.path, args.include_classes, args.stubs)
