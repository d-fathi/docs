Inductor
========

.. code-block:: python

    from pyams.models import Inductor

    L1 = Inductor("p", "n")
    L1.setParams("L=1e-3")

Terminals
---------

``Inductor(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``L``
     - 1e-3
     - H
     - Inductor value

Symbol
------

.. figure:: /_static/images/symbols/Inductor_symbol.svg
   :alt: Inductor symbol
   :align: center
   :width: 200px

   Inductor symbol as displayed in the PyAMS application.

Description
-----------

This class implements an Inductor model.

An inductor stores energy in a magnetic field and the voltage across it is
proportional to the rate of change of its current.

**Attributes**

* ``I`` (signal): Input current signal through the inductor, defined between nodes (p, n).
* ``V`` (signal): Output voltage signal across the inductor, defined between nodes (p, n).
* ``L`` (param): Inductance value in Henries (H), default is 1.0e-3 H.

**Methods**

* ``analog()``: Defines the inductor behavior using the equation:

  .. math::

     V = L \frac{dI}{dt}

.. note::

   The inductor imposes the voltage ``V``, so its current is an extra unknown
   of the circuit (the ``in`` current signal reads it). In a DC analysis
   ``dI/dt = 0``, so the inductor behaves as a short circuit.

Source Code
-----------

.. code-block:: python

    from pyams.lib import model, signal, param
    from pyams.lib import voltage, current
    from pyams.lib import ddt


    class Inductor(model):

        def __init__(self, p, n):
            self.I = signal('in', current, p, n)
            self.V = signal('out', voltage, p, n)
            self.L = param(1.0e-3, 'H', 'Inductor value')

        def analog(self):
            self.V += self.L * ddt(self.I)
