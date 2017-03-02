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
__author__ = "Gus Dunn"
__email__ = "w.gus.dunn@gmail.com"


# Functions
def main():
    pass
