#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import inspect
from pathlib import Path

HOME_DIR = Path(inspect.getfile(inspect.currentframe())).parent


def filter_req_paths(paths, func):
    """Return list of filtered libs."""
    if not isinstance(paths, list):
        raise ValueError("Paths must be a list of paths.")

    libs = set()
    junk = set(['\n'])
    for p in paths:
        with p.open(mode='r') as reqs:
            lines = set([line for line in reqs if func(line)])
            libs.update(lines)

    return list(libs - junk)


def is_pipable(line):
    """Filter for pipable reqs."""
    if "# not_pipable" in line:
        return False
    elif line.startswith('#'):
        return False
    else:
        return True


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = filter_req_paths(paths=[HOME_DIR / "requirements.txt",
                                       HOME_DIR / "requirements.pip.txt"], func=is_pipable)

setup_requirements = ["pytest-runner"]

test_requirements = test_requirements = ["pytest"]


setuptools.setup(
    name="{{ cookiecutter.project_slug }}",
    version="0.0.1",
    url="{{ cookiecutter.github_url }}",

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.email }}",

    description="{{ cookiecutter.description }}",
    # long_description=open('README.rst').read(),

    packages=setuptools.find_packages('src'),
    package_dir={"": "src"},


    include_package_data=True,
    install_requires=requirements,
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,

    zip_safe=False,
    entry_points={
    "console_scripts": [
        "{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}.cli.main:run",
        ]
    },
)
