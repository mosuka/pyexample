=========
PyExample
=========


This is an example Python project.

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

Once Poetry is installed, change the virtual environment to be created in the project folder.

.. code-block:: bash

   $ poetry config virtualenvs.in-project true

Setup virtual environment
-------------------------

Prepare and activate the Python virtual environment with the following command.

.. code-block:: bash

   $ poetry install
   $ source .venv/bin/activate

Run tests on Poetry
===================

.. code-block:: bash

   $ poetry run pytest

Run lint check
==============

.. code-block:: bash

   $ flake8 ./pyexample

Run coverage on Poetry
======================

.. code-block:: bash

   $ poetry run pytest --cov=pyexample --cov-report=html -v ./tests

Run on Poetry
=============

$ poetry run pyexample

Build
=====

.. code-block:: bash

   $ poetry build

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

Build documents
===============

.. code-block:: bash

   $ cd docs
   $ make apidoc
   $ make html