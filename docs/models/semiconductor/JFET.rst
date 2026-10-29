JFET
====

.. code-block:: python

    from pyams.models import JFET

    X1 = JFET("d", "g", "s")
    X1.setParams("Beta=0.0005 Vto=-2")

Terminals
---------

``JFET(d, g, s)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Beta``
     - 0.0005
     - A/V²
     - Transconductance parameter
   * - ``Vto``
     - -2
     - V
     - Pinch-off (threshold) voltage
   * - ``Lambda``
     - 0.01
     - 1/V
     - Channel-length modulation
   * - ``Is``
     - 1e-14
     - A
     - Gate junction saturation current
   * - ``N``
     - 1
     - –
     - Gate junction ideality factor
   * - ``Vt``
     - 0.025
     - V
     - Thermal voltage
   * - ``Type``
     - 1
     - –
     - Polarity: 1 = N-channel, -1 = P-channel
   * - ``Cgs``
     - 2e-12
     - F
     - Gate-source capacitance
   * - ``Cgd``
     - 1e-12
     - F
     - Gate-drain capacitance

Description
-----------

The documentation of the class (``help(JFET)``)::

    This class implements a junction field-effect transistor (JFET).

    Terminals are given in the order (d, g, s): drain, gate, source.

    For an N-channel device (Type = 1), with vgs = V(g,s), vds = V(d,s) and
    vov = vgs - Vto (Vto is negative: the pinch-off voltage):

        vov <= 0               pinched off     Id = 0
        0 < vds < vov          triode          Id = Beta vds (2 vov - vds) (1 + Lambda vds)
        vds >= vov > 0         saturation      Id = Beta vov^2 (1 + Lambda vds)

    so the drain current at vgs = 0 in saturation is  Idss = Beta Vto^2.  If
    vds < 0 the drain and source change roles (the device is symmetric).
    A P-channel device (Type = -1) uses the same equations with all voltages and
    currents sign-reversed, with Vto still given as in the N-channel case (-2 V): the sign reversal of
    the voltages takes care of the polarity.

    The gate is a pair of p-n junctions (gate-source and gate-drain).  They are
    reverse biased in normal use and then draw almost nothing, but they conduct
    when the gate is driven positive (N-channel) by more than about 0.6 V:

        Igs = Is (exp(vgs / (N Vt)) - 1)         Igd = Is (exp(vgd / (N Vt)) - 1)

    Two constant junction capacitances Cgs and Cgd are added in parallel.

    Attributes:
        Vgs, Vds, Vgd (signal): Input voltages gate-source, drain-source, gate-drain.
        Id (signal): Output channel current from drain to source.
        Igs, Igd (signal): Output gate currents (junction + capacitor), gate to source / drain.
        Beta (param): Transconductance parameter in A/V^2 (default: 0.5 mA/V^2).
        Vto (param): Pinch-off voltage (default: -2 V for N-channel).
        Lambda (param): Channel-length modulation in 1/V (default: 0.01).
        Is (param): Gate junction saturation current (default: 1e-14 A).
        N (param): Gate junction ideality factor (default: 1).
        Vt (param): Thermal voltage (default: 0.025 V).
        Type (param): Polarity, 1 for N-channel (default) or -1 for P-channel.
        Cgs, Cgd (param): Gate capacitances (default: 2 pF and 1 pF).

    Methods:
        analog(): Defines the channel current, the gate junctions and capacitors.

Used in the examples
--------------------

* :doc:`JFET output characteristics (Id versus Vds for several Vgs) </examples/jfet_curves>`
* :doc:`JFET common-source amplifier (self bias) </examples/jfet_amplifier>`

