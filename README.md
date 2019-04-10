# Vanilla package
[![Build Status](https://travis-ci.org/Feralo/vanilla_pkg.svg?branch=master)](https://travis-ci.org/Feralo/vanilla_pkg)
[![Coverage Status](https://coveralls.io/repos/github/Feralo/vanilla_pkg/badge.svg?branch=master)](https://coveralls.io/github/Feralo/vanilla_pkg?branch=master)


This is a simple class which takes borrows heavily from the examples in [the docs](https://docs.python.org/3/tutorial/classes.html) package, built process outlined [python's](https://python.org) official [packaging project tutorial](https://packaging.python.org/tutorials/packaging-projects/).

This is a place to prototype testing methods and build pipelines.

Unit tests reside in the **test** subdirectory of the vanilla_pkg directory. 

Tests can be run with:
     `pytest -v --cov=vanilla_pkg`


## Anaconda package
Building of a conda package can be done by following [the user guide for uploading packages](http://docs.anaconda.com/anaconda-cloud/user-guide/tasks/work-with-packages/#uploading-packages). 
The user guide refers to a meta.yaml file but provides no examples. Fortunately, there is an [example package in the conda demo](https://github.com/Anaconda-Platform/anaconda-client).
