Zener Diode
===========

.. code-block:: python

    from pyams.models import ZenerDiode

    X1 = ZenerDiode("p", "n")
    X1.setParams("Vz=5.1 Ibv=0.001")

Terminals
---------

``ZenerDiode(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Vz``
     - 5.1
     - V
     - Zener voltage at the test current
   * - ``Ibv``
     - 0.001
     - A
     - Test current
   * - ``Nz``
     - 1.5
     - –
     - Breakdown knee sharpness
   * - ``Rz``
     - 5
     - Ω
     - Bulk resistance beyond the knee
   * - ``Is``
     - 1e-14
     - A
     - Forward saturation current
   * - ``N``
     - 1
     - –
     - Forward emission coefficient
   * - ``Vt``
     - 0.025
     - V
     - Thermal voltage
   * - ``Cj``
     - 5e-11
     - F
     - Junction capacitance

Description
-----------

The documentation of the class (``help(ZenerDiode)``)::

    Zener diode: a normal junction in the forward direction and a sharp reverse
    breakdown at the zener voltage Vz.

        I(V) = Is (exp(V / N Vt) - 1)                      forward / leakage
               - Ibv exp(-(V + Vz) / (Nz Vt))              breakdown knee
               - max(-(V + Vz), 0) / Rz                    slope beyond the knee
               + Cj dV/dt

    V is the voltage from anode (p) to cathode (n), so the breakdown happens for
    V = -Vz (cathode more positive than the anode by Vz).

    * Vz is the voltage at which the reverse current equals Ibv (the "test
      current", 1 mA by default) : Vz is what the data sheet calls V_Z at I_ZT.
    * The knee is rounded by Nz: near the test current the dynamic resistance is
      rz ~ Nz Vt / I (Nz = 1.5 gives 37 ohm at 1 mA, 7.5 ohm at 5 mA).
    * Rz is the bulk (series) resistance that dominates at high current: the
      current beyond the knee rises as (|V| - Vz) / Rz.

    Terminals: ZenerDiode(p, n)   (anode, cathode).  Use it with the cathode
    towards the positive supply.

    Parameters:
        Vz (V)     zener voltage at the test current (5.1)
        Ibv (A)    test current (1 mA)
        Nz         breakdown knee sharpness (1.5)
        Rz (ohm)   bulk resistance beyond the knee (5)
        Is (A), N, Vt   forward junction (1e-14 A, 1, 25 mV)
        Cj (F)     junction capacitance (50 pF)

Used in the examples
--------------------

* :doc:`Zener diode: I(V) characteristic and shunt regulator </examples/zener_regulator>`

