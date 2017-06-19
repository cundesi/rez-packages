name = "boost"

version = "1.63.0"

authors = [
    "boost.org"
]

description = \
    """
    Peer-reviewed portable C++ source libraries.
    """

build_requires = [
    "gcc-4.8.3",
    "python-2.7"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-CentOS-6.8", "python-2.7"]
]

uuid = "repository.boost"

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")

    # cmake FindPackage env vars
    env.BOOST_ROOT = "{root}"
    env.BOOST_INCLUDEDIR = "{root}/include"
