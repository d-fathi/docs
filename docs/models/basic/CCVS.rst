Current-Controlled Voltage Source (CCVS)
========================================

.. code-block:: python

    from pyams.models import CCVS

    X1 = CCVS("p", "n", "cp", "cn")
    X1.setParams("Rm=1000")

Terminals
---------

``CCVS(p, n, cp, cn)``

* ``p``, ``n``: output port (an ideal voltage source).
* ``cp``, ``cn``: control branch. ``Ic`` is the current that flows through it from ``cp`` to ``cn``.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Rm``
     - 1e3
     - Ω
     - Transresistance

Symbol
------

.. figure:: /_static/images/symbols/CCVS_symbol.svg
   :alt: Current-Controlled Voltage Source (CCVS) symbol
   :align: center
   :width: 260px

   Current-Controlled Voltage Source (CCVS) symbol as displayed in the PyAMS application.

Description
-----------

This class implements a current-controlled voltage source (SPICE ``H`` element, a
transresistance).

``Ic`` is the current that flows through the control branch from ``cp`` to ``cn``.
The control branch is built into the element: it is a zero-volt source, an
ideal ammeter, so connect ``(cp, cn)`` **in series** with the branch whose
current controls the source (the current enters at ``cp`` and leaves at ``cn``).

**Attributes**

* ``Vs`` (signal): The 0 V sensing branch between cp and cn.
* ``Ic`` (signal): Its current, from cp to cn.
* ``V`` (signal): Output voltage v(p) - v(n).
* ``Rm`` (param): Transresistance in Ohms (Ω), default is 1 kΩ.

**Methods**

* ``analog()``: Defines the source behavior using the equation:

  .. math::

     v(p) - v(n) = R_m \cdot I_c

.. note::

   Typical uses: a current-to-voltage (transimpedance) converter, a gyrator,
   the primary-current sensing half of an ideal transformer.

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model
    from pyams.lib import voltage, current


    class CCVS(model):

        def __init__(self, p, n, cp, cn):
            self.Vs = signal('out', voltage, cp, cn)       # zero-volt ammeter
            self.Ic = signal('in', current, cp, cn)
            self.V = signal('out', voltage, p, n)
            self.Rm = param(1.0e3, 'Ω', 'Transresistance')

        def analog(self):
            self.Vs += 0.0
            self.V += self.Rm * self.Ic
