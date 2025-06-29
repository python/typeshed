import logging
from argparse import ArgumentParser
from typing import Any

from channels.layers import BaseChannelLayer
from channels.worker import Worker
from django.core.management.base import BaseCommand

logger: logging.Logger

class Command(BaseCommand):
    leave_locale_alone: bool = ...
    worker_class: type[Worker] = ...
    verbosity: int
    channel_layer: BaseChannelLayer

    def add_arguments(self, parser: ArgumentParser) -> None: ...
    def handle(
        self, *args: Any, application_path: str | None = ..., channels: list[str] | None = ..., layer: str = ..., **options: Any
    ) -> None: ...
