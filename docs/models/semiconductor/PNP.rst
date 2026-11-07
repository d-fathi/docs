PNP
===

.. code-block:: python

    from pyams.models import BJT

    Q1 = BJT("c", "b", "e")
    Q1.setParams("Type=-1")

Terminals
---------

``BJT(c, b, e)``

Collector, base and emitter.

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
     - -
     - Forward current gain
   * - ``Br``
     - 1
     - -
     - Reverse current gain
   * - ``Type``
     - 1 / -1
     - -
     - Polarity: 1 = NPN, -1 = PNP
   * - ``Cje``
     - 4.5e-12
     - F
     - Base-emitter junction capacitance
   * - ``Cjc``
     - 3.6e-12
     - F
     - Base-collector junction capacitance

Symbol
------

.. figure:: /_static/images/symbols/PNP_symbol.svg
   :alt: PNP symbol
   :align: center
   :width: 220px

   PNP symbol as displayed in the PyAMS application.

Description
-----------

This class implements a bipolar junction transistor (Ebers-Moll model). This page describes the PNP device, obtained with ``Type = -1``.

Terminals are given in the order ``(c, b, e)``: collector, base, emitter.

With the junction voltages of an NPN transistor, :math:`V_{be} = V(b,e)` and
:math:`V_{bc} = V(b,c)`:

.. math::

   I_f = I_s \left( e^{V_{be}/V_t} - 1 \right) \qquad
   I_r = I_s \left( e^{V_{bc}/V_t} - 1 \right)

.. math::

   I_c = I_f - I_r \left( 1 + \frac{1}{B_r} \right) \qquad
   I_b = \frac{I_f}{B_f} + \frac{I_r}{B_r}

where :math:`I_c` is the current into the collector and :math:`I_b` the current
into the base; the emitter carries :math:`-(I_c + I_b)`. A PNP transistor
(``Type = -1``) uses the same equations with all voltages and currents
sign-reversed.

Two constant junction capacitances are added in parallel with the diodes, as in
a real transistor: ``Cje * d(Vbe)/dt`` between base and emitter and
``Cjc * d(Vbc)/dt`` between base and collector. They are not a detail: with
``Cje = Cjc = 0`` every node coupled through a capacitor has no capacitance of
its own, and a regenerative circuit (an astable multivibrator, a latch) makes
the circuit equations jump discontinuously when a transistor switches, so no
time step can follow it and the solver fails. The defaults are those of a
2N3904 (small-signal NPN).

**Attributes**

* ``Vbe`` (signal): Input voltage between base and emitter.
* ``Vbc`` (signal): Input voltage between base and collector.
* ``Ic`` (signal): Output current from collector to emitter.
* ``Ib`` (signal): Output current from base to emitter.
* ``Is`` (param): Saturation current, default is 1.0e-14 A.
* ``Vt`` (param): Thermal voltage, default is 0.025 V.
* ``Bf`` (param): Forward current gain, default is 100.
* ``Br`` (param): Reverse current gain, default is 1.
* ``Type`` (param): Polarity, 1 for NPN (default) or -1 for PNP.
* ``Cje`` (param): Base-emitter junction capacitance, default is 4.5 pF.
* ``Cjc`` (param): Base-collector junction capacitance, default is 3.6 pF.

**Methods**

* ``analog()``: Defines the collector and base currents (Ebers-Moll equations) and the junction capacitances.

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

    # BJT Model (Ebers-Moll, transport form) ----------------------------------------
    class BJT(model):
        def __init__(self, c, b, e):
            # Signals declarations------------------------------------------------
            self.Vbe = signal('in', voltage, b, e)
            self.Vbc = signal('in', voltage, b, c)
            self.Ic = signal('out', current, c, e)
            self.Ib = signal('out', current, b, e)

            # Parameters declarations----------------------------------------------
            self.Is = param(1.0e-14, 'A', 'Saturation current')
            self.Vt = param(0.025, 'V', 'Thermal voltage')
            self.Bf = param(100.0, ' ', 'Forward current gain')
            self.Br = param(1.0, ' ', 'Reverse current gain')
            self.Type = param(1, ' ', 'Polarity: 1 = NPN, -1 = PNP')
            self.Cje = param(4.5e-12, 'F', 'Base-emitter junction capacitance')
            self.Cjc = param(3.6e-12, 'F', 'Base-collector junction capacitance')

        def analog(self):
            k = float(self.Type)
            If = self.Is * (_limexp(k * self.Vbe / self.Vt) - 1.0)
            Ir = self.Is * (_limexp(k * self.Vbc / self.Vt) - 1.0)
            self.Ic += k * (If - Ir * (1.0 + 1.0 / self.Br))
            self.Ib += k * (If / self.Bf + Ir / self.Br)

            # Junction capacitances (same sign convention for NPN and PNP) --------
            self.Ib += self.Cje * ddt(self.Vbe)      # base -> emitter
            Icap = self.Cjc * ddt(self.Vbc)          # base -> collector
            self.Ib += Icap                          # leaves the base ...
            self.Ic -= Icap                          # ... and enters the collector
