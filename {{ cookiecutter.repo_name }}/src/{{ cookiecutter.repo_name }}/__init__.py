#!/usr/bin/env python
"""Provide code that should be accessable from the TOP level of the package."""

# Imports
import logging
log = logging.getLogger(__name__)

from pathlib import Path

import munch

from {{ cookiecutter.project_name }}.misc import load_csv
from {{ cookiecutter.project_name }}.logging import setup_logging

# Metadata
__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.email }}"


__all__ = ["setup_logging", "load_csv"]

