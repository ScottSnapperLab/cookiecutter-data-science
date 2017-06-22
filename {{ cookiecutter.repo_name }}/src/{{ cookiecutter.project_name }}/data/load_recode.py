#!/usr/bin/env python
"""Provide logic to import, parse, and recode project data into usable structures for analysis."""

# Imports
import os
from pathlib import Path
import logging

import pandas as pd
import numpy as np

from munch import Munch, munchify, unmunchify

import {{ cookiecutter.project_name }}.errors as e

# Metadata
__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.email }}"


# Functions
def main():
    pass
