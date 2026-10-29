Operational Amplifier
=====================

.. code-block:: python

    from pyams.models import OpAmp

    X1 = OpAmp("p", "n", "out")
    X1.setParams("A=100000 Vcc=12")

Terminals
---------

``OpAmp(p, n, out)``

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
     - 100000
     - –
     - Open-loop DC gain
   * - ``Vcc``
     - 12
     - V
     - Positive saturation voltage
   * - ``Vee``
     - -12
     - V
     - Negative saturation voltage
   * - ``Ro``
     - 75
     - Ω
     - Output resistance
   * - ``Tau``
     - 2e-07
     - s
     - Output time constant
   * - ``Vos``
     - 0
     - V
     - Input offset voltage

Description
-----------

The documentation of the class (``help(OpAmp)``)::

    This class implements an operational amplifier with a finite gain, output
    saturation and a single dominant pole.

    Terminals are given in the order (p, n, out): non-inverting input (+),
    inverting input (-) and output.  The inputs draw no current.

    The ideal output voltage follows the differential input Vd = V(p) - V(n) + Vos
    and saturates smoothly at the supply rails:

        Vtarget = Vmid + Vh * tanh(A * Vd / Vh)
        Vmid = (Vcc + Vee) / 2        Vh = (Vcc - Vee) / 2

    The output is a Thevenin source Vtarget behind the output resistance Ro,
    with a time constant Tau (the dominant pole), which limits the speed of the
    output:

        Iout = (Vout - Vtarget) / Ro + (Tau / Ro) * dVout/dt

    The pole is not a detail: a circuit with positive feedback (a comparator,
    a relaxation oscillator) makes the algebraic equations jump when the
    output switches, so without it the solver cannot follow the transition.

    Attributes:
        Vd (signal): Differential input voltage between p and n.
        Vo (signal): Output voltage, measured against ground.
        Io (signal): Output current from the output node to ground.
        A (param): Open-loop DC gain (default: 1.0e5).
        Vcc (param): Positive supply / saturation voltage (default: 12 V).
        Vee (param): Negative supply / saturation voltage (default: -12 V).
        Ro (param): Output resistance (default: 75 ohm).
        Tau (param): Output time constant (default: 0.2 us).
        Vos (param): Input offset voltage (default: 0 V).

    Methods:
        analog(): Defines the output equation above.

    Note: with the ideal offset Vos = 0 a perfectly symmetric oscillator stays
    at its unstable equilibrium (0 V) and never starts, like a noise-free
    real circuit; a small offset (1 mV) starts it, as real amplifiers have.

Used in the examples
--------------------

* :doc:`AC analysis (small-signal frequency response) </examples/ac_analysis>`
* :doc:`Schmitt trigger with an op-amp (inverting) </examples/schmitt_opamp>`
* :doc:`Op-amp astable multivibrator (relaxation oscillator) </examples/opamp_multivibrator>`
* :doc:`Chua's circuit with op-amps (double-scroll chaotic oscillator) </examples/chua_opamp>`

