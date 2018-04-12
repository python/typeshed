import os
from setuptools import setup

import typeshed


CURRENT_DIR = os.path.dirname(__file__)


def get_long_description():
    readme_md = os.path.join(CURRENT_DIR, "README.md")
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()


assert not typeshed.__version__.endswith(".dirty"), (
    "DO NOT PUBLISH DIRTY VERSIONS TO PyPI! "
    "If you only wish to install locally, stash your changes first."
)


PROJECT_URL = "https://github.com/python/typeshed/"
ISSUES_URL = PROJECT_URL + "issues/"
SOURCE_URL = PROJECT_URL
v = typeshed.__version__.split("+", 1)
if len(v) == 2:
    SOURCE_URL += "commit/" + v[1]
PUBLIC_VERSION = v[0]


setup(
    name="typeshed",
    version=PUBLIC_VERSION,
    description="Collection of library stubs for Python, with static types",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license="MIT",
    url=PROJECT_URL,
    packages=["typeshed"],
    include_package_data=True,  # from MANIFEST.in
    project_urls={"Bug Tracker": ISSUES_URL, "Source Code": SOURCE_URL},
    install_requires=[],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    python_requires=">=2.7",
    zip_safe=True,
)
