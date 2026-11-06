Voltage-Controlled Current Source (VCCS)
========================================

.. code-block:: python

    from pyams.models import VCCS

    X1 = VCCS("p", "n", "cp", "cn")
    X1.setParams("Gm=1e-3")

Terminals
---------

``VCCS(p, n, cp, cn)``

* ``p``, ``n``: output port. The current flows through the source from ``p`` to ``n``.
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
   * - ``Gm``
     - 1e-3
     - S
     - Transconductance

Symbol
------

.. figure:: /_static/images/symbols/VCCS_symbol.svg
   :alt: Voltage-Controlled Current Source (VCCS) symbol
   :align: center
   :width: 260px

   Voltage-Controlled Current Source (VCCS) symbol as displayed in the PyAMS application.

Description
-----------

This class implements a voltage-controlled current source (SPICE ``G`` element, a
transconductance).

The current ``Gm * Vc`` flows through the source from ``p`` to ``n`` (it is taken
out of node ``p`` and pushed into node ``n``), like ``DCCurrent``. The control
port draws no current.

**Attributes**

* ``Vc`` (signal): Control voltage v(cp) - v(cn) (input, no current).
* ``I`` (signal): Output current from p to n.
* ``Gm`` (param): Transconductance in Siemens (S), default is 1 mS.

**Methods**

* ``analog()``: Defines the source behavior using the equation:

  .. math::

     i(p \rightarrow n) = G_m \cdot \left( v(cp) - v(cn) \right)

.. note::

   Typical uses: the ``gm*vgs`` generator of a small-signal transistor model,
   a transconductance amplifier, a gyrator (two VCCS with opposite signs make an
   inductor from a capacitor).

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model
    from pyams.lib import voltage, current


    class VCCS(model):

        def __init__(self, p, n, cp, cn):
            self.Vc = signal('in', voltage, cp, cn)
            self.I = signal('out', current, p, n)
            self.Gm = param(1.0e-3, 'S', 'Transconductance')

        def analog(self):
            self.I += self.Gm * self.Vc
