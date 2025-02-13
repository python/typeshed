import subprocess

from ts_utils.requirements import get_external_stub_requirements

requirements = get_external_stub_requirements()
subprocess.check_call(("pip", "install", *[str(requirement) for requirement in requirements]))
