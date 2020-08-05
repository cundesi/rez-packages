#!/usr/bin/env python


def init_module_paths(module_path):
    import os
    from rez.utils.lint_helper import env

    env.MAYA_PLUG_IN_PATH.append(os.path.join(module_path, "plug-ins"))
    env.MAYA_PRESET_PATH.append(os.path.join(module_path, "presets"))
    env.MAYA_SCRIPT_PATH.append(os.path.join(module_path, "scripts"))
    env.PYTHONPATH.append(os.path.join(module_path, "scripts"))
    env.XBMLANGPATH.append(os.path.join(module_path, "icons"))
    env.MAYA_SHELF_PATH.append(os.path.join(module_path, "shelfs"))
