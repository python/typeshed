from collections.abc import Callable
from typing import Any, ClassVar
from typing_extensions import TypeAlias

from channels.routing import ProtocolTypeRouter
from channels.utils import _ChannelApplication
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler
from django.test.testcases import TransactionTestCase
from django.test.utils import modify_settings

DaphneProcess: TypeAlias = Any  # TODO: temporary hack for daphne.testing.DaphneProcess; remove once daphne provides types

_StaticWrapper: TypeAlias = Callable[[ProtocolTypeRouter], _ChannelApplication]

def make_application(*, static_wrapper: _StaticWrapper | None) -> Any: ...

class ChannelsLiveServerTestCase(TransactionTestCase):
    host: ClassVar[str] = ...
    ProtocolServerProcess: ClassVar[type[DaphneProcess]] = ...
    static_wrapper: ClassVar[type[ASGIStaticFilesHandler]] = ...
    serve_static: ClassVar[bool] = ...

    _port: int
    _server_process: DaphneProcess
    _live_server_modified_settings: modify_settings

    @property
    def live_server_url(self) -> str: ...
    @property
    def live_server_ws_url(self) -> str: ...
