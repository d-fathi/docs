NMOS
====

.. code-block:: python

    from pyams.models import MOSFET

    M1 = MOSFET("d", "g", "s")
    M1.setParams("Kp=100e-6 W=10e-6 L=1e-6")

Terminals
---------

``MOSFET(d, g, s)``

Drain, gate and source. The bulk is connected to the source.

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
   * - ``Vth``
     - 1
     - V
     - Threshold voltage (magnitude)
   * - ``Lambda``
     - 0.02
     - 1/V
     - Channel-length modulation
   * - ``Type``
     - 1 / -1
     - -
     - Polarity: 1 = N-channel, -1 = P-channel
   * - ``Cgs``
     - 20e-15
     - F
     - Gate-source capacitance
   * - ``Cgd``
     - 20e-15
     - F
     - Gate-drain capacitance

Symbol
------

.. figure:: /_static/images/symbols/NMOS_symbol.svg
   :alt: NMOS symbol
   :align: center
   :width: 220px

   NMOS symbol as displayed in the PyAMS application.

Description
-----------

This class implements a MOSFET (square-law, level 1 model) with the bulk
connected to the source. This page describes the N-channel device (the default, ``Type = 1``).

Terminals are given in the order ``(d, g, s)``: drain, gate, source.

For an N-channel device (``Type = 1``), with :math:`v_{gs} = V(g,s)`,
:math:`v_{ds} = V(d,s)`, :math:`\beta = K_p W / L` and
:math:`v_{ov} = v_{gs} - V_{th}`:

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

If :math:`v_{ds} < 0` the drain and source change roles (the device is
symmetric). A P-channel device (``Type = -1``) uses the same equations with all
voltages and currents sign-reversed, with ``Vth`` the (positive) magnitude of
its threshold.

Two constant gate capacitances are added, as in a real transistor:
``Cgs * d(Vgs)/dt`` between gate and source and ``Cgd * d(Vgd)/dt`` between gate
and drain. They matter: the gate draws no DC current, so without them the gate
of a transistor driven only by other transistors has no capacitance of its own.

**Attributes**

* ``Vgs``, ``Vds``, ``Vgd`` (signal): Input voltages gate-source, drain-source, gate-drain.
* ``Id`` (signal): Output current from drain to source.
* ``Igs``, ``Igd`` (signal): Gate capacitor currents (gate-source, gate-drain).
* ``Kp`` (param): Transconductance parameter in A/V², default is 100 µA/V².
* ``W``, ``L`` (param): Channel width and length in metres, default are 10 µm and 1 µm.
* ``Vth`` (param): Threshold voltage magnitude, default is 1 V.
* ``Lambda`` (param): Channel-length modulation in 1/V, default is 0.02.
* ``Type`` (param): Polarity, 1 for N-channel (default) or -1 for P-channel.
* ``Cgs``, ``Cgd`` (param): Gate capacitances, default is 20 fF each.

**Methods**

* ``analog()``: Defines the drain current (square law) and the gate capacitor currents.

Source Code
-----------

.. code-block:: python

    from pyams.lib import model, signal, param
    from pyams.lib import voltage, current
    from pyams.lib import ddt

    def _ids(vgs, vds, beta, vth, lam):
        vov = vgs - vth
        if vov <= 0.0:                                   # cut-off
            return 0.0
        if vds < vov:                                    # triode (linear) region
            return beta * (vov * vds - 0.5 * vds * vds) * (1.0 + lam * vds)
        return 0.5 * beta * vov * vov * (1.0 + lam * vds)    # saturation

    # MOSFET Model (Shichman-Hodges, level 1) ---------------------------------------
    class MOSFET(model):
        def __init__(self, d, g, s):
            # Signals declarations---------------------------------------------------
            self.Vgs = signal('in', voltage, g, s)
            self.Vds = signal('in', voltage, d, s)
            self.Vgd = signal('in', voltage, g, d)
            self.Id = signal('out', current, d, s)
            self.Igs = signal('out', current, g, s)
            self.Igd = signal('out', current, g, d)

            # Parameters declarations----------------------------------------------
            self.Kp = param(100.0e-6, 'A/V²', 'Transconductance parameter')
            self.W = param(10.0e-6, 'm', 'Channel width')
            self.L = param(1.0e-6, 'm', 'Channel length')
            self.Vth = param(1.0, 'V', 'Threshold voltage (magnitude)')
            self.Lambda = param(0.02, '1/V', 'Channel-length modulation')
            self.Type = param(1, ' ', 'Polarity: 1 = N-channel, -1 = P-channel')
            self.Cgs = param(20.0e-15, 'F', 'Gate-source capacitance')
            self.Cgd = param(20.0e-15, 'F', 'Gate-drain capacitance')

        def analog(self):
            k = float(self.Type)
            beta = self.Kp * self.W / self.L
            vgs = k * self.Vgs
            vds = k * self.Vds
            if vds >= 0.0:
                i = _ids(vgs, vds, beta, self.Vth, self.Lambda)
            else:                                  # source and drain swap roles
                i = -_ids(vgs - vds, -vds, beta, self.Vth, self.Lambda)
            self.Id += k * i

            # Gate capacitances -----------------------------------------------------
            self.Igs += self.Cgs * ddt(self.Vgs)
            self.Igd += self.Cgd * ddt(self.Vgd)
