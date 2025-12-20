from __future__ import annotations

from docker.models.containers import Container


def check_attach_stream(c: Container) -> None:
    for line in c.attach(stdout=True, stderr=True, stream=True, logs=True):
        line.decode("utf-8")
