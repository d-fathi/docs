Transformer
===========

.. code-block:: python

    from pyams.models import Transformer

    T1 = Transformer("p1", "n1", "p2", "n2")
    T1.setParams("L1=0.1 L2=0.025 M=0.0495")

Terminals
---------

``Transformer(p1, n1, p2, n2)``

The primary winding is connected between ``p1`` and ``n1``, and the secondary
winding between ``p2`` and ``n2``.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``L1``
     - 100e-3
     - H
     - Primary inductance
   * - ``L2``
     - 25e-3
     - H
     - Secondary inductance
   * - ``M``
     - 49.5e-3
     - H
     - Mutual inductance

Symbol
------

.. figure:: /_static/images/symbols/Transformer_symbol.svg
   :alt: Transformer symbol
   :align: center
   :width: 240px

   Transformer symbol as displayed in the PyAMS application.

Description
-----------

This class implements a transformer: two inductors with a mutual inductance.

Terminals are given in the order ``(p1, n1, p2, n2)``: primary winding between
``p1`` and ``n1``, secondary winding between ``p2`` and ``n2``. Both currents
are positive when they flow into the winding at its ``p`` terminal (the dots
are at ``p1`` and ``p2``).

The mutual inductance ``M`` is the same in both equations (reciprocity), so the
coupling factor is :math:`k = M / \sqrt{L_1 L_2}` (:math:`k = 1` for an ideal
core). The turns ratio is :math:`n = N_2 / N_1 = \sqrt{L_2 / L_1}`, and for
:math:`k` close to 1 the secondary voltage is :math:`V_2 \approx n V_1`.

**Attributes**

* ``I1``, ``I2`` (signal): Currents of the primary / secondary winding.
* ``V1``, ``V2`` (signal): Voltages of the primary / secondary winding.
* ``L1`` (param): Primary inductance in Henries, default is 100 mH.
* ``L2`` (param): Secondary inductance in Henries, default is 25 mH.
* ``M`` (param): Mutual inductance in Henries, default is 49.5 mH (i.e. k = 0.99).

**Methods**

* ``analog()``: Defines the two coupled-inductor equations:

  .. math::

     V_1 = L_1 \frac{dI_1}{dt} + M \frac{dI_2}{dt}

  .. math::

     V_2 = M \frac{dI_1}{dt} + L_2 \frac{dI_2}{dt}

.. note::

   The two windings are isolated from each other, so one terminal of each
   winding must be connected to the rest of the circuit (e.g. through a diode
   bridge or a load) for the equations to have a unique solution.

   In DC the windings are short circuits (``dI/dt = 0``), so never connect the
   primary directly across an ideal voltage source: add a series resistance
   (the winding resistance).

   ``M`` must satisfy :math:`|M| \le \sqrt{L_1 L_2}`.

Source Code
-----------

.. code-block:: python

    from math import sqrt
    from pyams.lib import model, signal, param
    from pyams.lib import voltage, current
    from pyams.lib import ddt


    class Transformer(model):

        def __init__(self, p1, n1, p2, n2):
            self.I1 = signal('in', current, p1, n1)
            self.I2 = signal('in', current, p2, n2)
            self.V1 = signal('out', voltage, p1, n1)
            self.V2 = signal('out', voltage, p2, n2)
            self.L1 = param(100.0e-3, 'H', 'Primary inductance')
            self.L2 = param(25.0e-3, 'H', 'Secondary inductance')
            self.M = param(49.5e-3, 'H', 'Mutual inductance')

        def analog(self):
            if abs(self.M) > sqrt(self.L1 * self.L2) * (1 + 1e-9):
                raise ValueError("Transformer: |M| must not exceed sqrt(L1*L2)")
            d1 = ddt(self.I1)
            d2 = ddt(self.I2)
            self.V1 += self.L1 * d1 + self.M * d2
            self.V2 += self.M * d1 + self.L2 * d2
