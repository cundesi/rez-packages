# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building

name = "arnold_usd"


def _version():
    import os
    return os.path.basename(os.getcwd())


version = _version()

authors = ["SolidAngle"]

description = ""

tools = ['arnold_to_usd']

requires = ["usd", "arnold", "softs_install_path"]

build_command = False

uuid = "repository.arnold_usd"


def commands():
    import os
    import sys
    install_path = os.path.join(env.SOFTS_INSTALL_PATH.get(), 'Arnold_USD', str(this.version)).replace('\\', '/')

    env.PATH.append(os.path.join(install_path, "bin"))
    env.ARNOLD_PLUGIN_PATH.append(os.path.join(install_path, "procedural"))
    env.PYTHONPATH.append(os.path.join(install_path, "lib/python"))
    env.PXR_PLUGINPATH_NAME.append(os.path.join(install_path, "plugin"))
    env.PXR_PLUGINPATH_NAME.append(os.path.join(install_path, "lib/usd"))
    if 'linux' in sys.platform:
        env.LD_LIBRARY_PATH.append(os.path.join(install_path, "lib"))
        env.LD_PRELOAD.append(expandvars(os.path.join('$ARNOLD_ROOT', "bin/libai.so")))
    else:
        env.PATH.append(os.path.join(install_path, "lib"))


