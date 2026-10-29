Transformer
===========

.. code-block:: python

    from pyams.models import Transformer

    X1 = Transformer("p1", "n1", "p2", "n2")
    X1.setParams("L1=0.1 L2=0.025")

Terminals
---------

``Transformer(p1, n1, p2, n2)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``L1``
     - 0.1
     - H
     - Primary inductance
   * - ``L2``
     - 0.025
     - H
     - Secondary inductance
   * - ``M``
     - 0.0495
     - H
     - Mutual inductance

Description
-----------

The documentation of the class (``help(Transformer)``)::

    This class implements a transformer: two inductors with a mutual inductance.

    Terminals are given in the order (p1, n1, p2, n2): primary winding between
    p1 and n1, secondary winding between p2 and n2.  Both currents are
    positive when they flow into the winding at its p terminal (the dots are
    at p1 and p2).

        V1 = L1 * dI1/dt + M * dI2/dt
        V2 = M * dI1/dt + L2 * dI2/dt

    The mutual inductance M is the same in both equations (reciprocity), so the
    coupling factor is  k = M / sqrt(L1 * L2)  (k = 1 for an ideal core).  The
    turns ratio is  n = N2/N1 = sqrt(L2 / L1), and for k close to 1 the
    secondary voltage is  V2 ~ n * V1.

    Attributes:
        I1, I2 (signal): Currents of the primary / secondary winding.
        V1, V2 (signal): Voltages of the primary / secondary winding.
        L1 (param): Primary inductance in Henries (default: 100 mH).
        L2 (param): Secondary inductance in Henries (default: 25 mH).
        M  (param): Mutual inductance in Henries (default: 49.5 mH, i.e. k = 0.99).

    Methods:
        analog(): Defines the two coupled-inductor equations above.

    Note: the two windings are isolated from each other, so one terminal of
    each winding must be connected to the rest of the circuit (e.g. through a
    diode bridge or a load) for the equations to have a unique solution.
    In DC the windings are short circuits (dI/dt = 0), so never connect the
    primary directly across an ideal voltage source: add a series resistance
    (the winding resistance).  M must satisfy
    |M| <= sqrt(L1 * L2).

Used in the examples
--------------------

* :doc:`Full-wave bridge rectifier fed by a transformer </examples/bridge_rectifier>`

