name = "hotbox_designer"

version = "any"

authors = ["luckylyk"]

description = \
    """
    hotbox designer for CGI softwares
    """

requires = ['codeLibrary']

build_command = ""

uuid = "luckylyk.hotbox_designer"

def commands():
    package_root = expandvars("${CODELIBRARYROOT}/third_party/this.name")
    env.PYTHONPATH.append(package_root)
