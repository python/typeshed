# pyright: reportUnnecessaryTypeIgnoreComment=true

from invoke import task, Context

@task
def docker_build(context: Context) -> None:
    pass

@task(docker_build)
def docker_push(context: Context) -> None:
    pass
