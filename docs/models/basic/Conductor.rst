Conductor
=========

.. code-block:: python

    from pyams.models import Conductor

    W1 = Conductor("p", "n")
    W1.setParams("Len=2 Area=1e-6")

    # with self-heating
    W2 = Conductor("p", "n", thermal=True)

Terminals
---------

``Conductor(p, n, thermal=False)``

* ``p``, ``n``: the two ends of the conductor.
* ``thermal``: when ``True``, the conductor gets a thermal node and self-heating is simulated.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Rho``
     - 1.68e-8
     - Ω·m
     - Resistivity at T0 (copper)
   * - ``Len``
     - 1
     - m
     - Length
   * - ``Area``
     - 1e-6
     - m²
     - Cross-section area (1 mm²)
   * - ``Alpha``
     - 3.93e-3
     - 1/K
     - Temperature coefficient of the resistivity
   * - ``T0``
     - 20
     - °C
     - Reference temperature
   * - ``Tamb``
     - 25
     - °C
     - Ambient temperature
   * - ``Rth``
     - 10
     - K/W
     - Thermal resistance to the ambient (only with ``thermal=True``)
   * - ``Cth``
     - 1
     - J/K
     - Heat capacity (only with ``thermal=True``)

Symbol
------

.. figure:: /_static/images/symbols/Conductor_symbol.svg
   :alt: Conductor symbol
   :align: center
   :width: 260px

   Conductor symbol as displayed in the PyAMS application.

Description
-----------

This class implements a conductor: a wire, a PCB track, a bus bar or a lamp
filament. Unlike a Resistor, the resistance comes from the material and the
geometry, and it follows the temperature:

.. math::

   R_0 = \rho \, \frac{L}{A} \qquad
   R = R_0 \left( 1 + \alpha \, (T - T_0) \right) \qquad
   I = \frac{V}{R}

where :math:`R_0` is the resistance at the reference temperature :math:`T_0`
and :math:`T` is the temperature of the conductor. Without self-heating (the
default) :math:`T` is the ambient temperature ``Tamb``.

**Self-heating**

With ``Conductor(p, n, thermal=True)`` the conductor gets a thermal node whose
voltage is the temperature rise :math:`\Delta T` (in kelvin) above the ambient,
a thermal resistor ``Rth`` to the ambient (K/W) and a heat capacity ``Cth``
(J/K):

.. math::

   C_{th} \frac{d(\Delta T)}{dt} = P - \frac{\Delta T}{R_{th}}
   \qquad P = \frac{V^2}{R} \qquad T = T_{amb} + \Delta T

so the resistance changes with the dissipated power: a copper or tungsten wire
(``Alpha > 0``) limits its own current as it heats up, while with ``Alpha < 0``
(a thermistor) it would run away. The time constant is about :math:`R_{th} C_{th}`.
The temperature rise can be plotted with ``setOutPuts("W1.DT")``.

**Attributes**

* ``V`` (signal): Voltage across the conductor.
* ``I`` (signal): Current from p to n.
* ``DT`` (signal): Temperature rise node (only with ``thermal=True``).

**Methods**

* ``resistance(temperature=None)``: Returns the resistance at a temperature in °C (default: the ambient).
* ``analog()``: Defines the conductor behavior using Ohm's law with the
  temperature-dependent resistance:

  .. math::

     I = \frac{V}{R}

**Typical materials**

Resistivity ``Rho`` at 20 °C and temperature coefficient ``Alpha``:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Material
     - Rho (Ω·m)
     - Alpha (1/K)
   * - Copper
     - 1.68e-8
     - 3.93e-3
   * - Silver
     - 1.59e-8
     - 3.8e-3
   * - Gold
     - 2.44e-8
     - 3.4e-3
   * - Aluminium
     - 2.65e-8
     - 3.9e-3
   * - Tungsten
     - 5.6e-8
     - 4.5e-3
   * - Nichrome
     - 1.1e-6
     - 4e-4
   * - Constantan
     - 4.9e-7
     - 1e-5

Source Code
-----------

.. code-block:: python

    from pyams.lib import model, signal, param
    from pyams.lib import voltage, current
    from pyams.lib import ddt

    _counter = [0]          # every thermal conductor gets its own temperature node


    class Conductor(model):

        def __init__(self, p, n, thermal=False):
            self._thermal = bool(thermal)
            self.V = signal('in', voltage, p, n)
            self.I = signal('out', current, p, n)
            if self._thermal:
                _counter[0] += 1
                nt = '_cond%d_dT' % _counter[0]
                self.DT = signal('in', voltage, nt, '0')         # temperature rise (K)
                self.Ith = signal('out', current, nt, '0')       # heat flow out of the node

            self.Rho = param(1.68e-8, 'Ω·m', 'Resistivity at T0')
            self.Len = param(1.0, 'm', 'Length')
            self.Area = param(1.0e-6, 'm²', 'Cross-section area')
            self.Alpha = param(3.93e-3, '1/K', 'Temperature coefficient of the resistivity')
            self.T0 = param(20.0, '°C', 'Reference temperature')
            self.Tamb = param(25.0, '°C', 'Ambient temperature')
            self.Rth = param(10.0, 'K/W', 'Thermal resistance to the ambient')
            self.Cth = param(1.0, 'J/K', 'Heat capacity')

        def resistance(self, temperature=None):
            t = self.Tamb if temperature is None else temperature
            return self.Rho * self.Len / self.Area * (1.0 + self.Alpha * (t - self.T0))

        def analog(self):
            r0 = self.Rho * self.Len / self.Area
            if self._thermal:
                dT = float(self.DT)
                r = r0 * (1.0 + self.Alpha * (self.Tamb + dT - self.T0))
                if r < 1.0e-3 * r0:                    # keep R positive for a very strong NTC
                    r = 1.0e-3 * r0
                self.I += self.V / r
                power = self.V * self.V / r
                self.Ith += self.Cth * ddt(self.DT) + self.DT / self.Rth - power
            else:
                r = r0 * (1.0 + self.Alpha * (self.Tamb - self.T0))
                self.I += self.V / r
