Exponential Voltage
===================

.. code-block:: python

    from pyams.models import ExpVoltage

    X1 = ExpVoltage("p", "n")
    X1.setParams("V1=0 V2=5")

Terminals
---------

``ExpVoltage(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``V1``
     - 0
     - V
     - Initial value
   * - ``V2``
     - 5
     - V
     - Pulsed value
   * - ``TD1``
     - 0.001
     - s
     - Rise delay time
   * - ``TAU1``
     - 0.001
     - s
     - Rise time constant
   * - ``TD2``
     - 0.005
     - s
     - Fall delay time
   * - ``TAU2``
     - 0.001
     - s
     - Fall time constant

Description
-----------

The documentation of the class (``help(ExpVoltage)``)::

    Exponential voltage source (SPICE ``EXP``).

        t <  TD1        : V = V1
        TD1 <= t < TD2  : V = V1 + (V2 - V1) (1 - exp(-(t - TD1)/TAU1))
        t >= TD2        : V = V1 + (V2 - V1) (1 - exp(-(t - TD1)/TAU1))
                                + (V1 - V2) (1 - exp(-(t - TD2)/TAU2))

    Terminals: ExpVoltage(p, n)   (V(p) - V(n) = V).
    Parameters:
        V1   initial value (V)                 (0)
        V2   pulsed value (V)                  (5)
        TD1  rise delay time (s)               (1 ms)
        TAU1 rise time constant (s)            (1 ms)
        TD2  fall delay time (s)               (5 ms)
        TAU2 fall time constant (s)            (1 ms)
    The DC (operating point) value is V1.

Used in the examples
--------------------

* :doc:`Exponential sources (SPICE EXP): ExpVoltage drives an RC filter, ExpCurrent charges a capacitor </examples/exp_sources>`

