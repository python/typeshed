from typing import Any, Callable, Dict, List, Tuple

import docutils.nodes
import docutils.parsers.rst.states

def register_local_role(name: str,
                        role_fn: Callable[[str, str, str, int, docutils.parsers.rst.states.Inliner, Dict, List],
                                          Tuple[List[docutils.nodes.reference], List[docutils.nodes.reference]]]
                        ) -> None:
    ...

def __getattr__(name) -> Any: ...
