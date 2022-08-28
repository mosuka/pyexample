#!/usr/bin/env python

# -*- coding: utf-8 -*-

from pyexample import get_dist_name, get_version


def main():
    print("%s: %s" % (get_dist_name(), get_version()))


if __name__ == "__main__":
    main()
