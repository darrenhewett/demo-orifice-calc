# Demo Orifice Calculation

A simple python package containing a single-function module which calculates the orifice diameter required to acheive a given flowrate in a pipe. The calculation itself is straightforward and serves as an example of how Python libraries could be used to manage verified and tested calculations rather than using uncontrolled and untrusted spreadsheets.

[![Build Status](https://travis-ci.com/darrenhewett/demo-orifice-calc.svg?branch=master)](https://travis-ci.com/darrenhewett/demo-orifice-calc)

## Installation

You can install this demo orifice calculation module from PyPI:

	pip install demo-orifice-calc

## How to use

The module can be imported into any python 3.x environment such as [Jupyter](https://jupyter.org/). Or, using the Python interpreter:

	>>> from demo_orifice_calc import orifice_calc
	>>> help(orifice_calc)

As a working example if we want to find the orifice diameter required to give a 1.0&nbsp;m headloss in a 300&nbsp;mm diameter pipe at 100&nbsp;L/s :

	>>> orifice_calc(0.1, 0.3, 1.0)
	0.1892662941723228

## Trust

A test suite can be created to gain confidence in the validity of the results of calculation functions like this. This demo library includes one such test which can be checked by looking for the "build | passing" icon near the top of the page on GitHub. The tests can be run manually by downloading the source repo and running:

	pytest