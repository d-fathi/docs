Nonlinear Resistance
====================

.. code-block:: python

    from pyams.models import NonlinearResistance

    R1 = NonlinearResistance("p", "n")
    R1.setParams("Mu=1")

Terminals
---------

``NonlinearResistance(p, n)``

The current flows from ``p`` to ``n``.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Mu``
     - 1
     - S
     - Nonlinearity coefficient

Symbol
------

.. figure:: /_static/images/symbols/NonlinearResistance_symbol.svg
   :alt: Nonlinear resistance symbol
   :align: center
   :width: 260px

   Nonlinear resistance symbol as displayed in the PyAMS application.

Description
-----------

This class implements a voltage-controlled nonlinear (cubic) resistance used
in the Van der Pol oscillator. Its differential conductance is

.. math::

   \frac{1}{R(v)} = \frac{dI}{dV} = \mu \, (v^2 - 1)

that is, negative for :math:`|v| < 1` (it injects energy) and positive for
:math:`|v| > 1` (it dissipates energy). Integrating gives the current

.. math::

   I(v) = \mu \left( \frac{v^3}{3} - v \right)

Connected in parallel with a capacitor ``C`` and an inductor ``L``, the node
voltage obeys the Van der Pol equation:

.. math::

   C \, v'' + \mu \, (v^2 - 1) \, v' + \frac{v}{L} = 0

**Attributes**

* ``V`` (signal): Input voltage signal across the resistance, defined between nodes (p, n).
* ``I`` (signal): Output current signal through the resistance, flowing from p to n.
* ``Mu`` (param): Nonlinearity / damping coefficient in Siemens (S), default is 1 S.

**Methods**

* ``analog()``: Defines the nonlinear current:

  .. math::

     I = \mu \left( \frac{V^3}{3} - V \right)

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model
    from pyams.lib import voltage, current


    class NonlinearResistance(model):

        def __init__(self, p, n):
            self.V = signal('in', voltage, p, n)
            self.I = signal('out', current, p, n)
            self.Mu = param(1.0, 'S', 'Nonlinearity coefficient')

        def analog(self):
            v = self.V
            self.I += self.Mu * (v * v * v / 3.0 - v)
