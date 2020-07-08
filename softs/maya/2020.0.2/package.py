# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env
from rez.utils.lint_helper import building


def _version():
    import os
    return os.path.basename(os.getcwd())


name = "maya"
version = _version()
authors = ["Autodesk"]
description = "Autodesk maya %s" % version.split('.')[0]
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

    platform_name = platform_.name

    def find_maya_location(version):
        if os.getenv('MAYA_LOCATION'):
            return os.getenv('MAYA_LOCATION')
        if platform_name == 'windows':
            return "C:/Program Files/Autodesk/Maya{}".format(version.split('.')[0])
        elif platform_name == 'linux':
            return "/usr/autodesk/maya{}".format(version)

    env.MAYA_VERSION = str(this.version.major)
    maya_location = find_maya_location(env.MAYA_VERSION.get())
    env.MAYA_LOCATION = maya_location
    env.MAYA_UI_LANGUAGE = 'en_US'
    env.PATH.prepend(os.path.join(maya_location, "bin"))
    env.PATH.append(os.path.join(maya_location, "lib"))

    env.LD_LIBRARY_PATH.append(os.path.join(maya_location, "lib"))

    if platform_name == "windows":
        env.PATH.append("C:/Program Files/Common Files/Autodesk Shared/")
        env.PATH.append("C:/Program Files (x86)/Autodesk/Backburner/")

    elif platform_name == "darwin":
        env.DYLD_LIBRARY_PATH.append(os.path.join(maya_location, "MacOS"))

    # Override some Maya default settings (optimization)
    # todo: These might need to be moved out to be left to company specific choices

    env.MAYA_DISABLE_CIP = 1
    env.MAYA_DISABLE_CER = 1
    env.MAYA_DISABLE_CLIC_IPM = 1
    env.PYMEL_SKIP_MEL_INIT = 1
    env.LC_ALL = "C"

    # env.MAYA_COLOR_MANAGEMENT_POLICY_LOCK = 1
    # env.MAYA_COLOR_MANAGEMENT_POLICY_FILE = "{root}/MayaNoColorManagement.xml"

    if building:
        env.CMAKE_MODULE_PATH.append(os.path.join(maya_location, "cmake"))
