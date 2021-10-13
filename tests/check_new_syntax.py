#!/usr/bin/env python3

import ast
import sys
from itertools import chain
from pathlib import Path


def check_new_syntax(tree: ast.AST, path: Path) -> list[str]:
    errors = []

    class OldSyntaxFinder(ast.NodeVisitor):
        def visit_Subscript(self, node: ast.Subscript) -> None:
            if not isinstance(node.value, ast.Name):
                return

            if node.value.id == "Union" and isinstance(node.slice, ast.Tuple):
                new_syntax = " | ".join(ast.unparse(x) for x in node.slice.elts)
                errors.append(f"{path}:{node.lineno}: Use PEP 604 syntax for Union, e.g. `{new_syntax}`")
            if node.value.id == "Optional":
                new_syntax = f"{ast.unparse(node.slice)} | None"
                errors.append(f"{path}:{node.lineno}: Use PEP 604 syntax for Optional, e.g. `{new_syntax}`")
            if node.value.id in {"List", "Dict"}:
                new_syntax = f"{node.value.id.lower()}[{ast.unparse(node.slice)}]"
                errors.append(f"{path}:{node.lineno}: Use built-in generics, e.g. `{new_syntax}`")

    # This doesn't check type aliases (or type var bounds, etc), since those are not
    # currently supported
    #
    # TODO: can use built-in generics in type aliases
    class AnnotationFinder(ast.NodeVisitor):
        def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
            OldSyntaxFinder().visit(node.annotation)

        def visit_arg(self, node: ast.arg) -> None:
            if node.annotation is not None:
                OldSyntaxFinder().visit(node.annotation)

        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            if node.returns is not None:
                OldSyntaxFinder().visit(node.returns)
            self.generic_visit(node)

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
            if node.returns is not None:
                OldSyntaxFinder().visit(node.returns)
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
