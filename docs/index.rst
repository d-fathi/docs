Welcome to the PyAMS documentation
==================================

.. image:: https://img.shields.io/pypi/v/pyams-lib.svg
    :target: https://pypi.org/project/pyams-lib/
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pyams-lib.svg
    :target: https://pypi.org/project/pyams-lib/
    :alt: Supported Python versions

.. image:: https://img.shields.io/github/license/d-fathi/pyams_lib.svg
    :target: https://github.com/d-fathi/pyams_lib/blob/main/LICENSE
    :alt: License

What is PyAMS?
--------------

**PyAMS** (*Python for Analog and Mixed Signals*) is a Python library for modeling and
simulating analog and mixed-signal electronic circuits. It provides:

- The ability to create **custom models** of electronic components.
- **Simulation** of circuits in different modes of operation: DC, transient (TR) and AC.
- **Visualization** of the results with ``matplotlib`` in Python, or with ``Plotly`` in the CAD system.
- Compatibility with **Python 3+ and PyPy**, on Linux, Windows and macOS.
- **Circuit design** (schematic capture, symbol design and simulation) in a CAD environment, using either:

  1. **VS Code**, with the *PyAMS extension*.
  2. The **PyAMS software**: https://pyams.sf.net

Quick start
-----------

.. code-block:: sh

    pip install pyams-lib

.. toctree::
   :maxdepth: 2
   :caption: Contents

   overview
   installation
   modeling
   simulation
   models/index
   examples/index


.. panels::

    :ref:`News <news-page>`

    What's changed in versions

    ---

    :ref:`Installation <Installation-page>`

    How to install pyams.lib in python

    ---

    :ref:`Modeling <modeling-page>`

    Guidelines to method of modeling of analog elements by pyams.lib.

    ---
    
    :ref:`Simulation <simulation-page>`

    The method of conception and simulation circuits.

    ---
    
    :ref:`Analog-devices <Analog-devices>`

    PyAMS elements and models of analog.

    ---
    
    :ref:`Digital-devices <Digital-devices>`

    PyAMS elements and models of digital.

    ---

    :ref:`Examples <examples-page>`

    Circuit simulator examples.

    ---

    :ref:`Commands <commands-manual-page>`

    The pyams.lib command syntax for simulation.

    ---






.. toctree::
   :maxdepth: 2
   :caption: Contents

   overview
   news
   release_history
   features
   installation
   modeling
   simulation
   options
   models/index
   examples/index
   api

Indices
-------

* :ref:`genindex`
* :ref:`search`
