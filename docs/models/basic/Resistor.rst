Resistor
========

.. code-block:: python

    from pyams.models import Resistor

    R1 = Resistor("p", "n")
    R1.setParams("R=1000")

Terminals
---------

``Resistor(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``R``
     - 1000
     - Ω
     - Resistance

Symbol
------

.. figure:: /_static/images/symbols/Resistor_symbol.svg
   :alt: Resistor symbol
   :align: center
   :width: 200px

   Resistor symbol as displayed in the PyAMS application.

Description
-----------

This class implements a Resistor model.

A resistor limits current flow according to Ohm's Law, which states that
the current through a resistor is proportional to the voltage across it
and inversely proportional to its resistance.

**Attributes**

* ``V`` (signal): Input voltage signal across the resistor, defined between nodes (p, n).
* ``I`` (signal): Output current signal through the resistor, defined between nodes (p, n).
* ``R`` (param): Resistance value in Ohms (Ω), default is 1000 Ω.

**Methods**

* ``analog()``: Defines the resistor behavior using Ohm's Law:

  .. math::

     I = \frac{V}{R}

Source Code
-----------

.. code-block:: python

    from pyams.lib import model, signal, param
    from pyams.lib import voltage, current

    class Resistor(model):

        def __init__(self, p, n):
            self.V = signal('in', voltage, p, n)
            self.I = signal('out', current, p, n)
            self.R = param(1000.0, 'Ω', 'Resistance')

        def analog(self):
            self.I += self.V / self.R
