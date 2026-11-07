Diac
====

.. code-block:: python

    from pyams.models import Diac

    D1 = Diac("p", "n")
    D1.setParams("Vbo=36 Vh=16")

Terminals
---------

``Diac(p, n)``

The device is symmetrical, so ``p`` and ``n`` can be exchanged.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Vbo``
     - 36
     - V
     - Breakover voltage
   * - ``Vh``
     - 16
     - V
     - On-state voltage (zero-current extrapolation)
   * - ``Ih``
     - 1e-3
     - A
     - Holding current
   * - ``Ron``
     - 34
     - Ω
     - On-state dynamic resistance
   * - ``Roff``
     - 4e6
     - Ω
     - Off-state resistance

Symbol
------

.. figure:: /_static/images/symbols/Diac_symbol.svg
   :alt: Diac symbol
   :align: center
   :width: 260px

   Diac symbol as displayed in the PyAMS application.

Description
-----------

This class implements a diac: a two-terminal, symmetrical device that blocks
until the voltage reaches the breakover voltage, then switches to a
low-voltage conducting state, and stays on until the current falls below the
holding current.

The device has memory (hysteresis), so the model keeps a state, off or on:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - State
     - Equation
   * - off
     - :math:`I = V / R_{off}` (leakage, blocking)
   * - on
     - :math:`I = \mathrm{sign}(V) \, (|V| - V_h) / R_{on}` (conducting, for :math:`|V| > V_h`)

The device switches **off -> on** when :math:`|V| \ge V_{bo}` (breakover) and
**on -> off** when :math:`|I| < I_h` (current below the holding current).

The state changes only when a time step is accepted (never inside a step that
may be rejected), so within a step the diac is an ordinary smooth nonlinear
resistor. The turn-off therefore happens at about :math:`|V| = V_h + R_{on} I_h`.

A continuous S-shaped I-V curve is not used: at the breakover point the Newton
iteration of an implicit solver cannot cross the fold of such a curve. A
switching state avoids that, at the price of a current that jumps when the diac
changes state.

**Attributes**

* ``V`` (signal): Input voltage signal across the diac, between nodes (p, n).
* ``I`` (signal): Output current signal through the diac, between nodes (p, n).
* ``Vbo`` (param): Breakover voltage, default is 36 V.
* ``Vh`` (param): On-state voltage at zero current extrapolation, default is 16 V.
* ``Ih`` (param): Holding current, default is 1 mA.
* ``Ron`` (param): Dynamic resistance when conducting, default is 34 Ω.
* ``Roff`` (param): Resistance when blocking, default is 4 MΩ.

**Methods**

* ``analog()``: Defines the current of the present state and its transitions.

.. note::

   The state is updated when a transient step is accepted, so a transient
   analysis is needed (in a DC analysis the diac stays off). The circuit must
   contain a capacitor or an inductor, as usual for an oscillator.

Source Code
-----------

.. code-block:: python

    from math import sqrt
    from pyams.lib import model, signal, param
    from pyams.lib import voltage, current
    from pyams.lib import ddt, accepting

    def _pos(x, eps=0.05):
        return 0.5 * (x + sqrt(x * x + eps * eps))

    # Diac Model ----------------------------------------------------------------------
    class Diac(model):
        def __init__(self, p, n):
            # Signals declarations---------------------------------------------------
            self.V = signal('in', voltage, p, n)
            self.I = signal('out', current, p, n)
            # Parameter declarations-------------------------------------------------
            self.Vbo = param(36.0, 'V', 'Breakover voltage')
            self.Vh = param(16.0, 'V', 'On-state voltage (zero-current extrapolation)')
            self.Ih = param(1.0e-3, 'A', 'Holding current')
            self.Ron = param(34.0, 'Ω', 'On-state dynamic resistance')
            self.Roff = param(4.0e6, 'Ω', 'Off-state resistance')
            # State (hysteresis)
            self._on = False

        def analog(self):
            v = self.V
            ddt(v)              # makes the diac a stateful element: analog() is then
                                # also called, once, for every accepted time point
            if accepting():
                av = abs(v)
                if self._on:
                    if (av - self.Vh) / self.Ron < self.Ih:
                        self._on = False
                elif av >= self.Vbo:
                    self._on = True
                return
            if self._on:
                self.I += (_pos(v - self.Vh) - _pos(-v - self.Vh)) / self.Ron
            else:
                self.I += v / self.Roff
