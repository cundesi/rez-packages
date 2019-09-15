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
    'maya%s' % version.split('.')[0],
    'Render',
    'mayapy',
    "register_maya"]
has_plugins = True
uuid = "repository.maya"


def commands():

    env.MAYA_VERSION = str(this.version.major)
    env.MAYA_LOCATION.set("{root}/maya")

    env.PATH.prepend("{root}/maya/bin")
    env.PATH.prepend("{root}/bin")

    env.LD_LIBRARY_PATH.append("{root}/maya/lib")

    env.PYTHONPATH.append("{root}/maya/lib/python2.7/site-packages")

    env.AUTODESK_ADLM_THINCLIENT_ENV.set("{root}/AdlmThinClientCustomEnv.xml")

    env.MAYA_DISABLE_CIP = 1

    env.MAYA_DISABLE_CER = 1

    # env.MAYA_COLOR_MANAGEMENT_POLICY_LOCK = 1
    # env.MAYA_COLOR_MANAGEMENT_POLICY_FILE = "{root}/MayaNoColorManagement.xml"

    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
