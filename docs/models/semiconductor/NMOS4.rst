NMOS 4 terminal
===============

.. code-block:: python

    from pyams.models import MOSFET4

    M1 = MOSFET4("d", "g", "s", "b")
    M1.setParams("Vth0=1 Gamma=0.5")

Terminals
---------

``MOSFET4(d, g, s, b)``

Drain, gate, source and bulk.

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
     - 100e-6
     - A/V²
     - Transconductance parameter
   * - ``W``
     - 10e-6
     - m
     - Channel width
   * - ``L``
     - 1e-6
     - m
     - Channel length
   * - ``Vth0``
     - 1
     - V
     - Zero-bias threshold voltage (magnitude)
   * - ``Lambda``
     - 0.02
     - 1/V
     - Channel-length modulation
   * - ``Gamma``
     - 0.5
     - √V
     - Body-effect coefficient
   * - ``Phi``
     - 0.7
     - V
     - Surface potential
   * - ``Type``
     - 1 / -1
     - -
     - Polarity: 1 = N-channel, -1 = P-channel
   * - ``Is``
     - 1e-14
     - A
     - Bulk junction saturation current
   * - ``N``
     - 1
     - -
     - Bulk junction emission coefficient
   * - ``Vt``
     - 0.025
     - V
     - Thermal voltage
   * - ``Cgs``
     - 20e-15
     - F
     - Gate-source capacitance
   * - ``Cgd``
     - 20e-15
     - F
     - Gate-drain capacitance
   * - ``Cgb``
     - 10e-15
     - F
     - Gate-bulk capacitance
   * - ``Cbs``
     - 10e-15
     - F
     - Bulk-source junction capacitance
   * - ``Cbd``
     - 10e-15
     - F
     - Bulk-drain junction capacitance

Symbol
------

.. figure:: /_static/images/symbols/NMOS4_symbol.svg
   :alt: NMOS 4 terminal symbol
   :align: center
   :width: 240px

   NMOS 4 terminal symbol as displayed in the PyAMS application.

Description
-----------

This class implements a four-terminal MOSFET (drain, gate, source, bulk): the
level-1 square-law model of ``MOSFET`` with the **body effect** and the bulk
junctions. This page describes the N-channel device (the default, ``Type = 1``).

Terminals are given in the order ``(d, g, s, b)``.

For an N-channel device (``Type = 1``), with :math:`v_{gs} = V(g,s)`,
:math:`v_{ds} = V(d,s)`, :math:`v_{bs} = V(b,s)` and :math:`\beta = K_p W / L`:

.. math::

   V_{th} = V_{th0} + \gamma \left( \sqrt{\phi - v_{bs}} - \sqrt{\phi} \right)
   \qquad v_{ov} = v_{gs} - V_{th}

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Region
     - Drain current
   * - :math:`v_{ov} \le 0` (cut-off)
     - :math:`I_d = 0`
   * - :math:`0 < v_{ds} < v_{ov}` (triode)
     - :math:`I_d = \beta \left( v_{ov} v_{ds} - v_{ds}^2 / 2 \right) (1 + \lambda v_{ds})`
   * - :math:`v_{ds} \ge v_{ov} > 0` (saturation)
     - :math:`I_d = \frac{\beta}{2} v_{ov}^2 (1 + \lambda v_{ds})`

