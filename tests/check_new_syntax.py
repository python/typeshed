#!/usr/bin/env python3

import ast
import re
import sys
from itertools import chain
from pathlib import Path

STUBS_SUPPORTING_PYTHON_2 = frozenset(
    path.parent for path in Path("stubs").rglob("METADATA.toml") if "python2 = true" in path.read_text().splitlines()
)

CONTEXT_MANAGER_ALIASES = {"ContextManager": "AbstractContextManager", "AsyncContextManager": "AbstractAsyncContextManager"}
CONTEXTLIB_ALIAS_ALLOWLIST = frozenset({Path("stdlib/contextlib.pyi")})
FORBIDDEN_BUILTIN_TYPING_IMPORTS = frozenset({"List", "FrozenSet", "Set", "Dict", "Tuple", "Type"})

IMPORTED_FROM_TYPING_NOT_TYPING_EXTENSIONS = frozenset(
    {"ClassVar", "NewType", "overload", "Text", "Protocol", "runtime_checkable", "NoReturn"}
)

IMPORTED_FROM_COLLECTIONS_ABC_NOT_TYPING_EXTENSIONS = frozenset(
    {"Awaitable", "Coroutine", "AsyncIterable", "AsyncIterator", "AsyncGenerator"}
)

# The values in the mapping are what these are called in `collections`
IMPORTED_FROM_COLLECTIONS_NOT_TYPING = {
    "Counter": "Counter",
    "Deque": "deque",
    "DefaultDict": "defaultdict",
    "OrderedDict": "OrderedDict",
    "ChainMap": "ChainMap",
}


