AC Voltage
==========

.. code-block:: python

    from pyams.models import ACVoltage

    V1 = ACVoltage("p", "n")
    V1.setParams("Vac=1")

Terminals
---------

``ACVoltage(p, n)``

``p`` is the positive terminal.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Vdc``
     - 0
     - V
     - DC value (bias)
   * - ``Vac``
     - 1
     - V
     - AC amplitude
   * - ``Ph``
     - 0
     - °
     - AC phase

Symbol
------

.. figure:: /_static/images/symbols/ACVoltage_symbol.svg
   :alt: AC voltage source symbol
   :align: center
   :width: 160px

   AC voltage source symbol as displayed in the PyAMS application.

Description
-----------

This class implements a voltage source for the AC (small-signal frequency)
analysis.

In a DC or transient analysis it is a constant source :math:`V = V_{dc}`
(0 V by default, so the AC source is silent: it has no effect on the operating
point). In ``analysis(mode="ac", ...)`` the circuit is linearised around its
DC operating point and this source injects the phasor

.. math::

   V_{ac} \, e^{j \, Ph}

at every frequency, so each node voltage of the result is directly the
transfer function (with ``Vac = 1`` V, the default).

**Attributes**

* ``V`` (signal): Output voltage between nodes (p, n); ``p`` is the + terminal.
* ``Vdc`` (param): DC value in Volts (V), default is 0 V: the bias of the operating point.
* ``Vac`` (param): AC amplitude in Volts (V), default is 1 V.
* ``Ph`` (param): AC phase in degrees, default is 0.

**Methods**

* ``analog()``: Defines the DC / transient value:

  .. math::

     V = V_{dc}

* ``ac()``: Returns the (signal name, phasor) pair used by the AC analysis.

Source Code
-----------

.. code-block:: python

    import cmath
    import math
    from pyams.lib import signal, param, model
    from pyams.lib import voltage


    class ACVoltage(model):

        def __init__(self, p, n):
            self.V = signal('out', voltage, p, n)
            self.Vdc = param(0.0, 'V', 'DC value (bias)')
            self.Vac = param(1.0, 'V', 'AC amplitude')
            self.Ph = param(0.0, '°', 'AC phase')

        def analog(self):
            self.V += self.Vdc

        def ac(self):
            return 'V', self.Vac * cmath.exp(1j * math.radians(self.Ph))
