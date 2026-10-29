Thyristor (SCR)
===============

.. code-block:: python

    from pyams.models import Thyristor

    X1 = Thyristor("a", "g", "k")
    X1.setParams("Von=1 Ron=0.05")

Terminals
---------

``Thyristor(a, g, k)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Von``
     - 1
     - V
     - On-state threshold voltage
   * - ``Ron``
     - 0.05
     - Ω
     - On-state slope resistance
   * - ``Roff``
     - 1e+07
     - Ω
     - Forward blocking resistance
   * - ``Rrev``
     - 1e+07
     - Ω
     - Reverse blocking resistance
   * - ``Vrb``
     - 1000
     - V
     - Reverse breakdown voltage
   * - ``Rrb``
     - 1
     - Ω
     - Reverse breakdown slope resistance
   * - ``Igt``
     - 0.002
     - A
     - Gate trigger current
   * - ``Ih``
     - 0.01
     - A
     - Holding current
   * - ``Il``
     - 0.02
     - A
     - Latching current
   * - ``Vbo``
     - 1000
     - V
     - Forward breakover voltage
   * - ``Is``
     - 1e-14
     - A
     - Gate junction saturation current
   * - ``N``
     - 1
     - –
     - Gate junction emission coefficient
   * - ``Vt``
     - 0.025
     - V
     - Thermal voltage

Description
-----------

The documentation of the class (``help(Thyristor)``)::

    Silicon controlled rectifier (SCR): a four-layer device that blocks in both
    directions until it is triggered, then conducts like a diode and stays on
    (latches) after the trigger is removed, until its current falls below the
    holding current.

    Terminals (a, g, k): anode, gate, cathode.

    States (a latch, changed only when a time point is accepted - see Diac):

      OFF  Iak = Vak / Roff  (Vak > 0),  Vak / Rrev (Vak < 0)   (blocks, leakage)
      ON   Iak = Vak / Roff + (Vak - Von)+ / Ron    (conducts: Von = threshold
                                                      voltage, Ron = slope)
      reverse breakdown (any state)  Iak = -(-Vak - Vrb)+ / Rrb  for Vak < -Vrb

      OFF -> ON  when  Vak > 0 and Vak >= Vbo * (1 - Ig / Igt)
                 i.e. the forward breakover voltage falls linearly with the gate
                 current (Vbo at Ig = 0, zero at Ig = Igt): at Ig >= Igt the SCR
                 turns on at any positive Vak (gate trigger)
      latching: after the turn-on the anode current must reach the latching
                 current Il (> Ih) before the gate is removed; until then the
                 SCR falls back to OFF as soon as I < Il (gate not driven)
      ON -> OFF  when  the anode current falls below the holding current Ih
                 (this includes a reversed anode voltage); while the gate is
                 still driven (Ig >= Igt) and Vak > 0 it stays on

    The gate-cathode junction is a diode, Ig = Is (exp(Vgk / N Vt) - 1), so the
    gate must be driven through a resistor (like a real SCR).

    Attributes:
        Von (param): on-state threshold voltage (default 1.0 V).
        Ron (param): on-state slope resistance (default 0.05 ohm).
        Roff (param): forward blocking resistance (default 10 Mohm).
        Rrev (param): reverse blocking resistance (default 10 Mohm).
        Vrb (param): reverse breakdown voltage (default 1000 V), Rrb (param):
                     slope resistance of the reverse breakdown (default 1 ohm).
        Igt (param): gate trigger current (default 2 mA).
        Ih (param): holding current (default 10 mA).
        Il (param): latching current (default 20 mA).
        Vbo (param): forward breakover voltage (default 1000 V).
        Is, N, Vt: gate-cathode junction diode (1e-14 A, 1, 25 mV).

Used in the examples
--------------------

* :doc:`Thyristor characteristics I(V) </examples/thyristor_iv>`
* :doc:`Thyristor I(V) with several gate currents (IG0 ... IG3) </examples/thyristor_iv_family>`
* :doc:`Thyristor I(V) characteristic in the textbook form </examples/thyristor_iv_textbook>`
* :doc:`Thyristor phase control (half-wave, resistive load) </examples/thyristor_phase_control>`
* :doc:`Thyristor lamp dimmer (half-wave phase control, three angles) </examples/thyristor_lamp_dimmer>`

