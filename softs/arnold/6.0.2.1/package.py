# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "arnold"

def _version():
    import os
    return os.path.basename(os.getcwd())

version = _version()

authors = ["SolidAngle"]

description = ""

requires = ['softs_install_path']

tools = [
    'kick',
    'oslc',
    'oslinfo',
    'maketx'
]

build_command = False

uuid = "repository.arnold"


def commands():
    import os
    install_path = os.path.join(env.SOFTS_INSTALL_PATH.get(), 'Arnold', str(this.version)).replace('\\', '/')
    env.PATH.append(os.path.join(install_path, "bin"))
    env.LD_LIBRARY_PATH.append(os.path.join(install_path, "bin"))
    env.PYTHONPATH.append(os.path.join(install_path, "python"))
