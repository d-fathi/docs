Transmission Line
=================

.. code-block:: python

    from pyams.models import TransmissionLine

    T1 = TransmissionLine("p1", "p2", "0", sections=20)
    T1.setParams("Z0=50 Td=1e-9")

Terminals
---------

``TransmissionLine(p1, p2, ref="0", sections=20)``

* ``p1``, ``p2``: the two ends of the line.
* ``ref``: the common (return) conductor, usually ground ``"0"``.
* ``sections``: number of lumped sections ``N`` (fixed when the element is made).

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Z0``
     - 50
     - Ω
     - Characteristic impedance
   * - ``Td``
     - 1e-9
     - s
     - One-way delay
   * - ``R``
     - 0
     - Ω
     - Total series resistance
   * - ``G``
     - 0
     - S
     - Total shunt conductance

Symbol
------

.. figure:: /_static/images/symbols/TransmissionLine_symbol.svg
   :alt: Transmission line symbol
   :align: center
   :width: 260px

   Transmission line symbol as displayed in the PyAMS application.

Description
-----------

This class implements a two-port (single-conductor) transmission line,
modelled as a ladder of ``sections`` identical lumped sections (pi network:
half a shunt capacitor at each end of every section).

.. code-block:: text

    p1 --[R/N + L/N]--o--[R/N + L/N]--o-- ... --[R/N + L/N]-- p2
                      |                |
                   C/N, G/N         C/N, G/N      (C/2N, G/2N at the ends)
                      |                |
    ref ---------------------------------------------------------

The line is described by its characteristic impedance and delay:

.. math::

   L = Z_0 T_d \qquad C = \frac{T_d}{Z_0}

where ``L`` is the total series inductance (H), ``C`` is the total shunt
capacitance (F), ``R`` is the total series resistance (Ω) and ``G`` is the
total shunt conductance (S).

A lossless line has the impedance :math:`Z_0 = \sqrt{L/C}` and delays a signal
by :math:`T_d = \sqrt{LC}`. Every section has a series branch

.. math::

   V = \frac{R}{N} I + \frac{L}{N} \frac{dI}{dt}

(its current is an extra unknown) and shunt currents

.. math::

   I = \frac{C}{N} \frac{dV}{dt} + \frac{G}{N} V

**Attributes**

* ``Z0`` (param): Characteristic impedance, default is 50 Ω.
* ``Td`` (param): One-way delay of the line, default is 1 ns.
* ``R`` (param): Total series resistance of the line, default is 0 Ω.
* ``G`` (param): Total shunt conductance of the line, default is 0 S.

**Methods**

* ``analog()``: Defines, for every section, the series R + L branch and the
  shunt C ∥ G branches (half weight at the two ends of the line).

.. note::

   **Accuracy:** a ladder is a low-pass filter whose cut-off frequency is about
   :math:`N / (\pi T_d)`. Use :math:`N \ge 10 \, T_d / t_r` for a signal of rise
   time :math:`t_r` (for a sine wave of frequency :math:`f`,
   :math:`N \ge 10 \, f \, T_d \, 2\pi` gives about 1 % error in amplitude).
   A large ``N`` costs more, since there are about :math:`2N` unknowns.

Source Code
-----------

.. code-block:: python

    from pyams.lib import model, signal, param
    from pyams.lib import voltage, current
    from pyams.lib import ddt

    _counter = [0]          # gives every line its own internal node names


    class TransmissionLine(model):

        def __init__(self, p1, p2, ref="0", sections=20):
            n = int(sections)
            if n < 1:
                raise ValueError('sections must be >= 1')
            _counter[0] += 1
            tag = '_tl%d_' % _counter[0]
            # nodes: x[0] = p1 ... x[n] = p2, the middle ones are internal
            x = [p1] + [tag + str(k) for k in range(1, n)] + [p2]
            self.N = n
            # series branches (R + L)
            self._si, self._sv = [], []
            for k in range(n):
                iname, vname = 'Is%d' % k, 'Vs%d' % k
                setattr(self, iname, signal('in', current, x[k], x[k + 1]))
                setattr(self, vname, signal('out', voltage, x[k], x[k + 1]))
                self._si.append(iname)
                self._sv.append(vname)
            # shunt branches (C || G) at every node
            self._pv, self._pi = [], []
            for k in range(n + 1):
                vname, iname = 'Vp%d' % k, 'Ip%d' % k
                setattr(self, vname, signal('in', voltage, x[k], ref))
                setattr(self, iname, signal('out', current, x[k], ref))
                self._pv.append(vname)
                self._pi.append(iname)

            self.Z0 = param(50.0, 'Ω', 'Characteristic impedance')
            self.Td = param(1e-9, 'Sec', 'One-way delay')
            self.R = param(0.0, 'Ω', 'Total series resistance')
            self.G = param(0.0, 'S', 'Total shunt conductance')

        def analog(self):
            n = self.N
            L = self.Z0 * self.Td / n          # per section
            C = self.Td / self.Z0 / n
            R = self.R / n
            G = self.G / n
            # series R + L
            for iname, vname in zip(self._si, self._sv):
                i = getattr(self, iname)
                setattr(self, vname, getattr(self, vname) + R * i + L * ddt(i))
            # shunt C || G (half weight at the two ends)
            last = n
            for k, (vname, iname) in enumerate(zip(self._pv, self._pi)):
                w = 0.5 if k == 0 or k == last else 1.0
                v = getattr(self, vname)
                setattr(self, iname, getattr(self, iname) + w * (C * ddt(v) + G * v))
