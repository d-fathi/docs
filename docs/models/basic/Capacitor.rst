Capacitor
=========

.. code-block:: python

    from pyams.models import Capacitor

    C1 = Capacitor("p", "n")
    C1.setParams("C=1e-6")

Terminals
---------

``Capacitor(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``C``
     - 1e-6
     - F
     - Capacitor value

Symbol
------

.. figure:: /_static/images/symbols/Capacitor_symbol.svg
   :alt: Capacitor symbol
   :align: center
   :width: 200px

   Capacitor symbol as displayed in the PyAMS application.

Description
-----------

This class implements a Capacitor model.

A capacitor stores electrical energy in an electric field and its current
is proportional to the rate of change of voltage across it.

**Attributes**

* ``V`` (signal): Input voltage signal across the capacitor, defined between nodes (p, n).
* ``I`` (signal): Output current signal through the capacitor, defined between nodes (p, n).
* ``C`` (param): Capacitance value in Farads (F), default is 1.0e-6 F.

**Methods**

* ``analog()``: Defines the capacitor behavior using the equation:

  .. math::

     I = C \frac{dV}{dt}

Source Code
-----------

.. code-block:: python

    from pyams.lib import model, signal, param
    from pyams.lib import voltage, current
    from pyams.lib import ddt


    class Capacitor(model):

        def __init__(self, p, n):
            self.V = signal('in', voltage, p, n)
            self.I = signal('out', current, p, n)
            self.C = param(1.0e-6, 'F', 'Capacitor value')

        def analog(self):
            self.I += self.C * ddt(self.V)
