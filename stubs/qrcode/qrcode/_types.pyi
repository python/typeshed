# Type aliases used in this stub package
from typing_extensions import TypeAlias

Box: TypeAlias = tuple[tuple[int, int], tuple[int, int]]
Ink: TypeAlias = tuple[int, int, int] | tuple[int, int, int, int]

# Don't try to make these Literal[x, y, z] as this really wreaks
# havoc with overloads in mypy.
ErrorCorrect: TypeAlias = int
MaskPattern: TypeAlias = int
