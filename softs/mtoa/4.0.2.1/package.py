# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building

name = "mtoa"


def _version():
    import os
    return os.path.basename(os.getcwd())


version = _version()

authors = ["SolidAngle"]

description = ""

plugin_for = ["maya"]

tools = ['kick', 'oslc', 'oslinfo', 'maketx']

requires = ['softs_install_path']

build_command = False

uuid = "repository.mtoa"


def commands():
    import os
    install_path = os.path.join(env.SOFTS_INSTALL_PATH.get(), 'Mtoa', str(this.version),
                                env.REZ_MAYA_MAJOR_VERSION.get()).replace('\\', '/')
    env.PATH.append(os.path.join(install_path, "bin"))
    env.LD_LIBRARY_PATH.append(os.path.join(install_path, "bin"))
    env.MAYA_MODULE_PATH.append(install_path)
    env.MAYA_RENDER_DESC_PATH.append(install_path)
    env.MTOA_EXTENSIONS_PATH.append(install_path)
