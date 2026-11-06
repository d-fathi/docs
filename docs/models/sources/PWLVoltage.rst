PWL Voltage
===========

.. code-block:: python

    from pyams.models import PWLVoltage

    V1 = PWLVoltage("p", "n")
    V1.setPoints("0 0, 1m 5, 2m 5, 3m 0")      # SI prefixes allowed
    V1.setParams("Rep=1")

Terminals
---------

``PWLVoltage(p, n)``

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
   * - ``Td``
     - 0
     - s
     - Delay
   * - ``Scale``
     - 1
     - -
     - Amplitude scale
   * - ``Voff``
     - 0
     - V
     - Offset
   * - ``Rep``
     - 0
     - -
     - Repeat (1) or single shot (0)

Symbol
------

.. figure:: /_static/images/symbols/PWLVoltage_symbol.svg
   :alt: PWL voltage source symbol
   :align: center
   :width: 160px

   PWL voltage source symbol as displayed in the PyAMS application.

Description
-----------

This class implements a piece-wise linear voltage source (SPICE ``PWL``): the voltage is
defined by a list of (time, value) points and linearly interpolated between them.

.. math::

   V(t) = \text{Scale} \cdot pwl(t - T_d) + V_{off}

Before the first point it holds the first value, after the last point it holds
the last value. Two points with the same time make a vertical step. With
``Rep = 1`` the waveform between the first and last points repeats. The DC
(operating point) value is the waveform value at ``t = 0``.

The points can be given in the constructor, as a list of ``(t, value)`` pairs or
as a string (SI prefixes allowed), or later with ``setPoints()``. The default
points are (0, 0), (1 ms, 5 V), (2 ms, 5 V), (3 ms, 0).

**Attributes**

* ``V`` (signal): Output voltage between nodes (p, n).
* ``Td`` (param): Delay in seconds, default is 0.
* ``Scale`` (param): Amplitude scale factor, default is 1.
* ``Voff`` (param): Offset in Volts (V), default is 0.
* ``Rep`` (param): 1 = repeat, 0 = single shot, default is 0.

**Methods**

* ``setPoints(points)``: Sets the waveform points (a list of pairs, a flat list or a string).
* ``analog()``: Interpolates the waveform at the current simulation time.

Source Code
-----------

.. code-block:: python

    from bisect import bisect_right
    from pyams.lib import signal, param, model, time
    from pyams.lib import voltage
    from pyams.lib import _parse_value


    # parse_points(), pwl_value() and pwl_eval() are helper functions of the same file


    class PWLVoltage(model):

        def __init__(self, p, n, points=None):
            self.V = signal('out', voltage, p, n)
            self.Td = param(0.0, 's', 'Delay')
            self.Scale = param(1.0, ' ', 'Amplitude scale')
            self.Voff = param(0.0, 'V', 'Offset')
            self.Rep = param(0.0, ' ', 'Repeat (1) or single shot (0)')
            self.setPoints(points if points is not None
                           else [(0.0, 0.0), (1e-3, 5.0), (2e-3, 5.0), (3e-3, 0.0)])

        def setPoints(self, points):
            self._ts, self._vs = parse_points(points, 'V')

        def analog(self):
            y = pwl_eval(float(time), self._ts, self._vs, float(self.Td), float(self.Rep) > 0.5)
            self.V += float(self.Scale) * y + float(self.Voff)
