#!/usr/bin/env python
"""Provide error classes for {{ cookiecutter.project_name }}."""

# Imports


# Metadata
__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.email }}"




class {{ cookiecutter.project_name.title().replace('_','') }}Error(Exception):

    """Base error class for {{ cookiecutter.project_name }}."""


class ValidationError({{ cookiecutter.project_name.title().replace('_','') }}Error):

    """Raise when a validation/sanity check comes back with unexpected value."""
