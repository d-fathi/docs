Exp Voltage
===========

.. code-block:: python

    from pyams.models import ExpVoltage

    V1 = ExpVoltage("p", "n")
    V1.setParams("V1=0 V2=5 TD1=1e-3 TAU1=1e-3 TD2=5e-3 TAU2=1e-3")

Terminals
---------

``ExpVoltage(p, n)``

``p`` is the positive terminal: V(p) - V(n) = V.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``V1``
     - 0
     - V
     - Initial value
   * - ``V2``
     - 5
     - V
     - Pulsed value
   * - ``TD1``
     - 1e-3
     - s
     - Rise delay time
   * - ``TAU1``
     - 1e-3
     - s
     - Rise time constant
   * - ``TD2``
     - 5e-3
     - s
     - Fall delay time
   * - ``TAU2``
     - 1e-3
     - s
     - Fall time constant

Symbol
------

.. figure:: /_static/images/symbols/ExpVoltage_symbol.svg
   :alt: Exp voltage source symbol
   :align: center
   :width: 160px

   Exp voltage source symbol as displayed in the PyAMS application.

Description
-----------

This class implements an exponential voltage source (SPICE ``EXP``).

The voltage rises from ``V1`` towards ``V2`` after the delay ``TD1`` (time constant
``TAU1``), then falls back towards ``V1`` after the delay ``TD2`` (time constant ``TAU2``).

.. math::

   V(t) =
   \begin{cases}
   V_1 & t < T_{D1} \\
   V_1 + (V_2 - V_1) \left(1 - e^{-(t - T_{D1})/\tau_1}\right) & T_{D1} \le t < T_{D2} \\
   V_1 + (V_2 - V_1) \left(1 - e^{-(t - T_{D1})/\tau_1}\right) + (V_1 - V_2) \left(1 - e^{-(t - T_{D2})/\tau_2}\right) & t \ge T_{D2}
   \end{cases}

The DC (operating point) value is ``V1``.

**Attributes**

* ``V`` (signal): Output voltage between nodes (p, n).
* ``V1`` (param): Initial value in Volts (V), default is 0.
* ``V2`` (param): Pulsed value in Volts (V), default is 5 V.
* ``TD1`` (param): Rise delay time in seconds, default is 1 ms.
* ``TAU1`` (param): Rise time constant in seconds, default is 1 ms.
* ``TD2`` (param): Fall delay time in seconds, default is 5 ms.
* ``TAU2`` (param): Fall time constant in seconds, default is 1 ms.

**Methods**

* ``analog()``: Evaluates the exponential waveform at the current simulation time and adds it to ``V``.

Source Code
-----------

.. code-block:: python

    from math import exp
    from pyams.lib import signal, param, model, time
    from pyams.lib import voltage


    def exp_wave(t, v1, v2, td1, tau1, td2, tau2):
        if t < td1:
            return v1
        y = v1 + (v2 - v1) * (1.0 - exp(-(t - td1) / tau1))
        if t >= td2:
            y += (v1 - v2) * (1.0 - exp(-(t - td2) / tau2))
        return y


    class ExpVoltage(model):

        def __init__(self, p, n):
            self.V = signal('out', voltage, p, n)
            self.V1 = param(0.0, 'V', 'Initial value')
            self.V2 = param(5.0, 'V', 'Pulsed value')
            self.TD1 = param(1e-3, 's', 'Rise delay time')
            self.TAU1 = param(1e-3, 's', 'Rise time constant')
            self.TD2 = param(5e-3, 's', 'Fall delay time')
            self.TAU2 = param(1e-3, 's', 'Fall time constant')

        def analog(self):
            self.V += exp_wave(float(time), float(self.V1), float(self.V2), float(self.TD1),
                               float(self.TAU1), float(self.TD2), float(self.TAU2))
