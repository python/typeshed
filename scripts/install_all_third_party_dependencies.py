import subprocess
import sys

from ts_utils.requirements import get_external_stub_requirements

use_uv = "--uv" in sys.argv
if use_uv:
    sys.argv.remove("--uv")
    pip_command = ["uv", "pip", "install"]
else:
    pip_command = ["pip", "install"]

requirements = get_external_stub_requirements()
subprocess.check_call(pip_command + [str(requirement) for requirement in requirements])
