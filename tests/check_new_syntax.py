#!/usr/bin/env python3

import ast
import sys
from itertools import chain
from pathlib import Path
from typing import TypedDict


class ModuleImportsDict(TypedDict):
    set_from_collections_abc: bool
    context_manager_from_typing: bool
    async_context_manager_from_typing: bool


STUBS_SUPPORTING_PYTHON_2 = frozenset(
    {path.parent for path in Path("stubs").rglob("METADATA.toml") if "python2 = true" in path.read_text().splitlines()}
)


def check_new_syntax(tree: ast.AST, path: Path) -> list[str]:
    errors = []
    python_2_support_required = any(directory in path.parents for directory in STUBS_SUPPORTING_PYTHON_2)

    def unparse_without_tuple_parens(node: ast.AST) -> str:
        if isinstance(node, ast.Tuple) and node.elts:
            return ast.unparse(node)[1:-1]
        return ast.unparse(node)

    def is_dotdotdot(node: ast.AST) -> bool:
        return isinstance(node, ast.Constant) and node.s is Ellipsis

    def raise_ContextManager_error(node: ast.Subscript | ast.Name, is_subscript: bool = True) -> None:
        first_part = f"{path}:{node.lineno}: Use `contextlib.AbstractContextManager` instead of `typing.ContextManager`"

        if is_subscript:
            new_syntax = f"contextlib.AbstractContextManager[{ast.unparse(node.slice)}]"
            error_msg = f"{first_part}, e.g. `{new_syntax}`"
        else:
            error_msg = first_part

        errors.append(error_msg)

    def raise_AsyncContextManager_error(node: ast.Subscript | ast.Name, is_subscript: bool = True) -> None:
        first_part = f"{path}:{node.lineno}: Use `contextlib.AbstractAsyncContextManager` instead of `typing.AsyncContextManager`"

        if is_subscript:
            new_syntax = f"contextlib.AbstractAsyncContextManager[{ast.unparse(node.slice)}]"
            error_msg = f"{first_part}, e.g. `{new_syntax}`"
        else:
            error_msg = first_part

        errors.append(error_msg)

    class OldSyntaxFinder(ast.NodeVisitor):
        def __init__(self, module_imports_info_dict: ModuleImportsDict) -> None:
            self.module_imports_info_dict = module_imports_info_dict

        def visit_Subscript(self, node: ast.Subscript) -> None:
            if isinstance(node.value, ast.Name):
                if node.value.id == "Union" and isinstance(node.slice, ast.Tuple):
                    new_syntax = " | ".join(ast.unparse(x) for x in node.slice.elts)
                    errors.append(f"{path}:{node.lineno}: Use PEP 604 syntax for Union, e.g. `{new_syntax}`")
                if node.value.id == "Optional":
                    new_syntax = f"{ast.unparse(node.slice)} | None"
                    errors.append(f"{path}:{node.lineno}: Use PEP 604 syntax for Optional, e.g. `{new_syntax}`")
                if node.value.id in {"List", "FrozenSet"}:
                    new_syntax = f"{node.value.id.lower()}[{ast.unparse(node.slice)}]"
                    errors.append(f"{path}:{node.lineno}: Use built-in generics, e.g. `{new_syntax}`")
                if not self.module_imports_info_dict["set_from_collections_abc"] and node.value.id == "Set":
                    new_syntax = f"set[{ast.unparse(node.slice)}]"
                    errors.append(f"{path}:{node.lineno}: Use built-in generics, e.g. `{new_syntax}`")
                if node.value.id == "Deque":
                    new_syntax = f"collections.deque[{ast.unparse(node.slice)}]"
                    errors.append(f"{path}:{node.lineno}: Use `collections.deque` instead of `typing.Deque`, e.g. `{new_syntax}`")
                if node.value.id == "Dict":
                    new_syntax = f"dict[{unparse_without_tuple_parens(node.slice)}]"
                    errors.append(f"{path}:{node.lineno}: Use built-in generics, e.g. `{new_syntax}`")
                if node.value.id == "DefaultDict":
                    new_syntax = f"collections.defaultdict[{unparse_without_tuple_parens(node.slice)}]"
                    errors.append(
                        f"{path}:{node.lineno}: Use `collections.defaultdict` instead of `typing.DefaultDict`, "
                        f"e.g. `{new_syntax}`"
                    )
                # Tuple[Foo, ...] must be allowed because of mypy bugs
                if node.value.id == "Tuple" and not (
                    isinstance(node.slice, ast.Tuple) and len(node.slice.elts) == 2 and is_dotdotdot(node.slice.elts[1])
                ):
                    new_syntax = f"tuple[{unparse_without_tuple_parens(node.slice)}]"
                    errors.append(f"{path}:{node.lineno}: Use built-in generics, e.g. `{new_syntax}`")
                if not python_2_support_required:
                    if self.module_imports_info_dict["context_manager_from_typing"] and node.value.id == "ContextManager":
                        raise_ContextManager_error(node)
                    if (
                        self.module_imports_info_dict["async_context_manager_from_typing"]
                        and node.value.id == "AsyncContextManager"
                    ):
                        raise_AsyncContextManager_error(node)

            self.generic_visit(node)

    # This doesn't check type aliases (or type var bounds, etc), since those are not
    # currently supported
    #
    # TODO: can use built-in generics in type aliases
    class AnnotationFinder(ast.NodeVisitor):
        def __init__(self) -> None:
            self.module_imports_info_dict = ModuleImportsDict(
                set_from_collections_abc=False, context_manager_from_typing=False, async_context_manager_from_typing=False
            )

        def old_syntax_finder(self) -> OldSyntaxFinder:
            """Convenience method to create an `OldSyntaxFinder` instance with the correct state"""
            return OldSyntaxFinder(self.module_imports_info_dict)

        def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
            if node.module == "collections.abc":
                classes_from_collections_abc = node.names
                if any(cls.name == "Set" for cls in classes_from_collections_abc):
                    self.module_imports_info_dict["set_from_collections_abc"] = True

            elif node.module == "typing":
                classes_from_typing = node.names

                for cls in classes_from_typing:
                    cls_name = cls.name
                    if cls_name == "ContextManager":
                        self.module_imports_info_dict["context_manager_from_typing"] = True
                    elif cls_name == "AsyncContextManager":
                        self.module_imports_info_dict["async_context_manager_from_typing"] = True

            self.generic_visit(node)

        def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
            self.old_syntax_finder().visit(node.annotation)

        def visit_arg(self, node: ast.arg) -> None:
            if node.annotation is not None:
                self.old_syntax_finder().visit(node.annotation)

        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            if node.returns is not None:
                self.old_syntax_finder().visit(node.returns)
            self.generic_visit(node)

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
            if node.returns is not None:
                self.old_syntax_finder().visit(node.returns)
            self.generic_visit(node)

        if not python_2_support_required:

            def visit_ClassDef(self, node: ast.ClassDef) -> None:
                context_manager_from_typing = self.module_imports_info_dict["context_manager_from_typing"]
                async_context_manager_from_typing = self.module_imports_info_dict["async_context_manager_from_typing"]

                for base in node.bases:
                    match base:
                        case ast.Subscript(value=ast.Name(id="ContextManager")) if context_manager_from_typing:
                            raise_ContextManager_error(base)
                        case ast.Subscript(value=ast.Name(id="AsyncContextManager")) if async_context_manager_from_typing:
                            raise_AsyncContextManager_error(base)
                        case ast.Name(id="ContextManager") if context_manager_from_typing:
                            raise_ContextManager_error(base, is_subscript=False)
                        case ast.Name(id="AsyncContextManager") if async_context_manager_from_typing:
                            raise_AsyncContextManager_error(base, is_subscript=False)
                        case _:
                            pass

                self.generic_visit(node)

    AnnotationFinder().visit(tree)
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
