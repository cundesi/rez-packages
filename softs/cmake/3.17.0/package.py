name = "cmake"

def _version():
    import os
    return os.path.basename(os.getcwd())

version = _version()

authors = [
    "Kitware"
]

description = \
    """
    Cross platform build system
    """

build_requires = []

requires = ['softs_install_path']

build_command = False

uuid = "repository.cmake"

def commands():
    import os
    install_path = os.path.join(env.SOFTS_INSTALL_PATH.get(), 'Cmake', str(this.version)).replace('\\', '/')
    env.PATH.append(os.path.join(install_path, "bin"))
