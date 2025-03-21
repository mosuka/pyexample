from importlib.metadata import version

__dist_name__ = __name__
"""str: __dist_name__ is the name of this distribution.
"""

__version__ = version(__dist_name__)
"""str: __version__ is the version of this distribution.
"""


def get_dist_name():
    """Get distribution name function.

    Returns:
        str: Distribution name.
    """
    return __dist_name__


def get_version():
    """Get version function.

    Returns:
        str: Distribution Version.
    """
    return __version__
