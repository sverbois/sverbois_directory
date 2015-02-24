sverbois_directory
==================

A Kotti POC with:

- new content types
- new workflows
- new roles
- edit permission control
- use colanderalchemy for edit view

Setup
-----

::

     kotti.configurators =
         ...
         sverbois_directory.kotti_configure

Test sverbois_directory
-----------------------

Installation::

    git clone git@github.com:sverbois/sverbois_directory.git
    cd sverbois_directory
    virtualenv-2.7 .
    ./bin/python bootstrap-buildout.py --version=2.3.1 --setuptools-version=12.0.5 -c apptest.cfg
    ./bin/buildout -c apptest.cfg

Start application::

    ./bin/pserve apptest.ini --reload
