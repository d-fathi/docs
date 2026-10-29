Diac
====

.. code-block:: python

    from pyams.models import Diac

    X1 = Diac("p", "n")
    X1.setParams("Vbo=36 Vh=16")

Terminals
---------

``Diac(p, n)``

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
     - 0.001
     - A
     - Holding current
   * - ``Ron``
     - 34
     - Ω
     - On-state dynamic resistance
   * - ``Roff``
     - 4e+06
     - Ω
     - Off-state resistance

Description
-----------

The documentation of the class (``help(Diac)``)::

    This class implements a diac: a two-terminal, symmetrical device that blocks
    until the voltage reaches the breakover voltage, then switches to a
    low-voltage conducting state, and stays on until the current falls below the
    holding current.

    The device has memory (hysteresis), so the model keeps a state, off or on:

        off :  I = V / Roff                       (leakage, blocking)
        on  :  I = sign(V) * (|V| - Vh) / Ron     (conducting, for |V| > Vh)

        off -> on   when |V| >= Vbo               (breakover)
        on  -> off  when |I| <  Ih                (current below the holding current)

    The state changes only when a time step is accepted (never inside a step
    that may be rejected), so within a step the diac is an ordinary smooth
    nonlinear resistor.  The turn-off therefore happens at about
    |V| = Vh + Ron * Ih.

    Why not a continuous S-shaped I-V curve?  The voltage is a single-valued
    function of the current, but at the breakover point the Newton iteration of
    an implicit solver cannot cross the fold of such a curve (it needs steps of
    picoseconds for as long as the voltage creeps up to Vbo).  A switching
    state avoids that, at the price of a current that jumps when the diac
    changes state.

    Attributes:
        V (signal): Input voltage signal across the diac, between nodes (p, n).
        I (signal): Output current signal through the diac, between nodes (p, n).
        Vbo (param): Breakover voltage (default: 36 V).
        Vh (param): On-state voltage at zero current extrapolation (default: 16 V).
        Ih (param): Holding current (default: 1 mA).
        Ron (param): Dynamic resistance when conducting (default: 34 ohm).
        Roff (param): Resistance when blocking (default: 4 Mohm).

    Methods:
        analog(): Defines the current of the present state and its transitions.

    Note: the state is updated when a transient step is accepted, so the
    transient analysis is needed (in a DC analysis the diac stays off).  The
    circuit must contain a capacitor or an inductor, as usual for an oscillator.

Used in the examples
--------------------

* :doc:`Diac relaxation oscillator </examples/diac_relaxation>`