def check_new_syntax(tree: ast.AST, path: Path) -> list[str]:
    errors = []
    python_2_support_required = any(directory in path.parents for directory in STUBS_SUPPORTING_PYTHON_2)

    def check_object_from_typing(node: ast.ImportFrom | ast.Attribute, object_name: str):
        if object_name in FORBIDDEN_BUILTIN_TYPING_IMPORTS:
            errors.append(f"{path}:{node.lineno}: Use `builtins.{object_name.lower()}` instead of `typing.{object_name}`")
        elif object_name in IMPORTED_FROM_COLLECTIONS_NOT_TYPING:
            errors.append(
                f"{path}:{node.lineno}: "
                f"Use `collections.{IMPORTED_FROM_COLLECTIONS_NOT_TYPING[object_name]}` instead of `typing.{object_name}`"
            )
        elif not python_2_support_required and path not in CONTEXTLIB_ALIAS_ALLOWLIST and object_name in CONTEXT_MANAGER_ALIASES:
            errors.append(
                f"{path}:{node.lineno}: Use `contextlib.{CONTEXT_MANAGER_ALIASES[object_name]}` instead of `typing.{object_name}`"
            )
        # We can't yet check for collections.abc imports due to pytype errors

    class UnionFinder(ast.NodeVisitor):
        def visit_Subscript(self, node: ast.Subscript) -> None:
            if isinstance(node.value, ast.Name):
                if node.value.id == "Union" and isinstance(node.slice, ast.Tuple):
                    new_syntax = " | ".join(ast.unparse(x) for x in node.slice.elts)
                    errors.append(f"{path}:{node.lineno}: Use PEP 604 syntax for Union, e.g. `{new_syntax}`")
                if node.value.id == "Optional":
                    new_syntax = f"{ast.unparse(node.slice)} | None"
                    errors.append(f"{path}:{node.lineno}: Use PEP 604 syntax for Optional, e.g. `{new_syntax}`")

            self.generic_visit(node)

    def check_instance_method_for_bad_typevars(
        *,
        method: ast.FunctionDef | ast.AsyncFunctionDef,
        first_arg_annotation: ast.Name | ast.Subscript,
        return_annotation: ast.Name,
    ) -> None:
        if not isinstance(first_arg_annotation, ast.Name):
            return

        if first_arg_annotation.id != return_annotation.id:
            return

        arg1_annotation_name = first_arg_annotation.id

        if not arg1_annotation_name.startswith("_"):
            return

        method.decorator_list.clear()
        new_syntax = re.sub(fr"(\W){arg1_annotation_name}(\W)", r"\1Self\2", ast.unparse(method)).replace("\n   ", "")
        errors.append(f"{path}:{method.lineno}: Use `_typeshed.Self` instead of `{arg1_annotation_name}`, e.g. `{new_syntax}`")

    def check_class_method_for_bad_typevars(
        *,
        method: ast.FunctionDef | ast.AsyncFunctionDef,
        first_arg_annotation: ast.Name | ast.Subscript,
        return_annotation: ast.Name,
    ) -> None:
        if not isinstance(first_arg_annotation, ast.Subscript):
            return

        if not isinstance(first_arg_annotation.slice, ast.Name):
            return

        if not isinstance(first_arg_annotation.value, ast.Name):
            return

        if first_arg_annotation.value.id != "type":
            return

        cls_typevar = first_arg_annotation.slice.id

        if cls_typevar == return_annotation.id and cls_typevar.startswith("_"):
            method.decorator_list.clear()
            new_syntax = re.sub(fr"(\W){cls_typevar}(\W)", r"\1Self\2", ast.unparse(method)).replace("\n   ", "")
            errors.append(f"{path}:{method.lineno}: Use `_typeshed.Self` instead of `{cls_typevar}`, e.g. `{new_syntax}`")

    class BadTypeVarFinder(ast.NodeVisitor):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            return_annotation = node.returns

            if not node.args.args:
                return

            first_arg_annotation = node.args.args[0].annotation

            if not isinstance(return_annotation, ast.Name):
                return

            if not isinstance(first_arg_annotation, (ast.Name, ast.Subscript)):
                return

            if node.name == "__new__":
                check_class_method_for_bad_typevars(
                    method=node, first_arg_annotation=first_arg_annotation, return_annotation=return_annotation
                )
                return

            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Name):
                    decorator_name = decorator.id
                    if decorator_name == "classmethod":
                        check_class_method_for_bad_typevars(
                            method=node, first_arg_annotation=first_arg_annotation, return_annotation=return_annotation
                        )
                        return
                    elif decorator_name == "staticmethod":
                        return

            check_instance_method_for_bad_typevars(
                method=node, first_arg_annotation=first_arg_annotation, return_annotation=return_annotation
            )
            return

        visit_AsyncFunctionDef = visit_FunctionDef

    class OldSyntaxFinder(ast.NodeVisitor):
        def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
            if node.module == "collections.abc":
                imported_classes = node.names
                if any(cls.name == "Set" and cls.asname != "AbstractSet" for cls in imported_classes):
                    errors.append(
                        f"{path}:{node.lineno}: "
                        f"Use `from collections.abc import Set as AbstractSet` to avoid confusion with `builtins.set`"
                    )
            elif node.module == "typing_extensions":
                for imported_object in node.names:
                    imported_object_name = imported_object.name
                    if imported_object_name in FORBIDDEN_BUILTIN_TYPING_IMPORTS:
                        errors.append(
                            f"{path}:{node.lineno}: "
                            f"Use `builtins.{imported_object_name.lower()}` instead of `typing_extensions.{imported_object_name}`"
                        )
                    elif imported_object_name in IMPORTED_FROM_TYPING_NOT_TYPING_EXTENSIONS:
                        errors.append(
                            f"{path}:{node.lineno}: "
                            f"Use `typing.{imported_object_name}` instead of `typing_extensions.{imported_object_name}`"
                        )
                    elif imported_object_name in IMPORTED_FROM_COLLECTIONS_ABC_NOT_TYPING_EXTENSIONS:
                        errors.append(
                            f"{path}:{node.lineno}: "
                            f"Use `collections.abc.{imported_object_name}` or `typing.{imported_object_name}` "
                            f"instead of `typing_extensions.{imported_object_name}`"
                        )
                    elif imported_object_name in IMPORTED_FROM_COLLECTIONS_NOT_TYPING:
                        errors.append(
                            f"{path}:{node.lineno}: "
                            f"Use `collections.{IMPORTED_FROM_COLLECTIONS_NOT_TYPING[imported_object_name]}` "
                            f"instead of `typing_extensions.{imported_object_name}`"
                        )
                    elif imported_object_name in CONTEXT_MANAGER_ALIASES:
                        if python_2_support_required:
                            errors.append(
                                f"{path}:{node.lineno}: "
                                f"Use `typing.{imported_object_name}` instead of `typing_extensions.{imported_object_name}`"
                            )
                        else:
                            errors.append(
                                f"{path}:{node.lineno}: Use `contextlib.{CONTEXT_MANAGER_ALIASES[imported_object_name]}` "
                                f"instead of `typing_extensions.{imported_object_name}`"
                            )

            elif node.module == "typing":
                for imported_object in node.names:
                    check_object_from_typing(node, imported_object.name)

        def visit_Attribute(self, node: ast.Attribute) -> None:
            if isinstance(node.value, ast.Name) and node.value.id == "typing":
                check_object_from_typing(node, node.attr)
            self.generic_visit(node)

        def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
            UnionFinder().visit(node.annotation)

        def visit_arg(self, node: ast.arg) -> None:
            if node.annotation is not None:
                UnionFinder().visit(node.annotation)

        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            if node.returns is not None:
                UnionFinder().visit(node.returns)
            self.generic_visit(node)

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
            if node.returns is not None:
                UnionFinder().visit(node.returns)
            self.generic_visit(node)

        # dateutil/relativedelta yields mypy errors about overlapping overloads if we use _typeshed.Self
        if path != Path("stubs/python-dateutil/dateutil/relativedelta.pyi"):

            def visit_ClassDef(self, node: ast.ClassDef) -> None:
                BadTypeVarFinder().visit(node)
                self.generic_visit(node)

    class ObjectClassdefFinder(ast.NodeVisitor):
        def visit_ClassDef(self, node: ast.ClassDef) -> None:
            if any(isinstance(base, ast.Name) and base.id == "object" for base in node.bases):
                errors.append(
                    f"{path}:{node.lineno}: Do not inherit from `object` explicitly, "
                    f"as all classes implicitly inherit from `object` in Python 3"
                )
            self.generic_visit(node)

    class IfFinder(ast.NodeVisitor):
        def visit_If(self, node: ast.If) -> None:
            if (
                isinstance(node.test, ast.Compare)
                and ast.unparse(node.test).startswith("sys.version_info < ")
                and node.orelse
                and not (len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If))  # elif statement (#6728)
            ):
                new_syntax = "if " + ast.unparse(node.test).replace("<", ">=", 1)
                errors.append(
                    f"{path}:{node.lineno}: When using if/else with sys.version_info, "
                    f"put the code for new Python versions first, e.g. `{new_syntax}`"
                )
            self.generic_visit(node)

    if path != Path("stdlib/typing_extensions.pyi"):
        OldSyntaxFinder().visit(tree)

    if not python_2_support_required:
        ObjectClassdefFinder().visit(tree)

    IfFinder().visit(tree)
    return errors


def main() -> None:
    errors = []
    for path in chain(Path("stdlib").rglob("*.pyi"), Path("stubs").rglob("*.pyi")):
        if "@python2" in path.parts:
            continue
        if Path("stubs/protobuf/google/protobuf") in path.parents:  # TODO: fix protobuf stubs
            continue

        with open(path) as f:
            tree = ast.parse(f.read())
        errors.extend(check_new_syntax(tree, path))

    if errors:
        print("\n".join(errors))
        sys.exit(1)


if __name__ == "__main__":
    main()
