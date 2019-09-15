# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


def _version():
    import os
    return os.path.basename(os.getcwd())


name = "maya"
version = _version()
authors = ["Autodesk"]
description = "Autodesk maya %s" % version.split('.')[0]
variants = [["platform-linux"]]
tools = [
    'maya',
    'Render',
    'mayapy',
]
has_plugins = True
build_command = ""
uuid = "repository.maya"


def commands():
    import os
    from rez.utils.platform_ import platform_

    def find_maya_location(version):
        if os.getenv('MAYA_LOCATION'):
            return os.getenv('MAYA_LOCATION')
        if platform_.name == 'windows':
            return "C:/Program Files/Autodesk/Maya{}".format(version)
        elif platform_.name == 'linux':
            return "/usr/autodesk/maya{}".format(version)

    env.MAYA_VERSION = str(this.version.major)
    maya_location = find_maya_location(env.MAYA_VERSION.get())
    env.MAYA_LOCATION.set(maya_location)

    env.PATH.prepend(os.path.join(maya_location, "bin"))
    env.PATH.append(os.path.join(maya_location, "lib"))

    env.LD_LIBRARY_PATH.append(os.path.join(maya_location, "lib"))

    env.MAYA_DISABLE_CIP = 1

    env.MAYA_DISABLE_CER = 1

    # env.MAYA_COLOR_MANAGEMENT_POLICY_LOCK = 1
    # env.MAYA_COLOR_MANAGEMENT_POLICY_FILE = "{root}/MayaNoColorManagement.xml"

    if building:
        env.CMAKE_MODULE_PATH.append(os.path.join(maya_location, "cmake"))
