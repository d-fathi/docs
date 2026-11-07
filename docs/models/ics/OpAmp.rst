OpAmp
=====

.. code-block:: python

    from pyams.models import OpAmp

    U1 = OpAmp("p", "n", "out")
    U1.setParams("A=1e5 Vcc=12 Vee=-12")

Terminals
---------

``OpAmp(p, n, out)``

* ``p``: non-inverting input (+).
* ``n``: inverting input (-).
* ``out``: output, measured against ground ``"0"``.

The inputs draw no current.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``A``
     - 1e5
     - -
     - Open-loop DC gain
   * - ``Vcc``
     - 12
     - V
     - Positive supply / saturation voltage
   * - ``Vee``
     - -12
     - V
     - Negative supply / saturation voltage
   * - ``Ro``
     - 75
     - Ω
     - Output resistance
   * - ``Tau``
     - 0.2e-6
     - s
     - Output time constant
   * - ``Vos``
     - 0
     - V
     - Input offset voltage

Symbol
------

.. figure:: /_static/images/symbols/OpAmp_symbol.svg
   :alt: OpAmp symbol
   :align: center
   :width: 260px

   OpAmp symbol as displayed in the PyAMS application.

Description
-----------

This class implements an operational amplifier with a finite gain, output
saturation and a single dominant pole.

The ideal output voltage follows the differential input
:math:`V_d = V(p) - V(n) + V_{os}` and saturates smoothly at the supply rails:

.. math::

   V_{target} = V_{mid} + V_h \tanh\left( \frac{A \, V_d}{V_h} \right)
   \qquad V_{mid} = \frac{V_{cc} + V_{ee}}{2}
   \qquad V_h = \frac{V_{cc} - V_{ee}}{2}

The output is a Thevenin source :math:`V_{target}` behind the output resistance
``Ro``, with a time constant ``Tau`` (the dominant pole) which limits the speed of
the output:

.. math::

   I_{out} = \frac{V_{out} - V_{target}}{R_o} + \frac{\tau}{R_o} \frac{dV_{out}}{dt}

The pole is not a detail: a circuit with positive feedback (a comparator, a
relaxation oscillator) makes the algebraic equations jump when the output
switches, so without it the solver cannot follow the transition.

**Attributes**

* ``Vd`` (signal): Differential input voltage between p and n.
* ``Vo`` (signal): Output voltage, measured against ground.
* ``Io`` (signal): Output current from the output node to ground.
* ``A`` (param): Open-loop DC gain, default is 1.0e5.
* ``Vcc`` (param): Positive supply / saturation voltage, default is 12 V.
* ``Vee`` (param): Negative supply / saturation voltage, default is -12 V.
* ``Ro`` (param): Output resistance, default is 75 Ω.
* ``Tau`` (param): Output time constant, default is 0.2 µs.
* ``Vos`` (param): Input offset voltage, default is 0 V.

**Methods**

* ``analog()``: Defines the output equation above.

.. note::

   With the ideal offset ``Vos = 0`` a perfectly symmetric oscillator stays at its
   unstable equilibrium (0 V) and never starts, like a noise-free real circuit; a
   small offset (1 mV) starts it, as real amplifiers have.

Source Code
-----------

.. code-block:: python

    from math import tanh
    from pyams.lib import model, signal, param
    from pyams.lib import voltage, current
    from pyams.lib import ddt


    # Operational Amplifier Model ------------------------------------------------------
    class OpAmp(model):
        def __init__(self, p, n, out):
            # Signals declarations---------------------------------------------------
            self.Vd = signal('in', voltage, p, n)
            self.Vo = signal('in', voltage, out, '0')
            self.Io = signal('out', current, out, '0')
            # Parameter declarations-------------------------------------------------
            self.A = param(1.0e5, ' ', 'Open-loop DC gain')
            self.Vcc = param(12.0, 'V', 'Positive saturation voltage')
            self.Vee = param(-12.0, 'V', 'Negative saturation voltage')
            self.Ro = param(75.0, 'Ω', 'Output resistance')
            self.Tau = param(0.2e-6, 's', 'Output time constant')
            self.Vos = param(0.0, 'V', 'Input offset voltage')

        def analog(self):
            vmid = 0.5 * (self.Vcc + self.Vee)
            vh = 0.5 * (self.Vcc - self.Vee)
            vtarget = vmid + vh * tanh(self.A * (self.Vd + self.Vos) / vh)
            self.Io += (self.Vo - vtarget) / self.Ro + (self.Tau / self.Ro) * ddt(self.Vo)
