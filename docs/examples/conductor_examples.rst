Conductor: resistance from geometry, temperature and self-heating
=================================================================

Script: ``conductor_examples.py``

Description::

      R = Rho Len / Area (1 + Alpha (T - T0)),   T = Tamb (+ DT with thermal=True)
      Cth d(DT)/dt = V^2 / R - DT / Rth
    Checks:
      1. resistance of copper wires from the geometry (a table of lengths and sections)
      2. resistance against the ambient temperature (Tamb sweep)
      3. self-heating of a tungsten filament (lamp): I(V) curve and the DC temperature
         against a numerical solution of the same equations
      4. lamp switch-on: inrush current while the filament heats up, against scipy

Code
----

.. literalinclude:: conductor_examples.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/conductor_examples.png
   :alt: Conductor: resistance from geometry, temperature and self-heating
   :align: center

