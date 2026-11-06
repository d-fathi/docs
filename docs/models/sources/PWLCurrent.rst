PWL Current
===========

.. code-block:: python

    from pyams.models import PWLCurrent

    I1 = PWLCurrent("p", "n")
    I1.setPoints("0 0, 1m 2m, 2m 2m, 3m 0")      # SI prefixes allowed
    I1.setParams("Rep=1")

Terminals
---------

``PWLCurrent(p, n)``

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
   * - ``Td``
     - 0
     - s
     - Delay
   * - ``Scale``
     - 1
     - -
     - Amplitude scale
   * - ``Ioff``
     - 0
     - A
     - Offset
   * - ``Rep``
     - 0
     - -
     - Repeat (1) or single shot (0)

Symbol
------

.. figure:: /_static/images/symbols/PWLCurrent_symbol.svg
   :alt: PWL current source symbol
   :align: center
   :width: 160px

   PWL current source symbol as displayed in the PyAMS application.

Description
-----------

This class implements a piece-wise linear current source (SPICE ``PWL``): the current is
defined by a list of (time, value) points and linearly interpolated between them.

.. math::

   I(t) = \text{Scale} \cdot pwl(t - T_d) + I_{off}

Before the first point it holds the first value, after the last point it holds
the last value. Two points with the same time make a vertical step. With
``Rep = 1`` the waveform between the first and last points repeats. The DC
(operating point) value is the waveform value at ``t = 0``.

The points can be given in the constructor, as a list of ``(t, value)`` pairs or
as a string (SI prefixes allowed), or later with ``setPoints()``. The default
points are (0, 0), (1 ms, 1 mA), (2 ms, 1 mA), (3 ms, 0).

**Attributes**

* ``I`` (signal): Output current through the source, from p to n.
* ``Td`` (param): Delay in seconds, default is 0.
* ``Scale`` (param): Amplitude scale factor, default is 1.
* ``Ioff`` (param): Offset in Amperes (A), default is 0.
* ``Rep`` (param): 1 = repeat, 0 = single shot, default is 0.

**Methods**

* ``setPoints(points)``: Sets the waveform points (a list of pairs, a flat list or a string).
* ``analog()``: Interpolates the waveform at the current simulation time.

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model, time
    from pyams.lib import current
    from .PWLVoltage import parse_points, pwl_eval


    class PWLCurrent(model):

        def __init__(self, p, n, points=None):
            self.I = signal('out', current, p, n)
            self.Td = param(0.0, 's', 'Delay')
            self.Scale = param(1.0, ' ', 'Amplitude scale')
            self.Ioff = param(0.0, 'A', 'Offset')
            self.Rep = param(0.0, ' ', 'Repeat (1) or single shot (0)')
            self.setPoints(points if points is not None
                           else [(0.0, 0.0), (1e-3, 1e-3), (2e-3, 1e-3), (3e-3, 0.0)])

        def setPoints(self, points):
            self._ts, self._vs = parse_points(points, 'A')

        def analog(self):
            y = pwl_eval(float(time), self._ts, self._vs, float(self.Td), float(self.Rep) > 0.5)
            self.I += float(self.Scale) * y + float(self.Ioff)
