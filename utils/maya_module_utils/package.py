#!/usr/bin/env python

from rez.utils.lint_helper import env

name = "maya_module_utils"

version = "0.0.1"

requires = []

build_command = "python -m build_utils build {root}"

private_build_requires = ["rez_build"]


def commands():
    env.PYTHONPATH.prepend("{root}/python")

