Overview
========

What is PyAMS?
--------------

PyAMS (*Python for Analog and Mixed Signals*) is a small, pure-Python circuit simulator.
A circuit is a set of **elements** (models) connected by **nodes**. PyAMS builds the
equations of the circuit by *modified nodal analysis* and solves them with the
Newton–Raphson method, so you only describe *what* each element does, never how to solve the circuit.

The workflow is always the same:

1. **Create the elements** — ``R1 = Resistor("In", "Out")``. The arguments are the node names.
2. **Set their parameters** — ``R1.setParams("R=1KΩ")``.
3. **Build the circuit** — ``cir = circuit(); cir.addElements({"R1": R1, ...})``.
4. **Choose the analysis and run it** — ``cir.analysis(mode="tran", ...); cir.run()``.
5. **Show the results** — ``cir.plot()``, or use the returned NumPy arrays.

Main ideas
----------

Models
    A model is a Python class derived from ``model``. Its terminals, signals and parameters
    are declared in ``__init__`` and its equations are written in ``analog()``.
    About 40 ready-made models are included (see :doc:`models/index`).

Signals and parameters
    A *signal* is a voltage or a current attached to two terminals. A *parameter* is a number
    with a unit and a description; it can be set with engineering prefixes
    (``"R=4.7KΩ"``, ``"C=100nF"``).

Analyses
    DC operating point, DC sweep, transient and small-signal AC analysis, plus a parametric
    sweep that repeats any analysis for a list of parameter values (see :doc:`simulation`).

Results
    ``run()`` returns plain dictionaries of NumPy arrays; ``plot()`` draws them with Matplotlib.

Related projects
----------------

* Documentation: https://pyams-lib.readthedocs.io/
* Source code: https://github.com/d-fathi/pyams_lib
* Package on PyPI: https://pypi.org/project/pyams-lib/
* Circuit design with a graphical (CAD) front-end: https://pyams.sf.net/

License
-------

PyAMS is free software distributed under the **MIT** license.
