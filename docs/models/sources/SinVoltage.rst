Sin Voltage
===========

.. code-block:: python

    from pyams.models import SinVoltage

    V1 = SinVoltage("p", "n")
    V1.setParams("Va=10 Fr=100")

Terminals
---------

``SinVoltage(p, n)``

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
   * - ``Fr``
     - 100
     - Hz
     - Frequency of sine wave
   * - ``Va``
     - 10
     - V
     - Amplitude of sine wave
   * - ``Ph``
     - 0
     - °
     - Phase of sine wave
   * - ``Voff``
     - 0
     - V
     - Voltage offset

Symbol
------

.. figure:: /_static/images/symbols/SinVoltage_symbol.svg
   :alt: Sine wave voltage source symbol
   :align: center
   :width: 160px

   Sine wave voltage source symbol as displayed in the PyAMS application.

Description
-----------

This class models a sinusoidal voltage source.

The voltage waveform follows the equation:

.. math::

   V(t) = V_a \sin(2 \pi \, F_r \, t + \varphi) + V_{off}

where the phase ``Ph`` is given in degrees.

**Attributes**

* ``V`` (signal): Output voltage between nodes (p, n).
* ``Fr`` (param): Frequency of the sine wave in Hertz (Hz), default is 100 Hz.
* ``Va`` (param): Amplitude of the sine wave in Volts (V), default is 10 V.
* ``Ph`` (param): Phase shift in degrees (°), default is 0.
* ``Voff`` (param): Voltage offset in Volts (V), default is 0.

**Methods**

* ``analog()``: Implements the sinusoidal voltage equation.

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model, time
    from pyams.lib import voltage
    from math import sin, pi


    class SinVoltage(model):

        def __init__(self, p, n):
            self.V = signal('out', voltage, p, n)
            self.Fr = param(100.0, 'Hz', 'Frequency of sine wave')
            self.Va = param(10.0, 'V', 'Amplitude of sine wave')
            self.Ph = param(0.0, '°', 'Phase of sine wave')
            self.Voff = param(0.0, 'V', 'Voltage offset')

        def analog(self):
            self.V += self.Va * sin(2 * pi * self.Fr * time + (self.Ph * pi / 180.0)) + self.Voff
