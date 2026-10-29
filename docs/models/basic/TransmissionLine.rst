Transmission Line
=================

.. code-block:: python

    from pyams.models import TransmissionLine

    X1 = TransmissionLine("p1", "p2")
    X1.setParams("Z0=50 Td=1e-09")

Terminals
---------

``TransmissionLine(p1, p2, ref=0, sections=20)``

Optional constructor arguments: ``ref`` (default ``'0'``), ``sections`` (default ``20``).

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Z0``
     - 50
     - Ω
     - Characteristic impedance
   * - ``Td``
     - 1e-09
     - Sec
     - One-way delay
   * - ``R``
     - 0
     - Ω
     - Total series resistance
   * - ``G``
     - 0
     - S
     - Total shunt conductance

Description
-----------

The documentation of the class (``help(TransmissionLine)``)::

    Two-port (single-conductor) transmission line, modelled as a ladder of
    ``sections`` identical lumped sections (pi network: half a shunt capacitor
    at each end of every section).

          p1 --[R/N + L/N]--o--[R/N + L/N]--o-- ... --[R/N + L/N]-- p2
                            |                |
                         C/N, G/N         C/N, G/N      (C/2N, G/2N at the ends)
                            |                |
          ref ---------------------------------------------------------

    The line is described by its characteristic impedance and delay:

        L = Z0 * Td        total series inductance   (H)
        C = Td / Z0        total shunt capacitance   (F)
        R                  total series resistance   (Ohm)
        G                  total shunt conductance   (S)

    so a lossless line has the impedance Z0 = sqrt(L/C) and delays a signal by
    Td = sqrt(L C).  Every section has a series branch  V = (R/N) I + (L/N) dI/dt
    (its current is an extra unknown) and shunt currents  (C/N) dV/dt + (G/N) V.

    Terminals: TransmissionLine(p1, p2, ref="0", sections=20)
        p1, p2   the two ends of the line
        ref      the common (return) conductor, usually ground "0"
        sections number of lumped sections N (fixed when the element is made)

    Accuracy: a ladder is a low-pass filter whose cut-off is about
    N / (pi Td).  Use N >= 10 * Td / tr for a signal of rise time tr (for a
    sine wave N >= 10 * f * Td * 2 pi gives ~1 % in amplitude).  Large N
    costs more (about 2N unknowns).

    Attributes:
        Z0 (param): characteristic impedance, default 50 Ohm.
        Td (param): one-way delay of the line, default 1 ns.
        R (param): total series resistance of the line, default 0 Ohm.
        G (param): total shunt conductance of the line, default 0 S.

Used in the examples
--------------------

* :doc:`Transmission line: pulse, reflections and the load resistance </examples/transmission_line>`

