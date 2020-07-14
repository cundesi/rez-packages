name = 'softs_install_path'
version = 'release'

build_command = False

def commands():
    import os
    import platform
    platform_string = platform.system()
    if platform_string == 'Windows':
        install_path_root = 'S:/Software'
    else:
        install_path_root = '/mnt/cundesiNas/Software'
    install_folder = os.path.join(install_path_root, platform_string)
    env.SOFTS_INSTALL_PATH = install_folder
