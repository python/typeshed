from __future__ import annotations

import yaml


def sequence_handler(loader: yaml.Loader, node: yaml.SequenceNode) -> str:
    return ""


def scalar_handler(loader: yaml.FullLoader, node: yaml.ScalarNode) -> str:
    return ""


def mapping_handler(loader: yaml.SafeLoader, node: yaml.MappingNode) -> str:
    return ""


def any_node_handler(loader: yaml.Loader | yaml.FullLoader | yaml.UnsafeLoader, node: yaml.Node) -> str:
    return ""


def multi_handler(loader: yaml.Loader, tag_suffix: str, node: yaml.MappingNode) -> str:
    return ""


# Handlers may be annotated with the narrowest loader and node classes they use.
yaml.add_constructor("!seq", sequence_handler)
yaml.add_constructor("!scalar", scalar_handler)
yaml.add_constructor("!any", any_node_handler)
yaml.add_constructor("!map", mapping_handler, Loader=yaml.SafeLoader)
yaml.add_multi_constructor("!multi", multi_handler)

# A SafeLoader handler can't be registered on the default loaders.
yaml.add_constructor("!map", mapping_handler)  # type: ignore
