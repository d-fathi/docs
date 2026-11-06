Capacitor with Initial Voltage
==============================

.. code-block:: python

    from pyams.models import CapacitorIc

    C1 = CapacitorIc("p", "n")
    C1.setParams("C=1e-6 Ic=0")

Terminals
---------

``CapacitorIc(p, n)``

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
     - Capacitance
   * - ``Ic``
     - 0
     - V
     - Initial voltage

Symbol
------

.. figure:: /_static/images/symbols/CapacitorIc_symbol.svg
   :alt: Capacitor with initial voltage symbol
   :align: center
   :width: 200px

   Capacitor with initial voltage symbol as displayed in the PyAMS application.

Description
-----------

This class implements a Capacitor model with an initial voltage
(SPICE ``C ... IC=``).

The capacitor is written in integral form, with the current ``I`` flowing
from ``p`` to ``n``:

.. math::

   V(t) = I_c + \frac{1}{C} \int I \, dt

In the operating point at the start of a transient analysis the integral is
zero, so the capacitor is held at ``V = Ic`` (like ``.ic`` / UIC in SPICE) and
then evolves freely.

**Attributes**

* ``I`` (signal): Input current signal through the capacitor, defined between nodes (p, n).
* ``V`` (signal): Output voltage signal across the capacitor, defined between nodes (p, n).
* ``C`` (param): Capacitance value in Farads (F), default is 1.0e-6 F.
* ``Ic`` (param): Initial voltage V(p) - V(n) in Volts (V), default is 0 V.

**Methods**

* ``analog()``: Defines the capacitor behavior using the integral form:

  .. math::

     V = I_c + \frac{1}{C} \int I \, dt

.. note::

   Use it together with ``InductorIc`` and a normal transient analysis
   (do not use ``uic=True``).

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model
    from pyams.lib import voltage, current
    from pyams.lib import idt


    class CapacitorIc(model):

        def __init__(self, p, n):
            self.I = signal('in', current, p, n)
            self.V = signal('out', voltage, p, n)
            self.C = param(1.0e-6, 'F', 'Capacitance')
            self.Ic = param(0.0, 'V', 'Initial voltage')

        def analog(self):
            self.V += idt(self.I / self.C, self.Ic)
