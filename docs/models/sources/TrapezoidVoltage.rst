Trapezoid Voltage
=================

.. code-block:: python

    from pyams.models import TrapezoidVoltage

    V1 = TrapezoidVoltage("p", "n")
    V1.setParams("V0=1 V1=1 Tw=0.05 T=0.1")

Terminals
---------

``TrapezoidVoltage(p, n)``

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
   * - ``V0``
     - 1
     - V
     - Initial voltage
   * - ``V1``
     - 1
     - V
     - Peak voltage
   * - ``Td``
     - 0
     - s
     - Initial delay time
   * - ``Tr``
     - 0
     - s
     - Rise time
   * - ``Tw``
     - 0.05
     - s
     - Pulse-width (high duration)
   * - ``Tf``
     - 0
     - s
     - Fall time
   * - ``T``
     - 0.1
     - s
     - Total period of the waveform
   * - ``Voff``
     - 0
     - V
     - Offset voltage

Symbol
------

.. figure:: /_static/images/symbols/TrapezoidVoltage_symbol.svg
   :alt: Trapezoid voltage source symbol
   :align: center
   :width: 160px

   Trapezoid voltage source symbol as displayed in the PyAMS application.

Description
-----------

This class models a trapezoidal waveform voltage source.

The waveform has an initial delay ``Td``, a rising edge ``Tr``, a constant peak
``Tw``, a falling edge ``Tf``, and repeats with the period ``T``.

With the cycle time :math:`c = (t - T_d) \bmod T`, the voltage is:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Interval
     - Voltage
   * - Before the delay (:math:`t \le T_d`)
     - :math:`V = V_0 + V_{off}`
   * - Rising edge (:math:`0 \le c \le T_r`)
     - :math:`V = V_0 + (V_1 - V_0) \, c / T_r + V_{off}`
   * - High state (:math:`T_r \le c \le T_r + T_w`)
     - :math:`V = V_1 + V_{off}`
   * - Falling edge (:math:`T_r + T_w \le c \le T_r + T_w + T_f`)
     - :math:`V` falls linearly from :math:`V_1 + V_{off}` to :math:`V_0 + V_{off}`
   * - Low state (afterwards)
     - :math:`V = V_0 + V_{off}`

Use non-zero ``Tr`` and ``Tf`` to get edges with a finite slope.

**Attributes**

* ``V`` (signal): Output voltage between nodes (p, n).
* ``V0`` (param): Initial (low) voltage in Volts (V), default is 1 V.
* ``V1`` (param): Peak (high) voltage in Volts (V), default is 1 V.
* ``Td`` (param): Initial delay time in seconds, default is 0.
* ``Tr`` (param): Rise time in seconds, default is 0.
* ``Tw`` (param): Pulse-width (high duration) in seconds, default is 0.05 s.
* ``Tf`` (param): Fall time in seconds, default is 0.
* ``T`` (param): Total period of the waveform in seconds, default is 0.1 s.
* ``Voff`` (param): Offset voltage in Volts (V), default is 0.

**Methods**

* ``analog()``: Defines the trapezoidal waveform equation.

Source Code
-----------

.. code-block:: python

    from pyams.lib import model, signal, param, time
    from pyams.lib import voltage


    class TrapezoidVoltage(model):

        def __init__(self, a, b):
            self.V = signal('out', voltage, a, b)
            self.V0 = param(1.0, 'V', 'Initial voltage')
            self.V1 = param(1.0, 'V', 'Peak voltage')
            self.Td = param(0, 'Sec', 'Initial delay time')
            self.Tr = param(0, 'Sec', 'Rise time')
            self.Tw = param(0.05, 'Sec', 'Pulse-width')
            self.Tf = param(0, 'Sec', 'Fall time')
            self.T = param(0.1, 'Sec', 'Total period of the waveform')
            self.Voff = param(0.0, 'V', 'Offset voltage')

        def analog(self):
            t = time
            if t <= self.Td:
                self.V += self.V0 + self.Voff
                return
            cycle_time = (t - self.Td) % self.T
            if cycle_time <= self.Tr:
                slope = (self.V1 - self.V0) / self.Tr
                self.V += slope * cycle_time + self.V0 + self.Voff
            elif cycle_time <= (self.Tr + self.Tw):
                self.V += self.V1 + self.Voff
            elif cycle_time <= (self.Tr + self.Tw + self.Tf):
                slope = (self.V0 - self.V1) / self.Tf
                self.V += slope * (cycle_time - self.Tr - self.Tw) + self.V1 + self.Voff
            else:
                self.V += self.V0 + self.Voff
