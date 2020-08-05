name = "maya_scenefile_parser"

version = "any"

authors = ["mottosso"]

description = \
    """
    Parse Binary and Ascii Maya scene files with Python.
    """

requires = ['codeLibrary']

build_command = ""

uuid = "mottosso.maya_scenefile_parser"

def commands():
    package_root = expandvars("${CODELIBRARYROOT}/third_party/this.name")
    env.PYTHONPATH.append(package_root)
