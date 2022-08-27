from pyexample import __dist_name__, __version__


def test_dist_name():
    assert __dist_name__ == "pyexample"


def test_version():
    assert __version__ == "0.1.0"
