name = 'ofx_install_path'
version = 'release'

build_command = False

def commands():
    import os
    import platform
    platform_string = platform.system()
    if platform_string == 'Windows':
        install_path_root = 'Z:/Software/Plugins/OFX'
    else:
        install_path_root = '/mnt/cundesiNas/Software/Plugins/OFX'
    env.OFX_INSTALL_PATH = install_path_root
