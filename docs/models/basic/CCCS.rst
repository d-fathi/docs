Current-Controlled Current Source (CCCS)
========================================

.. code-block:: python

    from pyams.models import CCCS

    X1 = CCCS("p", "n", "cp", "cn")
    X1.setParams("Gain=1")

Terminals
---------

``CCCS(p, n, cp, cn)``

* ``p``, ``n``: output port. The current ``Gain * Ic`` flows through the source from ``p`` to ``n``.
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
   * - ``Gain``
     - 1
     - A/A
     - Current gain

Symbol
------

.. figure:: /_static/images/symbols/CCCS_symbol.svg
   :alt: Current-Controlled Current Source (CCCS) symbol
   :align: center
   :width: 260px

   Current-Controlled Current Source (CCCS) symbol as displayed in the PyAMS application.

Description
-----------

This class implements a current-controlled current source (SPICE ``F`` element, a
current mirror / current amplifier).

``Ic`` is the current that flows through the control branch from ``cp`` to ``cn``.
The control branch is built into the element: it is a zero-volt source, an
ideal ammeter, so connect ``(cp, cn)`` **in series** with the branch whose
current controls the source (the current enters at ``cp`` and leaves at ``cn``).
The output current ``Gain * Ic`` flows through the source from ``p`` to ``n``.

**Attributes**

* ``Vs`` (signal): The 0 V sensing branch between cp and cn.
* ``Ic`` (signal): Its current, from cp to cn.
* ``I`` (signal): Output current from p to n.
* ``Gain`` (param): Current gain in A/A, default is 1.

**Methods**

* ``analog()``: Defines the source behavior using the equation:

  .. math::

     i(p \rightarrow n) = \text{Gain} \cdot I_c

.. note::

   Typical uses: the ``beta*ib`` generator of a transistor model, an ideal
   current mirror, the primary current of an ideal transformer.

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model
    from pyams.lib import voltage, current


    class CCCS(model):

        def __init__(self, p, n, cp, cn):
            self.Vs = signal('out', voltage, cp, cn)       # zero-volt ammeter
            self.Ic = signal('in', current, cp, cn)
            self.I = signal('out', current, p, n)
            self.Gain = param(1.0, 'A/A', 'Current gain')

        def analog(self):
            self.Vs += 0.0
            self.I += self.Gain * self.Ic
