name = "pw_MultiScriptEditor"

version = "any"

authors = ["paulwinex"]

description = \
    """
    Python Editor for CG Applications
    """

requires = ['codeLibrary']

build_command = ""

uuid = "paulwinex.pw_MultiScriptEditor"


def commands():
    package_root = expandvars("${CODELIBRARYROOT}/third_party/this.name")
    env.PYTHONPATH.append(package_root)
