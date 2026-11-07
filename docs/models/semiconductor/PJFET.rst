PJFET
=====

.. code-block:: python

    from pyams.models import JFET

    J1 = JFET("d", "g", "s")
    J1.setParams("Type=-1")

Terminals
---------

``JFET(d, g, s)``

Drain, gate and source.

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
     - 0.5e-3
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
     - -
     - Gate junction ideality factor
   * - ``Vt``
     - 0.025
     - V
     - Thermal voltage
   * - ``Type``
     - 1 / -1
     - -
     - Polarity: 1 = N-channel, -1 = P-channel
   * - ``Cgs``
     - 2e-12
     - F
     - Gate-source capacitance
   * - ``Cgd``
     - 1e-12
     - F
     - Gate-drain capacitance

Symbol
------

.. figure:: /_static/images/symbols/PJFET_symbol.svg
   :alt: PJFET symbol
   :align: center
   :width: 220px

   PJFET symbol as displayed in the PyAMS application.

Description
-----------

This class implements a junction field-effect transistor (JFET), SPICE level 1
(Shichman-Hodges). This page describes the P-channel device, obtained with ``Type = -1``.

Terminals are given in the order ``(d, g, s)``: drain, gate, source.

For an N-channel device (``Type = 1``), with :math:`v_{gs} = V(g,s)`,
:math:`v_{ds} = V(d,s)` and :math:`v_{ov} = v_{gs} - V_{to}` (:math:`V_{to}` is
negative: the pinch-off voltage):

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Region
     - Drain current
   * - :math:`v_{ov} \le 0` (pinched off)
     - :math:`I_d = 0`
   * - :math:`0 < v_{ds} < v_{ov}` (triode)
     - :math:`I_d = \beta \, v_{ds} (2 v_{ov} - v_{ds}) (1 + \lambda v_{ds})`
   * - :math:`v_{ds} \ge v_{ov} > 0` (saturation)
     - :math:`I_d = \beta \, v_{ov}^2 (1 + \lambda v_{ds})`

so the drain current at :math:`v_{gs} = 0` in saturation is
:math:`I_{dss} = \beta V_{to}^2`. If :math:`v_{ds} < 0` the drain and source
change roles (the device is symmetric).

A P-channel device (``Type = -1``) uses the same equations with all voltages and
currents sign-reversed, with ``Vto`` still given as in the N-channel case
(-2 V): the sign reversal of the voltages takes care of the polarity.

The gate is a pair of p-n junctions (gate-source and gate-drain). They are
reverse biased in normal use and then draw almost nothing, but they conduct
when the gate is driven positive (N-channel) by more than about 0.6 V:

.. math::

   I_{gs} = I_s \left( e^{v_{gs} / (N V_t)} - 1 \right) \qquad
   I_{gd} = I_s \left( e^{v_{gd} / (N V_t)} - 1 \right)

Two constant junction capacitances ``Cgs`` and ``Cgd`` are added in parallel.

**Attributes**

* ``Vgs``, ``Vds``, ``Vgd`` (signal): Input voltages gate-source, drain-source, gate-drain.
* ``Id`` (signal): Output channel current from drain to source.
* ``Igs``, ``Igd`` (signal): Output gate currents (junction + capacitor), gate to source / drain.
* ``Beta`` (param): Transconductance parameter in A/V², default is 0.5 mA/V².
* ``Vto`` (param): Pinch-off voltage, default is -2 V for N-channel.
* ``Lambda`` (param): Channel-length modulation in 1/V, default is 0.01.
* ``Is`` (param): Gate junction saturation current, default is 1e-14 A.
* ``N`` (param): Gate junction ideality factor, default is 1.
* ``Vt`` (param): Thermal voltage, default is 0.025 V.
* ``Type`` (param): Polarity, 1 for N-channel (default) or -1 for P-channel.
* ``Cgs``, ``Cgd`` (param): Gate capacitances, default are 2 pF and 1 pF.

**Methods**

* ``analog()``: Defines the channel current, the gate junctions and the gate capacitors.

Source Code
-----------

.. code-block:: python

    from math import exp
    from pyams.lib import model, signal, param
    from pyams.lib import voltage, current
    from pyams.lib import ddt

    def _limexp(x, xmax=40.0):
        if x <= xmax:
            return exp(x)
        return exp(xmax) * (1.0 + x - xmax)

    def _ids(vgs, vds, beta, vto, lam):
        vov = vgs - vto
        if vov <= 0.0:                                   # pinched off
            return 0.0
        if vds < vov:                                    # triode (ohmic) region
            return beta * vds * (2.0 * vov - vds) * (1.0 + lam * vds)
        return beta * vov * vov * (1.0 + lam * vds)      # saturation

    # JFET Model (Shichman-Hodges, SPICE level 1) -------------------------------------
    class JFET(model):
        def __init__(self, d, g, s):
            # Signals declarations---------------------------------------------------
            self.Vgs = signal('in', voltage, g, s)
            self.Vds = signal('in', voltage, d, s)
            self.Vgd = signal('in', voltage, g, d)
            self.Id = signal('out', current, d, s)
            self.Igs = signal('out', current, g, s)
            self.Igd = signal('out', current, g, d)

            # Parameters declarations----------------------------------------------
            self.Beta = param(0.5e-3, 'A/V²', 'Transconductance parameter')
            self.Vto = param(-2.0, 'V', 'Pinch-off (threshold) voltage')
            self.Lambda = param(0.01, '1/V', 'Channel-length modulation')
            self.Is = param(1.0e-14, 'A', 'Gate junction saturation current')
            self.N = param(1.0, ' ', 'Gate junction ideality factor')
            self.Vt = param(0.025, 'V', 'Thermal voltage')
            self.Type = param(1, ' ', 'Polarity: 1 = N-channel, -1 = P-channel')
            self.Cgs = param(2.0e-12, 'F', 'Gate-source capacitance')
            self.Cgd = param(1.0e-12, 'F', 'Gate-drain capacitance')

        def analog(self):
            k = float(self.Type)
            vgs = k * self.Vgs
            vds = k * self.Vds
            if vds >= 0.0:
                i = _ids(vgs, vds, self.Beta, self.Vto, self.Lambda)
            else:                                  # source and drain swap roles
                i = -_ids(vgs - vds, -vds, self.Beta, self.Vto, self.Lambda)
            self.Id += k * i

            # Gate junctions (forward conduction when the gate is driven the wrong way)
            nvt = self.N * self.Vt
            self.Igs += k * self.Is * (_limexp(vgs / nvt) - 1.0)
            self.Igd += k * self.Is * (_limexp((vgs - vds) / nvt) - 1.0)

            # Gate capacitances -----------------------------------------------------
            self.Igs += self.Cgs * ddt(self.Vgs)
            self.Igd += self.Cgd * ddt(self.Vgd)
