import importlib.metadata

__dist_name__ = __name__
"""str: __dist_name__ is the name of this distribution.
"""

__version__ = importlib.metadata.version(__package__ or __name__)
"""str: __version__ is the version of this distribution.
"""
