.. ESPEI documentation master file, created by
   sphinx-quickstart on Sat Jun 24 22:30:49 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====
ESPEI
=====

ESPEI, or Extensible Self-optimizing Phase Equilibria Infrastructure, is a tool for automated thermodynamic database development within the CALPHAD method.

The ESPEI package is based on a fork of `pycalphad-fitting`_ and uses `pycalphad`_ for calculating Gibbs free energies of thermodynamic models.
The implementation for ESPEI involves first fitting single-phase data by calculating parameters in thermodynamic models that are linearly described by the single-phase input data.
Then Markov Chain Monte Carlo (MCMC) is used to optimize the candidate models from the single-phase fitting to multi-phase zero-phase fraction data.
Single-phase and multi-phase fitting methods are described in Chapter 3 of `Richard Otis's thesis`_.

The benefit of this approach is the automated, simultaneous fitting for many parameters that yields uncertainty quantification, as shown in Otis and Liu High-Throughput Thermodynamic Modeling and Uncertainty Quantification for ICME. `Jom 69, (2017)`_.

The name and idea of ESPEI are originally based off of Shang, Wang, and Liu, ESPEI: Extensible, Self-optimizing Phase Equilibrium Infrastructure for Magnesium Alloys Magnes. Technol. 2010 617–622 (2010).

.. _pycalphad-fitting: https://github.com/richardotis/pycalphad-fitting
.. _pycalphad: http://pycalphad.org
.. _Richard Otis's thesis: https://etda.libraries.psu.edu/catalog/s1784k73d
.. _Jom 69, (2017): http://dx.doi.org/10.1007/s11837-017-2318-6

Installation
============

Creating a virual environment is highly recommended.
You can install ESPEI from PyPI

.. code-block:: bash

    pip install espei

or install in develop mode from source

.. code-block:: bash

    git clone https://github.com/phasesresearchlab/espei.git
    cd espei
    pip install -e .


Usage
=====

Run ``espei -h`` to see the options in the command utility.

ESPEI has two different fitting modes: single-phase and multi-phase fitting.
You can run either of these modes or both of them sequentially.

To run either of the modes, you need to have a fit settings file that describes the phases in the system using the standard CALPHAD approach within the compound energy formalism.
You also need to describe the data to fit.
You will need single-phase and multi-phase data for a full run.
Fit settings and all datasets are stored as JSON files and described in detail at the :ref:`Input Files` page.

The main output result is going to be a database (defaults to ``out.tdb``)
and an array of the steps in the MCMC chain (defaults to ``chain.txt``).

Full run
--------

A minimal run of ESPEI with single phase fitting and MCMC fitting would involve setting these two files

.. code-block:: bash

    espei --datasets=my-dataset-folder --fit-settings=my-input.json


Single-phase only
-----------------

If you have only heat capacity, entropy and enthalpy data and mixing data (e.g. from first-principles),
you may want to see the starting point for your MCMC calculation.
To do this, simply pass the ``--no-mcmc`` flag to ESPEI

.. code-block:: bash

    espei --no-mcmc --datasets=my-dataset-folder --fit-settings=my-input.json


Multi-phase only
----------------

If you have a database already and just want to do a multi-phase fitting, you can specify a starting TDB file with

.. code-block:: bash

    espei --datasets=my-dataset-folder --fit-settings=my-input.json --input-tdb=my-starting-database.tdb

The TDB file you input must have all of the degrees of freedom you want as FUNCTIONs with names beginning with ``VV``.

Customization
-------------

In all cases, ESPEI lets you control certain aspects of your calculations from the command line. Some useful options are

* ``verbose`` (or ``-v``) controls the logging level. Default is Warning. Using verbose once gives more detail (Info) and twice even more (Debug)
* ``tracefile`` lets you set the output trace of the chain to any name you want. The default is ``chain.txt``.
* ``output-tdb`` sets the name of the TDB output at the end of the run. Default is ``out.tdb``.
* ``input-tdb`` is for setting input TDBs. This will skip single phase fitting and fit all parameters defined as FUNCTIONs with names starting with ``VV``.
* ``no-mcmc`` will do single-phase fitting only. Default is to perform MCMC fitting.
* ``mcmc-steps`` sets the number of MCMC steps. The default is 1000.
* ``save-interval`` controls the interval for saving the MCMC chain. The default is 100 steps.

Run ``espei -h`` to see  all of the configurable options.


FAQ
---

Q: There is an error in my JSON files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A: Common mistakes are using single quotes instead of the double quotes required by JSON files.
Another common source of errors is misaligned open/closing brackets.

To find the offending files, you can rename the datasets to anything not ending in ``.json``, such as ``my_datasets.json.disabled``. The renamed files will be ignored and it allows you to track down any problematic files.

Module Hierarchy
================

* ``fit.py`` is the main entry point
* ``paramselect.py`` is where all of the fitting happens. This is the core.
* ``core_utils.py`` contains specialized utilities for ESPEI.
* ``utils.py`` are utilities with reuse potential outside of ESPEI.
* ``plot.py`` holds plotting functions

License
=======

ESPEI is MIT licensed. See LICENSE.

.. toctree::
   :maxdepth: 4
   :caption: Contents

   input_files
   CHANGES
   api/modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`