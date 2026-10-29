Diode
=====

.. code-block:: python

    from pyams.models import Diode

    X1 = Diode("p", "n")
    X1.setParams("Iss=1e-15 Vt=0.025")

Terminals
---------

``Diode(p, n)``

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
     - –
     - The ideality factor

Description
-----------

The documentation of the class (``help(Diode)``)::

    This class implements a simple Diode model.

    A diode is a semiconductor device that allows current to flow in one direction
    while blocking it in the reverse direction. It follows the Shockley diode equation
    to define its behavior.

    Attributes:
        V (signal): Input voltage signal across the diode, defined between nodes (p, n).
        I (signal): Output current signal through the diode, defined between nodes (p, n).
        Iss (param): Saturation current (default: 1.0e-15 A), representing the small leakage
                     current in reverse bias.
        Vt (param): Thermal voltage (default: 0.025 V), depending on temperature.
        n (param): Ideality factor (default: 1), representing how closely the diode follows
                   the ideal diode equation.

    Methods:
        analog(): Defines the diode behavior using the Shockley equation:
                  I = Iss * (exp(V / (n * Vt)) - 1)

Used in the examples
--------------------

* :doc:`Half wave rectification circuit </examples/half_wave_rectifier>`
* :doc:`Full-wave bridge rectifier fed by a transformer </examples/bridge_rectifier>`
* :doc:`IGBT chopper (low-side switch, inductive load, freewheel diode) </examples/igbt_chopper>`

