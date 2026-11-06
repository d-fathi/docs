Inductor with Initial Current
=============================

.. code-block:: python

    from pyams.models import InductorIc

    L1 = InductorIc("p", "n")
    L1.setParams("L=1e-3 Ic=0")

Terminals
---------

``InductorIc(p, n)``

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
     - Inductance
   * - ``Ic``
     - 0
     - A
     - Initial current

Symbol
------

.. figure:: /_static/images/symbols/InductorIc_symbol.svg
   :alt: Inductor with initial current symbol
   :align: center
   :width: 200px

   Inductor with initial current symbol as displayed in the PyAMS application.

Description
-----------

This class implements an Inductor model with an initial current
(SPICE ``L ... IC=``).

The inductor is written in integral form, with the current ``I`` flowing
from ``p`` to ``n``:

.. math::

   I(t) = I_c + \frac{1}{L} \int V \, dt

At the start of the transient analysis (operating point) the inductor carries
exactly ``Ic`` and then evolves freely.

**Attributes**

* ``V`` (signal): Input voltage signal across the inductor, defined between nodes (p, n).
* ``I`` (signal): Output current signal through the inductor, defined between nodes (p, n).
* ``L`` (param): Inductance value in Henries (H), default is 1.0e-3 H.
* ``Ic`` (param): Initial current from p to n in Amperes (A), default is 0 A.

**Methods**

* ``analog()``: Defines the inductor behavior using the integral form:

  .. math::

     I = I_c + \frac{1}{L} \int V \, dt

.. note::

   Use it with a normal transient analysis (not ``uic=True``).

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model
    from pyams.lib import voltage, current
    from pyams.lib import idt


    class InductorIc(model):

        def __init__(self, p, n):
            self.V = signal('in', voltage, p, n)
            self.I = signal('out', current, p, n)
            self.L = param(1.0e-3, 'H', 'Inductance')
            self.Ic = param(0.0, 'A', 'Initial current')

        def analog(self):
            self.I += idt(self.V / self.L, self.Ic)
