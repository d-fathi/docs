BJT
===

.. code-block:: python

    from pyams.models import BJT

    X1 = BJT("c", "b", "e")
    X1.setParams("Is=1e-14 Vt=0.025")

Terminals
---------

``BJT(c, b, e)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Is``
     - 1e-14
     - A
     - Saturation current
   * - ``Vt``
     - 0.025
     - V
     - Thermal voltage
   * - ``Bf``
     - 100
     - –
     - Forward current gain
   * - ``Br``
     - 1
     - –
     - Reverse current gain
   * - ``Type``
     - 1
     - –
     - Polarity: 1 = NPN, -1 = PNP
   * - ``Cje``
     - 4.5e-12
     - F
     - Base-emitter junction capacitance
   * - ``Cjc``
     - 3.6e-12
     - F
     - Base-collector junction capacitance

Description
-----------

The documentation of the class (``help(BJT)``)::

    This class implements a bipolar junction transistor (Ebers-Moll model).

    Terminals are given in the order (c, b, e): collector, base, emitter.

    With the junction voltages of an NPN transistor, Vbe = V(b,e) and
    Vbc = V(b,c):

        If = Is * (exp(Vbe / Vt) - 1)        forward diode current
        Ir = Is * (exp(Vbc / Vt) - 1)        reverse diode current
        Ic = If - Ir * (1 + 1 / Br)          current into the collector
        Ib = If / Bf + Ir / Br               current into the base

    and the emitter carries -(Ic + Ib).  A PNP transistor (Type = -1) uses the
    same equations with all voltages and currents sign-reversed.

    Two constant junction capacitances are added in parallel with the diodes,
    as in a real transistor:

        Cje * d(Vbe)/dt  between base and emitter
        Cjc * d(Vbc)/dt  between base and collector

    They are not a detail: with Cje = Cjc = 0 every node coupled through a
    capacitor has no capacitance of its own, and a regenerative circuit (an
    astable multivibrator, a latch) makes the circuit equations jump
    discontinuously when a transistor switches, so no time step can follow
    it and the solver fails.  The defaults are those of a 2N3904 (small-signal NPN).

    Attributes:
        Vbe (signal): Input voltage between base and emitter.
        Vbc (signal): Input voltage between base and collector.
        Ic (signal): Output current from collector to emitter.
        Ib (signal): Output current from base to emitter.
        Is (param): Saturation current (default: 1.0e-14 A).
        Vt (param): Thermal voltage (default: 0.025 V).
        Bf (param): Forward current gain (default: 100).
        Br (param): Reverse current gain (default: 1).
        Type (param): Polarity, 1 for NPN (default) or -1 for PNP.
        Cje (param): Base-emitter junction capacitance (default: 4.5 pF).
        Cjc (param): Base-collector junction capacitance (default: 3.6 pF).

    Methods:
        analog(): Defines the Ebers-Moll equations above plus the capacitances.

Used in the examples
--------------------

* :doc:`AC analysis (small-signal frequency response) </examples/ac_analysis>`
* :doc:`Astable multivibrator (two NPN BJT transistors) </examples/astable>`
* :doc:`BJT astable multivibrator (classic two-transistor circuit) </examples/bjt_astable>`
* :doc:`Schmitt trigger with two BJT transistors (emitter coupled) </examples/schmitt_bjt>`

