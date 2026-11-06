Exp Current
===========

.. code-block:: python

    from pyams.models import ExpCurrent

    I1 = ExpCurrent("p", "n")
    I1.setParams("I1=0 I2=1e-3 TD1=1e-3 TAU1=1e-3 TD2=5e-3 TAU2=1e-3")

Terminals
---------

``ExpCurrent(p, n)``

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
   * - ``I1``
     - 0
     - A
     - Initial value
   * - ``I2``
     - 1e-3
     - A
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

.. figure:: /_static/images/symbols/ExpCurrent_symbol.svg
   :alt: Exp current source symbol
   :align: center
   :width: 160px

   Exp current source symbol as displayed in the PyAMS application.

Description
-----------

This class implements an exponential current source (SPICE ``EXP``).

The current rises from ``I1`` towards ``I2`` after the delay ``TD1`` (time constant
``TAU1``), then falls back towards ``I1`` after the delay ``TD2`` (time constant ``TAU2``).
The current flows from ``p`` to ``n`` through the source.

.. math::

   I(t) =
   \begin{cases}
   I_1 & t < T_{D1} \\
   I_1 + (I_2 - I_1) \left(1 - e^{-(t - T_{D1})/\tau_1}\right) & T_{D1} \le t < T_{D2} \\
   I_1 + (I_2 - I_1) \left(1 - e^{-(t - T_{D1})/\tau_1}\right) + (I_1 - I_2) \left(1 - e^{-(t - T_{D2})/\tau_2}\right) & t \ge T_{D2}
   \end{cases}

The DC (operating point) value is ``I1``.

**Attributes**

* ``I`` (signal): Output current through the source, from p to n.
* ``I1`` (param): Initial value in Amperes (A), default is 0.
* ``I2`` (param): Pulsed value in Amperes (A), default is 1 mA.
* ``TD1`` (param): Rise delay time in seconds, default is 1 ms.
* ``TAU1`` (param): Rise time constant in seconds, default is 1 ms.
* ``TD2`` (param): Fall delay time in seconds, default is 5 ms.
* ``TAU2`` (param): Fall time constant in seconds, default is 1 ms.

**Methods**

* ``analog()``: Evaluates the exponential waveform at the current simulation time and adds it to ``I``.

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model, time
    from pyams.lib import current
    from .ExpVoltage import exp_wave


    class ExpCurrent(model):

        def __init__(self, p, n):
            self.I = signal('out', current, p, n)
            self.I1 = param(0.0, 'A', 'Initial value')
            self.I2 = param(1e-3, 'A', 'Pulsed value')
            self.TD1 = param(1e-3, 's', 'Rise delay time')
            self.TAU1 = param(1e-3, 's', 'Rise time constant')
            self.TD2 = param(5e-3, 's', 'Fall delay time')
            self.TAU2 = param(1e-3, 's', 'Fall time constant')

        def analog(self):
            self.I += exp_wave(float(time), float(self.I1), float(self.I2), float(self.TD1),
                               float(self.TAU1), float(self.TD2), float(self.TAU2))
