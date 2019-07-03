.. gcc.tree documentation master file.

=================================================
 GCC Tree: Your Tool For Compiler Tree Climbing
=================================================

Quickstart
==========

.. _installation-guide:

Installation
------------

To install :term:`gcc.tree`, open an interactive shell and run:

.. code::

    python<version> -m pip install gcc.tree

If you want :term:`gcc.tree` to be installed for your default Python
installation, you can instead use:

.. code::

    python -m pip install flake8

.. note::

    It is **very** important to install :term:`gcc.tree` on the *correct* version of
    Python for your needs. If you want :term:`gcc.tree` to properly parse new language
    features in Python 3.5 (for example), you need it to be installed on 3.5
    for :term:`gcc.tree` to understand those features. In many ways, gcc.tree is tied to
    the version of Python on which it runs.

Using gcc.tree
--------------

To start using :term:`gcc.tree`, open an interactive shell and run:

.. code::

    flake8 path/to/code/to/check.py
    # or
    flake8 path/to/code/

.. note::

    If you have installed :term:`gcc.tree` on a particular version of Python (or on
    several versions), it may be best to instead run ``python<version> -m
    flake8``.

If you only want to see the instances of a specific warning or error, you can
*select* that error like so:

.. code::

    flake8 --select E123,W503 path/to/code/

Alternatively, if you want to *ignore* only one specific warning or error:

.. code::

    flake8 --ignore E24,W504 path/to/code/

Please read our user guide for more information about how to use and configure
:term:`gcc.tree`.

FAQ and Glossary
================

.. toctree::
    :maxdepth: 2

    faq
    glossary
    manpage

General Indices
===============

* :ref:`genindex`
* :ref:`Index of Documented Public Modules <modindex>`
* :ref:`Glossary of terms <glossary>`
