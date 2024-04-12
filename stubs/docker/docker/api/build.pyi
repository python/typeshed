from _typeshed import Incomplete

log: Incomplete

class BuildApiMixin:
    def build(
        self,
        path: Incomplete | None = None,
        tag: str | None = None,
        quiet: bool = False,
        fileobj: Incomplete | None = None,
        nocache: bool = False,
        rm: bool = False,
        timeout: Incomplete | None = None,
        custom_context: bool = False,
        encoding: Incomplete | None = None,
        pull: bool = False,
        forcerm: bool = False,
        dockerfile: Incomplete | None = None,
        container_limits: Incomplete | None = None,
        decode: bool = False,
        buildargs: Incomplete | None = None,
        gzip: bool = False,
        shmsize: Incomplete | None = None,
        labels: Incomplete | None = None,
        cache_from: Incomplete | None = None,
        target: Incomplete | None = None,
        network_mode: Incomplete | None = None,
        squash: Incomplete | None = None,
        extra_hosts: Incomplete | None = None,
        platform: Incomplete | None = None,
        isolation: Incomplete | None = None,
        use_config_proxy: bool = True,
    ): ...
    def prune_builds(
        self, filters: Incomplete | None = None, keep_storage: Incomplete | None = None, all: Incomplete | None = None
    ): ...

def process_dockerfile(dockerfile, path): ...
