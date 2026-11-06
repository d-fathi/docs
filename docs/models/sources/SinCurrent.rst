Sin Current
===========

.. code-block:: python

    from pyams.models import SinCurrent

    I1 = SinCurrent("p", "n")
    I1.setParams("Ia=1e-3 Fr=100")

Terminals
---------

``SinCurrent(p, n)``

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
   * - ``Fr``
     - 100
     - Hz
     - Frequency of sine wave
   * - ``Ia``
     - 1e-3
     - A
     - Amplitude of sine wave
   * - ``Ph``
     - 0
     - °
     - Phase of sine wave
   * - ``Ioff``
     - 0
     - A
     - Current offset

Symbol
------

.. figure:: /_static/images/symbols/SinCurrent_symbol.svg
   :alt: Sine wave current source symbol
   :align: center
   :width: 160px

   Sine wave current source symbol as displayed in the PyAMS application.

Description
-----------

This class models a sinusoidal current source.

The current waveform follows the equation:

.. math::

   I(t) = I_a \sin(2 \pi \, F_r \, t + \varphi) + I_{off}

where the phase ``Ph`` is given in degrees.

**Attributes**

* ``I`` (signal): Output current through the source, from p to n.
* ``Fr`` (param): Frequency of the sine wave in Hertz (Hz), default is 100 Hz.
* ``Ia`` (param): Amplitude of the sine wave in Amperes (A), default is 1 mA.
* ``Ph`` (param): Phase shift in degrees (°), default is 0.
* ``Ioff`` (param): Current offset in Amperes (A), default is 0.

**Methods**

* ``analog()``: Implements the sinusoidal current equation.

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model, time
    from pyams.lib import current
    from math import sin, pi


    class SinCurrent(model):

        def __init__(self, p, n):
            self.I = signal('out', current, p, n)
            self.Fr = param(100.0, 'Hz', 'Frequency of sine wave')
            self.Ia = param(1e-3, 'A', 'Amplitude of sine wave')
            self.Ph = param(0.0, '°', 'Phase of sine wave')
            self.Ioff = param(0.0, 'A', 'Current offset')

        def analog(self):
            self.I += self.Ia * sin(2 * pi * self.Fr * time + (self.Ph * pi / 180.0)) + self.Ioff
