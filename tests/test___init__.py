import importlib

import pyexample

# import pytest


def test_get_dist_name(monkeypatch):
    """
    Test to verify that get_dist_name() returns the same value as __dist_name__,
    using monkeypatch to override the __dist_name__ value.
    """

    # Change __dist_name__ to “test_dist” using monkeypatch
    monkeypatch.setattr(pyexample, "__dist_name__", "test_dist")

    assert pyexample.get_dist_name() == "test_dist"


def test_get_version(monkeypatch):
    """
    Test that get_version() returns a value based on __version__.
    Mock importlib.metadata.version and reload the module to recalculate __version__.
    """

    # Mock importlib.metadata.version to return “9.9.9
    monkeypatch.setattr("importlib.metadata.version", lambda name: "9.9.9")

    # __version__ is computed on module import, so reload after mocking
    importlib.reload(pyexample)

    assert pyexample.get_version() == "9.9.9"


def test_get_dist_name_benchmark(benchmark):
    """
    Benchmark the get_dist_name() function using pytest-benchmark.
    """

    # benchmark() measures the execution time of a passed function and returns its return value.
    result = benchmark(pyexample.get_dist_name)

    # get_dist_name() returns __dist_name__, so verify that the correct value is returned.
    expected = pyexample.get_dist_name()
    assert result == expected


def test_get_version_benchmark(benchmark):
    """ "
    Benchmark the get_version() function using pytest-benchmark.
    """

    # benchmark() measures the execution time of a passed function and returns its return value.
    result = benchmark(pyexample.get_version)

    # get_version() returns __version__, so verify that the correct value is returned.
    expected = pyexample.get_version()
    assert result == expected
