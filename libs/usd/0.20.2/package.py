# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building

name = "usd"

def _version():
    import os
    return os.path.basename(os.getcwd())

version = _version()

authors = ['Pixar']

description = \
    """
Universal Scene Description (USD) is an efficient, scalable system for authoring, reading, and streaming time-sampled scene description for interchange between graphics applications.
    """

build_command = False

requires = ['softs_install_path']

tools = []

uuid = "repository.usd"


def commands():
    import os
    install_path = os.path.join(env.SOFTS_INSTALL_PATH.get(), 'USD', str(this.version)).replace('\\', '/')
    env.LD_LIBRARY_PATH.append(os.path.join(install_path, "lib"))
    env.PATH.append(os.path.join(install_path, "lib"))
    env.PYTHONPATH.append(os.path.join(install_path, "lib/python"))
    env.PATH.append(os.path.join(install_path, "bin"))