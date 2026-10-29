555 Timer
=========

.. code-block:: python

    from pyams.models import Timer555

    X1 = Timer555("trig", "thres", "ctrl", "reset", "disch", "out", "vcc", "gnd")
    X1.setParams("Rdiv=5000 Vdrop=1.5")

Terminals
---------

``Timer555(trig, thres, ctrl, reset, disch, out, vcc, gnd)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Rdiv``
     - 5000
     - Ω
     - Divider resistor
   * - ``Vdrop``
     - 1.5
     - V
     - Output high drop below Vcc
   * - ``Vol``
     - 0.1
     - V
     - Output low level
   * - ``Rout``
     - 20
     - Ω
     - Output resistance
   * - ``Cout``
     - 1e-10
     - F
     - Output capacitance
   * - ``Rdis``
     - 10
     - Ω
     - Discharge transistor on resistance
   * - ``Roff``
     - 1e+10
     - Ω
     - Discharge transistor off resistance
   * - ``Vrst``
     - 0.7
     - V
     - Reset threshold

Description
-----------

The documentation of the class (``help(Timer555)``)::

    555 timer.  Terminals (the same order as the data sheet functions):

        Timer555(trig, thres, ctrl, reset, disch, out, vcc, gnd)

                      vcc
                       |
                      5k
                       |------ ctrl   (2/3 Vcc, upper reference)
                      5k
                       |------ m      (1/3 Vcc, lower reference)
                      5k
                       |
                      gnd

        thres  > V(ctrl)  : upper comparator   -> flip-flop RESET (output low)
        trig   < V(m)     : lower comparator   -> flip-flop SET   (output high)
        reset  < 0.7 V    : forces the output low (has priority)
        Q = 1 : out = Vcc - Vdrop, discharge transistor OFF
        Q = 0 : out = Vol,         discharge transistor ON (disch -> gnd, Rdis)

    The three internal 5 k resistors are real, so a voltage forced on the ctrl
    pin moves both thresholds (V(ctrl) and V(ctrl)/2), exactly as in the chip.
    The comparator inputs draw no current.  The flip-flop state changes only
    when a time point is accepted (see ``accepting()``, like the Comparator and
    the Thyristor), so the timing error is at most one time step: use a step
    well below the period/pulse width.

    Output: Thevenin source  (Vo - Vtarget)/Rout + Cout dVo/dt , with
    Vtarget = Vcc - Vdrop (high) or Vol (low).  The supply current is the
    divider current only (the output stage current is not drawn from vcc).

    Parameters:
        Rdiv (ohm)   each of the three divider resistors (5 k)
        Vdrop (V)    output high drop below Vcc (1.5 V)
        Vol (V)      output low level (0.1 V)
        Rout (ohm)   output resistance (20)
        Cout (F)     output capacitance, sets the edge time Rout*Cout (100 pF -> 2 ns)
        Rdis (ohm)   discharge transistor on resistance (10), Roff when off (1e10)
        Vrst (V)     reset threshold (0.7)

Used in the examples
--------------------

* :doc:`555 timer, astable multivibrator </examples/timer555_astable>`
* :doc:`555 timer, monostable (one-shot) </examples/timer555_monostable>`

