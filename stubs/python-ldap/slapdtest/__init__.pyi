from logging.handlers import SysLogHandler as SysLogHandler

from slapdtest._slapdtest import (
    SlapdObject as SlapdObject,
    SlapdTestCase as SlapdTestCase,
    requires_init_fd as requires_init_fd,
    requires_ldapi as requires_ldapi,
    requires_sasl as requires_sasl,
    requires_tls as requires_tls,
    skip_unless_ci as skip_unless_ci,
)

__version__: str
