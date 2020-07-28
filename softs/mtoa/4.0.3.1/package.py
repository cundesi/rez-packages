# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env

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
    from rez.utils.platform_ import platform_

    platform_name = platform_.name

    install_path = os.path.join(
        env.SOFTS_INSTALL_PATH.get(), 'Mtoa', str(this.version), env.REZ_MAYA_MAJOR_VERSION.get()
    ).replace('\\', '/')

    # set mtoa env
    env.PATH.append(os.path.join(install_path, "bin"))
    if platform_name == 'linux':
        env.LD_LIBRARY_PATH.append(os.path.join(install_path, "bin"))

    env.MAYA_PLUG_IN_PATH.append(os.path.join(install_path, "plug-ins"))
    env.MAYA_PRESET_PATH.append(os.path.join(install_path, "presets"))
    env.MAYA_SCRIPT_PATH.append(os.path.join(install_path, "scripts"))
    env.PYTHONPATH.append(os.path.join(install_path, "scripts"))
    env.XBMLANGPATH.append(os.path.join(install_path, "icons"))

    env.MAYA_RENDER_DESC_PATH.append(install_path)
    env.MTOA_EXTENSIONS_PATH.append(install_path)
