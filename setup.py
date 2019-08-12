from setuptools import setup
from setuptools import find_packages, find_namespace_packages


NAME = "gitget"
DESCRIPTION = "Download a specific folder from a gitgub repository."
KEYWORDS = "github gitget"
MAINTAINER = "André P. Santos"
MAINTAINER_EMAIL = "andreztz@gmail.com"
URL = "https://github.com/andreztz/gitget"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "1.0.1"


def readme():
    with open("README.md") as f:
        return f.read()


def required():
    with open("requirements.txt") as f:
        return f.read().splitlines()


# https://setuptools.readthedocs.io/en/latest/setuptools.html#developer-s-guide
package = {
    "name": NAME,
    "version": VERSION,
    "description": DESCRIPTION,
    "long_description": readme(),
    "long_description_content_type": "text/markdown",
    "keywords": KEYWORDS,
    "maintainer": MAINTAINER,
    "maintainer_email": MAINTAINER_EMAIL,
    "python_requires": REQUIRES_PYTHON,
    "url": URL,
    "license": "my_license",
    # "package_dir": {"": "src"},
    # "packages": find_namespace_packages(where="src"),
    "packages": find_packages(),
    "install_requires": required(),
    "entry_points": {"console_scripts": ["gitget=src.__main__:main"]},
    "classifiers": [
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
    ],
}

setup(**package)