A source that is more positive than the bulk (:math:`v_{bs} < 0`, "reverse body
bias") raises the threshold: this is why an N-channel pass transistor cannot
pass a full high level, and why stacked transistors (NAND, source followers) are
slower than the 3-terminal model predicts.

The device is symmetric: if :math:`v_{ds} < 0` the drain and source change roles
and the body effect is taken against the new source (:math:`v_{bd}`). A P-channel
device (``Type = -1``) uses the same equations with all voltages and currents
sign-reversed, ``Vth0`` being the (positive) magnitude of its threshold.

The bulk junctions (diodes bulk-source and bulk-drain, forward when the bulk is
more positive than the channel end for an N device) are:

.. math::

   I_{bs} = I_s \left( e^{v_{bs} / (N V_t)} - 1 \right) \qquad
   I_{bd} = I_s \left( e^{v_{bd} / (N V_t)} - 1 \right)

and constant capacitances ``Cgs``, ``Cgd``, ``Cgb`` (gate) and ``Cbs``, ``Cbd``
(junctions) are added. With ``Gamma = 0`` and the bulk tied to the source the
model reduces to ``MOSFET`` (apart from the junction diodes and the extra
capacitances).

**Attributes**

* ``Vgs``, ``Vds``, ``Vgd``, ``Vbs``, ``Vbd``, ``Vgb`` (signal): Input voltages.
* ``Id`` (signal): Output drain-source channel current.
* ``Ibs``, ``Ibd``, ``Igs``, ``Igd``, ``Igb`` (signal): Junction and capacitor currents.
* ``Kp`` (param): Transconductance parameter, default is 100 µA/V².
* ``W``, ``L`` (param): Channel width and length, default are 10 µm and 1 µm.
* ``Vth0`` (param): Zero-bias threshold voltage magnitude, default is 1 V.
* ``Lambda`` (param): Channel-length modulation, default is 0.02 1/V.
* ``Gamma`` (param): Body-effect coefficient, default is 0.5 √V.
* ``Phi`` (param): Surface potential, default is 0.7 V.
* ``Type`` (param): 1 for N-channel (default), -1 for P-channel.
* ``Is`` (param): Bulk junction saturation current, default is 1e-14 A.
* ``N`` (param): Bulk junction emission coefficient, default is 1.
* ``Vt`` (param): Thermal voltage, default is 25 mV.
* ``Cgs``, ``Cgd`` (param): Gate capacitances, default is 20 fF each.
* ``Cgb`` (param): Gate-bulk capacitance, default is 10 fF.
* ``Cbs``, ``Cbd`` (param): Bulk junction capacitances, default is 10 fF each.

**Methods**

* ``analog()``: Defines the drain current with the body effect, the bulk junctions and the capacitor currents.

Source Code
-----------

.. code-block:: python

    from math import exp, sqrt
    from pyams.lib import model, signal, param
    from pyams.lib import voltage, current
    from pyams.lib import ddt

    def _limexp(x, xmax=40.0):
        if x <= xmax:
            return exp(x)
        return exp(xmax) * (1.0 + x - xmax)

    def _ids(vov, vds, beta, lam):
        if vov <= 0.0:                                   # cut-off
            return 0.0
        if vds < vov:                                    # triode (linear) region
            return beta * (vov * vds - 0.5 * vds * vds) * (1.0 + lam * vds)
        return 0.5 * beta * vov * vov * (1.0 + lam * vds)    # saturation

    # MOSFET Model (Shichman-Hodges, level 1, four terminals) -------------------------
    class MOSFET4(model):
        def __init__(self, d, g, s, b):
            # Signals declarations---------------------------------------------------
            self.Vgs = signal('in', voltage, g, s)
            self.Vds = signal('in', voltage, d, s)
            self.Vgd = signal('in', voltage, g, d)
            self.Vbs = signal('in', voltage, b, s)
            self.Vbd = signal('in', voltage, b, d)
            self.Id = signal('out', current, d, s)
            self.Ibs = signal('out', current, b, s)
            self.Ibd = signal('out', current, b, d)
            self.Igs = signal('out', current, g, s)
            self.Igd = signal('out', current, g, d)
            self.Igb = signal('out', current, g, b)
            self.Vgb = signal('in', voltage, g, b)

            # Parameters declarations----------------------------------------------
            self.Kp = param(100.0e-6, 'A/V²', 'Transconductance parameter')
            self.W = param(10.0e-6, 'm', 'Channel width')
            self.L = param(1.0e-6, 'm', 'Channel length')
            self.Vth0 = param(1.0, 'V', 'Zero-bias threshold voltage (magnitude)')
            self.Lambda = param(0.02, '1/V', 'Channel-length modulation')
            self.Gamma = param(0.5, '√V', 'Body-effect coefficient')
            self.Phi = param(0.7, 'V', 'Surface potential')
            self.Type = param(1, ' ', 'Polarity: 1 = N-channel, -1 = P-channel')
            self.Is = param(1.0e-14, 'A', 'Bulk junction saturation current')
            self.N = param(1.0, ' ', 'Bulk junction emission coefficient')
            self.Vt = param(0.025, 'V', 'Thermal voltage')
            self.Cgs = param(20.0e-15, 'F', 'Gate-source capacitance')
            self.Cgd = param(20.0e-15, 'F', 'Gate-drain capacitance')
            self.Cgb = param(10.0e-15, 'F', 'Gate-bulk capacitance')
            self.Cbs = param(10.0e-15, 'F', 'Bulk-source junction capacitance')
            self.Cbd = param(10.0e-15, 'F', 'Bulk-drain junction capacitance')

        def _vth(self, vbs):
            arg = self.Phi - vbs
            if arg < 1.0e-3:                     # forward-biased bulk: keep the root real
                arg = 1.0e-3
            return self.Vth0 + self.Gamma * (sqrt(arg) - sqrt(self.Phi))

        def analog(self):
            k = float(self.Type)
            beta = self.Kp * self.W / self.L
            vds = k * self.Vds
            if vds >= 0.0:                       # normal: the source terminal is the source
                vov = k * self.Vgs - self._vth(k * self.Vbs)
                i = _ids(vov, vds, beta, self.Lambda)
            else:                                # swapped: the drain terminal acts as source
                vov = k * self.Vgd - self._vth(k * self.Vbd)
                i = -_ids(vov, -vds, beta, self.Lambda)
            self.Id += k * i

            # bulk junctions: forward when k*vb* > 0
            nvt = self.N * self.Vt
            self.Ibs += k * self.Is * (_limexp(k * self.Vbs / nvt) - 1.0)
            self.Ibd += k * self.Is * (_limexp(k * self.Vbd / nvt) - 1.0)

            # capacitances ------------------------------------------------------------
            self.Igs += self.Cgs * ddt(self.Vgs)
            self.Igd += self.Cgd * ddt(self.Vgd)
            self.Igb += self.Cgb * ddt(self.Vgb)
            self.Ibs += self.Cbs * ddt(self.Vbs)
            self.Ibd += self.Cbd * ddt(self.Vbd)
