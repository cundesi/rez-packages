# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, alias, building


def _version():
    import os
    return os.path.basename(os.getcwd())


name = "nuke"

version = _version()

authors = ["Foundry"]

description = "Foundry Nuke {}".format(version)

variants = []

tools = ['nuke']

has_plugins = True

build_command = "python -m build_utils build {root}"

uuid = "repository.nuke"

private_build_requires = ["rez_build"]

def commands():

    import os
    from rez.utils.platform_ import platform_

    platform_name = platform_.name

    def find_nuke_location(version):
        if platform_name == 'windows':
            return "C:/Program Files/Nuke{}".format(version)
        elif platform_name == 'linux':
            return "/usr/local/nuke{}".format(version)

    nuke_install_location = find_nuke_location(this.version)
    env.NUKE_LOCATION_VERSION = str(this.version).split('v')[0]
    env.PATH.prepend('{root}/bin')
    env.PATH.prepend(nuke_install_location)
    env.FN_DISABLE_LICENSE_DIALOG = 1    # suppress temporary license dialog
