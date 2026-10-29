IGBT
====

.. code-block:: python

    from pyams.models import IGBT

    X1 = IGBT("c", "g", "e")
    X1.setParams("Kp=0.1 Vth=5")

Terminals
---------

``IGBT(c, g, e)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Kp``
     - 0.1
     - A
     - MOS transconductance Kp [A/V^2]
   * - ``Vth``
     - 5
     - V
     - Gate threshold voltage
   * - ``Lambda``
     - 0
     - V
     - Channel-length modulation [1/V]
   * - ``Alpha``
     - 0.5
     - –
     - PNP transport factor
   * - ``Is``
     - 1e-14
     - A
     - Emitter junction saturation current
   * - ``N``
     - 1
     - –
     - Emission coefficient
   * - ``Vt``
     - 0.025
     - V
     - Thermal voltage
   * - ``Tau``
     - 1e-06
     - Sec
     - Base charge-storage time
   * - ``Cge``
     - 5e-09
     - F
     - Gate-emitter capacitance
   * - ``Cgc``
     - 2e-10
     - F
     - Gate-collector (Miller) capacitance

Description
-----------

The documentation of the class (``help(IGBT)``)::

    N-channel IGBT, built as a MOSFET that drives the base of a PNP transistor
    (the classical macro-model).

                C (collector)
                |
               PNP emitter diode  Idc = Is (exp(Vd / N Vt) - 1)
                |            \
                B (internal)  alpha * Idc  ---->-----+
                |                                    |
               MOS channel  Imos(Vge, Vb - Ve)       |
                |                                    |
                E (emitter) -------------------------+

    G is the insulated gate (only capacitive currents).  Kirchhoff's current
    law at the internal base node B gives

        (1 - alpha) * Idc + Tau * dIdc/dt = Imos

    so in steady state Ic = Imos / (1 - alpha): the MOS current is multiplied by
    the PNP gain (high current for a small gate drive), the on-state voltage
    is one diode drop plus the MOS channel drop, and Ic saturates at
    Kp (Vge - Vth)^2 / (1 - alpha).  When the gate is switched off the
    stored base charge (Tau) decays with Tau / (1 - alpha), which gives the
    typical turn-off "tail current".

    The device blocks reverse voltage (no body diode): put a Diode in
    anti-parallel for a freewheeling path (see igbt_chopper.py).

    Terminals: IGBT(c, g, e)

    Signals (between nodes):
        Vd  (c, B)  emitter-junction voltage      Id  (c, B)  junction current
        Vds (B, e)  MOS channel voltage           Ibe (B, e)  MOS + transport
        Vge (g, e)  gate-emitter voltage          Ige (g, e)  Cge charging
        Vgc (g, c)  gate-collector voltage        Igc (g, c)  Cgc (Miller)

    Parameters:
        Kp (A/V^2)   MOS transconductance, Imos(sat) = Kp (Vge - Vth)^2
        Vth (V)      gate threshold voltage
        Lambda (1/V) channel-length modulation
        Alpha        PNP transport factor (0 ... <1); Ic = Imos / (1 - Alpha)
        Is (A), N, Vt (V)  emitter-junction diode
        Tau (s)      base charge-storage time (turn-off tail)
        Cge, Cgc (F) gate-emitter and gate-collector (Miller) capacitances

Used in the examples
--------------------

* :doc:`IGBT chopper (low-side switch, inductive load, freewheel diode) </examples/igbt_chopper>`

