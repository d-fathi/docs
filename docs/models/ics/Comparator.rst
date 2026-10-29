Comparator
==========

.. code-block:: python

    from pyams.models import Comparator

    X1 = Comparator("p", "n", "out")
    X1.setParams("Voh=5 Vol=0")

Terminals
---------

``Comparator(p, n, out)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Voh``
     - 5
     - V
     - High output level
   * - ``Vol``
     - 0
     - V
     - Low output level
   * - ``Vhys``
     - 0
     - V
     - Total hysteresis width
   * - ``Vos``
     - 0
     - V
     - Input offset voltage
   * - ``A``
     - 100000
     - –
     - Gain of the transition region
   * - ``Ro``
     - 50
     - Ω
     - Output resistance
   * - ``Tau``
     - 1e-08
     - s
     - Output time constant

Description
-----------

The documentation of the class (``help(Comparator)``)::

    Voltage comparator: the output goes to the high level Voh when the
    differential input Vd = V(p) - V(n) + Vos is positive and to the low level
    Vol when it is negative, with an optional built-in hysteresis Vhys.

    Terminals (p, n, out): non-inverting input (+), inverting input (-) and
    output.  The inputs draw no current.

    Compared with the OpAmp model:
      * the two output levels are free (Vol ... Voh, e.g. 0 ... 5 V logic);
      * the hysteresis is built in: with Vhys > 0 the output switches high
        when Vd rises above +Vhys/2 and low when Vd falls below -Vhys/2
        (between the two thresholds it keeps its last state), so a noisy or
        slowly varying input does not make it chatter.

    Equations (Vmid = (Voh + Vol)/2, Vh = (Voh - Vol)/2, Vd' = Vd + Vos):

        threshold  = +Vhys/2 while the state is low, -Vhys/2 while it is high
        Vtarget    = Vmid + Vh * tanh(A * (Vd' - threshold) / Vh)
        Iout       = (Vo - Vtarget)/Ro + (Tau/Ro) * dVo/dt

    The state (low/high) changes only when a time point is accepted (see
    ``accepting()``), never inside a Newton iteration; in a DC sweep it
    changes after each point, so running a sweep up and then down draws the
    hysteresis loop.  The delay of the comparator is set by Tau (the output
    reaches half of its swing about 0.7 Tau after the input crosses the
    threshold); a nonzero Tau is also what lets the solver follow the
    switching.

    Attributes:
        Vd (signal): differential input between p and n.
        Vo (signal): output voltage, measured against ground.
        Io (signal): output current from the output node to ground.
        Voh (param): high output level (default 5 V).
        Vol (param): low output level (default 0 V).
        Vhys (param): total hysteresis width (default 0 V = no hysteresis).
        Vos (param): input offset voltage (default 0 V).
        A (param): gain of the transition region (default 1e5): the output
                   goes through its swing within Vh/A of the threshold.
        Ro (param): output resistance (default 50 ohm).
        Tau (param): output time constant, i.e. the delay (default 10 ns).

Used in the examples
--------------------

* :doc:`Comparator: hysteresis loop and RC relaxation oscillator </examples/comparator_demo>`

