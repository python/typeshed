#!/usr/bin/env python3

import ast
import sys
from itertools import chain
from pathlib import Path


def check_pep_604(tree: ast.AST, path: Path) -> list[str]:
    errors = []

    class UnionFinder(ast.NodeVisitor):
        def visit_Subscript(self, node: ast.Subscript) -> None:
            if (
                isinstance(node.value, ast.Name)
                and node.value.id == "Union"
                and isinstance(node.slice, ast.Tuple)
            ):
                new_syntax = " | ".join(ast.unparse(x) for x in node.slice.elts)
                errors.append(
                    (f"{path}:{node.lineno}: Use PEP 604 syntax for Union, e.g. `{new_syntax}`")
                )
            if (
                isinstance(node.value, ast.Name)
                and node.value.id == "Optional"
            ):
                new_syntax = f"{ast.unparse(node.slice)} | None"
                errors.append(
                    (f"{path}:{node.lineno}: Use PEP 604 syntax for Optional, e.g. `{new_syntax}`")
                )

    # This doesn't check type aliases (or type var bounds, etc), since those are not
    # currently supported
    class AnnotationFinder(ast.NodeVisitor):
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
        errors.extend(check_pep_604(tree, path))

    if errors:
        print("\n".join(errors))
        sys.exit(1)


if __name__ == "__main__":
    main()
