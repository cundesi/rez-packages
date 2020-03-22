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

requires = ['softs_install_path']

build_command = False

uuid = "repository.maya_usd"


def commands():
    import os
    install_path = os.path.join(env.SOFTS_INSTALL_PATH.get(), 'Maya_USD', str(this.version),
                                env.REZ_MAYA_MAJOR_VERSION.get()).replace('\\', '/')
    pxr_usd_path = os.path.join(install_path, 'plugin/pxr')
    env.PYTHONPATH.prepend(os.path.join(pxr_usd_path, 'lib/python'))
    env.MAYA_MODULE_PATH.append(install_path)
