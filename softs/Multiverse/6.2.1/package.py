# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building

name = "Multiverse"


def _version():
    import os
    return os.path.basename(os.getcwd())


version = _version()

authors = ["j-cube"]

description = ""

tools = ['usdcat', 'usdview', 'usdzip', 'usdedit']

requires = ['softs_install_path']

build_command = False

uuid = "repository.Multiverse"


def commands():
    import os
    install_path = os.path.join(env.SOFTS_INSTALL_PATH.get(), 'Multiverse', str(this.version)).replace('\\', '/')

    env.MV_ROOT=install_path
    env.PATH.append(os.path.join(install_path, 'bin'))
    env.PATH.append(os.path.join(install_path, 'lib'))

    env.LD_LIBRARY_PATH.append(os.path.join(install_path, 'bin'))
    env.LD_LIBRARY_PATH.append(os.path.join(install_path, 'lib'))

    env.PYTHONPATH.append(os.path.join(install_path, 'lib', 'python'))
    env.USD_PLUG_IN_PATH.append(os.path.join(install_path, 'plugin', 'usd'))
    env.DL_PROCEDURALS_PATH.append(os.path.join(install_path, 'lib', 'procedurals', '3delight'))
    env.ARNOLD_PLUGIN_PATH.append(os.path.join(install_path, 'lib', 'procedurals', 'arnold'))
    env.MAYA_MODULE_PATH.append(os.path.join(install_path, 'maya'))
