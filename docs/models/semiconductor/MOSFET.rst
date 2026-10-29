MOSFET
======

.. code-block:: python

    from pyams.models import MOSFET

    X1 = MOSFET("d", "g", "s")
    X1.setParams("Kp=0.0001 W=1e-05")

Terminals
---------

``MOSFET(d, g, s)``

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
     - 0.0001
     - A/V²
     - Transconductance parameter
   * - ``W``
     - 1e-05
     - m
     - Channel width
   * - ``L``
     - 1e-06
     - m
     - Channel length
   * - ``Vth``
     - 1
     - V
     - Threshold voltage (magnitude)
   * - ``Lambda``
     - 0.02
     - 1/V
     - Channel-length modulation
   * - ``Type``
     - 1
     - –
     - Polarity: 1 = N-channel, -1 = P-channel
   * - ``Cgs``
     - 2e-14
     - F
     - Gate-source capacitance
   * - ``Cgd``
     - 2e-14
     - F
     - Gate-drain capacitance

Description
-----------

The documentation of the class (``help(MOSFET)``)::

    This class implements a MOSFET (square-law, level 1 model) with the bulk
    connected to the source.

    Terminals are given in the order (d, g, s): drain, gate, source.

    For an N-channel device (Type = 1), with vgs = V(g,s), vds = V(d,s),
    beta = Kp * W / L and vov = vgs - Vth:

        vov <= 0                 cut-off       Id = 0
        0 < vds < vov            triode        Id = beta (vov vds - vds^2/2) (1 + Lambda vds)
        vds >= vov > 0           saturation    Id = beta/2 vov^2 (1 + Lambda vds)

    If vds < 0 the drain and source change roles (the device is symmetric).
    A P-channel device (Type = -1) uses the same equations with all voltages and
    currents sign-reversed, with Vth the (positive) magnitude of its threshold.

    Two constant gate capacitances are added, as in a real transistor:

        Cgs * d(Vgs)/dt   between gate and source
        Cgd * d(Vgd)/dt   between gate and drain

    They matter: the gate draws no DC current, so without them the gate of a
    transistor driven only by other transistors has no capacitance of its own.

    Attributes:
        Vgs, Vds, Vgd (signal): Input voltages gate-source, drain-source, gate-drain.
        Id (signal): Output current from drain to source.
        Igs, Igd (signal): Gate capacitor currents (gate-source, gate-drain).
        Kp (param): Transconductance parameter in A/V^2 (default: 100 uA/V^2).
        W, L (param): Channel width and length in metres (default: 10 um / 1 um).
        Vth (param): Threshold voltage magnitude (default: 1 V).
        Lambda (param): Channel-length modulation in 1/V (default: 0.02).
        Type (param): Polarity, 1 for N-channel (default) or -1 for P-channel.
        Cgs, Cgd (param): Gate capacitances (default: 20 fF each).

    Methods:
        analog(): Defines the drain current and the gate capacitor currents.

Used in the examples
--------------------

* :doc:`Ring oscillator (3 CMOS inverters with RC delay) </examples/ring_oscillator>`

