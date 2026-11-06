AC Current
==========

.. code-block:: python

    from pyams.models import ACCurrent

    I1 = ACCurrent("p", "n")
    I1.setParams("Iac=1")

Terminals
---------

``ACCurrent(p, n)``

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
     - 0
     - A
     - DC value (bias)
   * - ``Iac``
     - 1
     - A
     - AC amplitude
   * - ``Ph``
     - 0
     - °
     - AC phase

Symbol
------

.. figure:: /_static/images/symbols/ACCurrent_symbol.svg
   :alt: AC current source symbol
   :align: center
   :width: 160px

   AC current source symbol as displayed in the PyAMS application.

Description
-----------

This class implements a current source for the AC (small-signal frequency)
analysis.

In DC and transient analyses it is a constant source :math:`I = I_{dc}`
(0 A by default). In ``analysis(mode="ac", ...)`` it injects the phasor

.. math::

   I_{ac} \, e^{j \, Ph}

at every frequency. The direction is the same as for ``DCCurrent``: a positive
current flows through the source from node ``p`` to node ``n``.

**Attributes**

* ``I`` (signal): Current through the source, from p to n.
* ``Idc`` (param): DC value in Amperes (A), default is 0 A.
* ``Iac`` (param): AC amplitude in Amperes (A), default is 1 A.
* ``Ph`` (param): AC phase in degrees, default is 0.

**Methods**

* ``analog()``: Defines the DC / transient value:

  .. math::

     I = I_{dc}

* ``ac()``: Returns the (signal name, phasor) pair used by the AC analysis.

Source Code
-----------

.. code-block:: python

    import cmath
    import math
    from pyams.lib import signal, param, model
    from pyams.lib import current


    class ACCurrent(model):

        def __init__(self, p, n):
            self.I = signal('out', current, p, n)
            self.Idc = param(0.0, 'A', 'DC value (bias)')
            self.Iac = param(1.0, 'A', 'AC amplitude')
            self.Ph = param(0.0, '°', 'AC phase')

        def analog(self):
            self.I += self.Idc

        def ac(self):
            return 'I', self.Iac * cmath.exp(1j * math.radians(self.Ph))
