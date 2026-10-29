Trapezoid (Pulse) Current
=========================

.. code-block:: python

    from pyams.models import TrapezoidCurrent

    X1 = TrapezoidCurrent("p", "n")
    X1.setParams("I0=0 I1=0.001")

Terminals
---------

``TrapezoidCurrent(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``I0``
     - 0
     - A
     - Initial current
   * - ``I1``
     - 0.001
     - A
     - Peak current
   * - ``Td``
     - 0
     - Sec
     - Initial delay time
   * - ``Tr``
     - 0
     - Sec
     - Rise time
   * - ``Tw``
     - 0.05
     - Sec
     - Pulse-width
   * - ``Tf``
     - 0
     - Sec
     - Fall time
   * - ``T``
     - 0.1
     - Sec
     - Total period of the waveform
   * - ``Ioff``
     - 0
     - A
     - Offset current

Description
-----------

The documentation of the class (``help(TrapezoidCurrent)``)::

    This class models a Trapezoidal Waveform Current Source (the current
    counterpart of TrapezoidVoltage).

    The waveform has an initial delay (Td), a rising edge (Tr), a constant
    peak (Tw), a falling edge (Tf) and repeats with the period T.  A positive
    current flows through the source from node p to node n (SPICE convention,
    see DCCurrent).

    Attributes:
        I (signal): Current through the source, from p to n.
        I0 (param): Initial (low) current.
        I1 (param): Peak (high) current.
        Td (param): Initial delay time.
        Tr (param): Rise time.
        Tw (param): Pulse-width (high duration).
        Tf (param): Fall time.
        T (param): Total period of the waveform.
        Ioff (param): Offset current.

    The current waveform is defined as (cycle time c = (t - Td) mod T):

    - **Before the delay (t <= Td):**             I = I0 + Ioff
    - **Rising edge (0 <= c <= Tr):**             I = I0 + (I1 - I0) c / Tr + Ioff
    - **High state (Tr <= c <= Tr + Tw):**        I = I1 + Ioff
    - **Falling edge (Tr+Tw <= c <= Tr+Tw+Tf):** I falls linearly from I1 to I0
    - **Low state (afterwards):**                 I = I0 + Ioff

    Methods:
        analog(): Defines the trapezoidal waveform equation.

Used in the examples
--------------------

* :doc:`Current sources: DCCurrent, SinCurrent, TrapezoidCurrent </examples/current_sources>`

