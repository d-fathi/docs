Features
========

Modeling
--------

* Write a new element in a few lines: declare signals and parameters, then write the equations in ``analog()``.
* Time derivative ``ddt(x)`` and integral ``idt(x)`` are available inside the equations.
* No derivatives to code: the Jacobian is obtained automatically by finite differences of ``analog()``.
* Parameters carry units and descriptions and accept engineering prefixes (``"C=100nF"``).
* About 40 built-in models: passive elements, controlled and independent sources, diodes, thyristors,
  BJT, MOSFET, JFET, IGBT, op-amp, comparator and 555 timer.

Simulation
----------

* DC operating point and DC sweep of any parameter.
* Transient analysis: backward Euler or second-order BDF, fixed or adaptive time step.
* Small-signal AC analysis with complex results (Bode plots).
* Parametric sweep that repeats any analysis for a list of values.
* Robust convergence: limited Newton steps, time-step bisection and gmin stepping.

Results
-------

* Results are NumPy arrays, ready for any post-processing.
* ``plot()`` draws transient, DC-sweep, AC and swept results with Matplotlib, and can save to a file.

General
-------

* Pure Python 3, working on Linux, Windows and macOS (CPython and PyPy).
* Only two dependencies: NumPy and Matplotlib.
* Free software under the MIT license.
