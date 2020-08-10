#!/usr/bin/env python

from rez.utils.lint_helper import env

name = "rez_build"

version = "0.0.1"

requires = ["python-2.7+,<4"]

build_command = "python {root}/install.py"


def commands():
    env.PYTHONPATH.prepend("{root}/python")
    env.PATH.prepend("{root}/bin")
