# -*- coding: utf-8 -*-

from rez.utils.lint_helper import env, building, scope  # make linter happy


name = "usdQt"

def _version():
    import os
    return os.path.basename(os.getcwd())

version = _version()

authors = [
    'LumaPictures'
]

description = \
    """
Reusable UI widgets for viewing and authoring USD files
    """

build_command = False

requires = ['softs_install_path', 'usd']

tools = [
]

uuid = "repository.usdQt"


def commands():
    import os
    install_path = os.path.join(env.SOFTS_INSTALL_PATH.get(), 'usdQt', str(this.version)).replace('\\', '/')
    env.PYTHONPATH.prepend(os.path.join(install_path, 'lib/python'))
