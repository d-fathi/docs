DC Voltage
==========

.. code-block:: python

    from pyams.models import DCVoltage

    V1 = DCVoltage("p", "n")
    V1.setParams("Vdc=5")

Terminals
---------

``DCVoltage(p, n)``

``p`` is the positive terminal.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Vdc``
     - 5
     - V
     - Constant voltage value

Symbol
------

.. figure:: /_static/images/symbols/DCVoltage_symbol.svg
   :alt: DC voltage source symbol
   :align: center
   :width: 160px

   DC voltage source symbol as displayed in the PyAMS application.

Description
-----------

This class models a constant (DC) voltage source.

The voltage is :math:`V = V_{dc}` at all times, so it is also the supply of
circuits that need a fixed rail (a battery, Vcc, a bias voltage).

**Attributes**

* ``V`` (signal): Output voltage between nodes (p, n); ``p`` is the + terminal.
* ``Vdc`` (param): Voltage value in Volts (V), default is 5.0 V.

**Methods**

* ``analog()``: Implements the constant voltage equation:

  .. math::

     V = V_{dc}

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model
    from pyams.lib import voltage


    class DCVoltage(model):

        def __init__(self, p, n):
            self.V = signal('out', voltage, p, n)
            self.Vdc = param(5.0, 'V', 'Constant voltage value')

        def analog(self):
            self.V += self.Vdc
