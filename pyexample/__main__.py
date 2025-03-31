#!/usr/bin/env python

# -*- coding: utf-8 -*-

from pyexample import get_dist_name, get_version
from pyexample.logging import getLogger


def main() -> None:
    """ "
    Main function.
    """

    # Set up logging
    logger = getLogger(get_dist_name())
    logger.info("This is an info message.", extra={"version": get_version()})

    print("%s: %s" % (get_dist_name(), get_version()))


if __name__ == "__main__":
    main()
