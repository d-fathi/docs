Voltage-Controlled Voltage Source (VCVS)
========================================

.. code-block:: python

    from pyams.models import VCVS

    X1 = VCVS("p", "n", "cp", "cn")
    X1.setParams("Gain=1")

Terminals
---------

``VCVS(p, n, cp, cn)``

* ``p``, ``n``: output port (an ideal voltage source).
* ``cp``, ``cn``: control port, which draws no current.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Gain``
     - 1
     - V/V
     - Voltage gain

Symbol
------

.. figure:: /_static/images/symbols/VCVS_symbol.svg
   :alt: Voltage-Controlled Voltage Source (VCVS) symbol
   :align: center
   :width: 260px

   Voltage-Controlled Voltage Source (VCVS) symbol as displayed in the PyAMS application.

Description
-----------

This class implements a voltage-controlled voltage source (SPICE ``E`` element).

The control port ``(cp, cn)`` draws no current. The output port ``(p, n)`` is an
ideal voltage source, so its current is set by the circuit around it.

**Attributes**

* ``Vc`` (signal): Control voltage v(cp) - v(cn) (input, no current).
* ``V`` (signal): Output voltage v(p) - v(n).
* ``Gain`` (param): Voltage gain in V/V, default is 1.

**Methods**

* ``analog()``: Defines the source behavior using the equation:

  .. math::

     v(p) - v(n) = \text{Gain} \cdot \left( v(cp) - v(cn) \right)

.. note::

   Typical uses: an ideal amplifier or buffer, an op-amp with a finite gain
   (``Gain = 1e5``), the secondary of an ideal transformer.

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model
    from pyams.lib import voltage


    class VCVS(model):

        def __init__(self, p, n, cp, cn):
            self.Vc = signal('in', voltage, cp, cn)
            self.V = signal('out', voltage, p, n)
            self.Gain = param(1.0, 'V/V', 'Voltage gain')

        def analog(self):
            self.V += self.Gain * self.Vc
