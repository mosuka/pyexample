from pyexample import get_dist_name, get_version


def test_get_dist_name():
    assert get_dist_name() == "pyexample"


def test_get_version():
    assert get_version() == "0.1.0"


def test_get_dist_name_benchmark(benchmark):
    ret = benchmark(get_dist_name)
    assert ret == "pyexample"


def test_get_version_benchmark(benchmark):
    ret = benchmark(get_version)
    assert ret == "0.1.0"
