# -*- coding: utf-8 -*-

# Copyright (C) Fix Studio, and/or its licensors.
# All rights reserved.
#
# The coded instructions, statements, computer programs, and/or related
# material (collectively the "Data") in these files contain unpublished
# information proprietary to Fix Studio and/or its licensors.
#
# The Data may not be disclosed or distributed to third parties or be
# copied or duplicated, in whole or in part, without the prior written
# consent of Fix Studio.

from rez.utils.lint_helper import env, building


name = "Sapphire"

def _version():
    import os
    return os.path.basename(os.getcwd())

version = _version()

authors = []

description = ""

requires = ['ofx_install_path']

build_command = False

uuid = "repository.lenscare"

plugin_for = ["nuke"]


def commands():
    import os
    from rez.utils.platform_ import platform_

    platform_name = platform_.name
    install_path = os.path.join(env.OFX_INSTALL_PATH.get(), this.name, platform_name, str(this.version))
    env.OFX_PLUGIN_PATH.prepend(install_path)
