name = "ninja"

def _version():
    import os
    return os.path.basename(os.getcwd())

version = _version()

authors = [
    "ninja"
]

description = \
    """
    a small build system with a focus on speed https://ninja-build.org/
    """

build_requires = []

requires = ['softs_install_path']

build_command = False

uuid = "repository.ninja"

def commands():
    import os
    install_path = os.path.join(env.SOFTS_INSTALL_PATH.get(), 'Ninja', str(this.version)).replace('\\', '/')
    env.PATH.append(os.path.join(install_path, "bin"))
