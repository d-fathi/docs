Diode
=====

.. code-block:: python

    from pyams.models import Diode

    D1 = Diode("p", "n")
    D1.setParams("Iss=1e-15 n=1")

Terminals
---------

``Diode(p, n)``

``p`` is the anode and ``n`` is the cathode.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Iss``
     - 1e-15
     - A
     - Saturation current
   * - ``Vt``
     - 0.025
     - V
     - Thermal voltage
   * - ``n``
     - 1
     - -
     - Ideality factor

Symbol
------

.. figure:: /_static/images/symbols/Diode_symbol.svg
   :alt: Diode symbol
   :align: center
   :width: 260px

   Diode symbol as displayed in the PyAMS application.

Description
-----------

This class implements a simple diode model.

A diode is a semiconductor device that allows current to flow in one direction
while blocking it in the reverse direction. It follows the Shockley diode
equation.

**Attributes**

* ``V`` (signal): Input voltage signal across the diode, defined between nodes (p, n).
* ``I`` (signal): Output current signal through the diode, defined between nodes (p, n).
* ``Iss`` (param): Saturation current, default is 1.0e-15 A (the small leakage current in reverse bias).
* ``Vt`` (param): Thermal voltage, default is 0.025 V (depends on the temperature).
* ``n`` (param): Ideality factor, default is 1 (how closely the diode follows the ideal diode equation).

**Methods**

* ``analog()``: Defines the diode behavior using the Shockley equation:

  .. math::

     I = I_{ss} \left( e^{V / (n V_t)} - 1 \right)

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, model, param
    from pyams.lib import voltage, current
    from math import exp

    # Simple Diode Model-----------------------------------------------------------
    class Diode(model):
        def __init__(self, p, n):
            # Signals declarations------------------------------------------------
            self.V = signal('in', voltage, p, n)
            self.I = signal('out', current, p, n)

            # Parameters declarations----------------------------------------------
            self.Iss = param(1.0e-15, 'A', 'Saturation current')
            self.Vt = param(0.025, 'V', 'Thermal voltage')
            self.n = param(1, ' ', 'The ideality factor')

        def analog(self):
            self.I += self.Iss * (exp(self.V / (self.n * self.Vt)) - 1)
