Trapezoid Current
=================

.. code-block:: python

    from pyams.models import TrapezoidCurrent

    I1 = TrapezoidCurrent("p", "n")
    I1.setParams("I0=0 I1=1e-3 Tw=0.05 T=0.1")

Terminals
---------

``TrapezoidCurrent(p, n)``

A positive current flows through the source from ``p`` to ``n``.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``I0``
     - 0
     - A
     - Initial current
   * - ``I1``
     - 1e-3
     - A
     - Peak current
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
   * - ``Ioff``
     - 0
     - A
     - Offset current

Symbol
------

.. figure:: /_static/images/symbols/TrapezoidCurrent_symbol.svg
   :alt: Trapezoid current source symbol
   :align: center
   :width: 160px

   Trapezoid current source symbol as displayed in the PyAMS application.

Description
-----------

This class models a trapezoidal waveform current source (the current counterpart of ``TrapezoidVoltage``).

The waveform has an initial delay ``Td``, a rising edge ``Tr``, a constant peak
``Tw``, a falling edge ``Tf``, and repeats with the period ``T``. A positive current flows through the source from node ``p`` to node ``n``.

With the cycle time :math:`c = (t - T_d) \bmod T`, the current is:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Interval
     - Current
   * - Before the delay (:math:`t \le T_d`)
     - :math:`I = I_0 + I_{off}`
   * - Rising edge (:math:`0 \le c \le T_r`)
     - :math:`I = I_0 + (I_1 - I_0) \, c / T_r + I_{off}`
   * - High state (:math:`T_r \le c \le T_r + T_w`)
     - :math:`I = I_1 + I_{off}`
   * - Falling edge (:math:`T_r + T_w \le c \le T_r + T_w + T_f`)
     - :math:`I` falls linearly from :math:`I_1 + I_{off}` to :math:`I_0 + I_{off}`
   * - Low state (afterwards)
     - :math:`I = I_0 + I_{off}`

Use non-zero ``Tr`` and ``Tf`` to get edges with a finite slope.

**Attributes**

* ``I`` (signal): Output current through the source, from p to n.
* ``I0`` (param): Initial (low) current in Amperes (A), default is 0 A.
* ``I1`` (param): Peak (high) current in Amperes (A), default is 1 mA.
* ``Td`` (param): Initial delay time in seconds, default is 0.
* ``Tr`` (param): Rise time in seconds, default is 0.
* ``Tw`` (param): Pulse-width (high duration) in seconds, default is 0.05 s.
* ``Tf`` (param): Fall time in seconds, default is 0.
* ``T`` (param): Total period of the waveform in seconds, default is 0.1 s.
* ``Ioff`` (param): Offset current in Amperes (A), default is 0.

**Methods**

* ``analog()``: Defines the trapezoidal waveform equation.

Source Code
-----------

.. code-block:: python

    from pyams.lib import model, signal, param, time
    from pyams.lib import current


    class TrapezoidCurrent(model):

        def __init__(self, p, n):
            self.I = signal('out', current, p, n)
            self.I0 = param(0.0, 'A', 'Initial current')
            self.I1 = param(1e-3, 'A', 'Peak current')
            self.Td = param(0, 'Sec', 'Initial delay time')
            self.Tr = param(0, 'Sec', 'Rise time')
            self.Tw = param(0.05, 'Sec', 'Pulse-width')
            self.Tf = param(0, 'Sec', 'Fall time')
            self.T = param(0.1, 'Sec', 'Total period of the waveform')
            self.Ioff = param(0.0, 'A', 'Offset current')

        def analog(self):
            t = time
            if t <= self.Td:
                self.I += self.I0 + self.Ioff
                return
            c = (t - self.Td) % self.T          # time within the current cycle
            if c < self.Tr:                     # rising edge
                self.I += self.I0 + (self.I1 - self.I0) * c / self.Tr + self.Ioff
            elif c <= self.Tr + self.Tw:        # high state
                self.I += self.I1 + self.Ioff
            elif c < self.Tr + self.Tw + self.Tf:   # falling edge
                self.I += self.I1 + (self.I0 - self.I1) \
                    * (c - self.Tr - self.Tw) / self.Tf + self.Ioff
            else:                               # low state
                self.I += self.I0 + self.Ioff
