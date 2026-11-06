DC Current
==========

.. code-block:: python

    from pyams.models import DCCurrent

    I1 = DCCurrent("p", "n")
    I1.setParams("Idc=1e-3")

Terminals
---------

``DCCurrent(p, n)``

A positive current flows through the source from ``p`` to ``n``.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Idc``
     - 1e-3
     - A
     - Constant current value

Symbol
------

.. figure:: /_static/images/symbols/DCCurrent_symbol.svg
   :alt: DC current source symbol
   :align: center
   :width: 160px

   DC current source symbol as displayed in the PyAMS application.

Description
-----------

This class models a constant (DC) current source.

The current is :math:`I = I_{dc}` at all times, whatever the voltage across it
(a bias current, a charging current, the tail current of a pair, ...).

**Direction** (same as the SPICE source ``I p n``): a positive current flows
through the source from node ``p`` to node ``n``, that is, it is taken out of
node ``p`` and pushed into node ``n``. A source from ``"0"`` to ``"x"`` with
``Idc > 0`` therefore raises the voltage of node ``x``.

**Attributes**

* ``I`` (signal): Current through the source, from p to n.
* ``Idc`` (param): Current value in Amperes (A), default is 1 mA.

**Methods**

* ``analog()``: Implements the constant current equation:

  .. math::

     I = I_{dc}

Source Code
-----------

.. code-block:: python

    from pyams.lib import signal, param, model
    from pyams.lib import current


    class DCCurrent(model):

        def __init__(self, p, n):
            self.I = signal('out', current, p, n)
            self.Idc = param(1e-3, 'A', 'Constant current value')

        def analog(self):
            self.I += self.Idc
