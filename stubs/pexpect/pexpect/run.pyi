from _typeshed import Incomplete

from pexpect.spawnbase import _Logfile

def run(
    command,
    timeout: float | None = 30,
    withexitstatus: bool = False,
    events: Incomplete | None = None,
    extra_args: Incomplete | None = None,
    logfile: _Logfile | None = None,
    cwd: Incomplete | None = None,
    env: Incomplete | None = None,
    **kwargs,
): ...
def runu(
    command,
    timeout: float | None = 30,
    withexitstatus: bool = False,
    events: Incomplete | None = None,
    extra_args: Incomplete | None = None,
    logfile: _Logfile | None = None,
    cwd: Incomplete | None = None,
    env: Incomplete | None = None,
    **kwargs,
): ...
