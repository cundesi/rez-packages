# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building

name = "maya_usd"


def _version():
    import os
    return os.path.basename(os.getcwd())


version = _version()

authors = ["Autodesk"]

description = ""

plugin_for = ["maya"]

tools = []

requires = ['maya-2020']

build_command = False

uuid = "repository.maya_usd"

private_build_requires = ['rez_build']

build_command = "rez_build {root}"

def commands():
    env.MAYA_MODULE_PATH.append('{root}')
