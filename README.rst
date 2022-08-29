=========
PyExample
=========

|MIT license|

.. |MIT license| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://lbesson.mit-license.org/

This is an example Python project.

https://mosuka.github.io/pyexample/


How to setup this repository
============================

Install dependencies for building Python
----------------------------------------

The following command will install the dependent libraries needed to build Python.

.. code-block:: bash

   $ sudo apt install -y libbz2-dev sqlite3 libsqlite3-dev libreadline-dev python3-tk

Setup Pyenv
-----------

Refer to the following URL to install Penv.

https://github.com/pyenv/pyenv

Install Python for development
------------------------------

If the target version of Python for development is not installed, Suse Pyenv to install it.

.. code-block:: bash

   $ pyenv install 3.10.6
   $ pyenv local 3.10.6

Setup Poetry
------------

Refer to the following URL to install Poetry.

https://github.com/python-poetry/poetry


Initialize the project
======================

.. code-block:: bash

   $ make init

Run tests on Poetry
===================

.. code-block:: bash

   $ make test

Run code formatter
==================

.. code-block:: bash

   $ make format

Run lint check
==============

.. code-block:: bash

   $ make lint

Run coverage on Poetry
======================

.. code-block:: bash

   $ make coverage

Run benchmark on Poetry
=======================

.. code-block:: bash

   $ make benchmark

Run on Poetry
=============

.. code-block:: bash

   $ make run

Build
=====

.. code-block:: bash

   $ make build

Build documents
===============

.. code-block:: bash

   $ make docs
   
Install
=======

.. code-block:: bash

   $ tar zxvf dist/pyexample-0.1.0.tar.gz
   $ cd pyexample-0.1.0
   $ pip install .

Run
===

.. code-block:: bash

   $ pyexample

Uninstall
=========

.. code-block:: bash

   $ pip uninstall pyexample
